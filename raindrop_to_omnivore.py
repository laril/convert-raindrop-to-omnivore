
import sys
import pandas as pd
from datetime import datetime
import time

def convert_to_unix(timestamp):
    '''Converts ISO 8601 timestamp to Unix timestamp in milliseconds'''
    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    unix_time = int(time.mktime(dt.timetuple()) * 1000)
    return unix_time

def format_labels(labels):
    '''Formats labels for the Omnivore CSV'''
    if pd.isna(labels) or labels.strip() == "":
        return ""
    labels_list = [label.strip() for label in labels.split(',')]
    formatted_labels = '[' + ', '.join(f'"{label}"' for label in labels_list) + ']'
    return formatted_labels

def convert_csv(input_csv):
    # Read the CSV content from STDIN
    df = pd.read_csv(input_csv)

    # Remove duplicate URLs
    df = df.drop_duplicates(subset='url', keep='first')

    # Convert 'created' date to Unix timestamp
    df['saved_at'] = df['created'].apply(convert_to_unix)

    # Format the labels
    df['labels'] = df['tags'].apply(format_labels)

    # Prepare the new DataFrame
    omnivore_df = pd.DataFrame({
        'url': df['url'],
        'state': 'ARCHIVED',
        'labels': df['labels'],
        'saved_at': df['saved_at'],
        'published_at': ''  # Assuming there's no published_at information
    })

    # Output the new DataFrame to STDOUT
    omnivore_df.to_csv(sys.stdout, index=False)

# Read from STDIN
input_csv_content = sys.stdin
convert_csv(input_csv_content)
