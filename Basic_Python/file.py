myfile=open("fruits.txt")
content=myfile.read()
myfile.close()
content=content.splitlines()
for i in content:
    print(i)