import os
import pandas as pd

# Define the path to the Excel file and the metadata directory
excel_path = os.path.expanduser("Excel file path")
metadata_dir = os.path.expanduser("Metadata file")

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_path, engine='openpyxl')

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    language = row['language']
    name = row['name']
    subtitle = row['subtitle']
    keywords = row['keywords']
    privacy = row['privacy_url']
    support = row['support_url']
    description = row['description']

    # Generate the path to the language-specific folder within the metadata directory
    lang_folder = os.path.join(metadata_dir, language)

    # If the folder doesn't exist, create it
    if not os.path.exists(lang_folder):
        os.makedirs(lang_folder)

    # Create or update the name.txt, subtitle.txt, keywords.txt, description.txt,"privacy_url.txt" & "support_url.txt" files
    for filename, content in [("name.txt", name), ("subtitle.txt", subtitle), ("keywords.txt", keywords),("description.txt", description),("privacy_url.txt", privacy),("support_url.txt", support)]:
        file_path = os.path.join(lang_folder, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(content))

print("Metadata files have been updated successfully.")
