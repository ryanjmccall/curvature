from math import radians
from typing import List

from sklearn.metrics.pairwise import haversine_distances

from curvature.calc import IUGG_MEAN_RADIUS_M


def sklearn_example():
    # distance b/w  Ezeiza Airport (Buenos Aires, Argentina) and Charles de Gaulle Airport (Paris, France)
    bas_coords = [-34.83333, -58.5166646]
    paris_coords = [49.0083899664, 2.53844117956]
    bsas_in_radians = [radians(_) for _ in bas_coords]
    paris_in_radians = [radians(_) for _ in paris_coords]
    result = haversine_distances([bsas_in_radians, paris_in_radians])
    print(result * 6371000/1000)  # multiply by Earth radius to get kilometers


def calc_haversine_distance(a: List[float], b: List[float]) -> float:
    dist = haversine_distances([[radians(_) for _ in a], [radians(_) for _ in b]])
    return dist[0][1] * IUGG_MEAN_RADIUS_M


def puget_distance():
    """Outputs the Haversine distance to Point No Point lighthouse from a given latitude, longitude pair.
    Uses sklearn: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html
    """
    pnp_coords = [47.912163, -122.526810]
    start_coords = [47.694469, -122.404946]  # golden gate
    start_coords = [47.806506, -122.395666]  # marina beach
    start_coords = [47.712409, -122.380048]  # carkeek
    dist_m = calc_haversine_distance(start_coords, pnp_coords)
    print(f"start to pnp\n{dist_m} meters")
    print(f"{dist_m/1609.34} miles")


def shorter_try():
    a = [47.576371, -122.420880] # alki point lighthouse
    b = [47.661856, -122.435826]  # near west point lighthouse
    b = [47.638603, -122.412524]  # mcgraw shoreline street
    dist_m = calc_haversine_distance(a, b)
    print(f"{dist_m/1609.34} miles")


if __name__ == "__main__":
    shorter_try()
