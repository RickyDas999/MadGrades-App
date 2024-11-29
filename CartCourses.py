from SearchCourse import SearchCourse
import time
from selenium.webdriver.common.by import By

# Goes to Course Search and Enroll website after prompting wisc.edu sign in
class CartCourses:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://enroll.wisc.edu/my-courses'
        self.driver.get(self.url)
        time.sleep(2)

        while True:
            current_url = self.driver.current_url
            if current_url == self.url:
                time.sleep(5)
                self.process_courses()
                break

# Finds all classes saved in the student's course enrollment cart and saves Course IDs for MadGrades searches
    def process_courses(self):
        cart_courses = self.driver.find_elements(By.CSS_SELECTOR, 'div.left.grow.catalog')
        main_window = self.driver.current_window_handle
        for course in cart_courses:
            print(course.text)
            search_url = SearchCourse.construct_url(course.text)
            SearchCourse.open_page(self.driver, search_url)
            course_link = SearchCourse.get_first_link_href(self.driver)
            print(course_link)
            if course_link:
                self.driver.get(course_link)

            self.driver.switch_to.window(main_window)
