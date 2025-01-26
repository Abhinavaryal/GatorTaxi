# GatorTaxi

## Overview
**GatorTaxi** is a Python-based ride management system designed to efficiently handle ride requests using advanced data structures like **Red-Black Tree (RBT)** and **Min Heap**. This project offers an optimized solution for dynamically tracking, managing, and processing ride requests.

## Features
- **Add Ride**: Create a new ride with a unique ID, cost, and trip duration.
- **Get Next Ride**: Retrieve and process the ride with the lowest cost.
- **Update Ride**: Modify the cost or trip duration of an existing ride.
- **Cancel Ride**: Remove a ride from the system.
- **Search Ride**: Retrieve details of a ride using its unique ID.
- **Print Ride Range**: Display all rides within a specified range of IDs.

## Technology Stack
- **Programming Language**: Python
- **Data Structures**:
  - **Red-Black Tree (RBT)**: Ensures efficient searching and range queries.
  - **Min Heap**: Facilitates quick retrieval of the ride with the lowest cost.

## How It Works
1. **Ride Management**: Rides are managed using a combination of RBT and Min Heap, enabling seamless addition, updates, and deletions.
2. **Efficient Search**: The Red-Black Tree ensures fast lookup times for ride queries and range operations.
3. **Dynamic Updates**: Update operations maintain data integrity across both data structures.

## Installation and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/GatorTaxi.git
   cd GatorTaxi
Run the main program:

python GatorTaxi.py <input_file>

Input Format
The input file should contain operations in the following format:

Insert Ride: Insert(<RideID>, <RideCost>, <TripDuration>)
Get Next Ride: GetNextRide()
Update Ride: UpdateTrip(<RideID>, <NewRideCost>, <NewTripDuration>)
Cancel Ride: CancelRide(<RideID>)
Search Ride: Search(<RideID>)
Print Ride Range: Print(<StartRideID>, <EndRideID>)
Example

Insert(1, 20, 15)
Insert(2, 15, 10)
Insert(3, 25, 20)
Search(2)
UpdateTrip(2, 18, 12)
GetNextRide()
CancelRide(3)
Print(1, 3)

Contributors
Abhinav Aryal

License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
 
