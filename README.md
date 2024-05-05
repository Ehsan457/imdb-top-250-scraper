# IMDb Top 250 Movies Scraper

## Description
This is a simple crawler that crawl and scrapes the IMDb Top 250 Movies list and generates a CSV file with details of each movie, including rank, title, release year, length, age rating, score, and link to the IMDb page.
This project is intended for educational purposes.

## Requirements
- Python 3.x
- requests
- BeautifulSoup
- pandas

   
   
## Running Scripts
To run this script, you can create and activate the virtual environment and then install dependencies via requirement.txt file.
for doing that open a terminal, change directory the the place you want clone the repository.
do the following commands in your terminal:

1. First create a virtual environment, here you can install and use virtualenv:

install virtualenv using pip:
```bash
pip install virtualenv
```
create your environment:
```bash
virtualenv imdbcrawlerenv
```
then activate your environment:
```bash
source ./imdbcrawlerenv/bin/activate
```

3. You can then clone the repository using this command:

```bash
git clone https://github.com/Ehsan457/weather-app.git
```

3. Install dependencies with this command:
```bash
pip install -r requirements.txt
```

4. Finally, you can modify the config file according to your needs and run the scripts. For ease of use, simply run createDB.py followed by createTable.py, and then run main.py to store the data in your database.

  
