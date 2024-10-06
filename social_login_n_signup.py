from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyperclip
import time
import random
import re

# PROXY = "185.199.231.45:8382"
PASSWORD = "Englishs123"
email = "vahabot471@fryshare.com"
password = "Englishs123"

chrome_options = Options()
chrome_options.add_argument("--enable-features=AllowPopupsDuringPageUnload")


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument("--disable-popup-blocking")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_extension(r"G:\Practice\100 Days of Code The Complete Python Pro Bootcamp for 2023\48 - Day 48 - Intermediate+ Selenium Webdriver Browser and Game Playing Bot\Selenium Practice\LinkdIn Auto Apply\CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_56_0_0.crx")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 150)

# Temporary Email Setup
driver.get("https://internxt.com/temporary-email")
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Copy email']")))
time.sleep(1)
driver.find_element(By.XPATH, "//p[normalize-space()='Copy email']").click()
time.sleep(1)
gmail = pyperclip.paste()
print(gmail)
username = gmail[:7]

# Head to Instagram
time.sleep(0.2)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.instagram.com/")

# Sign Up On Instagram
wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Sign up']")))
driver.find_element(By.XPATH, "//span[normalize-space()='Sign up']").click()
wait.until(lambda driver: "https://www.instagram.com/accounts/emailsignup/" in driver.current_url)

# Sign Up Window One
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Mobile Number or Email']")))
driver.find_element(By.XPATH, "//input[@aria-label='Mobile Number or Email']").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, f"{PASSWORD}")
driver.find_element(By.XPATH, "//input[@aria-label='Mobile Number or Email']").send_keys(f"{gmail}", Keys.TAB, f"{username}", Keys.TAB, f"{username * 2}{random.randint(99, 999)}")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign up']").click()
time.sleep(1)

# Sign Up Window Two
wait.until(EC.presence_of_element_located((By.XPATH, "//select[@title='Year:']")))
select_element = driver.find_element(By.XPATH, "//select[@title='Year:']")
select = Select(select_element)
select.select_by_value('1995')
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[text()='Next']").click()
time.sleep(3)

# Get Code
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.refresh()
driver.execute_script("window.scrollBy(0, 450)")
time.sleep(6)
driver.refresh()
wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'is your Instagram code')]")))
code_text = driver.find_element(By.XPATH, "//p[contains(text(), 'is your Instagram code')]").text
print(code_text)
code = code_text[:6]

# Verify Code in Instagram
driver.switch_to.window(driver.window_handles[1])
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@aria-label='Confirmation Code']")))
driver.find_element(By.XPATH, "//input[@aria-label='Confirmation Code']").send_keys({code})
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@aria-label='Confirmation Code']")))
time.sleep(2)
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[text() = 'Go back']")))
driver.find_element(By.XPATH, "//div[text() = 'Go back']").click()

# --------------------------- Facebook ------------------------------------
# Heading to Facebook

wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Log in with Facebook')]")))
driver.find_element(By.XPATH, "//button[contains(text(), 'Log in with Facebook')]").click()

# Start Signing Up with Facebook
wait.until(EC.presence_of_element_located((By.XPATH, "//a[text() = 'Sign up for Facebook']")))
driver.find_element(By.XPATH, "//a[text() = 'Sign up for Facebook']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='First name']")))
driver.find_element(By.XPATH, "//input[@aria-label='First name']").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, f"{PASSWORD}")
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='First name']")))
driver.find_element(By.XPATH, "//input[@aria-label='First name']").send_keys(f"{re.sub(r'\d+', '', username)}", Keys.TAB, f"{re.sub(r'\d+', '', username)}", Keys.TAB, f"{gmail}")
time.sleep(0.2)
driver.find_element(By.XPATH, "//input[@aria-label='First name']").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, f"{gmail}")


wait.until(EC.presence_of_element_located((By.XPATH, "//select[@title='Year']")))
fb_select_item = driver.find_element(By.XPATH, "//select[@title='Year']")
fb_select = Select(fb_select_item)
fb_select.select_by_value('1995')
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='1']")))
driver.find_element(By.XPATH, "//input[@value='1']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space(text()) = 'Sign Up']")))
driver.find_element(By.XPATH, "//button[normalize-space(text()) = 'Sign Up']").click()

time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='More options']")))
driver.find_element(By.XPATH, "//div[@aria-label='More options']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space(.)='Log out']")))
driver.find_element(By.XPATH, "//span[normalize-space(.)='Log out']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Log out']")))
driver.find_element(By.XPATH, "//span[text()='Log out']").click()

time.sleep(4)

# --------------------------- Follow The Account ----------------------------- #
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.instagram.com/")

driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']").send_keys(f"{email}", Keys.TAB, f"{password}")
driver.find_element(By.XPATH, "//div[text()='Log in']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Search']")))
driver.find_element(By.XPATH, "//span[text()='Search']").click()
wait.until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search input"]')))
driver.find_element(By.XPATH, '//input[@aria-label="Search input"]').send_keys("shaguftaafzal1234", Keys.ENTER)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[text() = 'Shagufta Afzal']")))
driver.find_element(By.XPATH, "//span[text() = 'Shagufta Afzal']").click()
wait.until(lambda driver: "https://www.instagram.com/shaguftaafzal1234/" in driver.current_url)
# //div[contains(text(), 'Follow')]/parent::button
wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//div[contains(text(), 'Follow')]]")))
driver.find_element(By.XPATH, "//button[.//div[contains(text(), 'Follow')]]").click()

