from subprocess import call

call("python -m pip install --upgrade pip")

with open("requirements.txt") as f:
    for line in f:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        pkg_name, version = line.split("==")
        call(f"pip install --upgrade {pkg_name}", shell=True)
