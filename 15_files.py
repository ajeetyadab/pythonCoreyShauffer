import os

print(os.getcwd())

# os.chdir("c:\\Users\\hp\\Desktop\\pythonCoreyShauffer")
with open("notes.txt","a+") as f:
    
    f.write("line 8 \n")
    f.seek(0)
    content = f.read()
    print(content)
    
