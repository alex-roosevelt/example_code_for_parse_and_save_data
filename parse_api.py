import requests
import csv

# URL API
url = "https://restcountries.com/v3.1/all"

# Выполняем запрос
response = requests.get(url)
if response.status_code == 200:
    countries = response.json()
else:
    print("Ошибка запроса:", response.status_code)
    exit()

# Открываем CSV файл для записи
with open("countries.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "cca2", "cca3", "cioc", "name.common", "name.official",
        "capital", "region", "subregion", "languages", "area", "population"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for country in countries:
        # Извлекаем данные
        row = {
            "cca2": country.get("cca2", ""),
            "cca3": country.get("cca3", ""),
            "cioc": country.get("cioc", ""),
            "name.common": country.get("name", {}).get("common", ""),
            "name.official": country.get("name", {}).get("official", ""),
            "capital": ", ".join(country.get("capital", [])),
            "region": country.get("region", ""),
            "subregion": country.get("subregion", ""),
            "languages": "\n".join(country.get("languages", {}).values()),
            "area": country.get("area", ""),
            "population": country.get("population", "")
        }
        # Записываем строку в файл
        writer.writerow(row)

print("Данные успешно записаны в файл countries.csv")
