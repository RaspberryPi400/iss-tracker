import requests
import sys
import reverse_geocoder as rg

# Define the function to change coordinates to the country the ISS is over or closest to (if it is over the ocean, which most of the time it is)
def latlon_to_country(lat, lon):
    # Defines the latitude and longitute
    coordinates = (lat, lon)
    # Returns a list of countries
    results = rg.search(coordinates, verbose=False)
    # Gets the country
    country = results[0]['cc']
    return country

def print_astronauts():
    # Get the astronauts' names from Open Notify
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    # If successfull:
    if response.status_code == 200:
        data = response.json()

        # Get the number of people and their names
        number = data['number']
        people = data['people']

        # Print the number of people in space, not just on the ISS
        print(f"There are currently {number} people in space:")
        print("----------------------------------------------")

        for person in people:
            # If the person is on the ISS, print their name(s)
            if person['craft'] == "ISS":
                print(f"- {person['name']}")
            # If no one is currently on the ISS, say that.

    # If it could not get the data, exit the program.
    else:
        print("Could not retrieve astronaut data.")
        print("Exiting...")
        sys.exit(0)

# The URL for the ISS current location API
url = "http://api.open-notify.org/iss-now.json"

outer_loop = True
# Make a outer loop so the user can run the code again.
while outer_loop:
# Make a inner loop so the user can run the code again
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

            # Print the country that the ISS is over
            country = latlon_to_country(lat, lon)
            print(f"The ISS is currently near/over {country}.")

            # Print the astronauts currently on the ISS
            print_astronauts()
    
            # Print the current location
            print(f"The ISS's Current Location --> Latitude: {lat}; Longitude: {lon}")
            again = input("Would you like to see the data again? ('y'/'n'): ")
            # Get the data again and print it if the user wants to see it again (the location is always changing)
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