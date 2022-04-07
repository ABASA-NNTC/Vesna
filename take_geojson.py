from rosreestr2coord import Area
import geojson

def cadaster_feature(cad_num):
    area = Area(cad_num, area_type=1)
    try:
        coords = area.get_coord()[0]
        if len(coords[0][0]) == 2:
            return {'center': coords[0][0]}
    except:
        return -1
    pol = geojson.Polygon(coords)
    feature = geojson.Feature(geometry=pol)
    feature['properties']['Parcel_KN'] = cad_num
    return feature