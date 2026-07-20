ETL Project Project Overview This project demonstrates an End-to-End ETL (Extract, Transform, Load) pipeline developed using Python. The project extracts data from CSV files and REST APIs, transforms and validates the data, cleans missing values, and loads the processed data into a SQLite database. The project also includes advanced concepts such as API pagination, SQLAlchemy ORM, Upsert operations, Pydantic models, logging, exception handling, and unit testing using Pytest. Features

Extract data from CSV files
Extract data from REST APIs
Transform data using Pandas
Validate data and detect missing values
Clean missing or invalid data
Load data into SQLite database
Use SQLAlchemy ORM for database operations
Implement Upsert functionality
Perform API Pagination
Use Pydantic for data validation
Implement Logging and Error Handling
Write Unit Tests using Pytest Technologies Used Python Pandas SQLite
SQLAlchemy Pydantic Pytest Git GitHub ETL Workflow CSV/API Data ↓ Extract Data ↓ Transform Data ↓ Validate Data ↓ Clean Data ↓ Load Data into SQLite Database ↓ Upsert Records ↓ API Pagination ↓ Unit Testing ↓ End-to-End Testing
Modules Explanation

Extract Module
Reads customer and payment data from CSV files.
Merges datasets using customer_id.
Transform Module
Performs data transformations.
Renames columns and formats data.
Validation Module
Checks for missing values.
Verifies data quality.
Data Cleaning Module
Replaces missing values with default values.
Cleans inconsistent records.
Load Module
Loads cleaned data into SQLite database.
API Extraction Module
Fetches data from REST APIs using Requests library.
Pagination Module
Retrieves API data page by page.
SQLAlchemy Module
Demonstrates ORM concepts.
Creates database models and performs CRUD operations.
Upsert Module
Updates existing records or inserts new records.
Testing Module
Performs unit testing using Pytest.
Ensures project reliability.


Team Members


Adudodla Sreeja
kadam Geethanjali
Patro Bhanupraksh
Sanapala Purna Sai Chandu
GitHub Repository This project is maintained using Git and GitHub for version control and collaboration.

