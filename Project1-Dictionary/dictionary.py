import json
import difflib
from difflib import get_close_matches

json_file=json.load(open("data.json"))
print("Total words in my Dictionary : %d" %len(json_file.keys()))
def translate(w):
        if w in json_file:
            return json_file[w]
        
        elif w.title() in json_file:
            return json_file[w.title()]
        elif w.upper() in json_file:
            return json_file[w.upper()]    
        
        elif len(get_close_matches(w,json_file.keys())) >0:
            again=input ("Do you mean \"%s\" : " %get_close_matches(w,json_file.keys())[0])
            if again=="y":
               return(json_file[get_close_matches(w,json_file.keys())[0]])
            elif again=="n":
                return("Alright")
            else: 
                print("Wrong Entry..Enter Again")
                again=input ("Do you mean \"%s\" : " %get_close_matches(w,json_file.keys())[0])
                if again=="y":
                    return(json_file[get_close_matches(w,json_file.keys())[0]])
                elif again=="n":
                    return("Alright")
                    

            
        else:
            return "The word doesn't exist..Pease recheck it"

word=str(input("Enter Word :\t"))

output=translate(word.lower())
count=0
if(type(output)==list):
    
    for item in output:
        count=count+1
        print ("%d : %s" %(count,item))
else:
    print(output)        