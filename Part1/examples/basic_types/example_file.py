f = open('data.txt', 'w') #open a new file
f.write('Hello\n')
f.close()

with open('other.txt', 'w') as f:
    f.write("this is madness\n")

with open('other.txt', 'r') as f:
    print f.read()
