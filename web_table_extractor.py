# ensure required packages are in your environment
from requests_html import HTMLSession
from pathlib import Path
import pandas as pd

# establish header and session for web scraping
session = HTMLSession()
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/605.1.15 (KHTML, "
                        "like Gecko) Version/14.1.2 Safari/605.1.15"}


# main function that takes an optional input set to true by default to use html_to_pandas over web scraping.
def main():
    # request user to input file name that csv will be saved as
    file_name = input('Input file name. Ex. Path/to/folder/file_name.csv\n')
    # check that it ends in .csv
    if file_name[-4:] == '.csv':
        pass
    # if it doesn't, it will
    else:
        file_name = file_name + '.csv'

    # Path file_name for cross platform use
    Path(file_name)
    # request web page holding table
    input_url = input('Input url to web page holding table:\n')

    # extracts table using pandas and saves as csv to the path specified using user input.
    # this will overwrite where that path is pointing to.
    def html_to_csv(url):
        # ask user to input what number table they want on the web page
        table_number = input("What number table is it? For example, enter 2 if it is the second table on the web "
                             "page.\n")
        # convert table number input to integer
        table_number = int(table_number)
        # variable to hold the table that pandas extracts from given url, stored as a list with 1 entry
        table = pd.read_html(url)
        # print the extracted table to be approved for saving by user
        print(table[table_number - 1])
        # require user input as to if the correct table was extracted
        answer = input('Does this table look correct?\n [y/n]')
        # if yes, save as csv in user defined
        if answer == 'y':
            table[table_number - 1].to_csv(file_name, sep=',')
        # if no, ask user to check table numbering and quit
        elif answer == 'n':
            print('Ensure table numbering was correct')
        # quit
        else:
            print('Invalid entry. Quitting process.')

    html_to_csv(input_url)


if __name__ == "__main__":
    main()