import requests
import sys

# The URL for the ISS current location API
url = "http://api.open-notify.org/iss-now.json"

outer_loop = True
# Make a outer loop so the user can run the code again.
while outer_loop:
# Make a inner loop so the user can run the code again.
    running = True
    while running:
        # Make the request to get the current location of the ISS
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
    
            # Get the coordinates from the JSON response
            # Convert the latitude and longitude to floats, as they are returned as strings.
            lat = float(data['iss_position']['latitude'])
            lon = float(data['iss_position']['longitude'])
    
            # Print the current location
            print(f"The ISS's Current Location --> Latitude: {lat}; Longitude: {lon}")
            again = input("Would you like to see the location again? ('y'/'n'): ")
            # Get the location again and print it if the user wants to see it again
            if again == "y":
                break
            # Exit the program if the user is done
            elif again == "n":
                print("Exiting...")
                sys.exit(0)

        # If the request failed, print that it failed and the status code.
        else:
            print(f"Failed to get data. Status code: {response.status_code}")
            again = input("Would you like to try again? ('y'/'n'): ")
            # Try getting the location again if the user wants to
            if again == "y":
                break
            # Exit the program if the user does not want to try again
            elif again == "n":
                print("Exiting...")
                sys.exit(0)