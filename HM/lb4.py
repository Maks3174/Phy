#1
countries = set()

def add_country():
    country = input("Введіть назву країни, яку потрібно додати: ")
    countries.add(country)
    print(f"{country} було додано")

def remove_country():
    country = input("Ввведіть назву країни, яку потрібно видалити: ")
    if country in countries:
        countries.remove(country)
        print(f"{country} було видалено з множини країн.")
    else:
        print(f"{country} не знайдено у множині країн")

def search_countre():
    substrung = input("Введіть підстроку для пошуку:")
    found_countries = [country for  country in countries if substrung.lower() in country.lower()]
    if found_countries:
        print("Знайдені країни: ")
        for country in found_countries:
            print(country)
    else:
        print("Країни не знайдено за вказаним підстроком.")

def check_country():
    country = input("Введіть назву країни для перевірки: ")
    if country in countries:
        print(f"{country} знаходиться у множині країн.")
    else:
        print(f"{country} не знайдено у множині країн.")

def display_menu():
    print("\nМеню:")
    print("1. Додати країну")
    print("2. Видалити країну")
    print("3. Пошук країни за підстрокою")
    print("4. Перевірити наявність країни")
    print("5. Вийти з програми")

def main():
    while True:
        display_menu()
        choice = input("Вуберіть опцію: ")
        if choice == "1":
            add_country()
        elif choice == "2":
            remove_country()
        elif choice == "3":
            search_countre()
        elif choice == "4":
            check_country()
        elif choice == "5":
            print("Програма завершила роботу.")
            break
        else:
            print("Некоректний ввід. Спробуйте ще раз. ")

if __name__ == "__main__":
    main()
print()
#2
cities_set1 = {"Kyiv", "Lviv", "Chortkiv", "Kharkiv", "Dnipro"}
cities_set2 = {"Kharkiv", "Lviv", "Chortkiv", "Chernivtsi", "Zaporizhzhia"}

common_cities = cities_set1.intersection(cities_set2)

print("Спільні міста в обох множинах:", common_cities)
print()
#3
set1 = {"Kyiv", "Lviv", "Kharkiv", "Odessa"}
set2 = {"Kyiv", "Odessa"}

result_set = set1.difference(set2)
print(f"Міста які містяться в першій множині,але відсутні у другій - {result_set}")
print()
#4
set1 = {"Kyiv", "Lviv", "Kharkiv", "Odessa"}
set2 = {"Kyiv", "Odessa", "Chortkiv", "Ternopil"}

result_set = set2.difference(set1)
print(f"Міста які містяться в другій множині,але відсутні в першій - {result_set}")
print()
#5
set1 = {"Kyiv", "Lviv", "Kharkiv"}
set2 = {"Odessa", "Lviv", "Dnipro"}

unique_set1 = set1.difference(set2)
unique_set2 = set2.difference(set1)

result_set = unique_set1.union(unique_set2)
print(f"Множина з унікальними назвами для кожної множини - {result_set}")
print()
#5
def remove_common_characters(str1, str2):
    unique_chars = set(str1) ^ set(str2)
    return ''.join(unique_chars)

result = remove_common_characters("hello", "world")
print(f"Унікальні букви - {result}")
