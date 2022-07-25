#!/usr/bin/env python
# coding: utf-8

# In[28]:


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




class engadget_crawler():
    
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
    def getPostLink(self, url, driver):
        # 關閉-------------      
        def FinishedCrawler(driver):
            driver.close()
        # -----------------  
        
        # 日期格式
        def func(x):
            dot = x.split("・")[0]
            year = x.split("・")[1].split("年")[0]
            month = x.split("・")[1].split("年")[1].split("月")[0]
            day = x.split("・")[1].split("年")[1].split("月")[1].split("日")[0]

            if len(day)  == 3:
                day = day[0] + day[2]
                year = "".join(str(i) for i in year)
                month = "".join(str(i) for i in month)
                day = "".join(str(i) for i in day)
            if len(month) == 3:
                month = month[0] + month[2]
            if len(day) == 3:
                day = day[0] + day[2]
            final_date = year + "." + month + "." + day
            return final_date
        #  ---------------------------------------------------     
        
        driver.get(url)
        try:
            older_btn=driver.find_element(By.XPATH,'//*[@id="module-engadget-tag-streams"]/div[2]/div/div[2]/div[1]/ul/li[21]/button')
            ActionChains(driver).move_to_element(older_btn).perform()
            older_btn.click()
            time.sleep(0.5)
        except:
            print("No older Btn")
            
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        post_link_list = []
        soup = BeautifulSoup(driver.page_source,"html.parser")

        for datee in soup.find_all("div", class_="Px(20px)--sm Py(15px)--sm Bgc(white)--sm W(100%)"):

            for l in datee.find_all("a", class_="C(engadgetFontBlack) Fw(400) Td(n) Bdbw(1px):h Bdbc(lightgrey):h Bdbs(s):h Fz(30px) Lh(35px) Fz(22px)--sm Lh(25px)--sm"):
                # 抓日期
                for d in datee.find_all("span", class_="C(engadgetFontLightGray) Mt(3px)"):
                    temp = []
                    temp.append(l.get_text())
                    temp.append("https://chinese.engadget.com/"+l["href"])
                    temp.append(d.get_text())
                    post_link_list.append(temp)

        link_df = pd.DataFrame(data=post_link_list, columns=['Post Title', 'Link', 'Date'])
        link_df["Date"] = link_df["Date"].apply(func)
        link_df["Date"] = pd.to_datetime(link_df["Date"], format="%Y/%m/%d")
        FinishedCrawler(driver)
        return link_df
    
    
    #抓取貼文留言
    def getPostComment(self, url, driver):
        
        #  關閉-----------------      
        def FinishedCrawler(driver):
            driver.close()
        # ----------------------         
        
        
        driver.get(url)
        #Get Comment       
        soup = BeautifulSoup(driver.page_source,"html.parser")
        content_all = str(soup.find("div",id="post-center-col"))
        content_html = content_all[:content_all.find('<div id="post-bottom-social-share">')]
        content_fix_soup = BeautifulSoup(content_html, "html.parser")
        content_text_all=[]
        for i in content_fix_soup.find_all("p"):
            if(i.find("a") != None):
                continue
            else:
                content_text_all.append(i.get_text())
        FinishedCrawler(driver)
        return content_text_all

    
    
if __name__ == "__main__":    
    link1 = 'https://chinese.engadget.com/tag/iphone%2013'
    now = datetime.datetime.now().strftime("%Y%m%d")
    
    engadget = engadget_crawler(link1)
    driver = engadget.OpenChromeDriver()
    
    # Title/Link    
    link_df = engadget.getPostLink(link1, driver)
    file_name = "crawler_data/Engadget_iphone13_Link"+now+".csv"
    link_df.to_csv(file_name, index=False, encoding="utf-8")
    print(f"Below is Post Title & Lnik: {link_df}")

    
    # Post Comment 
    contents = []
    for link in link_df.loc[:,"Link"]:
        driver = engadget.OpenChromeDriver()
        contents.append(engadget.getPostComment(link,driver))
    content_df = pd.DataFrame({'Content': contents})
    
    # 合併兩dataframe    
    all_df = link_df.join(content_df)
    all_df = all_df[all_df.Content.str.len()>0].reset_index(drop=True)
    for i in range(len(all_df)):
        if len(all_df.Content[i][0])<1:
            all_df = all_df.drop(i)
    file_name2 = "crawler_data/Engadget_iphone13_Data"+now+".csv"
    all_df.to_csv(file_name2, index=False, encoding="utf-8")
    print(f"Below is Post All information: {all_df}")


# In[ ]:




