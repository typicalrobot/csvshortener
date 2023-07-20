# csvshortener
Importing necessary modules: The script begins by importing the necessary Python modules: pandas, requests, and pyshorteners.

Loading the CSV file: The pandas library's read_csv function is used to load a CSV file that contains the URLs to be shortened. The file path is specified in the function.

Prepare data structure: An empty list called data is initialized. This list will be used to store the rows of the dataframe, each with a new column for the shortened URL.

Shorten URLs: The script then creates a shortener object using the pyshorteners library.

Iterating over rows: The script uses a for loop to iterate over each row of the dataframe.

URL shortening: Within the loop, the script retrieves the URL from the 'Website' column of the current row, shortens the URL using the TinyURL service, and then adds the shortened URL to the 'shorten_url' column of the row.

Storing results: The row, now with the added 'shorten_url' column, is appended to the 'data' list.

Create new DataFrame: After all URLs have been shortened, a new DataFrame is created from the 'data' list.

Saving to CSV: Finally, the new DataFrame, containing both the original and the shortened URLs, is saved into a new CSV file using the to_csv function. The path to the new file is specified in the function.
