import folium
import pandas as pd

sample_data = pd.read_csv('ucom_python\\data\\data5.csv', sep=',')
print sample_data.columns, sample_data.shape
sample_data.columns = ['section', 'road', 'road_detail', 'lon', 'lat', 'extra']
print sample_data.head()

location1 = [25.052833, 121.544158]
zoom = 16
map_osm = folium.Map(location=location1, zoom_start=zoom)

for i in range(len(sample_data)):
    coordinate = [sample_data.ix[i, 'lat'], float(sample_data.ix[i, 'lon'])]
    message = '%s,%s' % (sample_data.ix[i, 'road'], sample_data.ix[i, 'road_detail'])
    message = unicode(message, 'utf-8')
    folium.Marker(coordinate,
                  icon=folium.Icon(color='blue', icon='info-sign'),
                  popup=message).add_to(map_osm)
    print coordinate

dorm1 = [25.051899, 121.552183]
dorm2 = [25.042374, 121.558899]
folium.CircleMarker(dorm1, radius=200, popup='small dorm',
                    fill_color='#C0FFEE').add_to(map_osm)
folium.Circle(dorm2, radius=200, popup='dorm',
              fill_color='#FFEEC0').add_to(map_osm)

map_osm.save('map\\demo86.html')
