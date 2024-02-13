from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep
import message_telegram

def Find_Element(driver : webdriver.Chrome, by, value : str) -> WebElement:
    while True:
        try:
            element = driver.find_element(by, value)
            break
        except:
            pass
        sleep(0.1)
    return element

def Find_Elements(driver : webdriver.Chrome, by, value : str) -> list[WebElement]:
    while True:
        try:
            elements = driver.find_elements(by, value)
            if len(elements) > 0:
                break
        except:
            pass
        sleep(0.1)
    return elements

driver = webdriver.Chrome()
driver.maximize_window()

wise_percent_set = input('Please input Wise percent : ')
paypal_percent_set = input('Please input Paypal percent : ')
skrill_percent_set = input('Please input Skrill percent : ')

urls = ['https://saldo.com.ar/a/bitcoin/wise_usd/1', 'https://saldo.com.ar/a/bitcoin/skrill/1', 'https://saldo.com.ar/a/bitcoin/palpal/1']

start_number = 1

while True:
    driver.get(urls[0])

    if start_number == 1:
        more_button = Find_Element(driver, By.CLASS_NAME, 'more-options-button')
        driver.execute_script('arguments[0].click();', more_button)

    wise_price_lists = Find_Elements(driver, By.CLASS_NAME, 'tree-dot')
    wise_price = wise_price_lists[3].text.split(' ')
    wise_percent = wise_price[5]
    wise_start_index = next((i for i, c in enumerate(wise_percent) if c.isdigit()), None)
    wise_end_index = next((i for i in reversed(range(len(wise_percent))) if wise_percent[i].isdigit()), None)
    wise_percent_str = wise_percent[wise_start_index:wise_end_index + 1]
    wise_percent_number = float(wise_percent_str)
    cycle_number_result = f'{"-"*20} {start_number} {"-"*20}'
    message_telegram.send_message(cycle_number_result)

    if wise_percent_number >= float(wise_percent_set):
        wise_result = '$ ' + wise_price[0] + ' / Wise Market is ' + wise_price[5].replace(')', '').replace('+', '')
        print(wise_result)
        message_telegram.send_message(wise_result)
    else:
        print('None change')

    driver.get(urls[1])
    skrill_price_lists = Find_Elements(driver, By.CLASS_NAME, 'tree-dot')
    skrill_price = skrill_price_lists[3].text.split(' ')
    skrill_percent = skrill_price[5]
    skrill_start_index = next((i for i, c in enumerate(skrill_percent) if c.isdigit()), None)
    skrill_end_index = next((i for i in reversed(range(len(skrill_percent))) if skrill_percent[i].isdigit()), None)
    skrill_percent_str = skrill_percent[skrill_start_index:skrill_end_index + 1]
    skrill_percent_number = float(skrill_percent_str)

    if skrill_percent_number >= float(skrill_percent_set):
        skrill_result = '$ ' + skrill_price[0] + ' / Skrill Market is ' + skrill_price[5].replace(')', '').replace('+', '')
        print(skrill_result)
        message_telegram.send_message(skrill_result)
    else:
        print('None change')

    driver.get(urls[2])
    paypal_price_lists = Find_Elements(driver, By.CLASS_NAME, 'tree-dot')
    paypal_price = paypal_price_lists[4].text.split(' ')
    paypal_percent = paypal_price[5]
    paypal_start_index = next((i for i, c in enumerate(paypal_percent) if c.isdigit()), None)
    paypal_end_index = next((i for i in reversed(range(len(paypal_percent))) if paypal_percent[i].isdigit()), None)
    paypal_percent_str = paypal_percent[paypal_start_index:paypal_end_index + 1]
    paypal_percent_number = float(paypal_percent_str)

    if paypal_percent_number >= float(paypal_percent_set):
        paypal_result = '$ ' + paypal_price[0] + ' / Paypal Market is ' + paypal_price[5].replace(')', '').replace('+', '')
        print(paypal_result)
        message_telegram.send_message(paypal_result)
    else:
        print('None change')
    start_number += 1
    driver.delete_all_cookies()
    sleep(60)