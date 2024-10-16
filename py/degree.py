# function define for celsi to furen
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# function for fahr to cels
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        # function calling
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        # function calling
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()
