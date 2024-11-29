from selenium.webdriver.common.by import By
import urllib.parse
import time

class SearchCourse:
    @staticmethod

    # Build url for searching specific courses in MadGrades
    def construct_url(course_name):
        base_url = "https://madgrades.com/search?query="
        encoded_course_name = urllib.parse.quote(course_name)
        return base_url + encoded_course_name

    # Opens MadGrades course search in new window while maintaining the course cart in the original tab
    @staticmethod
    def open_page(driver, url):
        driver.execute_script("window.open('');")
        new_tab_index = len(driver.window_handles) - 1
        driver.switch_to.window(driver.window_handles[new_tab_index])
        driver.get(url)
        time.sleep(2)

    # Goes to the first link assuming that the first link corresponds to the correct course being searched
    # Returns an error message if no link is found
    @staticmethod
    def get_first_link_href(driver):
        try:
            first_link = driver.find_elements(By.CSS_SELECTOR, 'a.content')
            if first_link:
                first_link_href = first_link[0].get_attribute("href")
                return first_link_href
            else:
                print("No links found.")
                return None
        except Exception as e:
            print(f"Error during finding the link: {e}")
            return None
