import plotly.graph_objects as go
#Menggunakan plotly dan mapbox untuk visualisasi map

#px.set_mapbox_access_token('pk.eyJ1IjoiZ2lydmluanVub2QiLCJhIjoiY2tuMDB6ZmFyMGpjOTJubW82ZWJ3em1heCJ9.k5m3PeaIZjpWBM1QUAKeNQ')
class MapV:
    def __init__(self, a, b, c): #ctor
        self.mapbox_access_token = 'pk.eyJ1IjoiZ2lydmluanVub2QiLCJhIjoiY2tuMDB6ZmFyMGpjOTJubW82ZWJ3em1heCJ9.k5m3PeaIZjpWBM1QUAKeNQ'
        self.map= go.Figure(go.Scattermapbox(
        lat=a,
        lon=b,
        mode='markers',
        marker= dict(color = 'black', size = 14),
        text = c,
        name = "Simpul"
        ))
        self.count = 0

    def tambahAwal(self, latawal, lonawal, nawal): #tambah simpul awal
        self.map.add_trace(go.Scattermapbox(
            mode = "markers",
            lat = latawal,
            lon = lonawal,
            marker = dict(color = 'LightSkyBlue', size = 16),
            text = nawal,
            name = "Awal"
            ))

    def tambahAkhir(self, latakhir, lonakhir, nakhir): #tambah simpul akhir
        self.map.add_trace(go.Scattermapbox(
            mode = "markers",
            lat = latakhir,
            lon = lonakhir,
            marker = dict(color = 'purple', size = 16),
            text = nakhir,
            name = "Akhir"
            ))

    def tambahjalur(self, jalurlat, jalurlon, name): #tambah jalur
        if (self.count > 0):
            self.map.add_trace(go.Scattermapbox(
            mode = "lines",
            lat = jalurlat,
            lon = jalurlon,
            line = dict(color = 'black', width = 2),
            text = name,
            legendgroup="a",
            name = "Jalur",
            showlegend = False
            ))
        else:
            self.map.add_trace(go.Scattermapbox(
            mode = "lines",
            lat = jalurlat,
            lon = jalurlon,
            line = dict(color = 'black', width = 2),
            text = name,
            legendgroup="a",
            name = "jalur"
            ))
        self.count +=1

    def tambahjalurhasil(self, jalurlat, jalurlon, hasil): #tambah jalur hasil
        self.map.add_trace(go.Scattermapbox(
        mode = "lines",
        lat = jalurlat,
        lon = jalurlon,
        line = dict(color = 'red', width = 4),
        name = "Jalur terdekat",
        text = hasil
        ))

    def visualize(self): #gambar map
        self.map.update_layout(
        hovermode='closest',
        title = 'Peta Jalur Terdekat',
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

#driver
if __name__ == '__main__':
    mapbox_access_token = 'pk.eyJ1IjoiZ2lydmluanVub2QiLCJhIjoiY2tuMDB6ZmFyMGpjOTJubW82ZWJ3em1heCJ9.k5m3PeaIZjpWBM1QUAKeNQ'

    fig = go.Figure(go.Scattermapbox(
            lat=['46.181', '44.457', '45.794'],
            lon=['21.312', '26.093', '24.128'],
            mode='markers',
            marker=go.scattermapbox.Marker(size=14, color= 'purple'),
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
        line = dict(color = 'LightSkyBlue', width = 12)))

    fig.show()