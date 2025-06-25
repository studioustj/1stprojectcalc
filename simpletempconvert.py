unit = input("What is the temperature in? (C for Celsius, F for Fahrenheit): ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = round ((9 * temperature)/ 5 + 32, 1)
    print(f"The temperature is {temperature} degrees Fahrenheit!")
    pass
elif unit == "F":
    temperature = round ((temperature - 32)* 5 / 9, 1)
    print(f"The temperature is {temperature} degrees Celcuius!")
else:
    print(f"{unit} is an invalid unit of measurement")