# violence-Brazil-scraper

violence-Brazil-scraper is a script written to scrape Brazilian newspaper articles and filter for articles containing violence or police incidents for the UCSD URL Summer 2024 program with Idaliya Grigoryeva. This is part 1 of the scraping program by Cyrene, and it focuses on expanding the capacity of articles scraped using O'Globo's dynamic Most Recent articles page. My partner Affaan focuses on part 2: filtering article content input using AI models.

## Installation

Create a virtual environment and activate. Ensure that you are using a version 3+ of Python.
`python3 -m venv scrapevenv`
`source scrapevenv/bin/activate`

Use the package manager [pip] or [pip3] to install requests. It is possible that this package name has changed, so follow the directions given if it says to install a different package.

`pip3 install requests-html`

## Usage

The main program runs in `initial.py` and is executed using a bash script `test.sh`. `initial2.py` and other number initial.py/test.sh files are for running alternative number of articles simultaneously.

### Changing the output file names

Note that this process can be better automated using input from the command line.

Navigate to `initial.py` and change `csv_output_file` variable and `scrapeNum` variable (lines 21-22) to determine what csv file you would like to output to and the number of articles you would like to scrape.

```python
csv_output_file = 'clean_articles14.csv' # name of the csv file to output to
scrapeNum = 100 # number of articles you want to scrape
```
Navigate to `test.sh` and change `output14.txt` (line 6) to what output file you would like for the initial list of articles from "Most Recent".

```bash
python3 initial.py > output14.txt
# name of output file to output to for first loop of article name and link extraction
```

### Running the program

Run the `test.sh` bash script using `bash test.sh`.

## Contributing

### Future Development

Test cases need to be written to better test the program.

The `initial.py` script can be cleaned up by better automating renaming the output and csv files by implementing input from the command line and creating individual methods.

The main concern of the program for future development is the runtime. Scraping ~5000 articles usually requires running the script overnight (~8 hours) to finish. This can be improved by making the script more efficient and reducing looping and accessing the articles websites. I attempted to use a server to run the script, which reduced runtime 2x, but due to memory limitations, I was unable to fully extract a csv file with a greater capacity of articles. However, I was able to get the output file in my attempt to execute with 10,000 articles. So, the next step for development is to use a server with sufficient memory to execute with large quantities of articles.

However, 10,000 articles only scrapes ~1 month of articles, so attempting to scrape potentially years of data would require much greater runtime and memory, which would need to be resolved through efficiency or other methods.

I have not currently tested setting the initial page != 1, but this can be tested to see if articles from years prior can be accessed.

To duplicate the program to another news publisher, some edits may need to be made regarding where text is stored in the website HTML.

The script was initially implemented with Google Sheets API to scrape article data into a Google Sheet. However, when using this format, I found that accessing the API too many times (i.e. scraping too many articles) caused the script to break because the API prohibited this. The credentials were initially stored in `creds.json` but these credentials are now invalid due to the repository being public at one point, but they can be changed to reimplement the Google Sheets API if the API access issue can be resolved.

Currently, the script outputs a csv file, which can be imported into Google Sheets (preferred) or Excel.

Contact cyrenexwang@gmail.com or cyw007@ucsd.edu if you have any questions about the program.
