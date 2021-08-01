from subprocess import run

def pip_update_pkg(pkg_name: str):
    result = run(f"pip install --upgrade {pkg_name}", shell=True, capture_output=True, text=True)
    if result.stdout.startswith("Requirement already satisfied"):
        return
    print(result.stdout)
    if pkg_name == 'playwright':
        run('python -m playwright install chromium')

run("python -m pip install --upgrade pip")

with open("requirements.txt") as f:
    for line in f:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        pkg_name, version = line.split("==")
        pip_update_pkg(pkg_name)