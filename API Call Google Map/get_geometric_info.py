# This is a small python widget for getting the latitude & longitude by using 
# the Google Map API
# By Samuel Ko

# Reference : https://www.youtube.com/watch?v=vTFn9gWEtPA
import os
import pandas
import googlemaps
import os
from dotenv import load_dotenv

def get_geometric(inAddress):
    try:
        load_dotenv()
        GOOGLE_MAPS_API_KEY= os.environ.get("API_KEY") # Google Maps API key
        
        # Create Temperary List for storage
        goBack = []

        # GOOGLE_MAPS_API_KEY = 'AXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE'
        
        gmap_client = googlemaps.Client(GOOGLE_MAPS_API_KEY);

        result = gmap_client.geocode(inAddress)

        goBack.append(result[0]['geometry']['location']['lat'])
        goBack.append(result[0]['geometry']['location']['lng'])
    except:
        goBack.append(0.0)
        goBack.append(0.0)
        
    return(goBack)


# def main():
#     myList = []
#     myList = get_geometric('York Explore, UK')
#     for x in myList:
#         print(x)

# main()

