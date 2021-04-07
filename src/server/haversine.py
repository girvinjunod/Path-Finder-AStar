from math import pi,sin,cos,asin
def haversineDistance(koor1, koor2):
    #lengkapnya formulanya ada di https://en.wikipedia.org/wiki/Haversine_formula
    lat1 = koor1[0]
    lon1 = koor1[1]
    lat2 = koor2[0]
    lon2 = koor2[1]

    rad = pi / 180.0 #ubah dari derajat ke radian
    radiusbumi = 6371 #radiusbumi dalam km

    radlat = (lat2 - lat1) * rad
    radlon = (lon2 - lon1) * rad

    #fungsi haversine -> hav(x) = sin(x/2)**2
    #hav(Θ) = hav(lat2-lat1) + cos(lat1)cos(lat2)hav(lon2-lon1)
    #Θ = d/r, r = radius, d = distance
    #d = 2*radiusbumi * arcsin(hav(Θ)**0.5)
    hav = (sin(radlat / 2))**2 + cos(lat1 * rad) * cos(lat2 * rad) * (sin(radlon / 2))**2
    d = 2*radiusbumi * asin(hav**0.5)

    return d

#driver
if __name__ == '__main__':
    a  = (44.457, 26.093) 
    b = (46.181, 21.312)
    c = (-6.176716476545919, 106.98596393874463)
    d = (-6.176767387686766, 106.98672068536122)
    r = haversineDistance(c,d)
    print(r)