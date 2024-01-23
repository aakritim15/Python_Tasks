from forex_python.converter import CurrencyRates

def print_currency_codes():
    print("List of Common Currencies:")
    print("INR - Indian Rupee")
    print("USD - United States Dollar")
    print("EUR - Euro ")
    print("GBP - British Pound Sterling")
    print("JPY - Japanese Yen")
    print("THB - Thai Baht")
    print("AUD - Australian Dollar")
    print("CAD - Canadian Dollar")
    print("CHF - Swiss Franc")
    print("CNY - Chinese Yuan Renminbi")
    print("SEK - Swedish Krona")
    print("NZD - New Zealand Dollar")
    print("NOK - Norwegian Krone")
    print("BRL - Brazilian Real")
    print("RUB - Russian Ruble")
    print("ZAR - South African Rand")

while True:
    c = CurrencyRates()
    print("Currency Converter:")
    print_currency_codes()
    fc = input("Enter the source currency code: ").upper()
    tc = input("Enter the target currency code: ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    exchange_rate = c.get_rate(fc, tc)
    converted_amount = amount * exchange_rate
    print(f"{amount} {fc} is equal to {converted_amount:.2f} {tc}.")
    repeat = input("Do you want to convert another currency? (yes/no): ").lower()
    if (repeat == 'no' or  repeat== 'NO' ):
        print("Thank you!")
        break
