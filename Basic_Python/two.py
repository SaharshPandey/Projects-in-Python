celsius =input("celsius")
def cel_to_farr(cel):
    far=cel*9/5 +32
    return far

if celsius<-273.15:
    print("Temperature is too low")
else:
    print cel_to_farr(celsius)    