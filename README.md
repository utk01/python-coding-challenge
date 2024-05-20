# Parking Lot Challenge

## Requirements

The Parking Lot Challenge involves creating a simulation of a parking lot with the following features:

1. **ParkingLot Class**:
   - Takes in a square footage size as input.
   - Calculates the number of parking spots based on the size of each spot.
   - Initializes an array to represent the parking spots.
   - Provides methods to park a car and to map vehicles to their parked spots in JSON format.
   - Exits the program if the parking lot is full.

2. **Car Class**:
   - Takes in a 7-digit license plate.
   - Provides a method to output the license plate as a string.
   - Provides a method to park the car in a specified spot within a parking lot.

3. **Main Function**:
   - Generates an array of cars with random license plates.
   - Attempts to park each car in a random spot until all cars are parked or the parking lot is full.
   - Outputs the result of each parking attempt.
   - Saves the final mapping of parked cars to a JSON file.
   - Uploads the JSON file to an S3 bucket.

## Solution

### Classes

#### ParkingLot Class
- **Initialization**: Takes the square footage of the parking lot and the dimensions of each parking spot to calculate the total number of spots.
- **park_car Method**: Attempts to park a car in a given spot and returns a status message and a success flag.
- **is_full Method**: Checks if the parking lot is full.
- **map_vehicles_to_spots Method**: Creates a dictionary mapping spot numbers to car license plates.
- **save_mapping_to_json Method**: Saves the vehicle-to-spot mapping to a JSON file.
- **upload_to_s3 Method**: Uploads the JSON file to an S3 bucket.

#### Car Class
- **Initialization**: Takes a 7-digit license plate as input.
- **__str__ Method**: Returns the license plate when the car instance is converted to a string.
- **park Method**: Attempts to park the car in a random spot within the parking lot until it is successfully parked or all spots have been tried.

### Main Function
- Initializes a parking lot with a given square footage.
- Generates a list of cars with random license plates.
- Tries to park each car in a random spot, retrying if the spot is occupied, until all cars are parked or the parking lot is full.
- Outputs a message and exits the program if the parking lot is full.
- Saves the final mapping to a JSON file and uploads it to an S3 bucket.

### Example Usage
To run the program, execute the following command:
```bash
python main.py
