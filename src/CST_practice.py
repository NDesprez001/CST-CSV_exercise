import datetime
from datetime import datetime, timedelta


# d = datetime.now()




# dob = "June-16-2001 Sat, 11:59:00 AM"
# datetime_obj = datetime.strptime(dob, "%B-%d-%Y %a, %X %p")

now = datetime.utcnow()
registered_date =now - timedelta(days=3)


check_date = now
# print(check_date <= registered_date + timedelta(days=4))

def expiration_check(a):
    if check_date <= a + timedelta(days=4):
        return f'will expire on ' + str(check_date + timedelta(days=4))
    return f'Expired on ' + str(check_date)

print(registered_date)
print(expiration_check(registered_date))

#check_date = now
#registered date is 5 days before now