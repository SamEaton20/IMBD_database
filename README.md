# IMBD_database
# Data Engineering
# Hunter Becker, Jacob Woolley, Kowsar Abdi, Samantha Eaton
This is for Project 3, doing the Data engineering side. Combining IMBD databases and comparing movies on ratings and a variety of criteria.
# Getting the dataset
  To obtain the dataset, start by accessing the unzipped TSV files from IMDb at the following URL: [IMDb Datasets](https://datasets.imdbws.com/). Due to their large size, these files cannot be saved directly to GitHub. Once you have accessed the files place them in a folder labeled 'TSV' in the resources folder, use the "IMDB.ipynb" notebook to read in the TSV data.
  ![TSV's](https://github.com/user-attachments/assets/ff78d1b8-8f4f-4fe7-90ad-9dbb0e3c3f9e)

# Pandas
  Using Pandas in the ipynb, convert the TSV files into CSV format. During this process, follow the notebook to clean up the data to reduce the initial dataset from over a million entries to approximately 200,000 entries. Finally, export the cleaned data into new CSV files for Postgres.
# PostGres
  Utilize tableschema.SQL to create the tables in PostgreSQL, naming them title_basics and title_ratings. Once the tables are set up, upload the cleaned CSV files into the newly created PostgreSQL tables. Additionally, create an Entity-Relationship Diagram (ERD) to represent the relationships between the tables visually.
  - ![Screenshot 2024-10-16 193004](https://github.com/user-attachments/assets/ffd747db-46f6-4221-8c16-7471e837e4d0)

# Back to Pandas
  To retrieve data from PostgreSQL back into the IPYNB, use SQLAlchemy along with psycopg2. Edit the config.py to connect the code to your own Postgres server. Once you have the data, use the notebook to merge the title_basics and title_ratings tables using Pandas. Finally, implement a graphical user interface (GUI) using Tkinter to facilitate user interaction with the merged dataset.

# Ethical reasoning
This project is being used, purely, for educational purposes. As such, this is within the allowed uses of IMDbs non-commercial datasets. All code is original and sources for additional information that was utilized are listed below. 

# References
- ChatGPT
- Tkinter: https://docs.python.org/3/library/tk.html
