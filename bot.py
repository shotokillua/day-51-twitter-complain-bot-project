from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()


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
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
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

        # Log in w Google (tried but it wouldn't let you log in w Google :(

        sign_in_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
        sign_in_button.click()

        time.sleep(3)

        # # Switch windows to Google Sign In and fill in your info and click next (Google didn't let me sign in)
        # base_window = driver.window_handles[0]
        # google_window = driver.window_handles[1]
        # driver.switch_to.window(google_window)
        # time.sleep(2)
        #
        # email_bar = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        # email_bar.click()
        # email_bar.send_keys(TWITTER_EMAIL)
        # email_bar.send_keys(Keys.ENTER)

        # Angela's sign in code not using Google Sign-in
        email = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.click()
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
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

