import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGreenCityEvents(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def wait_for_events(self):
        card_xpath = "//*[contains(@class,'card-wrapper')]"
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, card_xpath))
        )

    def test_display_events_list(self):
        """
        Test Case 1: Display events list
        """

        self.assertIn("events", self.driver.current_url.lower(), "Сторінка events не відкрилась")

        cards = self.wait_for_events()
        self.assertTrue(len(cards) > 0, "Список івентів не відображається")

        first_card = cards[0]

        title = first_card.find_element(By.XPATH, ".//*[self::h1 or self::h2 or self::h3 or self::h4]")
        self.assertTrue(title.is_displayed(), "Назва івенту не відображається")

        date = first_card.find_element(By.XPATH, ".//*[contains(@class,'date')]")
        self.assertTrue(date.is_displayed(), "Дата івенту не відображається")

        description = first_card.find_element(By.XPATH, ".//*[contains(@class,'description') or contains(@class,'text')]")
        self.assertTrue(description.is_displayed(), "Опис івенту не відображається")

    def test_open_event_details(self):
        """
        Test Case 2: Open event details
        """

        cards = self.wait_for_events()
        self.assertTrue(len(cards) > 0, "Список івентів не відображається")

        more_button_xpath = "(//button[contains(normalize-space(), 'Більше') or contains(normalize-space(), 'More')])[1]"
        more_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, more_button_xpath))
        )
        more_button.click()

        details = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".event-info-block"))
        )
        self.assertTrue(details.is_displayed(), "Сторінка деталей івенту не відкрилася")

        title = self.driver.find_element(By.XPATH, "//*[self::h1 or self::h2]")
        self.assertTrue(title.is_displayed(), "Назва не відображається")

        date = self.driver.find_element(By.XPATH, "//*[contains(@class,'date')]")
        self.assertTrue(date.is_displayed(), "Дата не відображається")

        description = self.driver.find_element(By.XPATH, "//*[contains(@class,'description') or contains(@class,'text')]")
        self.assertTrue(description.is_displayed(), "Опис не відображається")

    def test_navigation_between_pages(self):
        """
        Test Case 3: Navigation between pages
        """

        # Scroll
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.assertTrue(True)

        # Pagination (optional)
        pagination_elements = self.driver.find_elements(
            By.XPATH,
            "//*[contains(@class,'pagination')]//button | //*[contains(@class,'pagination')]//a"
        )

        if len(pagination_elements) > 0:
            current_url = self.driver.current_url
            pagination_elements[0].click()
            self.wait.until(lambda d: d.current_url != current_url or len(self.wait_for_events()) > 0)

            cards = self.wait_for_events()
            self.assertTrue(len(cards) > 0, "Івенти не завантажились після переходу")
        else:
            print("Pagination не знайдена — пропускаємо крок")

        # Reload
        self.driver.refresh()
        cards = self.wait_for_events()
        self.assertTrue(len(cards) > 0, "Після refresh івенти не відображаються")


if __name__ == "__main__":
    unittest.main()
