from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    usuario = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    usuario.send_keys("tmsmith")

    senha = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    senha.send_keys("SuperSecretPassword!")

    botao = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type=submit]")))
    botao.click()

    sleep(1)

    msg = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "You logged into a secure area!" in msg
    assert driver.current_url.endswith("/secure")
    print("CT01 Aprovado: ", msg)
    print(driver.title)
    sleep(3)
finally:
    driver.quit()