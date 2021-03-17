from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas
#opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--star-maximized')
options.add_argument('--disable-extensions')

driver_path='/home/rogelio/Documentos/Python/scrapping/chromedriver'

driver=webdriver.Chrome(driver_path,chrome_options=options)


#inicializamos el navegadir
driver.get('https://www.meteored.mx/')


#WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#search'))).send_keys('Ozzy osburne')
#WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button#search-icon-legacy'))).click()
#WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ytd-video-renderer.style-scope ytd-item-section-renderer'.replace(" ",".")))).click()
#WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'ytd-video-renderer.style-scope ytd-item-section-renderer'.replace(" ",".")))).click()
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#buscador'))).send_keys('Garcia')
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#buscador'))).send_keys(Keys.ENTER)
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/span[2]/span/span/ul/li[3]/a'))).click()
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/span[2]/span/span[1]/section/span[2]/div[1]/div/svg/rect[1]')))

texto = driver.find_element_by_xpath('/html/body/main/span[2]/span/span[1]/section/span[2]/div[1]/div/svg/rect[1]')
texto = texto.text
print(texto)
