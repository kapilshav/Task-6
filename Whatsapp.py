from datetime import datetime
import pywhatkit
now = datetime.now()

time = now.strftime("%m %M")
hours = now.strftime("%d %H")


hour=int(hours[3:5]) 
minute=int(time[3:6]) + 2

pywhatkit.sendwhatmsg('+919926436393','face detected..!',hour,minute)
