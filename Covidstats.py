#import the necessary module!s
from plyer import notification
import datetime
import time
import requests

def Corona_Search():
    url = f"https://coronavirus-19-api.herokuapp.com/countries/{country}"
    stats = requests.get(url)
    json_stats = stats.json()
    totalCases = json_stats["cases"]
    todayCases = json_stats["todayCases"]
    totalDeaths = json_stats["deaths"]
    todayDeaths = json_stats["todayDeaths"]
    recovered = json_stats["recovered"]
    active = json_stats["active"]
    critical = json_stats["critical"]
    casesPerOneMillion = json_stats["casesPerOneMillion"]
    deathsPerOneMillion = json_stats["deathsPerOneMillion"]
    totalTests = json_stats["totalTests"]
    testsPerOneMillion = json_stats["testsPerOneMillion"]

    print(f"Total cases are {totalCases}")
    print(f"Today's cases are {todayCases}")
    print(f"Total deaths are {totalDeaths}")
    print(f"Today's deaths are {todayDeaths}")
    print(f"Recovered: {recovered}")
    print(f"Active cases are {active}")
    print(f"Critical cases are {critical}")
    print(f"Cases per One Million are {casesPerOneMillion}")
    print(f"Deaths per One Million are {deathsPerOneMillion}")
    print(f"Total tests are {totalTests}")
    print(f"Tests per One Million are {testsPerOneMillion}")
    print("")

#What 
def Covid_Search():
    url = f"https://coronavirus-19-api.herokuapp.com/countries/{country}"
    stats = requests.get(url)
    json_stats = stats.json()
    totalCases = json_stats["cases"]
    todayCases = json_stats["todayCases"]
    totalDeaths = json_stats["deaths"]
    todayDeaths = json_stats["todayDeaths"]
    recovered = json_stats["recovered"]
    active = json_stats["active"]
    critical = json_stats["critical"]
    casesPerOneMillion = json_stats["casesPerOneMillion"]
    deathsPerOneMillion = json_stats["deathsPerOneMillion"]
    totalTests = json_stats["totalTests"]
    testsPerOneMillion = json_stats["testsPerOneMillion"]

    print(f"Total cases are {totalCases}")
    print(f"Today's cases are {todayCases}")
    print(f"Total deaths are {totalDeaths}")
    print(f"Today's deaths are {todayDeaths}")
    print(f"Recovered: {recovered}")
    print(f"Active cases are {active}")
    print(f"Critical cases are {critical}")
    print(f"Cases per One Million are {casesPerOneMillion}")
    print(f"Deaths per One Million are {deathsPerOneMillion}")
    print(f"Total tests are {totalTests}")
    print(f"Tests per One Million are {testsPerOneMillion}")
    print("")
#Credits and info 
print("**********************************************************************")
print("Covid Tracker")
print("Program made by: Hiphop602, Lucifer Morningstar and Inky")
print("")
print("Uses Covid API and displays latest information regarding the virus")
print("Accurate and latest information")
print("Total Cases, Active Cases, Total Deaths, Total Cured and much more")
print("")
print("Website for API: https://coronavirus-19-api.herokuapp.com/countries/")
print("Data recieved in JSON format")
print("**********************************************************************")
print("")


ans = input("Would you like to set a reminder for the updated status of the corona cases? ? (y/n) : ")
if ans not in ["Y", "y", "Yes", "yes", "sure", "yup", "Yup", "Sure"]:
    country = input("Please enter country name for covid stats: ")
    print(f"You have chosen {country}")
    print("")   

    Covid_Search()
    print("Thanks for the running the program!")
    exit(0)

print("Please enter the date and time you want to recieve the reminder in the format of the below given example.")
print("January/1/2000/1:10 pm")
print("Mistake in format might show unexpected errors.")
ms = []
Dates_times = []
Reminders = {}
while True:
    date_string = input("Enter your reminder date and time : ")
    m = input("Enter your custom message please : ")
    inp = datetime.datetime.strptime(date_string, "%B/%d/%Y/%I:%M %p")
    ms.append(m)
    Dates_times.append(inp)
    break
for i in range(len(Dates_times)):
    Reminders[Dates_times[i]] = ms[i]
while len(Reminders) != 0:
    x = datetime.datetime.now()
    y = x.strftime("%d/%m/%Y %H:%M")
    now = datetime.datetime.strptime(y, "%d/%m/%Y %H:%M")
    if now in Reminders.keys():
        rem = Reminders[now]
        notification.notify(
            title = "Check out the covid stats!",
            message = rem,
            timeout = 20
        )
        del Reminders[now]
        country = input("Please enter country name for covid stats: ")
        print(f"You have chosen {country}")
        print("")  
        Corona_Search() #i could have used Covid_search but im not sure whether it would show the latest info *shrugs*







