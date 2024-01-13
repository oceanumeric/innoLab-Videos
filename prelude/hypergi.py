from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


def _make_grid_art(
    n_x: int = 15,
    n_y: int = 10,
    grout_size: float = 0.2,
    h_num: int = 10,
    color: str = "#DF5868",
    opacity: float = 0.0,
):
    """
    With x_min = -5, x_max = 5, y_min = -2.5, y_max = 2.5
    generate coordinates of n_square squares for polygon
    n_x: number of squares in x direction
    n_y: number of squares in y direction
    grout_size: size of grout between squares
    h_num: number of hysteresis
    """

    # construct the sequence of x_center based on n_x and [-5, 5]
    x_centers = np.linspace(-5, 5, n_x)
    y_centers = np.linspace(-2.5, 2.5, n_y)

    half_grout = (1 - grout_size) / 2
    num_squares = n_x * n_y

    squares = []

    h_params = 0

    for y in y_centers:
        for x in x_centers:
            if h_num < 1:
                # generate hyteresis from normal distribution
                # with mean half_grout and std 0
                hyst = np.random.normal(half_grout, 0, 8)
            else:
                # generate hyteresis from normal distribution
                # with mean half_grout and std = sin(h_params/(num_squares-1)*pi)/h_num
                hyst = np.random.normal(
                    half_grout, np.sin(h_params / (num_squares - 1) * np.pi) / h_num, 8
                )

            # bottom_left
            bl = [x - hyst[0], y - hyst[1], 0]
            # bottom_right
            br = [x + hyst[2], y - hyst[3], 0]
            # top_right
            tr = [x + hyst[4], y + hyst[5], 0]
            # top_left
            tl = [x - hyst[6], y + hyst[7], 0]

            polygon_points = [bl, br, tr, tl]

            polygon = Polygon(*polygon_points)

            polygon.set_color(color)
            polygon.set_fill(color, opacity=opacity)

            squares.append(polygon)

            h_params += 1

    return squares


class BootstrapSVGMobject(SVGMobject):
    def __init__(self, emoji, color=BLACK, **kwargs):
        url = f"https://raw.githubusercontent.com/twbs/icons/main/icons/{emoji}.svg"
        path_svg = Path.cwd() / f"{emoji}.svg"
        urllib.request.urlretrieve(url, path_svg)
        path_svg.write_text(path_svg.read_text().replace("currentColor", color))
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally


class Intro(Scene):
    def construct(self):
        # set background color
        self.camera.background_color = "#0f0e17"

        # the axis of sreen is x: -7 to 7, y: -3 to 3

        tech1 = "#ff5470"
        tech2 = "#7f5af0"
    

        squares = _make_grid_art(n_x=13, n_y=8, grout_size=0.5, h_num=0, color=tech1)

        squares2 = _make_grid_art(
            n_x=13, n_y=8, grout_size=0.5, h_num=30, color="#FD8927"
        )

        squares3 = _make_grid_art(
            n_x=13, n_y=8, grout_size=0.5, h_num=13, color="#00ebc7"
        )

        # self.play(
        #     *[GrowFromPoint(square, square.get_center()) for square in squares]
        # )
        # # remove squares and squares2 with secene.remove
        # self.play(
        #     *[FadeOut(square) for square in squares],
        #     *[GrowFromPoint(square, square.get_center()) for square in squares2]
        #     )

        self.play(
            # zip squares2 and squares3 together
            # and then use RlacementTransform to transform
            *[
                Broadcast(square, square.get_center(), lag_ratio=0.3)
                for square in squares
            ],
            *[ReplacementTransform(a, b) for a, b in zip(squares, squares3)],
            run_time=3,
        )

        # create moving objects
        stack = (
            BootstrapSVGMobject("stack", color="#37A48D").scale(1.2).shift(LEFT * 4.3)
        )
        stack.shift(UP * 0.2)
        title = SVGMobject("../images/HyperGI_2.svg")
        title.next_to(stack, RIGHT, buff=0.5).shift(DOWN * 0.3)
        self.play(
            FadeOut(*squares3, run_time=1.5),
            FadeIn(stack, title)
         )
        # group objects
        title_group = VGroup(stack, title)

        # add subtitle
        # sub_title = Text(
        #     "Generative Intelligence Video Series",
        #     font="Open Sans",
        #     color=WHITE,
        # ).scale(0.77)
        # sub_title.next_to(title_group, DOWN, buff=0.5)
        # self.play(FadeIn(sub_title))
        # self.play(FadeOut(sub_title), run_time=2.3)

        # move title and stack to the topleft corner
        self.play(
            title_group.animate.shift(UP * 3.2 + RIGHT * 6.1).scale(0.17),
        )
