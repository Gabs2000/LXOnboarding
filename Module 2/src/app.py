from calendar import week
from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

# Adding one month, week and 10 hours to now
now = now + relativedelta(months=1, weeks=1, hour=10)
print(now)