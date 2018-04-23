temp=[10,-20,-289,100]
def c_to_f(celsius):
    if(celsius< -273.15):
        print "Wrong Temp" 
    else:
        return celsius*9/5+32 
for i in temp:
    print(c_to_f(i))         