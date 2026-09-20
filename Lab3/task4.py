# 4 A*
locations = {
    'A': {'g': 3, 'h': 5},
    'B': {'g': 4, 'h': 2},
    'C': {'g': 2, 'h': 6}
}

f_values = {}

for location in locations:
    g = locations[location]['g']
    h = locations[location]['h']

    f = g + h
    f_values[location] = f

    print(location + ": f =", f)

best_location = min(f_values, key=f_values.get)

print("A* will select", best_location)
