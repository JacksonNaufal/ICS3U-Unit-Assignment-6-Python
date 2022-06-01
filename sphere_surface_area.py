#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: May 2022
# This is a sphere surface area  calculator

import math


def surface_area_function(radius):

    # process
    surface_area = math.pi * (radius**2) * 4

    return surface_area


def main():

    # input
    user_radius = input("Enter Your radius (mm): ")

    # output
    try:
        user_radius_int = float(user_radius)
        function_grade = round(
            surface_area_function(
                radius=user_radius_int,
            ),
            2,
        )

        print("The surface area of a sphere is {0} mm²".format(function_grade))

    except Exception:
        print("Not An Integer")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
