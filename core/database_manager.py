import json


def load_table(table_name):
    with open(f"database/{table_name}.json", "r") as file:
        return json.load(file)


def save_table(table_name, data):
    with open(f"database/{table_name}.json", "w") as file:
        json.dump(data, file, indent=4)