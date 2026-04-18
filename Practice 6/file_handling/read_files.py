# read_files.py
filename = "sample.txt"

with open(filename, "r") as f:
    content = f.read()
    print("File Contents:\n", content)