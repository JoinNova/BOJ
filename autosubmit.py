from selenium import webdriver
from time import sleep
browser = webdriver.Chrome(executable_path=r"C:\Users\win10\AppData\Local\Programs\Python\chromedriver.exe")
#browser.get('https://www.acmicpc.net/login/?next=%2F')
browser.get('https://www.acmicpc.net/login?next=%2F') #사이트주소바뀜
ID = "**************"
PW = "**************"
elem_login = browser.find_element_by_name("login_user_id")
elem_login.send_keys(ID)
elem_login = browser.find_element_by_name("login_password")
elem_login.send_keys(PW)
browser.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/form/div[4]/div[2]/button').click()
while True:
  browser.get('https://www.acmicpc.net/submit/10944/9280398') # 이전에 제출한 곳의 주소
  browser.find_element_by_xpath('//*[@id="submit_form"]/div[4]/div/button').click()
  sleep(72) #72초 룰 생김 72이내 재제출 불가
