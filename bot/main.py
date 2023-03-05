from phptravels.phptravels import Phptravels
import time


with Phptravels() as bot:
  bot.land_first_page()
  time.sleep(5)
  bot.check_nav_links()


