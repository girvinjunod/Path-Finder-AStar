import plotly.graph_objects as go
#px.set_mapbox_access_token('pk.eyJ1IjoiZ2lydmluanVub2QiLCJhIjoiY2tuMDB6ZmFyMGpjOTJubW82ZWJ3em1heCJ9.k5m3PeaIZjpWBM1QUAKeNQ')
if __name__ == '__main__':
    mapbox_access_token = 'pk.eyJ1IjoiZ2lydmluanVub2QiLCJhIjoiY2tuMDB6ZmFyMGpjOTJubW82ZWJ3em1heCJ9.k5m3PeaIZjpWBM1QUAKeNQ'

    fig = go.Figure(go.Scattermapbox(
            lat=['46.181', '44.457', '45.794'],
            lon=['21.312', '26.093', '24.128'],
            mode='markers',
            marker=go.scattermapbox.Marker(size=14),
            text = ['Arad', 'Bucharest', 'Sibiu']
        ))
    fig.update_layout(
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=44,
                lon=26
            ),
            pitch=0,
            zoom=5
        )
    )
    fig.add_trace(go.Scattermapbox(
        mode = "lines",
        lat = ['46.181', '44.457'],
        lon = ['21.312', '26.093'],
        marker = {'size': 10}))



    fig.show()

class MapV:
    def __init__(self, a, b, c):
        self.mapbox_access_token = 'pk.eyJ1IjoiZ2lydmluanVub2QiLCJhIjoiY2tuMDB6ZmFyMGpjOTJubW82ZWJ3em1heCJ9.k5m3PeaIZjpWBM1QUAKeNQ'
        self.map= go.Figure(go.Scattermapbox(
        lat=a,
        lon=b,
        mode='markers',
        marker=go.scattermapbox.Marker(size=14),
        text = c
        ))
    def tambahjalur(self, jalurlat, jalurlon):
        self.map.add_trace(go.Scattermapbox(
        mode = "lines",
        lat = jalurlat,
        lon = jalurlon,
        marker = {'size': 10}))
    def visualize(self):
        self.map.update_layout(
        hovermode='closest',
        mapbox=dict(
            accesstoken=self.mapbox_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=44,
                lon=26
            ),
            pitch=0,
            zoom=5
            )
        )
        self.map.show()
    