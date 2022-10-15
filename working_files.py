import json

with open('cities.json') as cities_file:
    cities = json.load(cities_file)
    for city in cities:
        print(f"Name : {city['name']},           Population: {city['pop']}")

# Path: working_files.py
