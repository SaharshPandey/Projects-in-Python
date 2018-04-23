import pandas
import folium as fol
map=fol.Map(location=[43, -122],zoom_start=6,tiles='Mapbox Bright')

data=pandas.read_csv("Volcanoes_USA.txt")
# jsut to show the columns name...........
print(data.columns)
#converting series object into list object...
latitudes=list(data['LAT'])
longitudes=list(data['LON'])
elevation=list(data['ELEV'])

def color_producer(elevations):
    if elev<1000:
        return 'green'
    elif 3000>elev>1000:
        return 'orange'
    elif elev>3000:
        return 'red'
print (latitudes)
print (longitudes)
#print(data)

fg_volacanoes=fol.FeatureGroup(name='Volcanoes')
for lat_coordinate,lon_coordinate,elev in zip(latitudes,longitudes,elevation):

    fg_volacanoes.add_child(fol.CircleMarker(location=[lat_coordinate,lon_coordinate],popup=str(elev)+' meters high',radius=8,fill_color=color_producer(elev),fill_opacity=0.8,color='white',fill=True))
#talking data from world.json and using labda  function which helps to write a function in a line..if else in lambda function is like..


fg_population=fol.FeatureGroup(name='Population')
fg_population.add_child(fol.GeoJson(open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] <10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000
else 'red'}))

map.add_child(fg_volacanoes)
map.add_child(fg_population)
map.add_child(fol.LayerControl())
map.save("Map1.html")
