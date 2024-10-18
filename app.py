import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# File path
input_file = 'Resources/CSV/imdb_merged.csv'

# Read the CSV file
new_imdb_df = pd.read_csv(input_file)

# Function to update the Treeview based on filter, sorting, and genre checkboxes
def update_treeview(title_filter=None, title_match_type=None, sort_column=None, sort_order=None, 
                    min_rating=None, min_votes=None, min_year=None, max_year=None, 
                    min_runtime=None, max_runtime=None):
    for row in treeview.get_children():
        treeview.delete(row)  # Clear existing rows
    
    filtered_df = new_imdb_df.copy()
    
    # Apply genre filters based on checkbox states
    genre_filters = {col: var.get() for col, var in genre_vars.items() if var.get() == 1}
    for genre in genre_filters.keys():
        filtered_df = filtered_df[filtered_df[genre] == 1]

    # Apply title filtering
    if title_filter:
        if title_match_type == 'Exact Matches':
            filtered_df = filtered_df[filtered_df['title'].str.lower() == title_filter.lower()]
        elif title_match_type == 'Starts With':
            filtered_df = filtered_df[filtered_df['title'].str.lower().str.startswith(title_filter.lower())]
        elif title_match_type == 'Contains':
            filtered_df = filtered_df[filtered_df['title'].str.lower().str.contains(title_filter.lower())]

    # Additional filtering on min/max values
    if min_rating:
        filtered_df = filtered_df[filtered_df['averagerating'] >= float(min_rating)]
    if min_votes:
        filtered_df = filtered_df[filtered_df['numvotes'] >= int(min_votes)]
    if min_year:
        filtered_df = filtered_df[filtered_df['year'] >= int(min_year)]
    if max_year:
        filtered_df = filtered_df[filtered_df['year'] <= int(max_year)]
    if min_runtime:
        filtered_df = filtered_df[filtered_df['runtimeminutes'] >= int(min_runtime)]
    if max_runtime:
        filtered_df = filtered_df[filtered_df['runtimeminutes'] <= int(max_runtime)]

    # Apply sorting if specified
    if sort_column and sort_column in filtered_df.columns:
        ascending = (sort_order == 'Ascending')
        
        # Handle numeric and string sorting
        if sort_column in ['year', 'runtimeminutes', 'averagerating', 'numvotes']:
            filtered_df = filtered_df.sort_values(by=sort_column, ascending=ascending, key=lambda x: pd.to_numeric(x, errors='coerce'))
        else:
            filtered_df = filtered_df.sort_values(by=sort_column, ascending=ascending)

    # Insert the filtered and sorted data into the treeview (excluding 'tconst')
    for _, row in filtered_df.iterrows():
        treeview.insert('', 'end', values=(row['title'], row['year'], 
                                            row['runtimeminutes'], row['averagerating'], row['numvotes']))



