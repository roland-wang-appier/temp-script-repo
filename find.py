import subprocess
out = subprocess.run('find / -name "*zuscoffee*.json" 2>/dev/null', shell=True, capture_output=True, text=True)
print("Find result:", out.stdout)
