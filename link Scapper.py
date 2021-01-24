import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
links=[]
f=[]
f.append('')
links.append('')
finalids=[]
finalids.append('')
finalids2=[]
finalids2.append('')
finalids2.append('')
cnx = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
cursor=cnx.cursor() 
cursor2=cnx.cursor()
cursor3=cnx.cursor()
cursor4=cnx.cursor()
def chekfun(link):
 count=0
 for x in range(0,len(links)):
     if str(links[x])==str(link):
        count=count+1
 if count ==0:
      return True
#######################################
repetids=[]
linksfg=[]
ffg=[]
ffg.append('')
ffg.append('')
linksfg.append('')
finalidsfg=[]
finalidsfg.append('')
def fungetlink(z):
 #print(z)
 a=requests.get('https://carap.ir/DetailsUnAdmin/%s'%str(z))     
 supfg=BeautifulSoup(a.text,'html.parser')
 for linkfg in supfg.find_all('a'):
   cfg=(linkfg.get('href'))
   linksfg.append(cfg)
 for x in range(0,len(linksfg)):
  if(('Details' in str(linksfg[x]))==True):
     bfg=linksfg[x]    
     idfg=re.search(r'\Details\/(\d+)',bfg)     
     if idfg!=False:
       ffg.append(idfg[1])
 if 1==1:
  for x in range(0,len(ffg)):
    counter=0  
    for y in range(0,len(finalidsfg)):
      if ffg[x]==finalidsfg[y]:
         counter=counter+1
    if counter==0:
      finalidsfg.append(ffg[x])
  #print(finalidsfg)
  return finalidsfg  
###########################################
print('I am Loading Links...Please Wait')
a=requests.get('https://carap.ir')    
sup=BeautifulSoup(a.text,'html.parser')
for link in sup.find_all('a'):
  c=(link.get('href'))
  links.append(c) 
for x in range(0,len(links)):
  if(('DetailsUnAdmin' in str(links[x]))==True):
    b=links[x]
    id=re.search(r'^\/\w+\/(\w+)',b)
    f.append(id[1])
for x in range(0,len(f)):
  counter=0
  for y in range(0,len(finalids)):
    if f[x]==finalids[y]:
       counter=counter+1
  if counter==0:
    finalids.append(f[x])
#print(finalids)
#print(len(finalids))
for x in range(1,len(finalids)):
 funre=[]
 #print('finalids[x] is\n')
 #print(finalids[x])
 #print('fune return is\n')
 funre=(fungetlink(finalids[x]))
 #print(funre)

 for x in range(1,len(funre)):
   finalids2.append(funre[x])
print('first links are: %i'%len(finalids2))
finalids2 = list(dict.fromkeys(finalids2))
      
print('last links are :%i'%len(finalids2))
query='select * from ids2 ;'
cursor.execute(query)
cnx.close()
sqldatas=[]

for (link ,ch) in cursor:
  sqldatas.append(link)

print('%s link loaded from DB'%len(sqldatas))
c=0 
#################################################################
#for x in range(1,len(sqldatas)):
#  temp=sqldatas[x]
#  finalids2.append(temp)
#finalids2 = list(dict.fromkeys(finalids2))  
#print('Now links are : %s'%str(len(finalids2)))
set1=set(finalids2)
set2=set(sqldatas)
finalids3=set1-set2
print('New %s links Added '%str(len(finalids3)))
for x in finalids3:
 query='insert into ids2 values(\'%s\',\'No\');'%(x)
 cursor2.execute(query)
 cnx.commit()