# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm
@time:2017/10/29 12:36
"""

import time
import pymysql
# import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from weibo_url import dict1, dict2
from lxml import etree
import random


class weibo():
  '''
  
  '''
  
  def __init__(self):
    self.username = 'userName'
    self.password = 'passwd'
    self.rootUrl = 'http://s.weibo.com/'
    
    self.connect = pymysql.connect(host='192.168.36.80', user='root', passwd='Temp@1026', db='gyp_test', charset='utf8')
    self.cursor = self.connect.cursor()
  
  def getRandomSleep(self):
    return random.randint(3, 5)
  
  def loginWeibo(self):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    executable_path = 'C:/Users/dell/Downloads/exe_file/chromedriver.exe'
    self.browser = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
    self.browser.get(self.rootUrl)  # 打开微博网址
    time.sleep(self.getRandomSleep())
    
    login_btn = self.browser.find_element_by_xpath('//a[@node-type="loginBtn"]')
    login_btn.click()  # 点击登陆按钮
    time.sleep(self.getRandomSleep())
    
    userNameInput = self.browser.find_element_by_xpath('//input[@node-type="username"]')
    passwordInput = self.browser.find_element_by_xpath('//input[@node-type="password"]')
    userNameInput.clear()
    userNameInput.send_keys(self.username)
    # time.sleep(self.getRandomSleep())
    passwordInput.clear()
    passwordInput.send_keys(self.password)
    time.sleep(self.getRandomSleep())  # 输入用户名和密码
    
    sub_btn = self.browser.find_element_by_xpath('//a[@suda-data="key=tblog_weibologin3&value=click_sign"]')
    sub_btn.click()  # 提交登陆
    time.sleep(self.getRandomSleep())
  
  def getPageForKeyWords(self, key, pageNum):
    self.isVerify()
    findUser = self.browser.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/ul/li/a[3]')
    findUser.click()  # 点击找人
    
    searchInput = self.browser.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/div/div/div[2]/div/input')
    searchInput.send_keys(key)  # 输入关键词
    # time.sleep(self.getRandomSleep())
    searchSubmit = self.browser.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/div/div/div[1]/a')
    searchSubmit.click()  # 点击搜索
    time.sleep(self.getRandomSleep())
    
    for i in range(pageNum):
      self.isVerify()
      self.parserHtml2Mysql(key, self.browser.page_source)  # 存入数据库
      self.browser.execute_script("window.scrollBy(0,4000)")  # 下滑
      time.sleep(1)  # 下滑
      nextPage = self.browser.find_element_by_css_selector('a.next')  # 翻页
      nextPage.click()
      time.sleep(self.getRandomSleep())
    
    self.browser.get('http://s.weibo.com/?Refer=STopic_icon')
    time.sleep(self.getRandomSleep())
  
  def getPageForUrl(self, key, url, pageNum):
    page = self.browser.get(url)
    for i in range(pageNum):
      if i != 0:
        nextPage = self.browser.find_element_by_css_selector('a.next')  # 翻页
        nextPage.click()
      time.sleep(self.getRandomSleep())
      self.isVerify()
      self.browser.execute_script("window.scrollBy(0,5000)")  # 下滑
      time.sleep(1)  # 下滑
      self.parserHtml2Mysql(key, self.browser.page_source)  # 存入数据库

  def parserHtml2Mysql(self, key, html):
    tree = etree.HTML(html)
    cover_urls = tree.xpath('//img[@class="W_face_radius"]/@src')
    nick_name = tree.xpath('//a[@class="W_texta W_fb"]/@title')
    # digests = tree.xpath('//div[@class="person_info"]/p/text()')

    digests = []
    person_details = tree.xpath('//div[@class="person_detail"]')
    for digest in person_details:
      try:
        digests.append(''.join(digest.xpath('div/p//text()')).strip())
      except:
        digests.append('')
        continue
        
    for cover, name, digest in zip(cover_urls, nick_name, digests):
      lst = [key, cover, name, digest]
      print(digest)
      # self.insert_data(lst)
  
  def insert_data(self, lst):
    sql = 'insert into weibo_user VALUES ("{}","{}","{}","{}")'
    
    self.cursor.execute(sql.format(lst[0], lst[1], lst[2], lst[3]))
    self.connect.commit()
  
  def isVerify(self):
    try:
      verify_img = self.browser.find_element_by_xpath('//img[@node-type="yzm_img"]')
      if verify_img:
        print('please input yzm in net page!')
        time.sleep(20)
    except NoSuchElementException:
      pass
  
  def closeMysql(self):
    self.cursor.close()
    self.connect.close()
  
  def closeBrowser(self):
    self.browser.close()


if __name__ == '__main__':
  obj = weibo()
  obj.loginWeibo()
  # method1 spider from keywords
  # for key in dict1.keys():
  #   obj.getPage(key,4)
  #   obj.closeBrowser()
  # for key in dict2.keys():
  #   obj.getPage(key,10)
  #   obj.closeBrowser()

  # method2 spider from fixed url
  for key, url in dict1.items():
    print('current is:{},url:{}'.format(key,url))
    obj.getPageForUrl(key, url, 6)

  obj.closeBrowser()
  obj.closeMysql()
  
  # test temp.txt
  # with open('temp.txt','r',encoding='utf8') as f:
  #   html = f.read()
  # obj.parserHtml2Mysql('temp',html)
