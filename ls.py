import os
print("CWD:", os.getcwd())
for file in os.listdir('.'):
    if 'zuscoffee' in file:
        print(file)
