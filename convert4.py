#Converts Fahrenheit to Celsius

F = float(input("Enter temperature in Fahrenheit:"))
C = (F-32)*(5/9)
print('That would be {}° celsius.').format(C)
