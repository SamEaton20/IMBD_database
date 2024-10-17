# IMBD_database
# Data Engineering
# Hunter Becker, Jacob Woolley, Kowsar Abdi, Samantha Eaton
This is for Project 3, doing the Data engineering side. Combining IMBD databases on ratings and a variety of criteria.
# Getting the dataset
  - Get the TSV files from IMBD
      - Use this URL to get the unzipped TSV files (The files are too big to save on to GitHub.)
          - https://datasets.imdbws.com/
          - ![TSV's](https://github.com/user-attachments/assets/e82d2dfd-2b00-4d02-b2c6-880bb1e08336)
          - using IMDB.IPYNB read in the TSV files
# Pandas
  - Convert TSV files into CSV files in Pandas
  - Clean up the data
    - Went from over a million entries to around 200,000 entries
  - Output the data into cleaned CSV files
# PostGres
  - Use tableschema.SQL to create the tables in PostGres
    - Table names being title_basics and title_ratings
  - Upload created CSV's into newly created Postgres tables
  - Create an ERD for the tables
  - ![Screenshot 2024-10-16 193004](https://github.com/user-attachments/assets/ffd747db-46f6-4221-8c16-7471e837e4d0)

# Back to Pandas
  - Get data back from PostGres into the IPYNB using SQLAlchemy and psycopg2
  - Merge the tables, title_basics and title_ratings, in Pandas
  - Use tkinter code to create a GUI

# Ethical reasoning
This project is being used, purely, for educational purposes.
Not a commercial project
