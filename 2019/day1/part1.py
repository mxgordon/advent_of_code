import numpy as np
import json

with open('masses.json', 'r') as f:
    masses_list = json.load(f)


masses_arr = np.array(masses_list)

masses_arr = (masses_arr//3) - 2

print(masses_arr.sum())
