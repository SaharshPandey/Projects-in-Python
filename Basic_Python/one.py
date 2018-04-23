import urllib.request,json,jupyter_client
import numpy,pandas
def string_len(my_string):
    if type(my_string)==int:
        print ("Sorry integers don't have length")
    elif type(my_string)==float:
        print ("This is Float Value")
    
    else:
        return len(my_string)
        
print (string_len("dsdad"))

output=urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?lat=29.88930833333333&lon=77.95958833333334&appid=2e4cece87a1d0ae4bec92a7be776258a&units=metric")
response=json.load(output)