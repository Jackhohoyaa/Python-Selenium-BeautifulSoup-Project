import pandas  as pd
import re
data=pd.read_csv(r"C:\Users\USER\OneDrive\桌面\(V2)104職缺.csv")
data=data.drop(["Unnamed: 0"],axis=1)
clean_data=[]
county=[]
district=[]
address=[]
for i in range(len(data)):
    if re.match("..市..區.",data["公司地址"][i]) or re.match("..市.區.",data["公司地址"][i]) or re.match("..縣..市.",data["公司地址"][i]) or re.match("..縣..鎮.",data["公司地址"][i]) or re.match("..縣..鄉.",data["公司地址"][i]):
        clean_data.append(data["公司地址"][i])
    else:
        data=data.drop([i],axis=0)
for i in clean_data:
    county.append(i[:3])
    address.append(i[6:])
    if re.search(".區",i[3:5]):
        district.append(i[3:5])
    if re.match("..區",i[3:6])  or re.match("..市",i[3:6]) or re.match("..鄉",i[3:6]) or re.match("..鎮",i[3:6]):
        district.append(i[3:6])

data=data.reset_index()
data=data.drop(["index"],axis=1)
#%%
county=pd.Series(county,name="縣市")
district=pd.Series(district,name="區")
address=pd.Series(address,name="地址")
final=pd.concat([data,county,district,address],axis=1)
final=final.drop(["公司地址"],axis=1)


final.to_csv("104資料PowerBI.csv",encoding="utf-8-sig")


