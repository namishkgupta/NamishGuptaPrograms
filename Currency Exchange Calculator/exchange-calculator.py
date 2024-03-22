import googlemaps

API = open("API Key.txt","r")
APIKey = API.read()

Maps = googlemaps.Client(key = APIKey)

start = input('What is your start destination: ')
end = input('What is your end destination: ')

distance = Maps.direcions(start, end)

print(distance)