"""17.6 Gasup

Given cities on the circular road, find an "ample" city, i.e. the one that will provide
enough gas to go around

Length of the road is 3,000 miles and vehicle get 20 m/g

City  Fuel   Next city
 A    50      900
 B    20      600
 C    5       200
 D    30      400   => gets to E with
 E    25      600
 F    10      200
 G    10      100

Answer: D - can start without gas and complete the circle

Does not work:
- Start from a city with the most gas. A has most gas, but cannot get to C
- Closest city
- City with best distance to gas ratio

Need to come to city with minimum of gas.

"""

import collections

MPG = 20


def find_ample_city(gallons, distances):
    remaining_gallons = 0
    CityAndRemainingGas = collections.namedtuple(
        "CityAndRemaining", ("city", "remaining_galons")
    )
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if (
            remaining_gallons < city_remaining_gallons_pair.remaining_galons
        ):  # Can we run out of gas?
            city_remaining_gallons_pair = CityAndRemainingGas(
                i, remaining_gallons
            )  # No, take next one

    return city_remaining_gallons_pair.city
