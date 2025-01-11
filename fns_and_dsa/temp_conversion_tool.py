FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR +32

try :  
    entered_temp = float(input("Enter the temperature to convert: "))
except:
    raise Exception("Invalid temperature. Please enter a numeric value.")

type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if type == "C":
    result, type_r = convert_to_fahrenheit(entered_temp), "F"
elif type =="F":
    result, type_r = convert_to_celsius(entered_temp), "C"
else:
    raise Exception("Invalid temperature. Please enter a numeric value.")

print (f"{entered_temp}°{type} is {result}°{type_r}")
