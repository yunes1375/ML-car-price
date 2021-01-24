from sklearn import tree
import mysql.connector
cnx = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
cursor=cnx.cursor() 
xf=[]
yf=[]
a=[]
b=[]
brand=[]
fav=[]
nam=[]
final=[]
def funbrand():
 query='select * from machin ;'
 cursor.execute(query)
 for line in cursor:
   a=line
   brand.append(a[1])
 return brand
c=funbrand()
c2 = list(dict.fromkeys(c))

for x in c2:
    id=c2.index(x)
    print(str(x)+':''%s'%(id))
print('Enter your Brand Number From list')
o=int(input())
ibrand=o
query='select * from machin where brand =\'%s\' ;'%c2[o]
cursor.execute(query)
for line in cursor:
    fav.append(line)
for line in fav:
    temp=line
    nam.append((temp[2]))
nam2 = list(dict.fromkeys(nam))
for x in nam2:
    id=nam2.index(x)
    print(str(x)+':''%s'%(id))
print('Enter your Model Number From list')
z=int(input())
imodel=z
query='select * from machin where brand =\'%s\' and nam=\'%s\' ;'%(c2[ibrand],nam2[imodel])
cursor.execute(query)
for line in cursor:
    final.append(line)
for line in final:
    xf.append(line[3:5])
    yf.append(line[5])
clf=tree.DecisionTreeClassifier()
clf.fit(xf,yf)
print('Enter Your Car Product Year(13**):')
new=int(input())
print('Enter Your Car Used Distance(KM):')
new2=int(input())
newdata=[[new,new2]]
answer=clf.predict(newdata)
print(answer)