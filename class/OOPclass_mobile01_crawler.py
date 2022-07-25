#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sys
import time
import pandas as pd
import datetime




class mobile01_crawler():
    
    def __init__(self, url):
        self.url = url
        
        
    #開啟瀏覽器新分頁
    def OpenChromeDriver(self):
        ban_notify=webdriver.ChromeOptions()
        prefs={"profile.default_content_setting_values.notifications" : 2}
        ban_notify.add_experimental_option("prefs",prefs)
        gchrome=webdriver.Chrome(options=ban_notify)
        return gchrome    
    
    #抓取貼文連結
    def getAllPageLink(self, url, driver):
        
        # 關閉-------------      
        def FinishedCrawler(driver):
            driver.close()
        # -----------------       
        
        
        # 抓取單一貼文連結----------------- 
        def getPostLink(driver):
            post_link_list = []
            search_page = driver.page_source
            soup = BeautifulSoup(search_page,"html.parser")

            for l in soup.find_all("div", class_="gsc-thumbnail-inside"):
                temp_soup = BeautifulSoup(str(l),"html.parser")
                temp_target = temp_soup.find("a", class_="gs-title")
                temp = []
                temp.append(temp_target.get_text())
                temp.append(temp_target.get('href'))
                post_link_list.append(temp)

            return post_link_list
        # ----------------------------------  
        
        
        # Parameter Set
        all_post_link = []

        driver.get(url)
        time.sleep(2)

        #Close Cookie Btn
        close_cookie_btn = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/button")
        ActionChains(driver).move_to_element(close_cookie_btn).perform()
        close_cookie_btn.click()
        time.sleep(2)

        #Get All Link
        all_post_link.extend(getPostLink(driver))
        pages = driver.find_elements(By.CLASS_NAME, "gsc-cursor-page")
        for page in range(1,len(pages)):
            try:
                now_page_btn = pages[page]
                ActionChains(driver).move_to_element(now_page_btn).perform()
                now_page_btn.click()
                time.sleep(5)
            except:
                print("No More Pages")

            all_post_link.extend(getPostLink(driver))
            pages = driver.find_elements(By.CLASS_NAME, "gsc-cursor-page")

        link_df = pd.DataFrame(data=all_post_link, columns=['Post Title', 'Link'])
        FinishedCrawler(driver)
        return link_df
    
    
    #抓取貼文留言
    def getPostComment(self, url, driver):
        
        #  關閉-----------------      
        def FinishedCrawler(driver):
            driver.close()
        # ----------------------         
        
        
        driver.get(url)
        errortime = 0
        post_date_list = []
        
        try:
            #Get Comment       
            soup = BeautifulSoup(driver.page_source,"html.parser")
            content_all = soup.find("div",itemprop="articleBody")
            date_all = soup.find("span", class_="o-fNotes o-fSubMini")
            if isinstance(content_all, type(None)):
                content_all = 'No Content'
                date_all = 'No Date'
            else:
                content_all = content_all.get_text().strip().split('\n')
                date_all = date_all.get_text()
            FinishedCrawler(driver)

        except OSError:
            if errortime == 0:
                print(url)
                time.sleep(15)
                soup = BeautifulSoup(driver.page_source,"html.parser")
                content_all = soup.find("div",itemprop="articleBody")
                date_all = soup.find("span", class_="o-fNotes o-fSubMini")

                if isinstance(content_all, type(None)):
                    content_all = 'No Content'
                    date_all = 'No Date'
                else:
                    content_all = content_all.get_text().strip().split('\n')
                    date_all = date_all.get_text()
                FinishedCrawler(driver)

            else:
                print(url)
                time.sleep(15)
                soup = BeautifulSoup(driver.page_source,"html.parser")
                content_all = soup.find("div",itemprop="articleBody")
                date_all = soup.find("span", class_="o-fNotes o-fSubMini")

                if isinstance(content_all, type(None)):
                    content_all = 'No Content'
                    date_all = 'No Date'
                else:
                    content_all = content_all.get_text().strip().split('\n')
                    date_all = date_all.get_text()
                FinishedCrawler(driver)
                errortime+=1

        post_date_list.append(content_all)
        post_date_list.append(date_all)

        return post_date_list

    
    
if __name__ == "__main__":    
    link1 = 'https://www.mobile01.com/googlesearch.php?q=iphone%252013&c=16'
    now = datetime.datetime.now().strftime("%Y%m%d")
    
    mobile01 = mobile01_crawler(link1)
    driver = mobile01.OpenChromeDriver()
    
    # Title/Link    
    Title_Link = mobile01.getAllPageLink(link1, driver)
    Title_Link = Title_Link[Title_Link.Link.str.len()>0].reset_index(drop=True)
    file_name = "crawler_data/Mobile01_iphone13_Link"+now+".csv"
    Title_Link.to_csv(file_name, index=False, encoding="utf-8")
    print(f"Below is Post Title & Lnik: {Title_Link}")
    
    # Post Comment 
    contents = []
    for link in Title_Link.loc[:,"Link"]:
        driver = mobile01.OpenChromeDriver()
        contents.append(mobile01.getPostComment(link,driver))
    content_df = pd.DataFrame(contents)
    
    # 重設欄位
    re_columns = ['Content', 'Date']
    content_df.columns = re_columns
    
    # 調整日期
    content_df['Date'] = pd.to_datetime(content_df['Date'], errors='coerce')
    content_df['Date'] = content_df['Date'].dt.date
    
    # 合併兩dataframe    
    all_df = Title_Link.join(content_df)
    all_df = all_df.drop(all_df[all_df['Content'] == 'No Content'].index).reset_index(drop=True)
    file_name2 = "crawler_data/Mobile01_iphone13_Data"+now+".csv"
    all_df.to_csv(file_name2, index=False, encoding="utf-8")
    print(f"Below is Post All information: {all_df}")

