import math

EARTH_RADIUS = 6378137

def offset(coord, distance, bearing):
    """
    Calculate the coordinate x meters away from a given
    latitude, longitude point with bearing X degrees.
    """
    lat, lon = map(math.radians, coord)
    if lat == 0 or lon == 0 or lat is None or lon is None:
        print("WARN")
    bearing = math.radians(bearing)
    new_lat = math.asin(math.sin(lat) * math.cos(distance / EARTH_RADIUS) + math.cos(lat) * math.sin(distance / EARTH_RADIUS) * math.cos(bearing))
    new_lon = lon + math.atan2(math.sin(bearing) * math.sin(distance / EARTH_RADIUS) * math.cos(lat),
                                   math.cos(distance / EARTH_RADIUS) - math.cos(lat) * math.sin(new_lat))
    return math.degrees(new_lat), math.degrees(new_lon)

def create_circle_points(coord, radius, points=10):
    """
    Creates a polygonal approximation of a circle around a given latitude/longitude coordinate.
    Radius is in meters.
    """
    out = []
    for i in range(points):
        out.append(offset(coord[::-1], radius, (360 / points) * i)[::-1])
    return out
