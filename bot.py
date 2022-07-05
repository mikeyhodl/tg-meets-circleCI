"""
bot app
"""
import time
import schedule
from btc import to_tg
START_NOW = to_tg()

print(START_NOW)
def job():
    """
  btc bot"""
    return to_tg()
  # print("I'm working...")
schedule.every(1).minutes.do(job)
# schedule.every(1).minutes.until("2023-01-01 00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
