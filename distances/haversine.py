import numpy as np


def haversine(lon1, lat1, lon2, lat2, unit='km'):
    """Calculate the great circle distance between two points on the earth (specified in decimal degrees)

    Args:
        lon1 (float): Longitude of point 1 in decimal degrees
        lat1 (float): Latitude of point 1 in decimal degrees
        lon2 (float): Longitude of point 2 in decimal degrees
        lat2 (float): Latitude of point 2 in decimal degrees

    Returns:
        float: Distance between the two points in kilometers
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    if unit == 'km':
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    else:
        r = 3956  # Radius of earth in miles. Use 6371 for kilometers
    return c * r