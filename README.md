
# CSV Converter for Omnivore

This is a ChatGPT4 generated script to convert csv export of all bookmarks on Raindrop to the format needed by Omnivore. If there are a lot of bookmarks, you can't just drag and drop the generated file to Omnivore, but you must use the upload method described here https://github.com/omnivore-app/import-demo .  

Rest of the Readme is also generated by ChatGPT4. 

This Python script takes a CSV input via STDIN, converts the data to a specific format for Omnivore import, ensures that all URLs are unique by removing duplicates, and outputs the result to STDOUT.

## Features

- Reads CSV input from STDIN.
- Outputs converted CSV to STDOUT.
- Removes duplicate URLs, ensuring uniqueness.
- Converts date to Unix timestamp in milliseconds.
- Formats tags into a list of labels.

## Requirements

- Python 3
- Pandas library

## Usage

To use the script, you can use the following command in a Unix-like command-line environment:

```bash
cat path_to_your_input_csv.csv | python raindrop_to_omnivore.py >import.csv
```

Make sure to replace `path_to_your_input_csv.csv` with the actual path to your CSV file.

## Input CSV Format

The script expects the input CSV to have the following columns:

- id
- title
- note
- excerpt
- url
- folder
- tags
- created
- cover
- highlights

## Output CSV Format

The output CSV will have the following columns:

- url
- state
- labels
- saved_at
- published_at

The `state` column is set to `ARCHIVED`, and the `published_at` column will be empty as it's not provided in the input.

## Contributing

Feel free to fork this project and submit a pull request if you have any improvements or fixes.

## License

This script is released under the MIT License.
