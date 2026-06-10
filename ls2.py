import os
print(os.listdir('/'))
try:
    print("workspace", os.listdir('/workspace'))
except Exception as e:
    pass
