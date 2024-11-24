import requests
import sqlite3

# URL API
url = "https://restcountries.com/v3.1/all"

# Выполняем запрос
response = requests.get(url)
if response.status_code == 200:
    countries = response.json()
else:
    print("Ошибка запроса:", response.status_code)
    exit()

# Подключение к SQLite
conn = sqlite3.connect("countries.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cca2 TEXT,
    cca3 TEXT,
    cioc TEXT,
    name_common TEXT,
    name_official TEXT,
    capital TEXT,
    region TEXT,
    subregion TEXT,
    languages TEXT,
    area REAL,
    population INTEGER,
    UNIQUE(cca2) ON CONFLICT REPLACE
)
""")

# Обновление/вставка данных в таблицу
for country in countries:
    languages = "\n".join(country.get("languages", {}).values())
    cursor.execute("""
    INSERT INTO countries (cca2, cca3, cioc, name_common, name_official, capital, region, subregion, languages, area, population)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        country.get("cca2", ""),
        country.get("cca3", ""),
        country.get("cioc", ""),
        country.get("name", {}).get("common", ""),
        country.get("name", {}).get("official", ""),
        ", ".join(country.get("capital", [])),
        country.get("region", ""),
        country.get("subregion", ""),
        languages,
        country.get("area", ""),
        country.get("population", 0)
    ))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Данные успешно обновлены в базе данных countries.db")
