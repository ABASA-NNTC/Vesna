import pandas as pd
import geopandas as gpd
import json
from CONSTS import Filter
from copy import deepcopy


def get_total_gjs(cadasters_js, fields_js, *filters):
    try:
        cadasters = gpd.GeoDataFrame.from_features(cadasters_js)
        fields = gpd.GeoDataFrame.from_features(fields_js)
    except TypeError:
        return -1
    main_tables = {Filter.CADASTRE: cadasters, Filter.FIELD: fields, Filter.BORDER_FIELD: fields, Filter.BORDER_CAD: cadasters}
    arr_map = []
    for filter_name in filters:
        if filter_name in Filter.OVERLAY_HOW:
            how = Filter.OVERLAY_HOW[filter_name]
            if filter_name == Filter.CAPTURE:
                gdf = gpd.overlay(fields, cadasters, how=how)
            else:
                gdf = gpd.overlay(cadasters, fields, how=how)
            arr_map.append(add_property(gdf, filter_name))
        elif filter_name in main_tables:
            arr_map.append(add_property(main_tables[filter_name], filter_name))
            if filter_name in (Filter.CADASTRE, Filter.FIELD):
                arr_map = arr_map[-1:]
                break

    all_map = pd.concat(arr_map, )
    return json.loads(all_map.to_json())


def add_property(gdf, filter_name):
    gdf = deepcopy(gdf)
    if filter_name in Filter.COLOR:
        gdf['fill'] = Filter.COLOR[filter_name]
        # gdf['fill-opacity'] = 1
    if filter_name in Filter.BORDER_PROPERTIES:
        for prop_name, prop_value in Filter.BORDER_PROPERTIES[filter_name].items():
            gdf[prop_name] = prop_value
    return gdf


if __name__ == '__main__':
    with open('geojsons/Кадастры.geojson') as file:
        cadasters_js = json.load(file)

    with open('geojsons/Поля.geojson') as file:
        fields_js = json.load(file)

    with open('geojsons/filter.geojson', 'w') as file:
        new_json = get_total_gjs(cadasters_js, fields_js, 'border_cad', 'border_field', 'entry', 'capture', 'unused', 'field')
        json.dump(new_json, file, indent=4)

