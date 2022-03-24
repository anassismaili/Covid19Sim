import folium
import webbrowser

from folium import plugins
import ipywidgets
import geocoder
import geopy
from vega_datasets import data as vds

m = folium.Map(location = [34.0240853, -5.0717811], zoom_start=12)

tooltip = 'Click For More Info'


folium.Marker([34.0240853, -5.0717811], popup='<strong>Location One</strong>', tooltip=tooltip).add_to(m)





m.save('map.html')

webbrowser.open('map.htm')
