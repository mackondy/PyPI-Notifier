from subprocess import call

call("python -m pip install --upgrade pip")

pkgs = []
with open("requirements.txt") as f:
    for line in f:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        pkg_name, version = line.split("==")
        pkgs.append(pkg_name)
        
call("pip install --upgrade " + " ".join(pkgs), shell=True)