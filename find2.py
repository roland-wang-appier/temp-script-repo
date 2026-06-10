import os
def find_files(startpath):
    for root, dirs, files in os.walk(startpath):
        for f in files:
            if 'zuscoffee' in f and f.endswith('.json'):
                print(os.path.join(root, f))
find_files('/')
