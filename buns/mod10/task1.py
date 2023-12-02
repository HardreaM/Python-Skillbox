import json
import requests

ship_url = "https://swapi.dev/api/starships/?search=Millennium Falcon"
response = requests.get(ship_url)
data = response.json()

ship_response = requests.get(data['results'][0]['url'])
ship_info = ship_response.json()

pilots = []

for pilot_url in ship_info["pilots"]:
    pilot_data = requests.get(pilot_url).json()

    homeworld_url = pilot_data["homeworld"]
    homeworld_data = requests.get(homeworld_url).json()

    pilot_info = {
        "height": pilot_data["height"],
        "homeworld": homeworld_data["name"],
        "homeworld_url": pilot_data["homeworld"],
        "mass": pilot_data["mass"],
        "name": pilot_data["name"],
    }
    pilots.append(pilot_info)

info = {
    "max_atmosphering_speed": ship_info["max_atmosphering_speed"],
    "pilots": pilots,
    "ship_name": ship_info["name"],
    "starship_class": ship_info["starship_class"],
}

print(json.dumps(info, indent=4))

with open("millennium_falcon_info.json", "w") as file:
    json.dump(info, file, indent=4)