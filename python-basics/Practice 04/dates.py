import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) 

z = datetime.datetime(2026, 1, 1)
print(z)

print(z.strftime("%B")) # .strftime format -> str