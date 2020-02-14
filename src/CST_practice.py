import datetime
from datetime import datetime


d = datetime.now()
# dates = datetime.utcnow()



dob = "June-16-2001 Sat, 11:59:00 AM"

print(datetime.strptime(dob, "%B-%d-%Y %a, %X %p"))
