import json


def calc_fuel(new_mass: int, fuel_total: int = 0) -> int:
    new_fuel_mass = (new_mass//3) - 2
    return calc_fuel(new_fuel_mass, fuel_total=new_fuel_mass+fuel_total) if new_fuel_mass > 0 else fuel_total


with open('masses.json', 'r') as f:
    masses_list = json.load(f)

total_mass = 0


for mass in masses_list:
    total_mass += calc_fuel(mass)

print(total_mass)