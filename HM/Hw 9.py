def convert_currency(amount, exchange_rate):
    return amount * exchange_rate
def main():
    print("Конвертер валют")
    while True:
        print("1. USD to UAH")
        print("2. EUR to UAH")
        print("3. PLN to UAH")
        print("4. GBP to UAH")
        print("5. Exit")

        choice = input("Виберіть опцію (1/2/3/4/5): ")

        if choice == '1':
            usd_amount = float(input("Введіть суму в USD: "))
            exchange_rate_usd = 38.09
            uah_result = convert_currency(usd_amount, exchange_rate_usd)
            print(f"{usd_amount} USD = {uah_result:2f} UAH\n" )
        elif choice == '2':
            eur_amount = float(input("Введіть суму в EUR: "))
            exchange_rate_eur = 41.81
            uah_result = convert_currency(eur_amount, exchange_rate_eur)
            print(f"{eur_amount} EUR = {uah_result:.2f} UAH\n")
        elif choice == '3':
            pln_amount = float(input("Введіть суму в PLN: "))
            exchange_rate_pln = 9.59
            uah_result = convert_currency(pln_amount, exchange_rate_pln)
            print(f"{pln_amount} PLN = {uah_result:.2f} UAH\n")
        elif choice == '4':
            gbp_amount = float(input("Введіть суму в GBP: "))
            exchange_rate_gbp = 48.60
            uah_result = convert_currency(gbp_amount, exchange_rate_gbp)
            print(f"{gbp_amount} GBP = {uah_result:.2f} UAH\n")
        elif choice == '5':
            print("Дякуємо за використання конвертера валют. До побачення!")
            break
        else:
            print("Неправильний вибір. Будь ласка, введіть число від 1 до 5.\n")

if __name__ == "__main__":
     main()