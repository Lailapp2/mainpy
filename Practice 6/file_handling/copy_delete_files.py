# copy_delete_files.py
import shutil
import os

filename = "sample.txt"
backup_filename = "sample_backup.txt"

# Append new lines
with open(filename, "a") as f:
    f.write("Appending a new line.\n")

# Verify content
with open(filename, "r") as f:
    print(f"Updated File Contents:\n{f.read()}")

# Copy file
shutil.copy(filename, backup_filename)
print(f"Backup created as {backup_filename}")

# Delete file safely
if os.path.exists(backup_filename):
    os.remove(backup_filename)
    print(f"{backup_filename} deleted safely.")