from math import sin, cos, sqrt, atan2, radians
import os
import requests
import pandas as pd

#Transforming office object into GeoPoint for office
def OFFToGeoPoint(row):
    office = row.offices
    if type(office) == dict:
        if 'latitude' in office and 'longitude' in office:
            if(type(office["latitude"])) == float and type(office["longitude"]) == float:
                return ({
                    "type":"Point",
                    "coordinates":[office["longitude"],office["latitude"]]
                },"success")
            else:
                return(None,"Invalid lat lat and long")
        else:
            return (None,"No lat and long keys in office dict")
    return (None,"No office")



#Divide into different columns latitude and longitude
def easyLatLng(row):
    of = row.office
    return {
        "longitude":of["coordinates"][0],
        "latitude":of["coordinates"][1]
        }



#Calculate the distance between two points knowing its coordinates (Haversine formula)

def distance(lat1,lon1,lat2,lon2):
 
    R = 6373.0  

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

#Makes a call to foursquare's API and finds your closet requierement to the place you set

def getFromFS(coord,radius,query,):
    url = 'https://api.foursquare.com/v2/venues/search'

    params = dict(
    client_id=os.getenv("client_ID"),
    client_secret=os.getenv("client_S"),
    v='20200212',
    ll= coord,
    intent="browse",
    radius=radius,
    openNow="0",
    query= query,
    limit=20,

    )
 
    res = requests.get(url=url, params=params)
    print(res.status_code)
    result = res.json()

    return result


def FS_to_df(x): 
    out = []
    for e in range(len(x["response"]["venues"])):
        name = x["response"]["venues"][e]["name"]
        distance = (x["response"]["venues"][e]["location"]["distance"])/1000
        lat = x["response"]["venues"][e]["location"]["lat"]
        long = x["response"]["venues"][e]["location"]["lng"]
        out.append((name,lat,long,distance))
    
    #from list to df
    df=pd.DataFrame(out)
    #rename
    df = df.rename(columns={0:"nombre",1:"long",2:"lat",3:"Distance"}).sort_values(by='Distance', ascending=True).reset_index(drop=True)
    #Just first
    df = df[0:1]
    return df

#Transforming geo column into GeoPoint 

def GEOToGeoPoint(row):
    geoloc = row._geoloc
    if type(geoloc) == dict:
        if 'lat' in geoloc and 'lng' in geoloc:
            if(type(geoloc["lat"])) == float and type(geoloc["lng"]) == float:
                return ({
                    "type":"Point",
                    "coordinates":[geoloc["lng"],geoloc["lat"]]
                },"success")
            else:
                return(None,"Invalid lat lat and long")
        else:
            return (None,"No lat and long keys in office dict")
    return (None,"No office")