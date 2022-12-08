# API that shows all timezones.
# includes a world map that labels all timezones
# every time the user refreshes the page, it takes the current time and converts it to the appropriate time zone.
# does not update in real-time. Too difficult.


# Number 1:
# currentTime = (time.local())
#Number 2:
# currentDateAndTime = datetime.now()
# formattedCurrentDateAndTime = currentDateAndTime.strftime("Local time: %H:%M, %a %b %d, %Z (%z)")






import time
from datetime import datetime

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
#API : 'https://timezone.com'


timezone = {-10: {"name": "Hawaiian Standard Time", "abbreviation": "HAST", "UTC-time": -10},
    -9: { "name": "Alaska Standard Time",       "abbreviation":"AK",  "UTC-time": -9},
    -8: { "name": "Pacific Standard Time",      "abbreviation":"PT",  "UTC-time": -8},
    -7: { "name": "Mountain Standard Time",     "abbreviation":"MT",  "UTC-time": -7},
    -6: { "name": "Central Standard Time",      "abbreviation":"CT",  "UTC-time": -6},
    -5: { "name": "Eastern Standard Time",      "abbreviation":"ET",  "UTC-time": -5},
    -4:{ "name": "Altantic Standard Time",      "abbreviation":"AST", "UTC-time": -4},
    0:{ "name": "Universal Coordinated Time", "abbreviation":"UTC", "UTC-time": 0}
  }
# print(time.gmtime(0))
# currentDateAndTime = datetime.now()
# newT = currentDateAndTime.strftime("%Z, %z")
# print(newT)
# timed = currentDateAndTime.tzname()
# print("Timezone: " + str(timed))
# print("time.altzone: ", time.altzone)

# the easy way
# currentTime = time.strftime("%H:%M")
# print(currentTime)


usersTimeZone = -1 * (time.altzone/3600)
currentDateAndTime = datetime.now()
formattedCurrentDateAndTime = currentDateAndTime.strftime("Local time: %H:%M, %a %b %d")
print(formattedCurrentDateAndTime)

class userProfile:
    def __init___(self, CalculatedTimeZone, CurrentTime):
        self.CalculatedTimeZone = CalculatedTimeZone
        self.CurrentTime = CurrentTime

    def returnCalculatedTimeZone(self):
        return self.CalculatedTimeZone


class OtherTimeZones:
    def __init__(self, zoneName, zoneAbbreviation, zoneTime):
        self.zoneName = zoneName
        self.zoneAbbreviation = zoneAbbreviation
        self.zoneTime = zoneTime


@app.route('/')
def index():
  return "<h1>Welcome to My Website</h1>"


@app.post("/")
def usersLocalTime():
    if request.is_json:
        zone = request.get_json()
        currentTime = time.strftime("%H:%M")                  # Obtains the current time in the user's timezone
        usersTimeZone = -1 * (time.altzone/3600)              # Obtains the number of hours behind Greenwitch time (GMT) - obtains timezone. Obtains difference in time (in seconds) between user's local timezone and GMT. If 0, user is in GMT. If -3600, user is 1 hour behind GMT or 1 timezone away. And vice versa. In all, it calculates which timezone the user is in.
        calculatedTimeZone = timezone[usersTimeZone]["name"]
        userProfile(calculatedTimeZone, currentTime)
        strLocalTime_LocalTimezone = "Your timezone: " + calculatedTimeZone  + "/nLocal time: " + currentTime
        return strLocalTime_LocalTimezone, 201
    return {"error": "Request must be Json"}, 415

@app.post("/")
def otherTimeZones():
    lstTimeZone = []
    for el in timezone:
        relativeTimeZone = userProfile.returnCalculatedTimeZone() + timezone[el]["UTC-time"]
        timeZoneName = timeZoneName[el]["name"]
        timeZoneAbbreviation = timeZoneName[el]["abbreviation"]
        lstTimeZone.append(otherTimeZones(timeZoneName, timeZoneAbbreviation, relativeTimeZone))
    return lstTimeZone











if __name__=="main":
    app.run

# @app.route("/image/<i>")
# def showImage(i):
#     url = f"https://dog.ceo/api/breeds/image/random/{i}"
#     print(url)
#     response = requests.get(url)
#     imagetags = response.json()["message"]
#     return render_template("images.html",imagetags=imagetags,i=int(i))









# import random
#
# wordBank = ["quantum", "physics", "ocular", "vile", "variant", "onning"]
# chosenWord = random.choice(wordBank)
#
# stillWantsToPlay = True
# nWrongGuesses = 0
# firstCheck  = None
#
# print("Hangman\n")
# print("If you 7 wrong gueeses, you lose.\n")
# print("Type exit if you wish to stop playing")
# while (stillWantsToPlay == True or nWrongGuesses != 7):
#     userGuess = str(input("Your guess: "))
#     firstCheck = chosenWord.find(userGuess)
#     if firstCheck == -1:
#         nWrongGuesses+=1
#     else:
#         pass


