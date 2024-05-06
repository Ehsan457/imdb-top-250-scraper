import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

'''
There is no need to use the logging module, 
but I use it because of my educational purpose. :)
'''


def create_soup(url):
    '''
    This function takes URL as input and returns a BeautifulSoup object.
    It uses headers to prevent any possible HTTP errors.
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL: {e}")

def parse_imdb_soup(soup):
    '''
    This function takes IMDb soup as input, parses it, and returns a list of top 250 movies
    with their informations.
    '''
    try:
        movie_list = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base")
        output = []
        for movie in movie_list:
            o = {}
            movie_link = movie.find("a", class_="ipc-title-link-wrapper").get("href")
            full_name = movie.find("h3", class_="ipc-title__text").text
            rank, name = full_name.split(".", 1)
            movie_info = movie.find_all("span", class_="sc-b189961a-8 kLaxqf cli-title-metadata-item")
            released_year = movie_info[0].text
            length = movie_info[1].text
            age_rating = movie_info[2].text if len(movie_info) == 3 else None
            score_info = movie.find("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text
            movie_score = score_info.split()[0]
            total_voters = score_info.split()[1].replace("(", "").replace(")", "")
            
            o["Rank"] = rank.strip()
            o["Movie_Name"] = name.strip()
            o["Released_Year"] = released_year.strip()
            o["Length"] = length.strip()
            o["Age_Rating"] = age_rating.strip() if age_rating else None
            o["Movie_Score"] = movie_score.strip()
            o["Total_Voters"] = total_voters.strip()
            o["Link"] = "https://www.imdb.com" + movie_link.strip()
            
            output.append(o)
        return output
    
    except Exception as e:
        logging.error(f"Error parsing IMDb soup:{e}")

def main():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    soup = create_soup(url)
    if soup:
        output = parse_imdb_soup(soup)
        if output:
            df = pd.DataFrame(output)
            # Save the output file as a CSV in the Output folder
            df.to_csv("imdb_top_250_movies.csv", index=False)
            logging.info("CSV file created.")
        else:
            logging.warning("No data found to create CSV.")
    else:
        logging.error("Failed to fetch IMDb URL.")

if __name__ == "__main__": 
    # Configure logging
    logging.basicConfig(filename='imdb_scraping.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    main()
