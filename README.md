# MIT People Directory web scraper

## Dependencies
This uses the BeautifulSoup package.
- `pip install BeautifulSoup` for Python 2
- `pip install bs4` for Python 3

This code runs with both Python 2 and 3.

## Files
- `MITpeople.py` (The web scraper)
- `MITpeople_script.py` (Command line tool for using the scraper)

## Usage
Import `MITpeople` to use in another Python program.
Usage should be clear from the documentation.

The simple usage of the script is as follows.  
`python /path/to/MITpeople_script.py barryam3`

As this command is long, I recommend creating an executable shell script.  
For example, on Mac OS, I have the file `/usr/local/bin/mitpeople`  
Which contains the following command:  
`python ~/path/to/MITpeople_script.py "$@"`  
And then from anywhere I can do:  
`mitpeople barryam3`

## Caveats
This web scraper gets information from the publicly-available [MIT People Directory](http://web.mit.edu/people.html). If the structure of that site ever changes, this tool will probably stop working.
