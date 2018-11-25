#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time
from selenium.webdriver.chrome.options import Options
import json


# In[11]:


#data={"Id":[],"Tên người dùng":[],"SĐT":[],"Địa chỉ":[],"Khu vực":[],"Mặt hàng":[],"Giá":[],"Mô tả":[],"Thời gian đăng":[],"Loại tin":[]}
data_xpath={"Tên người dùng":[],"SĐT":[],"Địa chỉ":[],"Khu vực":[],"Mặt hàng":[],"Giá":[],"Mô tả":[],"Thời gian đăng":[],"Loại tin":[]}


# In[12]:


data_xpath['Tên người dùng']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]'
data_xpath['Giá']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]'
data_xpath['Mặt hàng']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[1]/h1'
data_xpath['Mô tả']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/p'
data_xpath['SĐT']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/h4/strong'
data_xpath['Địa chỉ']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/span'
data_xpath['Thời gian đăng']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[1]/div[2]/span'
data_xpath['Khu vực']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[4]/div/div[2]/div'
data_xpath['Loại tin']='//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[3]/div/div/div/div[2]/span'


# In[19]:


#Ham an next bai
def Next_ad():
    try:
        element_Next=browser.find_element_by_id('next_ad')
        element_Next.click()
    except:
        browser.refresh()
#Ham show so dien thoai
def show_phone_bnt():
    try:
        element_showphone=browser.find_element_by_id('show_phone_bnt')
        element_showphone.click()
    except:
        pass
def Crawl_item():
    try:
        Id=browser.current_url.split('/')[5].split('.')[0]
        data['Id']=Id
    except:
        data['Id']=''
    try:
        data['Thời gian đăng']=browser.find_element_by_xpath(data_xpath['Thời gian đăng']).text
    except:
        data['Thời gian đăng']=''
    try:
        data['Tên người dùng']=browser.find_element_by_xpath(data_xpath['Tên người dùng']).text
    except:
        data['Tên người dùng']=''
    try:
        data['Giá']=browser.find_element_by_xpath(data_xpath['Giá']).text
    except:
        data['Giá']=''
    try:
        data['Mô tả']=browser.find_element_by_xpath(data_xpath['Mô tả']).text
    except:
        data['Mô tả']=''
    try:
        data['Mặt hàng']=browser.find_element_by_xpath(data_xpath['Mặt hàng']).text
    except:
        data['Mặt hàng']=''
    try:
        data['SĐT']=browser.find_element_by_xpath(data_xpath['SĐT']).text
    except:
        data['SĐT']=''
    try:
        data['Địa chỉ']=browser.find_element_by_xpath(data_xpath['Địa chỉ']).text
    except:
        data['Địa chỉ']=''
    try:
        data['Khu vực']=browser.find_element_by_xpath(data_xpath['Khu vực']).text
    except:
        pass
    try:
        data['Loại tin']=browser.find_element_by_xpath(data_xpath['Loại tin']).text
    except:
        data['Loại tin']='Cần bán'


# In[20]:


#chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)


# In[21]:


browser.get("https://www.chotot.com/ha-noi/quan-ba-dinh/mua-ban")
time.sleep(1)
browser.maximize_window()
time.sleep(2)


# In[22]:


element=browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div/div[1]/main/div/div[1]/div[6]/div/div[2]/ul/div[1]')
element.click()
time.sleep(1)


# In[23]:


file = open("Data.json", "w")


# In[24]:


for i in range(1,1000):
    data={}
    print("Crawl data",i,end=' ')
    print(".",end=' ')
    show_phone_bnt()
    time.sleep(1)
    print(".",end=' ')
#     try:
#         Id=''
#         Id=browser.current_url.split('/')[5].split('.')[0]
#         if Id in list(data['Id']):
#             Next_ad()
#             continue
#         data['Id']=Id
#     except:
#         continue
    Crawl_item()
    print(".",end=' ')
    line = json.dumps(dict(data), ensure_ascii=False)+"\n"
    file.write(line)
    Next_ad()
    print('Done')
    time.sleep(2)


# In[25]:


file.close()


# In[ ]:




