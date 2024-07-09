import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument("--user-agent=")


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def page(request):
    driver = webdriver.Chrome(service=service, options=options)
    param = request.param
    if param == "whats_new":
        driver.get("https://magento.softwaretestingboard.com/what-is-new.html")
    if param == "sale":
        driver.get("https://magento.softwaretestingboard.com/sale.html")
    yield driver
    driver.quit()
