import pandas as pd

# Load the Excel file
file_path = 'db2.xlsx'  # مسیر فایل اکسل خود را به درستی وارد کنید
excel_data = pd.ExcelFile(file_path)

# Read the specific sheets into dataframes
kanon_df = excel_data.parse('dataset')
kol_df = excel_data.parse('total')

# Get unique values from the specified columns in each sheet and drop empty cells
kanon_unique_reshte_name = kanon_df['reshte_name'].dropna().drop_duplicates().reset_index(drop=True)
kanon_unique_university_name = kanon_df['university_name'].dropna().drop_duplicates().reset_index(drop=True)
kol_unique_reshte = kol_df['reshte'].dropna().drop_duplicates().reset_index(drop=True)
kol_unique_university = kol_df['university'].dropna().drop_duplicates().reset_index(drop=True)

# Find the maximum length of the unique columns
max_length = max(len(kanon_unique_reshte_name), len(kanon_unique_university_name), len(kol_unique_reshte), len(kol_unique_university))

# Extend the shorter series with empty strings to match the max length
kanon_unique_reshte_name = kanon_unique_reshte_name.reindex(range(max_length), fill_value='')
kanon_unique_university_name = kanon_unique_university_name.reindex(range(max_length), fill_value='')
kol_unique_reshte = kol_unique_reshte.reindex(range(max_length), fill_value='')
kol_unique_university = kol_unique_university.reindex(range(max_length), fill_value='')

# Create a new dataframe for the unique values
unique_df = pd.DataFrame({
    'reshte_name': kanon_unique_reshte_name,
    'university_name': kanon_unique_university_name,
    'reshte': kol_unique_reshte,
    'university': kol_unique_university
})

# Write the unique values to a new sheet in the Excel file
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    unique_df.to_excel(writer, sheet_name='unique', index=False)

print("Unique sheet created successfully.")
