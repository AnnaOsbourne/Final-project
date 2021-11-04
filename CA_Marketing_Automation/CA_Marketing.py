import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Chrome

class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_wordpress_website_chrome(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        wait = WebDriverWait(driver, 3)

        driver.find_element_by_xpath('(//a[@href="https://qasvus.wordpress.com/"])[2]').get_attribute("href")
        print(driver.find_element_by_xpath('(//*[@class="wp-image-55"])'))

        assert 'California Real Estate' in driver.title
        print("Page title in Chrome 1120x550 is:", driver.title)
        time.sleep(1)

        driver.find_element_by_xpath('//*[@value="Close and accept"]').click()
        driver.find_element_by_class_name("bottom-sticky__ad-close-btn")
        driver.implicitly_wait(5)

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

        driver.find_element_by_xpath("//input[@id='g2-name']").send_keys("Anna")
        driver.find_element_by_name("g2-email").send_keys("Anna@gmail.com")
        driver.find_element_by_id("contact-form-comment-g2-message").send_keys("Hi.I'm Anna")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))
        driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Go Back button is ready!")
        except TimeoutException:
            print("Go Back button took too much time!")

        driver.find_element_by_xpath("//a[contains(text(),'go back')]").click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-55')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-34')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-56')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-30')))
        time.sleep(2)

        assert 'California Real Estate' in driver.page_source
        print("Page title in Chrome 1120x550 is:", driver.page_source)
        time.sleep(1)

    def test_wordpress_website_chrome_1120x850(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://qasvus.wordpress.com/")
        wait = WebDriverWait(driver, 3)

        driver.find_element_by_xpath('(//a[@href="https://qasvus.wordpress.com/"])[2]').get_attribute("href")
        print(driver.find_element_by_xpath('(//*[@class="wp-image-55"])'))

        assert 'California Real Estate' in driver.title
        print("Page title in Chrome 1120x550 is:", driver.title)
        time.sleep(1)

        driver.find_element_by_xpath('//*[@value="Close and accept"]').click()
        time.sleep(2)
        driver.find_element_by_class_name("bottom-sticky__ad-close-btn")
        driver.implicitly_wait(5)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        driver.find_element_by_xpath("//h2[contains(text(),'Send Us a Message')]")
        search = driver.find_element_by_xpath("//*[@name='g2-name']")
        search.clear()
        search = driver.find_element_by_xpath("//input[@id='g2-email']")
        search.clear()
        search = driver.find_element_by_id("contact-form-comment-g2-message")
        driver.find_element_by_xpath("//input[@id='g2-name']").send_keys("Anna")
        driver.find_element_by_name("g2-email").send_keys("Anna@gmail.com")
        driver.find_element_by_id("contact-form-comment-g2-message").send_keys("Hi.I'm Anna")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))

        driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Go Back button is ready!")
        except TimeoutException:
            print("Go Back button took too much time!")

        driver.find_element_by_xpath("//a[contains(text(),'go back')]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='wp-image-55']")))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='wp-image-34']")))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-56')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='wp-image-30']")))
        time.sleep(2)

        assert 'California Real Estate' in driver.page_source
        print("Page title in Chrome 1120x550 is:", driver.page_source)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_wordpress_website_firefox(self):
        driver = self.driver
        driver.get("https://www.firefox.com/")
        driver.get("https://qasvus.wordpress.com/")

        driver.implicitly_wait(5)

        driver.find_element_by_xpath('(//a[@href="https://qasvus.wordpress.com/"])[2]').get_attribute("href")
        print(driver.find_element_by_xpath('(//*[@class="wp-image-55"])'))

        assert 'California Real Estate' in driver.title
        print("Page title in Chrome 1120x550 is:", driver.title)
        time.sleep(1)

        driver.find_element_by_xpath('//*[@value="Close and accept"]').click()
        # driver.find_element_by_class_name("bottom-sticky__ad-close-btn")
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        # driver_find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()

        driver.find_element_by_xpath("//input[@id='g2-name']").send_keys("Anna")
        driver.find_element_by_name("g2-email").send_keys("Anna@gmail.com")
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))
        driver.find_element_by_id("contact-form-comment-g2-message").send_keys("Hi.I'm Anna")
        # driver_find_element(By.XPATH, "//button[contains(text(Send Us a Message), 'Submit')]")
        # driver.find_element_by_xpath("//*[@class='pushbutton-wide']").send_keys('\n')

        driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Go Back button is ready!")
        except TimeoutException:
            print("Go Back button took too much time!")

        driver.find_element_by_xpath("//a[contains(text(),'go back')]").click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-55')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-34')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-56')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-30')))
        time.sleep(2)

        assert 'California Real Estate' in driver.page_source
        print("Page title in Chrome 1120x550 is:", driver.page_source)
        time.sleep(1)

    def test_wordpress_website_firefox_1250x850(self):
        driver = self.driver
        driver.set_window_size(1250, 850)
        driver.get("https://qasvus.wordpress.com/")
        driver.implicitly_wait(5)

        driver.find_element_by_xpath('(//a[@href="https://qasvus.wordpress.com/"])[2]').get_attribute("href")
        print(driver.find_element_by_xpath('(//*[@class="wp-image-55"])'))

        assert 'California Real Estate' in driver.title
        print("Page title in Chrome 1120x550 is:", driver.title)
        time.sleep(1)

        driver.find_element_by_xpath('//*[@value="Close and accept"]').click()
        # driver.find_element_by_class_name("bottom-sticky__ad-close-btn")
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        driver.find_element_by_xpath("//h2[contains(text(),'Send Us a Message')]")
        search = driver.find_element_by_xpath("//input[@id='g2-name']")
        search.clear()
        search = driver.find_element_by_xpath("//input[@id='g2-email']")
        search.clear()
        search = driver.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        driver.find_element_by_xpath("//input[@id='g2-name']").send_keys("Anna")
        driver.find_element_by_name("g2-email").send_keys("Anna@gmail.com")
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.ID, "//textarea[@id='contact-form-comment-g2-message']")))
        driver.find_element_by_id("contact-form-comment-g2-message").send_keys("Hi.I'm Anna")
        # driver_find_element(By.XPATH, "//button[contains(text(Send Us a Message), 'Submit')]")
        # driver.find_element_by_xpath("//*[@class='pushbutton-wide']").send_keys('\n')

        driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Go Back button is ready!")
        except TimeoutException:
            print("Go Back button took too much time!")

        driver.find_element_by_xpath("//a[contains(text(),'go back')]").click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-55')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-34')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-56')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wp-image-30')))
        time.sleep(2)

        assert 'California Real Estate' in driver.page_source
        print("Page title in Chrome 1120x550 is:", driver.page_source)
        time.sleep(1)

    def tearDown(self):
        # Close the browser.
        self.driver.quit()
