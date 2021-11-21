from subprocess import run

def pip_update_pkg(pkg_name: str):
    result = run(f"pip install --upgrade {pkg_name}", shell=True, capture_output=True, text=True)
    if pkg_name == 'playwright':
        run('playwright install chromium') # run directly
    
    for line in result.stdout.split('\n'):
        if line.startswith("Successfully installed"):
            print(line)

run("python -m pip install --upgrade pip") # run directly

with open("requirements.txt") as f:
    for line in f:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        pkg_name, version = line.split("==")
        pip_update_pkg(pkg_name)

print("Update Done!")