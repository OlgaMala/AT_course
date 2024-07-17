# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
fix_site = 'https://fix-online.sbis.ru/'
user_login, user_password = 'Гремлины123', 'Гремлины123'

try:
    driver.get(fix_site)
    driver.maximize_window()
    sleep(2)

    print('Авторизация на сайте')
    login = driver.find_element(By.CSS_SELECTOR,
                                '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_hideCustomPlaceholder')
    login.send_keys(user_login, Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(7)

    print('Перейти в реестр Контакты')
    tab_contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] [data-qa="NavigationPanels-Accordion__title"]')
    tab_contacts.click()
    sleep(2)
    contacts_sub = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contacts_sub.click()
    sleep(5)

    print('Написать сообщение')
    button_plus = driver.find_element(By.CSS_SELECTOR, 'i.controls-BaseButton__icon.icon-RoundPlus')
    button_plus.click()
    sleep(6)

    print('Выбрать адресата')
    input_place = driver.find_element(By.CSS_SELECTOR,
                                      'input.controls-Field.controls-Search__nativeField_caretEmpty_theme_default')
    input_place.send_keys('Гремлин Гремлин', Keys.ENTER)
    sleep(2)
    receiver = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-selector__addressee')
    receiver.click()
    sleep(2)

    print('Отправить сообщение')
    message = driver.find_element(By.CSS_SELECTOR, 'p.textEditor_Viewer__Paragraph')
    message.send_keys('Hello123', Keys.ENTER)
    sleep(2)
    send_button = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    send_button.click()
    sleep(3)

    print('Проверить реестр на наличие сообщения')
    search_place = driver.find_element(By.CSS_SELECTOR, 'input.controls-Field')
    search_place.send_keys('Hello123', Keys.ENTER)
    result = driver.find_element(By.CSS_SELECTOR, '.msg-entity-content_indent_m')
    assert result.text == "Я:\nHello123", 'Неверный результат'

finally:
    driver.quit()
