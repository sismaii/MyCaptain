# web scrapping
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import connect # importing the other file(connect.py)

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help = 'Enter the number of pages to parse', type = int)
parser.add_argument("--dbname", help = 'Enter the name of db', type = str )
args = parser.parse_args()

oyo_url = 'https://www.oyorooms.com/hotels-in-bangalore/?page='
page_num_max = args.page_num_max
scrapped_info_list = []
connect.connect(args.dbname)

for page_num in range(1,page_num_max):

    req = rq.get(oyo_url + str(page_num))
    content = req.content

    soup = BeautifulSoup(content, "html.parser")
    all_hotels = soup.find_all("div", {'class':'hotelCardlisting'})

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict['name'] = hotel.find('h3', {'class' : 'listingHotelDescription_hotelName'}).text
        hotel_dict['address'] = hotel.find('span', {'itemprop': 'streetAddress'}).text
        hotel_dict['price'] = hotel.find('span', {'class': 'listingprice__finalprice'}).text
        # try ... except
        try:
            hotel_dict['rating'] = hotel.find('span', {'class' : 'hotelRating_ratingSummary'}).text
        except AttributeError:
            hotel_dict['rating'] = None

        parent_amenities_element = hotel.find("div", {'class' : 'amenityWrapper'})

        amenities_list = []
        for amenity in parent_amenities_element.find_all("div", {'class' : 'amenityWrapper__amenity'}):
            amenities_list.append(amenity.find('span', {'class' : 'd_body_sm'}).text.strip())

        hotel_dict['amenities'] = ', '.join(amenities_list[:-1])

        scrapped_info_list.append(hotel_dict)

        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))

        # print(hotel_name,hotel_address,hotel_price,hotel_rating)


connect.get_hotel_info(args.dbname)
