import random
import string
import json
import boto3

class ParkingLot:
    def __init__(self, square_footage, spot_length=8, spot_width=12):
        self.square_footage = square_footage
        self.spot_area = spot_length * spot_width
        self.capacity = square_footage // self.spot_area
        self.spots = [None] * self.capacity

    def park_car(self, car, spot_number):
        if 0 <= spot_number < self.capacity:
            if self.spots[spot_number] is None:
                self.spots[spot_number] = car
                return f"Car with license plate {car} parked successfully in spot {spot_number}.", True
            else:
                return f"Spot {spot_number} is already occupied.", False
        else:
            return f"Spot number {spot_number} is out of bounds.", False

    def is_full(self):
        return all(spot is not None for spot in self.spots)

    def map_vehicles_to_spots(self):
        mapping = {i: str(car) if car else None for i, car in enumerate(self.spots)}
        return mapping

    def save_mapping_to_json(self, filename):
        mapping = self.map_vehicles_to_spots()
        with open(filename, 'w') as file:
            json.dump(mapping, file)
        return filename

    def upload_to_s3(self, file_name, bucket_name, object_name=None):
        s3_client = boto3.client('s3')
        try:
            s3_client.upload_file(file_name, bucket_name, object_name or file_name)
            print(f"File {file_name} uploaded to {bucket_name}/{object_name or file_name} successfully.")
        except e as Exception:
            print(e)
        

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot):
        available_spots = list(range(parking_lot.capacity))
        while available_spots:
            spot_number = random.choice(available_spots)
            result, success = parking_lot.park_car(self, spot_number)
            print(result)
            if success:
                return True
            available_spots.remove(spot_number)
        return False

def main():
    square_footage = 2000
    parking_lot = ParkingLot(square_footage)

    num_cars = 25  # length of cars array
    cars = [Car(''.join(random.choices(string.ascii_uppercase + string.digits, k=10))) for _ in range(num_cars)]

    for car in cars:
        if parking_lot.is_full():
            print("Parking lot is full. Exiting program.")
            break
        car.park(parking_lot)

    # Save mapping to JSON
    json_filename = parking_lot.save_mapping_to_json('parking_lot_mapping.json')

    # Upload JSON to S3
    bucket_name = 's3-bucket-name'  
    parking_lot.upload_to_s3(json_filename, bucket_name)

if __name__ == "__main__":
    main()
