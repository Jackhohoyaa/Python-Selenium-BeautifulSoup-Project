import MySQLdb as MSdb
import pandas as pd
data_104=pd.read_csv(r"C:\Users\USER\OneDrive\桌面\(V2)104職缺.csv")

try:
    connect=MSdb.connect(host='127.0.0.1',
                         user='104Data',
                         password='jack061060028',
                         port=3306,
                         database='104database',
                         charset='utf8')
    cursor=connect.cursor()
    for i in range(len(data_104)):
        write_in='''insert into 104data (ID,職稱,更新日期,薪資待遇,公司名稱,工作性質,公司地址)
                                           values(%d,"%s","%s","%s","%s","%s","%s")'''%(data_104.iloc[i,0],
                                                                            data_104.iloc[i,1],
                                                                            data_104.iloc[i,2],
                                                                            data_104.iloc[i,3],
                                                                            data_104.iloc[i,4],
                                                                            data_104.iloc[i,5],
                                                                            data_104.iloc[i,6])
        cursor.execute(write_in)
        connect.commit() 
    print("資料寫入成功!")     
    cursor.close()
    connect.close()
except Exception as err:
    print("連線失敗",err)
#print(data_104.iloc[i,0],data_104.iloc[i,1],data_104.iloc[i,2],data_104.iloc[i,3],data_104.iloc[i,4],data_104.iloc[i,5],data_104.iloc[i,6])
