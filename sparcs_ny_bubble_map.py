from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv

m = Basemap(projection='stere', lat_0= 42, lon_0 = -75, llcrnrlat= 40, llcrnrlon=-80, urcrnrlat=45, urcrnrlon=-71,resolution='i')
m.drawcoastlines()
m.drawstates()
m.drawcountries()

f = open('hvsites07.csv', 'rU')
reader = csv.reader(f)
zips = []
lats = []
longs = []
trials = []

for row in reader:
    zips.append(row[0])
    lats.append(row[1])
    longs.append(row[2])
    trials.append(row[3])

for i in range(0,(len(zips))):
    x,y = m(longs[i],lats[i])
    
    if int((trials[i])) == 1:
        col = '#C6DBEF'
    if int((trials[i])) == 2:
        col = '#9ECAE1'
    if int((trials[i])) == 3:
        col = '#6BAED6'
    if int((trials[i])) == 4:
        col = '#3182BD'
    if int((trials[i])) == 5:
        col = '#08519C'
    m.plot(x,y, marker='o',color=col, markersize=(int(trials[i]))*5)

plt.show()