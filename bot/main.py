from booking.booking import Booking
import time


with Booking() as bot:
  bot.land_first_page()
  time.sleep(5)
  bot.close_popup()
  bot.change_currency()


