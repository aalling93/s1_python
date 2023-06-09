import numpy as np
from sentinelsat import geojson_to_wkt


def intersection(lst1, lst2):

    # Use of hybrid method
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


def intersect_ids(products_df):
    names = np.array(
        [
            name.split("_")[0]
            + name.split("_")[1]
            + name.split("_")[-3]
            + name.split("_")[-2]
            for name in products_df.title.values
        ]
    )
    missionid = products_df.missiondatatakeid.values
    names = [name + "_" + str(missionid[ix]) for ix, name in enumerate(names)]
    return names



def get_area(bbox: list = []):
    # getting area func
    area = {
        "coordinates": [
            [
                [bbox[0], bbox[2]],
                [bbox[0], bbox[3]],
                [bbox[1], bbox[3]],
                [bbox[1], bbox[2]],
                [bbox[0], bbox[2]],
            ]
        ],
        "type": "Polygon",
    }
    footprint = geojson_to_wkt(area)
    return footprint


def original_metadata(self):
    self.products_df = self.org_products_df

    return self
