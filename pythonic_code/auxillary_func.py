my_values = {
    'red': ['5'],
    'green': [''],
    'blue': ['0']
}

red = my_values.get('red', [''])[0] or 0
blue = my_values.get('blue', [''])[0] or 0
print(red)
print(blue)

