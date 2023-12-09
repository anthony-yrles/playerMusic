import json

def save(filename, newEntry, data):
    data.append(newEntry)
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)