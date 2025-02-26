from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service(executable_path='C:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#Abre una página web
driver.get('https://juansalinasponce.github.io/')

# Imprime el título de la página
print(driver.title)

# Cierra el navegador
#driver.quit()