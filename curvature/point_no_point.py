from curvature import calc


def main():
    """Outputs hidden height of Point No Point lighthouse when viewed from various vantage points"""
    h0 = calc.SIX_FOOT_OBSERVER_M / 2
    pnp_elevation_ft = 12 + 30
    print(f'point no point light house elevation {pnp_elevation_ft} ft\n')

    # choice of radius affects hidden height by less than 1 foot
    # equatorial radius gives smallest hidden height
    earth_radius_m = calc.EQUATORIAL_RADIUS_M

    # gmaps: https://tinyurl.com/y573shcs
    s_ppp_pnp_mi = 9.25

    # gmaps: https://tinyurl.com/42z5h9k6
    s_marina_beach_pnp_mi = 9.500277835663875

    # gmaps: https://tinyurl.com/y69l9pty
    s_carkeek_beach_pnp_mi = 15.39029835770028

    # gmaps: https://tinyurl.com/yyrxeyn2
    s_golden_gardens_pnp_mi = 16.06936411764026

    for name, s in [('picnic point', s_ppp_pnp_mi), ('marina beach', s_marina_beach_pnp_mi),
                    ('carkeek', s_carkeek_beach_pnp_mi), ('golden gardens', s_golden_gardens_pnp_mi)]:
        hh = calc.calc_hidden_height(h0=h0, s=calc.to_meters(s), r=earth_radius_m)
        print(f"hh from {name}\n{hh} m\n{m2ft(hh)} ft\n")


def m2ft(x):
    """ Convert meters to feet"""
    return x * 3.28084


if __name__ == "__main__":
    main()
