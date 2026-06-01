#PROBLEM: Create a function that asks for a user’s birthdate (YYYY-MM-DD) and calculates their exact age today in years, months, and days.
#PURPOSE: Date math is notoriously difficult because of leap years and varying month lengths. This exercise teaches you to use the datetime and dateutil.relativedelta modules, which are the industry standards for handling temporal data in Python.
from datetime import datetime,timedelta,date

def age_calculator(Birthdate,Today):
    Bd = Birthdate.split("-")
    Current = Today.split("-")
    t1 = date(year = int( Bd[0]), month = int(Bd[1]), day = int(Bd[2]))
    t2 = date(year = int(Current[0]), month = int(Current[1]), day=int(Current[2]))

    t3 = t1 - t2

    diff =str(t3).split(" ")[0]
    result = round(int(diff) / 365)
    return (f"{abs(result)} Years")


Birthdate = "1995-05-15"
Today = datetime.today().strftime("%Y-%m-%d")

sample = age_calculator(Birthdate,Today)
print(sample)