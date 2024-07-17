# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
tenzor_site = 'https://tensor.ru/'
tenzor_site_about = 'https://tensor.ru/about'

try:
    driver.get(sbis_site)
    driver.maximize_window()
    sleep(1)
    print('Навести курсор на Контакты и кликнуть')
    tab_contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    tab_contacts.click()
    print('Найти баннер Тензор и кликнуть по нему')
    banner_tenzor = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-12"]')
    banner_tenzor.click()
    print('Проверить адрес сайта')
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    assert driver.current_url == tenzor_site, 'Неверный адрес сайта'
    print('Поиск блока "Сила в людях"')
    block_sila = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    print('Проверка названия блока Сила в людях')
    assert block_sila.text[0:12] == 'Сила в людях'
    print('Перейти по кнопке Подробнее')
    button_else = driver.find_element(By.CSS_SELECTOR, 'a[href="/about"]')
    assert button_else.is_displayed()
    button_else.click()
    sleep(3)
    print('Проверить адрес сайта')
    assert driver.current_url == tenzor_site_about, 'Неверный адрес сайта'
    print('Пройден успешно')

finally:
    driver.quit()
