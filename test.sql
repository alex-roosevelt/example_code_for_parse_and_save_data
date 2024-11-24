-- Сумма популяций стран, где говорят на английском
SELECT SUM(population) AS total_population
FROM countries
WHERE languages LIKE '%English%';

-- Количество стран в каждом саб-регионе
SELECT subregion, COUNT(DISTINCT cca2) AS country_count
FROM countries
GROUP BY subregion
ORDER BY country_count DESC;

-- Страны, где говорят больше чем на одном языке
SELECT name_common, languages
FROM countries
WHERE LENGTH(languages) - LENGTH(REPLACE(languages, ' ', '')) + 1 > 1;
