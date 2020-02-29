from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions
import getpass
import time
from date_checks import *



vusername = input('Username: ')
vpassword = getpass.getpass(prompt='Password: ')
dateday_beg = input('Informe primeira data (dd/mm/yyyy): ')
dateday_end = input('Informe última data (dd/mm/yyyy): ')


beg_work = '09:00'
out_lunch = '13:00'
in_lunch = '14:00'
out_work = '18:00'
description = 'Manutencao regular'
geckodriver_driver_path=r'C:\geockdriver\geckodriver.exe'
url = 'http://apps.wafx.com.br/chronus/Pages/Cadastro/Apontamento.aspx'


profile = webdriver.FirefoxProfile()
profile.set_preference("intl.accept_languages","pt")
profile.update_preferences
driver = webdriver.Firefox(executable_path=geckodriver_driver_path, firefox_profile=profile)
driver.get(url)
assert "Chronus" in driver.title


def chronus_login(vusername, vpassword):
    username = driver.find_element_by_name('LoginAcessoNucleo1$txtUsuario')
    username.clear()
    username.send_keys(vusername)

    password = driver.find_element_by_name('LoginAcessoNucleo1$txtSenha')
    password.clear()
    password.send_keys(vpassword)

    btnlogin = driver.find_element_by_name('LoginAcessoNucleo1$btnLogar')
    btnlogin.click()



def slow_type(vfield, text):
    for character in text:
        vfield.send_keys(character)
        time.sleep(0.03)
    vfield.send_keys(Keys.TAB)
    time.sleep(2)


def fill_body_fields():
    
    body_data = [
    ['ctl00$content_body_area$txtEntrada', beg_work],
    ['ctl00$content_body_area$txtAlmoco', out_lunch],
    ['ctl00$content_body_area$txtRetorno', in_lunch],
    ['ctl00$content_body_area$txtSaida', out_work],
    ['ctl00$content_body_area$txtAtividade', description],
    ['ctl00$content_body_area$btnGravar_input', '']
    ]

    for field_name, field_value in body_data:
        try:
            field = WebDriverWait(driver, 3).until(Ec.presence_of_element_located((By.NAME, field_name)))
            
            if 'Gravar_input' in field_name:
                field.click()
            else:
                field.clear()
                slow_type(field, field_value)

        except exceptions.StaleElementReferenceException as e:
            print(e)



def fill_date_field(vdate):
    field = WebDriverWait(driver, 3).until(Ec.presence_of_element_located((By.NAME, 'ctl00$content_body_area$rdiData')))
    field.clear()
    field.send_keys(vdate)
    field.send_keys(Keys.TAB)
    time.sleep(1.5)
            


chronus_login(vusername, vpassword)


dateday_beg = conv_str_to_date(dateday_beg)
dateday_end = conv_str_to_date(dateday_end)

while dateday_beg <= dateday_end:
    
    dateday_str = datetime.datetime.strftime(dateday_beg, '%d/%m/%Y')

    if (check_if_not_holiday(dateday_beg) and dateday_beg.weekday() not in (5, 6)):
        fill_date_field(dateday_str)
        fill_body_fields()
    else:
        print(dateday_str + ' is an holiday or weekend.')
    
    dateday_beg += datetime.timedelta(days=1)
    
driver.close()