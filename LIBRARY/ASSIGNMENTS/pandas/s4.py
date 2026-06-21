"""
1.
Download a sample CSV file of IPL cricket match scores from Kaggle or any public dataset, and use pd.read_csv() to load it into a DataFrame. Print the first 5 rows to verify the data.
2.
Find a small JSON dataset of trending songs (for example, from Spotify's API samples or any open JSON file), and use pd.read_json() to import it into a DataFrame. Display the DataFrame's column names and data types using df.info().
3.
You have a TSV (tab-separated values) file containing Zomato restaurant data. Use pd.read_csv() with the correct separator to load the data, and then use df.describe(include='all') to generate summary statistics.<br><br><em><strong>Hint:</strong> The separator for TSV files is '\t'.</em>
4.
Download a large Excel file (at least 10,000 rows) of Flipkart product listings. Use pd.read_excel() with the chunksize parameter to read the file in chunks of 2000 rows, and print the number of rows in each chunk as you iterate.
5.
Use ChatGPT or Copilot to generate a Python code snippet that reads a semicolon-separated CSV of Paytm transactions, detects missing values, and prints out which columns have nulls. Test the code with a small sample file and fix any errors you encounter.
"""