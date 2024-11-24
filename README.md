Overview
The tasks involved working with data from a public API, structuring it, and storing it in a manageable format. The primary focus was on fetching country-related data from the REST API https://restcountries.com/v3.1/all, processing it, and then storing it in a database. Additionally, the solution included functionality for identifying and updating existing data to ensure the database stays consistent and up-to-date during repeated runs of the script. Finally, SQL queries were crafted to extract meaningful insights from the database.
 
Task 2: Parsing JSON and Storing in a Database
The objective was to parse JSON data from the API and store the relevant fields into an SQLite database. The process included:
1.	Fetching Data: A Python script was developed to perform an HTTP GET request to retrieve all countries' data from the REST API.
2.	Data Processing: The script extracted specific fields for each country, including:
o	cca2, cca3, cioc: Country codes.
o	name.common, name.official: Common and official country names.
o	capital, region, subregion: Geographic information.
o	languages: A list of official languages for each country.
o	area: Land area in square kilometers.
o	population: Total population.
3.	Database Design: An SQLite database was created with a table called countries, structured to store the extracted fields. The schema included constraints to maintain data integrity, such as making the cca2 field unique.
4.	Data Insertion: Each country's data was inserted into the database. To handle duplicate or updated data, the UNIQUE constraint on the cca2 field, paired with ON CONFLICT REPLACE, ensured that existing records were replaced if conflicts arose during insertion.
 
Task 3: Querying the Database for Insights
This task extended the functionality of Task 2 by adding SQL queries to derive meaningful insights:
1.	Sum of Populations for English-speaking Countries:
o	A query calculated the total population of all countries where English was listed as an official language. The query matched languages fields containing "English" and aggregated their populations.
2.	Subregions and Country Counts:
o	Another query grouped countries by their subregions and counted the number of unique countries in each subregion. This helped identify the geographic distribution of countries at a subregional level.
3.	Countries with Multiple Official Languages:
o	A query identified countries with more than one official language. By counting line breaks (“ ”) in the languages field, the query determined the number of languages listed for each country and filtered those with more than one.
 
Key Features and Benefits
•	Data Consistency: The use of ON CONFLICT REPLACE ensures the database always reflects the latest data from the API.
•	Flexibility: The SQLite database format was chosen for its simplicity and wide compatibility, allowing the results to be easily viewed and queried in tools like VS Code.
•	Scalability: The database structure and queries are designed to handle large datasets efficiently, enabling potential expansions such as additional fields or new queries.
