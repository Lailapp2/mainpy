# write_files.py
filename = "sample.txt"

# Create and write to file
with open(filename, "w") as f:
    f.write("Hello, this is a sample file.\n")
    f.write("It contains multiple lines of text.\n")

print(f"{filename} created and data written.")