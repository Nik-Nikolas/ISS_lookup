import json
import turtle
import urllib.request
import time

# call the webservice
url = 'http://api.open-notify.org/astros.json'
responce = urllib.request.urlopen(url)

# to load json data to a py data structure
# deserialize (Convert) JSON to Python Object (Dict)
jsonData = json.loads(responce.read())

# Establish background screen
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('earthmap.png') # jpg doesnt work!
screen.register_shape('iss.gif') # gif only!

# to directly access data
#for i in range (0, result['number']):
#    print('  ', result['people'][i]['name'])

# Space center Houston
lat = 29.5502
lon = -95.097
location = turtle.Turtle()
location.penup()
location.color('black')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

# Make request to server to get data
# which corresponds to certain coordinates
url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
jsonData3 = json.loads(response.read())

# Get timestamp
over = jsonData3['response'][1]['risetime']

# convert and print  timestamp
style = ('Arial', 7, 'bold')
string = 'Nearest time when ISS is over Houston is' + str(time.ctime(over)) + '\n\nPeople in space: '
string += (str(jsonData['number']) + '\n')

# Python list
people = jsonData['people']

# Work with list
for p in people:    
    string += ('    ' + p['name'] + '\n')

# Write text to the location: timestamp + astronauts list
location.write(string, font = style)

# Show ISS current position and coordinates
style = ('Arial', 10, 'bold')

iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
while(True):
    
    url = 'http://api.open-notify.org/iss-now.json'
    responce = urllib.request.urlopen(url)
    jsonData2 = json.loads(responce.read())

    location = jsonData2['iss_position']
    lat = location['latitude']
    lon = location['longitude']

    iss.goto(round(float(lon)), round(float(lat)))
    iss.color('red')
    iss.clear()
    iss.write(str(lat) + "\n" + str(lon), font=style)
    
    time.sleep(3)



