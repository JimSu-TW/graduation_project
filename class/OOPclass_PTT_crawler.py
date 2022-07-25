#!/usr/bin/env python
# coding: utf-8

# In[23]:


import datetime
from selenium import webdriver
from PTTLibrary import PTT
import bs4
from bs4 import BeautifulSoup
import requests 
from dateutil import parser
import pandas as pd
import time


class ptt_crawler():
    
    def __init__(self, url):
        self.url = url
        
        
    #開啟瀏覽器新分頁
    def OpenChromeDriver(self):
        ban_notify=webdriver.ChromeOptions()
        prefs={"profile.default_content_setting_values.notifications" : 2}
        ban_notify.add_experimental_option("prefs",prefs)
        gchrome=webdriver.Chrome(options=ban_notify)
        return gchrome    

# ---------------------------------------------------
    #抓取單一頁數的貼文連結
    def getOnePage(self, url, driver):
        
        post_title_list = []
        post_link_list = []

        my_headers = {'cookie': 'over18=1;'}
        response = requests.get(url, headers = my_headers)

        soup = bs4.BeautifulSoup(response.text,"html.parser")
        titles = soup.find_all('div','title')

        for t in titles:
            temp1 = []
            # 爬標題
            temp1.append(t.text.strip())
            post_title_list.append(temp1)

        for items in soup.select('div[class = "title"] a'):
            temp2 = []
            # 爬網址
            temp2.append("https://www.ptt.cc" + str(items.get('href')))
            post_link_list.append(temp2)

        Title_list = pd.DataFrame(post_title_list)
        Title_list = Title_list.rename(columns={0: 'Post Title'})
        Link_list = pd.DataFrame(post_link_list)
        # 合併    
        df_ptt_TNL = pd.concat([Title_list, Link_list],axis=1)
        df_ptt_TNL = df_ptt_TNL.rename(columns={0: 'Link'})
        return df_ptt_TNL
    
# ---------------------------------------------------    
    #抓取貼文文章
    def getPttContent(self, url):
        my_headers = {'cookie': 'over18=1;'}
        response = requests.get(url, headers = my_headers)

        #Get Content       
        soup = BeautifulSoup(response.text,"html.parser")

        main_container = soup.find(id='main-container')
        all_text = main_container.text
        pre_text = all_text.split('--')[0]

        # 把每段文字 根據 '\n' 切開
        texts = pre_text.split('\n')
        contents = texts[2:]
        content = ''.join(contents)
        return content
    
# ---------------------------------------------------
    # 抓取貼文下的回覆
    def getPttComment(self, url):

        my_headers = {'cookie': 'over18=1;'}
        response = requests.get(url, headers = my_headers)      
        soup = BeautifulSoup(response.text,"html.parser")
        articles = soup.find_all('div', 'push')

        comment_text=[]
        for article in articles:
            messages = article.find('span','f3 push-content').getText().replace(':','').strip()
            comment_text.append(messages)
        comment_text = "。".join(comment_text)
        return comment_text
    
# ---------------------------------------------------
    # 抓取貼文日期
    def getPttDate(self, url):
        my_headers = {'cookie': 'over18=1;'}
        response = requests.get(url, headers = my_headers)     
        soup = BeautifulSoup(response.text,"html.parser")

        main_container = soup.find(id='main-container')
        all_text = main_container.find_all(class_='article-meta-value')
        pre_text = all_text[3].text
        datetime_date = parser.parse(pre_text)
        date = "{:%Y/%m/%d}".format(datetime_date)
        return date

# ---------------------------------------------------
    # 抓出最後一頁
    def getLastPage(self, url, driver):
        
        #  關閉-----------------      
        def FinishedCrawler(driver):
            driver.close()
        # ----------------------   
        
        my_headers = {'cookie': 'over18=1;'}
        response = requests.get(url, headers = my_headers)
        soup = bs4.BeautifulSoup(response.text,"html.parser")

        # 抓尾頁
        final_page1 = soup.find(id='action-bar-container')
        final_page2 = final_page1.find_all(class_='btn wide')
        pre_text_1 = str(final_page2[0].get('href'))
        pre_text_2 = pre_text_1.split("page=")
        final_page = pre_text_2[1].split("&q")
        FinishedCrawler(driver)
        return final_page[0]
    
# ---------------------------------------------------

    
if __name__ == "__main__":    
    storing = pd.DataFrame(columns=['Post Title', 'Link'])
# ******修改link*******
    link1 = 'https://www.ptt.cc/bbs/iOS/search?q=iPhone+13+Pro+max'
    now = datetime.datetime.now().strftime("%Y%m%d")
    
    ptt = ptt_crawler(link1)
    driver = ptt.OpenChromeDriver()
    
# Title/Link ---------------------------------------------------
    # (1)storing ->將多頁資訊加入該df中  
    storing = pd.DataFrame(columns=['Post Title', 'Link'])
    # page1
    Title_Link_page1 = ptt.getOnePage(link1, driver)
    storing = storing.append(Title_Link_page1)
    
    # 剩餘pages(start從第二頁起)
    # getLastPage->最後一頁頁碼
    driver1 = ptt.OpenChromeDriver()
    ptt_last = ptt_crawler(link1)
    number = ptt_last.getLastPage(link1, driver1)
    for i in range(2, int(number)+1):
        try:
            # ******修改link*******
            link = "https://www.ptt.cc/bbs/iOS/search?page="+str(i)+"&q=iPhone+13+Pro+max"
            # 執行單頁面網頁爬蟲
            driver2 = ptt.OpenChromeDriver()
            ptt_perPage = ptt_crawler(link)
            Title_Link = ptt_perPage.getOnePage(link, driver)
            storing = storing.append(Title_Link, ignore_index=True)
            time.sleep(1)
            print('Page'+str(i)+' is printed')
        except:
            pass
    
    # 存入  
    # ******修改link*******
    file_name1 = "crawler_data/IPHONE/Link/iphone13promax/PTT_iphone13promax_Link"+now+".csv"
    storing.to_csv(file_name1, index=False, encoding="utf-8")
    print(f"Below is Post Title & Lnik: {storing}")
    

# Post Comment&Content&Date---------------------------------------------------
    data = []
    try:
        i=0
        for index, row in storing.iterrows():
            ptt_content = ptt_crawler(link)
            ptt_comment = ptt_crawler(link)
            ptt_date = ptt_crawler(link)
            
            title = row["Post Title"]
            content = ptt_content.getPttContent(row["Link"])
            comment = ptt_comment.getPttComment(row["Link"])
            date = ptt_date.getPttDate(row["Link"])
            data.append([title,content,comment,date])
            i+=1
    except:
        print(i)

    print("done")
    
    # 存入    
    # ******修改link*******
    iphone13_ptt_df = pd.DataFrame(data)
    re_columns = ["Title", "Content", "Comment", "Date"]
    iphone13_ptt_df.columns = re_columns
    file_name2 = "crawler_data/IPHONE/Data/iphone13promax/PTT_iphone13promax_Data"+now+".csv"
    iphone13_ptt_df.to_csv(file_name2, index=False, encoding='utf_8_sig')


# In[ ]:




