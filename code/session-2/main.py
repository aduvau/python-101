import requests
import json

base_url = "https://api.spacexdata.com/v4"

def get_json(url: str) -> json:
    result = requests.get(url)
    return result.json()

def write_json(data: json, data_type: str) -> None:
    with open(f"output/data_{data_type}.json", "w") as file:
        json.dump(data, file, indent=2)

def main():
    print('Initiated')
    
    # Fetch the next launch and write the data to a JSON file
    launch_url = f"{base_url}/launches/next"
    launch = get_json(launch_url)
    # write_json(launch, "launch")

    # Fetch its launchpad and write the data to a JSON file
    launchpad_url = f"{base_url}/launchpads/{launch["launchpad"]}"
    launchpad = get_json(launchpad_url)
    # write_json(launchpad, "launchpad")

    # Fetch its rocket and write the data to a JSON file
    rocket_url = f"{base_url}/rockets/{launch["rocket"]}"
    rocket = get_json(rocket_url)
    # write_json(rocket, "rocket")

    next_launch = {
        'id': launch['id'],
        "location": {
            'city': launchpad['locality'],
        }
    }

    print(next_launch)

    print("Success")

if __name__ == '__main__':
    main()