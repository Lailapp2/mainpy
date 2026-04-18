# create_list_dirs.py
import os

# Create nested directories
os.makedirs("Practice6/data/nested_dir", exist_ok=True)
print("Nested directories created.")

# List all files and folders in current directory
entries = os.listdir(".")
print("Files and folders in current directory:", entries)

# Find files by extension
py_files = [f for f in os.listdir(".") if f.endswith(".py")]
print("Python files:", py_files)