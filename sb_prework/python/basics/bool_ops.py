name = " " #"Mosh"

if not name.strip():
    print("Name is empty")

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# chaining comparison
if 18 <= age < 65:
    print("Eligible")
