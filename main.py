from core.database_manager import *

print("Welcome to QueryVault!")

from core.database_manager import *

student = {
    "id": 1,
    "name": "Alice",
    "age": 20
}

insert_record("students", student)

print(load_table("students"))