from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re
Options().chrome_executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver=webdriver.Chrome(Options())
def connect(url2): 
     driver.get(url2)
     driver.minimize_window()
def search(job,page):
   data=[]
   driver.maximize_window()
   search=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/div/div/form/div/div/div[1]/div/input')
   search.send_keys(job)
   submit=driver.find_element(By.CLASS_NAME,"btn.btn-secondary.btn-block.btn-lg").click()
   time.sleep(1)
   for i in range(int(page)):  
     select=Select(driver.find_element(By.CLASS_NAME,"page-select.js-paging-select.gtm-paging-top"))
     select.select_by_index(i)
     time.sleep(2)
     job_title=driver.find_elements(By.CSS_SELECTOR,"[data-qa-id=jobSeachResultTitle]")
     time.sleep(2)
     try:
         for title in job_title:
          info=[]
          title.click()
          time.sleep(1)
          driver.switch_to.window(driver.window_handles[1])
          time.sleep(1)
          try:  
            main=driver.find_element(By.TAG_NAME,"h1")
            salary=driver.find_element(By.CLASS_NAME,"t3.mb-0.mr-2.text-primary.font-weight-bold.align-top.d-inline-block")
            company=driver.find_element(By.CLASS_NAME,"btn-link.t3.mr-6")
            type_=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div')
            site=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[5]/div[2]/div/div/span')
            date=re.search("\d{2}\/\d{2}",main.text).group()
            info.append(main.text[:-7])
            info.append(date)
            info.append(salary.text)
            info.append(company.text)
            info.append(type_.text)
            info.append(site.text)
            data.append(info)
          except:
            pass
          driver.close()
          driver.switch_to.window(driver.window_handles[0])
          time.sleep(0.5)
     except:
         continue
   data=pd.DataFrame(data)
   return data

if __name__ == "__main__":
    job=input("請輸入欲查詢職缺:")
    page=input("請輸入欲查詢頁數(輸入整數):")
    index=["職稱","更新日期","薪資待遇","公司名稱","工作性質","公司地址"]
    starttime=time.time()
    url2="https://www.104.com.tw/jobs/main/?v=2"
    connect(url2)
    data=search(job,page)       
    endtime=time.time()
    processtime=endtime-starttime
    data.columns=index
    data.to_csv("(V2)104職缺.csv",encoding="utf-8-sig")    
    print("運行時間:%d分%.2f秒"%(processtime//60,processtime%60))

    a=driver.page_source
