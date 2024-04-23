import datetime
import pytz

d = datetime.date(2024, 1,20)
print(d)
today = datetime.date.today()
print(today)
print(today.year)
print(today.weekday())
print(today.isoweekday())
# Adding and substracting dates
tdelta = datetime.timedelta(days=7)
print(today + tdelta)

t = datetime.time(9,30,45,100000)
print(t)

dt = datetime.datetime(2020, 7, 27, 12, 30, 45, tzinfo = pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_pl = dt_now.astimezone(pytz.timezone('Poland'))
print(dt_pl)

# strptime - String to data
# strftime - Data to string

data_str = 'July 26, 2016'
dt_conv = datetime.datetime.strptime(data_str,'%B %d, %Y')
print(dt_conv)

