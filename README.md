# IMBD_database
# Data Engineering
# Hunter Becker, Jacob Woolley, Kowsar Abdi, Samantha Eaton
This is for Project 3, doing the Data engineering side. Combining IMBD databases on ratings and a variety of criteria.
# Getting the dataset
  To obtain the dataset, start by accessing the unzipped TSV files from IMDb at the following URL: IMDb Datasets. Due to their large size, these files cannot be saved directly to GitHub. For a visual reference, you can view an image of the TSV files here. Once you have accessed the files, use the "IMDB.IPYNB" notebook to read in the TSV data.
# Pandas
  Using Pandas, convert the TSV files into CSV format. During this process, clean up the data to reduce the initial dataset from over a million entries to approximately 200,000 entries. Finally, export the cleaned data into new CSV files for further analysis.
# PostGres
  Utilize tableschema.SQL to create the tables in PostgreSQL, naming them title_basics and title_ratings. Once the tables are set up, upload the cleaned CSV files into the newly created PostgreSQL tables. Additionally, create an Entity-Relationship Diagram (ERD) to visually represent the relationships between the tables
  - ![Screenshot 2024-10-16 193004](https://github.com/user-attachments/assets/ffd747db-46f6-4221-8c16-7471e837e4d0)

# Back to Pandas
  To retrieve data from PostgreSQL back into the IPYNB, use SQLAlchemy along with psycopg2. Once you have the data, merge the title_basics and title_ratings tables using Pandas. Finally, implement a graphical user interface (GUI) using Tkinter to facilitate user interaction with the merged dataset.

# Ethical reasoning
This project is being used, purely, for educational purposes.
Not a commercial project
