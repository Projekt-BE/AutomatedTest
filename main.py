from random import random
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


LOADING_TIMEOUT = 10
WAIT_TIME = 1


def main():
    driver = webdriver.Firefox()

    driver.get("http://0976baee8833.ngrok.io/index.php")
    driver.set_window_size(1200, 833)

    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-389 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-389 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(1) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary > .material-icons"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-399 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(1) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-422 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(2) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-389 > .dropdown-item"))).click()

    driver.find_element(By.LINK_TEXT, "Tworzenie gier").click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(1) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-389 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(5) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bootstrap-touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary > .material-icons"))).click()
    element = WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".add-to-cart")))

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body")))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-436 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(2) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary > .material-icons"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".header .hidden-sm-down"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-389 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(8) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary > .material-icons"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-408 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(8) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))).click()
    element = WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ol > li:nth-child(4) span")))

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-389 > .dropdown-item"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature:nth-child(7) img"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".touchspin-up"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary > .material-icons"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-secondary"))).click()

    time.sleep(WAIT_TIME)
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".header"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".header .hidden-sm-down"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-item:nth-child(7) .col-md-2 .material-icons"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-sm-center > .btn"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "firstname"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "firstname"))).send_keys("adam")
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "lastname"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "lastname"))).send_keys("nowak")
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "email"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "email"))).send_keys(f'{int(random()*1000000)}@gmail.com')
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "password"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "password"))).send_keys("test12345")
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "continue"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "address1"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "address1"))).send_keys("adamkowo")
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "postcode"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "postcode"))).send_keys("12-123")
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-group:nth-child(9)"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "city"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "city"))).send_keys("adamowo")
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-fields"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "confirm-addresses"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(4) .col-sm-5 .col-xs-12"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.NAME, "confirmDeliveryOption"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#payment-option-2-container > label > span"))).click()

    driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ps-shown-by-js > .btn"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".account > .hidden-sm-down"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#history-link .material-icons"))).click()
    WebDriverWait(driver, LOADING_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".logout"))).click()

    driver.quit()


if __name__ == '__main__':
    main()
