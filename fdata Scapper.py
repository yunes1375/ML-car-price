import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
links=[]

cnx = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
cursor=cnx.cursor() 
cursor2=cnx.cursor()
cursor3=cnx.cursor()
cursor4=cnx.cursor()
def delfun(mys):
 dig=''
 for x in mys:
     if (x.isdigit()==1):
          dig=dig+str(x)
 if len(dig)!=0:
     return dig
 else:
     return 0

def funbrand(x):
 fbrand=''
 brandt=x.text
 brand=re.search(r'برند\n(.+)\n',brandt)
 if brand!=None:
   fbrand=brand[1]
 else:
   fbrand='None'
 return fbrand
def funname(x):
 fbrand=''
 brandt=x.text
 brand=re.search(r'نام خودرو\n(.+)[\w,\n]',brandt)
 if brand!=None:
   fbrand=brand[1]
 else:
   fbrand='None'
 return fbrand
def funmodel(x):
 fbrand=''
 brandt=x.text
 brand=re.search(r'13.+\d',brandt)
 if brand!=None:
   fbrand=brand[0]
 else:
   fbrand='None'
 return fbrand
def funuse(x):
 fbrand=''
 brandt=x.text
 brand=re.search(r'\d+,.+\s',brandt)
 if brand!=None:
   fbrand=brand[0]
 else:
   fbrand='0'
 return fbrand
def funbadane(x):
 fbrand=''
 brandt=x.text
 brand=re.search(r'فن.+\n+(\w*\n).*\n',brandt)
 if brand!=None:
   fbrand=brand[1]
 else:
   fbrand='None'
 return fbrand
def funlastic(x):
 fbrand=''
 brandt=x.text
 brand=re.search(r'لاست.*\s*(\d.*)\w',brandt)
 if brand!=None:
   fbrand=brand[1]
 else:
   fbrand='None'
 return fbrand
def fung(x):
 fbrand=''
 if x==None:
   return 'Cant'
 else:
    brandt=x.text
    brand=re.search(r'(\d.+)\s',brandt)
 if brand!=None:
    fbrand=brand[1]
 else:
    fbrand='None'
 return fbrand
def funlinks():
 query='select * from ids2 where ch = \'No\'; '
 links=[]
 cursor.execute(query)
 
 cnx.close()
 for (link ,ch) in cursor:
   links.append(link)
 return(links)
print('I am Loading Datas...please Wait!!')
links=funlinks()
if (len(links)>1):
 for num in range(1,len(links)):
  a=requests.get('https://carap.ir/Details/%s'%links[num])
  sup=BeautifulSoup(a.text,'html.parser')
  vals=sup.find_all('table',attrs={'class':'table table-bordered table-condensed table-hover table-responsive table-striped'})
  if len(vals)>1:
     x=vals[0]
     x1=(funbrand(x))
     x2=(funname(x))
     x3t=(funmodel(x))
     x3=delfun(str(x3t))
     x4t=(funuse(x))
     x4=delfun(str(x4t))
     #x5=(funbadane(x))
     #x6t=(funlastic(x))
     #x6=delfun(str(x6t))
     sup2=BeautifulSoup(a.text,'html.parser')
     vals2=sup2.find('span',id='price2')
     x7t=fung(vals2)
     x7=delfun(str(x7t))
     if int(x7) >10000000:
       query='insert into machin values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(links[num],x1,x2,x3,x4,x7)
       cursor2.execute(query)
       query='update ids2 set ch = \'yes\' where link =\'%s\';'%(links[num])
       cnx.commit()
       cursor3.execute(query)
       cnx.commit()
     else:
       query='update ids2 set ch = \'yes\' where link =\'%s\';'%(links[num])
       cursor4.execute(query)
       cnx.commit()
  else:  
        pass
print('Done!!')

 