# Function to export the current view to a CSV file
def export_to_csv():
    rows = treeview.get_children()
    data = [treeview.item(row)['values'] for row in rows]
    
    if not data:
        messagebox.showwarning("Export Error", "No data to export.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                               filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if file_path:
        df = pd.DataFrame(data, columns=['Title', 'Start Year', 'Runtime (min)', 'Average Rating', 'Number of Votes'])
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Export Successful", "Data exported successfully!")

# Set up the GUI
root = tk.Tk()
root.title("IMDB Movie Info")

# Create a frame for the filter
filter_frame = ttk.Frame(root)
filter_frame.pack(pady=10)

# Title filter
title_filter_label = tk.Label(filter_frame, text="Title Filter:")
title_filter_label.grid(row=0, column=0)

title_filter_entry = tk.Entry(filter_frame)
title_filter_entry.grid(row=0, column=1)

title_match_type_label = tk.Label(filter_frame, text="Match Type:")
title_match_type_label.grid(row=0, column=2)

title_match_type_combobox = ttk.Combobox(filter_frame, values=['Exact Matches', 'Starts With', 'Contains'])
title_match_type_combobox.grid(row=0, column=3)

# Year filters
min_year_label = tk.Label(filter_frame, text="Min Year:")
min_year_label.grid(row=1, column=0)

min_year_entry = tk.Entry(filter_frame)
min_year_entry.grid(row=1, column=1)

max_year_label = tk.Label(filter_frame, text="Max Year:")
max_year_label.grid(row=1, column=2)

max_year_entry = tk.Entry(filter_frame)
max_year_entry.grid(row=1, column=3)

# Runtime filters
min_runtime_label = tk.Label(filter_frame, text="Min Runtime (min):")
min_runtime_label.grid(row=2, column=0)

min_runtime_entry = tk.Entry(filter_frame)
min_runtime_entry.grid(row=2, column=1)

max_runtime_label = tk.Label(filter_frame, text="Max Runtime (min):")
max_runtime_label.grid(row=2, column=2)

max_runtime_entry = tk.Entry(filter_frame)
max_runtime_entry.grid(row=2, column=3)

# Rating and votes filters
min_rating_label = tk.Label(filter_frame, text="Min Rating:")
min_rating_label.grid(row=3, column=0)

min_rating_entry = tk.Entry(filter_frame)
min_rating_entry.grid(row=3, column=1)

min_votes_label = tk.Label(filter_frame, text="Min Votes:")
min_votes_label.grid(row=3, column=2)

min_votes_entry = tk.Entry(filter_frame)
min_votes_entry.grid(row=3, column=3)

# Apply Filter button
apply_filter_button = tk.Button(filter_frame, text="Apply Filter", command=lambda: update_treeview(
    title_filter_entry.get(), 
    title_match_type_combobox.get(), 
    sort_column_combobox.get(), 
    sort_order.get(), 
    min_rating_entry.get(), 
    min_votes_entry.get(), 
    min_year_entry.get(), 
    max_year_entry.get(), 
    min_runtime_entry.get(), 
    max_runtime_entry.get()
))
apply_filter_button.grid(row=4, columnspan=4, pady=10)

# Sort buttons
sort_frame = ttk.Frame(root)
sort_frame.pack(pady=10)

sort_label = tk.Label(sort_frame, text="Sort By:")
sort_label.grid(row=0, column=0)

sort_column_combobox = ttk.Combobox(sort_frame, values=['title', 'year', 'runtimeminutes', 'averagerating', 'numvotes'])
sort_column_combobox.grid(row=0, column=1)

# Store the current sort order
sort_order = tk.StringVar(value='Ascending')  # Default sort order

ascending_button = tk.Button(sort_frame, text="Sort Ascending", command=lambda: update_treeview(
    title_filter_entry.get(), 
    title_match_type_combobox.get(), 
    sort_column_combobox.get(), 
    'Ascending', 
    min_rating_entry.get(), 
    min_votes_entry.get(), 
    min_year_entry.get(), 
    max_year_entry.get(), 
    min_runtime_entry.get(), 
    max_runtime_entry.get()
))
ascending_button.grid(row=0, column=2)

descending_button = tk.Button(sort_frame, text="Sort Descending", command=lambda: update_treeview(
    title_filter_entry.get(), 
    title_match_type_combobox.get(), 
    sort_column_combobox.get(), 
    'Descending', 
    min_rating_entry.get(), 
    min_votes_entry.get(), 
    min_year_entry.get(), 
    max_year_entry.get(), 
    min_runtime_entry.get(), 
    max_runtime_entry.get()
))
descending_button.grid(row=0, column=3)

# Export CSV button
export_button = tk.Button(root, text="Export to CSV", command=export_to_csv)
export_button.pack(pady=10)

# Create checkboxes for each genre column, arranged in alphabetical order
genre_frame = ttk.Frame(root)
genre_frame.pack(pady=10)

genre_vars = {}
genre_columns = sorted(['documentary', 'drama', 'mystery', 'romance', 'adventure',
                        'war', 'western', 'musical', 'comedy', 'thriller', 'crime', 'filmnoir',
                        'history', 'biography', 'fantasy', 'action', 'sport', 'family', 'music',
                        'horror', 'animation', 'scifi', 'news', 'talkshow', 'realitytv',
                        'gameshow'])

for i, col in enumerate(genre_columns):  # Loop through the genres
    var = tk.IntVar()
    checkbox = tk.Checkbutton(genre_frame, text=col, variable=var, command=lambda: update_treeview(
        title_filter_entry.get(), 
        title_match_type_combobox.get(), 
        sort_column_combobox.get(), 
        sort_order.get(), 
        min_rating_entry.get(), 
        min_votes_entry.get(), 
        min_year_entry.get(), 
        max_year_entry.get(), 
        min_runtime_entry.get(), 
        max_runtime_entry.get()
    ))
    checkbox.grid(row=i // 9, column=i % 9)  # Arrange in rows of 9
    genre_vars[col] = var  # Store the variable to check its state later

# Create the Treeview, excluding 'tconst'
treeview = ttk.Treeview(root, columns=('title', 'year', 'runtimeminutes', 'averagerating', 'numvotes'), show='headings')
treeview.pack(fill='both', expand=True)

# Set column headings and widths
treeview.heading('title', text='Title')
treeview.heading('year', text='Start Year')
treeview.heading('runtimeminutes', text='Runtime (min)')
treeview.heading('averagerating', text='Average Rating')
treeview.heading('numvotes', text='Number of Votes')

# Initialize the Treeview with all data
update_treeview()

# Start the main loop
root.mainloop()
