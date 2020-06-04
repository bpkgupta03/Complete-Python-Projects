from selenium import webdriver

chrome_browser=webdriver.Chrome('./chromedriver.exe')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo ' in chrome_browser.title

chrome_browser.maximize_window()
show_msg_button=chrome_browser.find_element_by_class_name('btn-default')
#print(show_msg_button.get_attribute('innerHTML'))


msg=chrome_browser.find_element_by_id('user-message')
msg.clear()
msg.send_keys('heyyyy My name is Bhanu')

show_msg_button.click()

#chrome_browser.quit()
display=chrome_browser.find_element_by_id('display')
#assert 'heyyyy My name is Bhanu' in display.text
print(display.get_attribute('innerHTML'))

chrome_browser.close()
