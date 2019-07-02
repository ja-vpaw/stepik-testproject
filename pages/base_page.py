from selenium.common.exceptions import NoSuchElementException


class BasePage(object):


    def __init__(self, browser, url, timeout=5):
        """Конструктор класса.
               :param browser:
               :param url:
               :param timeout: неявное время ожидания появления элемента на странице
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        """метод открывает нужную страницу,
               используя метод get()
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
