def fahrenheit_to_celsius(f):
    c = (f - 32) * 5.0/9.0
    return c

def celsius_to_fahrenheit(c):
    f = c * 9.0/5.0 + 32
    return f

print("Temperature Converter!")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
while(True):
    choice = int(input("Enter your choice: "))
    if choice == 1:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f} Fahrenheit is equal to {c:.2f} Celsius.")
    elif choice == 2:
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c} Celsius is equal to {f:.2f} Fahrenheit.")
    else:
        print("Invalid choice.")
    repeat = input("Do you want to convert another temperature? (yes/no): ").lower()
    if repeat == 'no':
        print("Thank you!")
        break
