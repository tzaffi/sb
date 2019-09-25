names = ["NJohn", "Mary"]

# don't need a boolean because for has an else!!!
for name in names:
    if name.startswith("J"):
        print("Found")
        found = True
        break
else:
    print("Not found")
    
