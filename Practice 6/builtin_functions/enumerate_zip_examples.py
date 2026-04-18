# enumerate_zip_examples.py
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# enumerate
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

# zip
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Type checking and conversions
x = "123"
print("Type before:", type(x))
x_int = int(x)
print("Type after conversion:", type(x_int))