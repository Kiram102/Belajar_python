# module date time

from datetime import datetime, date, time, timedelta
import time as time_module

now = datetime.now()
print(now)

today = datetime.today()
print(today)

specific_time = time(14 , 20 , 10)
print(specific_time)

# Membuat Date dan date time

from datetime import datetime as dt

# membuat date spesipic
birthday = dt(1900, 5, 15)
print(birthday)

# membuat date time spesipic
sekolah = dt(2025, 12, 25, 14, 30, 0)
print(sekolah)

# dari string (parshing)
date_string = "2007-07-07"
parshed = dt.strptime(date_string, "%Y-%m-%d")
print(parshed)