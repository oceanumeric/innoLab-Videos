from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


class BootstrapSVGMobject(SVGMobject):
    def __init__(self, emoji, color=BLACK, **kwargs):
        url = f"https://raw.githubusercontent.com/twbs/icons/main/icons/{emoji}.svg"
        path_svg = Path.cwd() / f"{emoji}.svg"
        urllib.request.urlretrieve(url, path_svg)
        path_svg.write_text(path_svg.read_text().replace("currentColor", color))
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally


class Ch1(MovingCameraScene):
    def construct(self):
        # set background color
        self.camera.background_color = WHITE
        # top right logo
        stack = BootstrapSVGMobject(
            "stack", color="#37A48D"
            ).scale(1.3).shift(LEFT*4.3)
        stack.shift(UP*0.2)
        title = SVGMobject("../images/HyperGI_2.svg")
        title.next_to(stack, RIGHT, buff=0.5).shift(DOWN*0.3)
        title_group = VGroup(stack, title)
        title_group.shift(UP*3.2+RIGHT*5.6).scale(0.17)
        self.add(title_group)

        # vertical bar
        vertical_bar = Rectangle(
            height=0.5,
            width=0.09,
            fill_color="#83EDBC",
            fill_opacity=1.6,
            stroke_width=0.5,
        ).shift(UP*0.4+LEFT*3.5)
        self.play(FadeIn(vertical_bar))

        # add text
        title1 = Text(
            "Why is RESTful API so popular",
            font = "Roboto",
            color = "#3b3a3a",
            weight = BOLD,
        ).scale(0.7)
        title1.next_to(vertical_bar, RIGHT, buff=0.2).shift(DOWN*0.03)
        self.play(Write(title1))

        # group vertical bar and title1
        title1_group = VGroup(vertical_bar, title1)

        # add bottom right corner shape
        cloudy = BootstrapSVGMobject(
            "cloudy-fill", color="#d2f7e6"
        ).scale(1.7)
        cloudy.shift(DOWN*3+RIGHT*5.3).rotate(PI/7.7)
        self.play(FadeIn(cloudy))

        # move the title1 to the top left corner
        self.play(
          title1_group.animate.shift(UP*3+LEFT*4.3).scale(0.7),
        )

        # add { REST }
        rest_text1 = Text(
            "{",
            font = "Open Sans",
            color = "#37CB8F",
            weight = BOLD
        ).shift(UP*0.2+LEFT*1.7)

        rest_text2 = Text(
            "REST",
            font = "Linux Libertine O",
            color = "#26ADC3",
            weight = BOLD,
        )
        rest_text2.next_to(rest_text1, RIGHT, buff=0.2)
        
        rest_text3 = Text(
            "}",
            font = "Open Sans",
            color = "#37CB8F",
            weight = BOLD
        )

        rest_text3.next_to(rest_text2, RIGHT, buff=0.2)

        rest_text_group = VGroup(rest_text1, rest_text2, rest_text3).scale(3.3)

        self.play(Write(rest_text_group), run_time=2.7)
