import csv
from io import StringIO

# Example CSV content based on the user's description
csv_content = """id,title,note,excerpt,url,folder,tags,created,cover,highlights
683178424,When Idiot Savants Do Climate Economics,,How an elite clique of math-addled economists hijacked climate policy.,https://theintercept.com/2023/10/29/william-nordhaus-climate-economics/,Unsorted,"nordhaus, climate",2023-11-23T09:13:03.212Z,https://theintercept.com/wp-content/uploads/2023/10/GettyImages-1047733276-ft.jpg?fit=4096%2C2048&w=2048,
"""

# Convert the example CSV content to a StringIO object so it can be read like a file
csv_file_like_object = StringIO(csv_content)

# Read the example CSV content into a DataFrame
original_df = pd.read_csv(csv_file_like_object)

# Now, let's create the conversion function based on the provided example
def convert_csv_to_omnivore_format(df):
    # Conversion of date to Unix timestamp in milliseconds
    df['saved_at'] = pd.to_datetime(df['created']).astype(int) / 10**6

    # Preparing the labels
    df['labels'] = df['tags'].apply(lambda x: f"[{x}]" if pd.notnull(x) and x.strip() != '' else '[]')

    # Creating the new DataFrame for Omnivore format
    omnivore_df = pd.DataFrame({
        'url': df['url'],
        'state': 'ARCHIVED',  # Assuming all entries should be set as ARCHIVED
        'labels': df['labels'],
        'saved_at': df['saved_at'],
        'published_at': ''  # Assuming there's no published_at information
    })

    return omnivore_df

# Convert the original DataFrame to the Omnivore format
omnivore_df = convert_csv_to_omnivore_format(original_df)

# Display the first few rows of the converted DataFrame
omnivore_df.head()
