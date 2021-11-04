import math

# Max radius at the equator
EQUATORIAL_RADIUS_M = 6378137

# Min radius at the poles
POLAR_RADIUS_M = 6356752.3

# Estimate of mean is about 6371000 M
IUGG_MEAN_RADIUS_M = (2 * EQUATORIAL_RADIUS_M + POLAR_RADIUS_M) / 3

# 6ft observer height in meters
SIX_FOOT_OBSERVER_M = 1.8288

# 5'6" observer height in meters
FIVE_SIX_OBSERVER_M = 1.6764

# approx meters per mile
METERS_PER_MILE = 1609.344

FEET_PER_METER = 3.28084


def to_meters(miles: float) -> float:
    return miles * METERS_PER_MILE


def main():
    # TODO metric or imperial?
    is_metric = True

    radius_m = EQUATORIAL_RADIUS_M
    height_observer_m = SIX_FOOT_OBSERVER_M / 3
    print('mi\tft\tm')
    for tenths in range(40, 101, 1):
        total_distance_m = METERS_PER_MILE * tenths/10
        ft, meters = _print_hh(height_observer_m, radius_m, total_distance_m)
        print(f"{tenths/10}\t{ft}\t{meters}")


def _print_hh(height_observer_m, radius_m, total_distance_m, full_figures=False):
    hh_meters = calc_hidden_height(h0=height_observer_m, s=total_distance_m, r=radius_m)
    hh_feet = hh_meters * FEET_PER_METER
    # print(f"Sphere radius (r) \n{radius_m:,}m\n\n"
    #       f"Observer height (h_0) \n{height_observer_m:,}m\n\n"
    #       f"Observer-to-target distance (s) \n{total_distance_m:,}m\n")
    f_str = f"{hh_feet:,}" if full_figures else f"{round(hh_feet, 3):,}"
    m_str = f"{hh_meters:,}" if full_figures else f"{round(hh_meters, 3):,}"
    return f_str, m_str


# testing the correctness of the formula...
# symmetry test with 1/4 of the circumference of the earth. what observer height yields equivalent hidden height?
# distance to target is s=pi*r/2 or 1/4 the circumference
# s0 must be pi*r/4 then, and plugging that in and solving for h_0 gives (sqrt(2) - 1) * R
# plugging in these values given hidden_height = observer height
# total_distance_m = (math.pi * radius_m) / 2
# height_observer_m = (math.sqrt(2) - 1) * radius_m


# TODO print HH for range of distances

def calc_hidden_height(h0: float, s: float, r: float = IUGG_MEAN_RADIUS_M) -> float:
    """

    :param h0: Height of observer from sea level
    :param s: Arc length distance from observer to target
    :param r: Radius of the sphere
    :return: The radial height of the target that will be hidden from view by the sphere when viewed by the observer
    """
    if r <= 0 or h0 <= 0 or s <= 0:
        raise ValueError('All inputs must be greater than zero')

    if s > 2 * math.pi * r:
        raise ValueError('Observer to target distance must be less than circumference')

    # Define s0 to be the arc length from observer to point were sight is tangent to the sphere
    s0 = r * math.acos(r / (r + h0))

    # arc length from tangent point to target  |--s0--|----s1----|
    s1 = s - s0

    # hidden height
    return r / math.cos(s1 / r) - r


if __name__ == "__main__":
    main()
