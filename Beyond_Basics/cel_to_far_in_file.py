temp=[10,-20,-289,100]
myFile=open("temp.txt",'a+')
def c_to_f(celsius):
    if(celsius< -273.15):
        print ("Wrong Temp") 
    else:
       
        data= celsius*9/5+32
        myFile.write(str(data)+"\n")
        return data 
for i in temp:
    (c_to_f(i))   
   
myfile=myFile.read() 
myFile.close()  
myfile=myfile.splitlines()
for j in myfile:
    print(j)    
