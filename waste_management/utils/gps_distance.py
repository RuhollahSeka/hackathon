from geopy.distance import distance


def gps_distance(first_coords, second_coords):
    return distance(first_coords, second_coords)
