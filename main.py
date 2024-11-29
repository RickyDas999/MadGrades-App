from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from CartCourses import CartCourses
from SearchCourse import SearchCourse

# Allows searches to stay after end of program
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Pass driver instance to CartCourses
cart = CartCourses(driver)
