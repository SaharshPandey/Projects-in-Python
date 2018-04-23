from datetime import datetime
delta=datetime.now()

delta=delta.strftime("%Y:%m:%d")
print(delta)

delta=datetime.strptime("1990:11:21:05:55","%Y:%m:%d:%H:%M")
print (delta)
delta=datetime.now()
print(delta.strftime("%Y:%m:%d:%H:%M"))
print(delta.strftime("%c"))
print(datetime.now().__format__("%A"))