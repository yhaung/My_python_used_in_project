txtfile = r"C:\Users\Ye\Desktop\Waypoints_12_JUN_19.txt"
with open(txtfile) as txt:
    gpx = txt.read()

oldData = gpx.split(",")
rtxt = ['<wptlat=', 'ele>' , '</ele', 'time>','</time', '</name', '/wpt>', 'name>']

newData = []
for item in oldData:
    newtxt = item
    for x in rtxt:
        newtxt = newtxt.replace(x,'')
    #print (newtxt)
    newData.append([newtxt])
#print (newData)

rtxt = ['lon=', '><','</<']

newData2 = []

for item in newData:
    newtxt = item[0]
    for x in rtxt:
        newtxt = newtxt.replace(x,',')
    #print (newtxt)
    newData2.append([newtxt])
#print (newData2)
import pandas as pd

df = pd.DataFrame(newData2)
print (df)
df.to_csv(txtfile[:-3]+"csv")
