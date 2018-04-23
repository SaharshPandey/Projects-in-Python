a=15
b=0
try:
    print(a/b)
except(ZeroDivisionError):
    print("Division not succesfull")
finally:
    print("This block runs everytime")
