Retail-sales-insights-using-SQL-and-Python
Project Overview:

This project is an end-to-end data analysis solution designed to extract critical business insights from retail sales data. We utilize Python for data processing and analysis, SQL for advanced querying, and structured problem-solving techniques to solve key business questions. The project is ideal for data analysts looking to develop skills in data manipulation, SQL querying, and data pipeline creation

1. Set Up the Environment
Tools Used:  Python, SQL
Goal: Create a structured workspace within VS Code and organize project folders for smooth development and data handling.

2. Set Up Kaggle API
API Setup: Obtain your Kaggle API token from Kaggle by navigating to your profile settings and downloading the JSON file.
Configure Kaggle:
Place the downloaded kaggle.json file in your local .kaggle folder.
Use the command kaggle datasets download -d <dataset-path> to pull datasets directly into your project.

3. Download retail Sales Data
Data Source: Use the Kaggle API to download the Walmart sales datasets from Kaggle.
Dataset Link: retail Sales Dataset
Storage: Save the data in the data/ folder for easy reference and access.

4. Install Required Libraries and Load Data
Libraries: Install necessary Python libraries using:
pip install pandas numpy sqlalchemy mysql-connector-python psycopg2
Loading Data: Read the data into a Pandas DataFrame for initial analysis and transformations.

5. Explore the Data
Goal: Conduct an initial data exploration to understand data distribution, check column names, types, and identify potential issues.
Analysis: Use functions like .info(), .describe(), and .head() to get a quick overview of the data structure and statistics.

6. Data Cleaning
Remove Duplicates: Identify and remove duplicate entries to avoid skewed results.
Handle Missing Values: Drop rows or columns with missing values if they are insignificant; fill values where essential.
Fix Data Types: Ensure all columns have consistent data types (e.g., dates as datetime, prices as float).
Currency Formatting: Use .replace() to handle and format currency values for analysis.
Validation: Check for any remaining inconsistencies and verify the cleaned data.

7. Feature Engineering
Create New Columns: Calculate the Total Amount for each transaction by multiplying unit_price by quantity and adding this as a new column.
Enhance Dataset: Adding this calculated field will streamline further SQL analysis and aggregation tasks.

9. Load Data into MsSQL
Set Up Connections: Connect to MS SQL and  load the cleaned data into each database.
Table Creation: Set up tables in MS SQL to automate table creation and data insertion.
Verification: Run initial SQL queries to confirm that the data has been loaded accurately.

9. SQL Analysis: Complex Queries and Business Problem Solving
Highest revenue generating Products
Highest selling products in each region
month over month growth comparison for 2022 and 2023 sales eg : jan 2022 vs jan 2023
For each category which month had highest sales
which sub category had highest growth by profit in 2023 compare to 2022
Documentation: Keep clear notes of each query's objective, approach, and results.
