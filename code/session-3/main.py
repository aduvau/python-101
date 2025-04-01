import requests
import json

base_url = "https://api.spacexdata.com/v4"

def get_json(url: str) -> json:
    result = requests.get(url)
    return result.json()

def write_json(data: json, data_type: str) -> None:
    with open(f"output/data_{data_type}.json", "w") as file:
        json.dump(data, file, indent=2)

def build_next_launch() -> object:
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
        'launch_time': launch['date_local'],
        'location': {
            'city': launchpad['locality'],
            'name': launchpad['full_name']
        },
        'rocket': {
            'height': rocket['height']['meters'],
            'mass': rocket['mass']['kg']
        }
    }

    return next_launch

def answer_on_location(next_launch: object) -> None:
    user_input = ''

    while user_input != "q":
        print('What do you want specifically?')
        print('1. City of the next launch')
        print('2. Facility of the next launch')
        print('q. Go back to the main menu')
        print('>')

        user_input = input()

        if user_input == '1':
            print(f'The next launch will be in {next_launch['location']['city']}')
        elif user_input == '2':
            print(f'The next launch will be in {next_launch['location']['name']}')
        elif user_input == 'q':
            return
        else:
            print('You should only choose between the above options')

def answer_to_user(next_launch: object) -> None:
    user_input = ''
    
    while user_input != "q":
        print('What do you want?')
        print('1. Time of the next launch')
        print('2. Location of the next launch')
        print('3. Details about the rocket used')
        print('q. Exit the program')
        print('>')

        user_input = input()

        if user_input == '1':
            print(f'The next launch will be one {next_launch['launch_time']}')
        elif user_input == '2':
            answer_on_location(next_launch)
        elif user_input == '3':
            print(f'The rocket is going to be massive: {next_launch['rocket']['height']}m heigh and {next_launch['rocket']['mass']} weight!')
        elif user_input == 'q':
            return
        else:
            print('You should only choose between the above options')

def main():
    print('Initiated')

    next_launch = build_next_launch()

    answer_to_user(next_launch)    
        
    print("Success")

if __name__ == '__main__':
    main()