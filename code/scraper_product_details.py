from time import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import pandas as pd


from selenium.webdriver.chrome.service import Service

service_gecko = Service(executable_path=r'C:\chrome driver\chromedriver.exe')

driver = webdriver.Chrome(service=service_gecko)

Amazon_url = 'https://www.amazon.com/Best-Sellers-Electronics-Televisions/zgbs/electronics/172659'
driver.get(Amazon_url)
driver.maximize_window()
from selenium.webdriver.common.by import By
WebDriverWait(driver, timeout=45).until(lambda d: d.find_element(By.CSS_SELECTOR,'div#gridItemRoot:nth-of-type(1)>div>div:nth-of-type(2)>div>a>div>img'))

image_sel='div#gridItemRoot>div#p13n-asin-index-rep>div:nth-of-type(2)>div>a>div>img'
#image_sel='div#gridItemRoot:nth-of-type(1)>div>div:nth-of-type(2)>div>a>div>img'
price_sel='div#gridItemRoot>div#p13n-asin-index-rep>div.zg-grid-general-faceout>div>div:nth-of-type(2)>div>div>a>div>span>span'
id_sel='div#gridItemRoot>div#p13n-asin-index-rep>div.zg-grid-general-faceout>div'
sleep(2)


#from selenium.webdriver.common.action_chains import ActionChains

product_Name=[]
product_ID=[]
product_Price=[]
product_Rating=[]
Product_Screensize=[]
Product_Brand=[]
Product_Resolution=[]
height=0
i=0
page_num=1

while i<51: 
    #break for page 2  
    if(page_num==2 and i==50):
        break
    for iter in range(20):        
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_UP)
    #if(i==7):
        #i=i+1
        #continue
    #modifying css selctor based on i value
    image_sel_upd=image_sel.replace('rep',str(i))
    price_sel_upd=price_sel.replace('rep',str(i))
    id_sel_upd=id_sel.replace('rep',str(i))
    
    
    for counter in range(35):
        try:
            sleep(2)
            driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
            sleep(2)
            if(i==50):
               
                next_btn=driver.find_element(By.CSS_SELECTOR,'ul.a-pagination>li.a-normal')
                if(next_btn.size!=0):
                    i=0
                    image_sel_upd=image_sel.replace('rep',str(i))
                    price_sel_upd=price_sel.replace('rep',str(i))
                    page_num=2
                    next_btn.click()
                    break
            else:
                find_img=driver.find_element(By.CSS_SELECTOR,image_sel_upd)
                if(find_img.size!=0):
                    break
        except:
            pass
           

    sleep(5)
    #height=new_height
   
   
    #driver.execute_script("arguments[0].scrollIntoView();",find_img)
    prod_ID=driver.find_elements(By.CSS_SELECTOR,id_sel_upd)
    if(len(prod_ID)>0):
        for a in prod_ID:
            print(a.get_attribute("ID"))
            product_ID.append(a.get_attribute("ID"))
    else:
        product_ID.append(None)
    prod_price=driver.find_elements(By.CSS_SELECTOR,price_sel_upd)
    if(len(prod_price)>0):
        for a in prod_price:
            print(a.text)
            product_Price.append(a.text)
    else:
        product_Price.append(None)
    prod_url=driver.find_element(By.CSS_SELECTOR,image_sel_upd)
    prod_url.click()
    sleep(4)
    prod_name= driver.find_elements(By.CSS_SELECTOR,'#titleSection>h1>span')
    for a in prod_name:
        print(a.text)
        product_Name.append(a.text)
   
   

    prod_rating=driver.find_elements(By.XPATH,'//div[@id="averageCustomerReviews_feature_div"]/div[@id="averageCustomerReviews"]/span/span[@id="acrPopover"][1]')
    if(len(prod_rating)>0):
        for a in prod_rating:
            print(a.get_attribute("title"))
            product_Rating.append(a.get_attribute("title"))
    else:
        product_Rating.append(None)


    prod_size=driver.find_elements(By.XPATH,'//table[@class="a-normal a-spacing-micro"]/tbody/tr[@class="a-spacing-small po-display.size"]/td[2]/span')
    if(len(prod_size)>0):
        for a in prod_size:
            print(a.text)
            Product_Screensize.append(a.text)
    else:
        Product_Screensize.append(None)

   
    prod_brand=driver.find_elements(By.CSS_SELECTOR,'table.a-normal.a-spacing-micro>tbody>tr.a-spacing-small.po-brand>td:nth-of-type(2)>span')
    if(len(prod_brand)>0):
        for a in prod_brand:
            print(a.text)
            Product_Brand.append(a.text)
    else:
        Product_Brand.append(None)

   
    prod_res=driver.find_elements(By.CSS_SELECTOR,'table.a-normal.a-spacing-micro>tbody>tr.a-spacing-small.po-resolution>td:nth-of-type(2)>span')
    if(len(prod_res)>0):
        for a in prod_res:
            print(a.text)
            Product_Resolution.append(a.text)
    else:
        Product_Resolution.append(None)

    i=i+1
    
    sleep(1)      
    driver.back()
    sleep(1)

print(product_Name)
print(product_ID)
print(product_Price)
print(Product_Screensize)
print(Product_Brand)
print(Product_Resolution)

df=pd.DataFrame()
   

df['product_Name']=pd.Series(product_Name)
df['Product_ID']=pd.Series(product_ID)
df['product_Price']=pd.Series(product_Price)
df['product_Rating']=pd.Series(product_Rating)
df['Product_Screensize']=pd.Series(Product_Screensize)
df['Product_Brand']=pd.Series(Product_Brand)
df['Product_Resolution']=pd.Series(Product_Resolution)
df.to_csv(r"C:\Users\sriha\OneDrive\Documents\GitHub\project-deliverable-1-cowboys\data\Top_100_selling_TV.csv",sep=',',index=None)

driver.quit()