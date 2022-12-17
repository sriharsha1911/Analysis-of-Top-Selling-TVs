import pandas as pd
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter.filedialog import SaveAs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep


ser= Service(r"C:\chrome driver\chromedriver.exe")

sleep(2)
prod_id_df = pd.read_table(r"C:\Users\sriha\OneDrive\Documents\GitHub\project-deliverable-1-cowboys\data\Top_100_selling_TV.csv", sep=',')
#print(prod_id_df)

prod_id_list = []
#get list of product ids from csv 
prod_id_list.extend(prod_id_df['Product_ID'].tolist())
print(len(prod_id_list))
#url to be replaced with product id
review_url='https://www.amazon.com/product-reviews/chgprodid/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1'

no_of_Products=1
prod_id_1=[]
body_1 = []
title_1=[]
size_1=[]
rating_1=[]
#iterate through every product id
for a in prod_id_list:
    driver = webdriver.Chrome(service=ser)
    review_url_upd = review_url.replace('chgprodid',str(a))
    
    print(review_url_upd)
    driver.get(review_url_upd)
    sleep(4)
    driver.maximize_window()
    sleep(3)
    i=1
    prdid_cnt=0
    
    #iterate for 3 review pages
    while(i<4):
        
        
        body=driver.find_elements(By.XPATH,'//span[@class="a-size-base review-text review-text-content"]/span')
        for element in body:
            #sleep(5)
            #print(element.text)
            prdid_cnt=prdid_cnt+1
            body_1.append(element.text)
        title=driver.find_elements(By.XPATH,'//a[@class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"]/span')
        for element in title:
            #sleep(5)
            #print(element.text)
            title_1.append(element.text)
        size=driver.find_elements(By.CSS_SELECTOR,'a.a-size-mini.a-link-normal.a-color-secondary')
        for element in size:
            size_1.append(element.text)
        #rating=driver.find_elements(By.CSS_SELECTOR,'i.a-icon.a-icon-star.a-star-4.review-rating>span.a-icon-alt')
        rating=driver.find_elements(By.CSS_SELECTOR,'div#cm_cr-review_list>div>div>div>div:nth-of-type(2)>a:nth-of-type(1)')
        for element in rating:
            
            rating_1.append(element.get_attribute("title"))
        sleep(3)
        if(i==3):
            break
        try:
            next_btn=driver.find_element(By.CSS_SELECTOR,'ul.a-pagination>li:nth-child(2)>a')
            next_btn.click()
            sleep(1)
        except:
            break
        i=i+1

    driver.quit()
    tbad=1
    while(tbad<prdid_cnt+1):
        prod_id_1.append(a)
        tbad=tbad+1
    no_of_Products=no_of_Products+1
    #if(no_of_Products==21):
        #break
#create dataframe
df=pd.DataFrame()
df['body']=pd.Series(body_1)
df['Product_ID']=pd.Series(prod_id_1)
df['title']=pd.Series(title_1)
df['size_for_review']=pd.Series(size_1)
df['rating_for_review']=pd.Series(rating_1)

print(df)

df.to_csv(r"C:\Users\sriha\OneDrive\Documents\GitHub\project-deliverable-1-cowboys\data\reviews_total.csv",sep=',',index=None)
