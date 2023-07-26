from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

PROMISED_UP = 100
PROMISED_DOWN = 20
CHROME_DRIVER_PATH = "\D:Development\chromedriver.exe"
TWITTER_EMAIL = "***" # sign in with Google
TWITTER_PASSWORD = "***"

SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login"

chromedriver_autoinstaller.install()
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# driver = webdriver.Chrome(service=service, options=options)
#
# # # Open speedtest website and fullscreen in
# # driver.get(SPEEDTEST_URL)
# # time.sleep(5)
# # driver.fullscreen_window()
# # time.sleep(3)
# #
# # # Click GO button and let the speedtest run
# # go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
# # go_button.click()
# # time.sleep(90)
# #
# # # Print download and upload speed in console
# # down = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
# # print(f"down: {down.text}")
# # up = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
# # print(f"up: {up.text}")
#
#
# # Go to twitter and fullscreen it
#
# driver.get(TWITTER_URL)
# driver.fullscreen_window()
# time.sleep(3)
#
# # Log in w Google (tried but it wouldn't let you log in w Google :(
#
# sign_in_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
# sign_in_button.click()
#
# time.sleep(3)
# # # Switch windows to Google Sign In and fill in your info and click next
# # base_window = driver.window_handles[0]
# # google_window = driver.window_handles[1]
# # driver.switch_to.window(google_window)
# # time.sleep(2)
# #
# # email_bar = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
# # email_bar.click()
# # email_bar.send_keys(TWITTER_EMAIL)
# # email_bar.send_keys(Keys.ENTER)
#
# # Tweet at internet service provider (ISP)
#
# tweet_box = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
# tweet_box.click()
# tweet_box.send_keys(f"Hey internet service provider, why is my internet speed {PROMISED_DOWN}down/{PROMISED_UP}up when I pay for 100down/20up?")
# time.sleep(2)
#
# tweet_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
# tweet_button.click()
# time.sleep(2)
#
# driver.quit()

class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.chrome_driver_path = chrome_driver_path
        self.service = Service(self.chrome_driver_path)
        self.options = webdriver.ChromeOptions().add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Open speedtest website and fullscreen in
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        self.driver.fullscreen_window()
        time.sleep(3)
        # Click GO button and let the speedtest run
        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(90)
        # Print download and upload speed in console
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        print(f"down: {self.down.text}")
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(f"up: {self.up.text}")

    def tweet_at_provider(self):
        # Go to twitter and fullscreen it

        self.driver.get("https://twitter.com/login")
        self.driver.fullscreen_window()
        time.sleep(3)

        # Log in w Google [tried but it wouldn't let you log in w Google :( log on w an email and pw instead]

        sign_in_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
        sign_in_button.click()

        time.sleep(3)

        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.click()
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # Tweet at internet service provider (ISP)

        tweet_box = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet_box.click()
        tweet_box.send_keys(
            f"Hey internet service provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(2)

        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)

        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()