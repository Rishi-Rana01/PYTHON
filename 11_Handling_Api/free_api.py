import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
        user_data=data["data"]
        username=user_data["login"]["username"]
        country = user_data["location"]["country"]
        coordinates = user_data["location"]["coordinates"]
        return username, country, coordinates
    else:
        raise Exception("Failed to fetch Data")
    

def main():
    try:
       username, country, coordinates = fetch_random_user_freeapi() 
       print(f"Username: {username} \nCountry: {country}")
       print(f"Coordinates: Latitude {coordinates['latitude']}, Longitude {coordinates['longitude']}")
    except Exception as e:
        print(str(e))

if __name__== "__main__":
    main()