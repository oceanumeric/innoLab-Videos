#%%
'''
grid_squares.py
author: oceanumeric
reference: https://www.r-bloggers.com/2019/05/turn-a-square-generative-art/
'''
from itertools import repeat
import numpy as np
import matplotlib.pyplot as plt


def make_grid_art(
        x_size: int = 10, y_size: int = 10, grout_size: float = 0.2, h_num: int = 10
        ):
    """
    Make a grid of squares with a grout size between them.
    x_size: number of squares in x direction
    y_size: number of squares in y direction
: size of each square
    grout_size: size of grout between squares
    h_num: number of hysteresis
    """

    x_coords = []
    y_coords = []

    half_grout = (1-grout_size)/2
    num_squares = x_size * y_size


    for x in range(x_size):
        for y in range(y_size):
            if h_num < 1:
                # generate hyteresis from normal distribution
                # with mean half_grout and std 0
                hyst = np.random.normal(half_grout, 0, 8)
            else:
                # generate hyteresis from normal distribution
                # with mean half_grout and std = sin(x/(num_squares-1)*pi)/h_num
                hyst = np.random.normal(
                    half_grout, np.sin(x/(num_squares-1)*np.pi)/h_num, 8
                    )

            x_points = [
                x-hyst[0], x-hyst[1], 
                x+hyst[2], x+hyst[3], 
                x-hyst[0]
            ]
            y_points = [
                y+hyst[4], y-hyst[5], 
                y-hyst[6], y+hyst[7], 
                y+hyst[4]
            ]

            # now shaffle the points

            plt.plot(x_points, y_points, color="black")


if __name__ == "__main__":
    print("Hello World")
    make_grid_art(
        x_size=10, y_size=10, grout_size=0.2, h_num=4
    )


# %%
