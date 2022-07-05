import schedule
import time
from btc import Totg
start = Totg()

def job():
  print("I'm working...")
schedule.every(1).minutes.do(job)
# schedule.every(1).minutes.until("2023-01-01 00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)