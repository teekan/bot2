from selenium import webdriver
import os, time
from selenium.webdriver.firefox.options import Options
#opts = Options()
#opts.headless = True
path = os.getcwd()+"/geckodriver"
driver=webdriver.Firefox(executable_path=path)
driver.get("http://www.slutbags.tk/video.php?id=1")
popunder = driver.find_elements_by_class_name("text-center")
popunder[0].click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
driver.close()
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
driver.close()
