import datetime
import time
from playsound import playsound

def processTime( timeString ):
    # if(datetime.datetime.now().hour >= 12):
    #     timeString += "pm"
    # else: 
    #     timeString += "am"

    try:
        if(len(timeString) < 6):
            return datetime.datetime.combine( datetime.date.today(), datetime.datetime.strptime( timeString, "%I%M%p" ).time())
        else:
            return datetime.datetime.combine( datetime.date.today(), datetime.datetime.strptime( timeString, "%I%M%S%p" ).time())
    except Exception as e:
        print(e)
        print("you fucked it up. Try again\n")
        return processTime(input("when you tryna time until??\n"))

soundpath = 'purgeSiren.mp3'

eventTime = processTime( input("when you tryna time until?\n" ) )

print("Roger! I'll start goin off at", eventTime, "\n")

while( datetime.datetime.now() < eventTime):
    time.sleep(5) #10?


playsound(soundpath)

# stop = input("type \"disable alarm\" to stop the noise").capitalize

# while(stop != "DISABLE ALARM"):
#     stop = input("what did I say? try again. DISABLE ALARM\n")

# print("\n\n\nget your ass to class bitch")
exit()


