# Question :  Write a Python Program to Convert Celsius to Fahrenheit and vice –a-versa.

def fah(fahrenheit):
	celsius = ( fahrenheit - 32) * 5.0/9.0
	print("\n\tFahrenheit "+ str(fahrenheit))
	print("\n\tcelsius "+ str(celsius))


def cel(celsius):
	fahrenheit = 9.0/5.0 * celsius + 32
	print(" \n\tcelsius "+ str(celsius))
	print(" \n\tFahrenheit "+ str(fahrenheit))

raj = input("\n\tInput Temprature :  ")
print("\n********************************************************************")
print("\n\tfahrenheit To Celsius ")
fah(float(raj))
print("\n********************************************************************")
print("\n\tCelsius To fahrenheit ")
cel(float(raj))
print("\n********************************************************************")
