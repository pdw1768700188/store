from selenium import  webdriver

from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()

driver.get("http://bilibili.com")

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/span[1]/div/span/div').click()

data=driver.window_handles

driver.switch_to(data[1])

driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(13077096702)
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('pdw03226611')

driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()






