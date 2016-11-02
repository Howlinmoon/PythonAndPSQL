with open("thisfile.txt", 'w') as f:
    f.write('hello world')

print("File should be opened, written and closed")

with open("thisfile.txt", 'r') as r:
    print(r.readline())

