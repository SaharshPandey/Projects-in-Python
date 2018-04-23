from datetime import datetime
import glob2
filenames=glob2.glob("*txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,'r') as content:
            file.write(content.read()+"\n")

    

    