catNames = []

while True:
    print(f'Enter the name of cat {len(catNames) + 1} (Or enter nothing to stop.):')
    name = input()

    if name == "":
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(f"    {name}")