from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = "test01user"
password = "quTruv-sepbaz-9cipjy"

log_adress_xpath = "https://passport.yandex.ru/auth?retpath=https%3A%2F%2Ftaxi.yandex.ru%2Fru_ru%2F&from=taxi"
login_area_xpath = '//*[@id="passp-field-login"]'
password_area_xpath = '//*[@id="passp-field-passwd"]'
adress_a_xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[5]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/span[1]/span[2]/textarea'
adress_a_menu_xpath = '/html/body/div[5]/div/div[1]'
adress_b_xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[5]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/span[1]/span[2]/textarea'
adress_b_menu_xpath = '/html/body/div[5]/div/div[1]'
text_price_xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[5]/div/div[1]/div/div[2]/div/div/div/button[1]/span[2]/span[3]/span[3]'

class Action:

    def __init__(self,ad_a,ad_b,pri):
        self.driver = webdriver.Safari()
        self.adress_a= ad_a
        self.adress_b = ad_b
        self.price=pri

    def login(self,logg,passs):

        self.driver.get(log_adress_xpath)
        self.driver.find_element(By.XPATH,login_area_xpath).click()
        self.driver.find_element(By.XPATH,login_area_xpath).send_keys(logg)
        self.driver.find_element(By.XPATH,login_area_xpath).send_keys(Keys.ENTER)

        time.sleep(1)
        self.driver.find_element(By.XPATH,password_area_xpath).click()
        self.driver.find_element(By.XPATH,password_area_xpath).send_keys(passs)
        self.driver.find_element(By.XPATH,password_area_xpath).send_keys(Keys.ENTER)

    def count_cost(self):
        time.sleep(4)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,adress_a_xpath ))).clear()
        time.sleep(4)
        self.driver.find_element(By.XPATH,adress_a_xpath).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.XPATH, adress_a_xpath).send_keys(Keys.ARROW_RIGHT)
        for i in range(70):
            self.driver.find_element(By.XPATH, adress_a_xpath).send_keys(Keys.BACKSPACE)
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,adress_a_xpath))).send_keys(self.adress_a)
        time.sleep(4)
        self.driver.find_element(By.XPATH,adress_a_menu_xpath).click()


        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH,adress_b_xpath ))).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,adress_b_xpath).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.XPATH, adress_b_xpath).send_keys(Keys.ARROW_RIGHT)
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH,adress_b_xpath))).send_keys(self.adress_b  )
        time.sleep(3)
        self.driver.find_element(By.XPATH,adress_b_menu_xpath).click()
        time.sleep(3)
        return self.driver.find_element(By.XPATH,text_price_xpath).get_attribute("innerHTML")
        #.split(">")[-3].split("<")[0]

    def close(self):
        self.driver.close()

def start(add_a,add_b,price):
        try:
            zapros = Action(add_a,add_b,price)
            zapros.login(username,password)
            k =  str(zapros.count_cost())
            print(k)
            k = k.split("₽")[0]
            try:
                k = int(k)
            except:
                k = 99999
            zapros.close()
            return k
        except:
            print("ERRR")
            return 99999
#start("Ярославль Гагарина 11","Ярославль Губкина 16",250)








#https://passport.yandex.ru/auth/reg?retpath=https%3A%2F%2Fhelpers.tap.yandex.ru%2Freturn-to-app%3Ffb%3Dhttps%3A%2F%2Ftaxi.yandex.ru%2Fru_ru%2F&origin=taxi_front_form
