# web_table_extractor
 Handy input/output script for scraping table data from web pages

I work a lot with web page based tables for bringing in data for my projects. Because of this, I wanted a straight forward i/o script where I didn't have to change variable names in the code every time I needed data from a new table.

To use this script you need three things:
1. A path for the file to be stored in. Ex; /path/to/folder/file_name.csv
2. The website url to take the table from
3. Which table it is. 1, 2, 3 etc.

Simply run the script with no arguments and you will be asked input this information one by one. Afterwards it will print a preview of the table and confirm the save location. If everything looks correct, input y and you'll have your data in csv form.