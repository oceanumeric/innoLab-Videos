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


class Intro3(Scene):
    def construct(self):
        # set background color
        self.camera.background_color = WHITE
        # create moving objects
        stack = BootstrapSVGMobject(
            "stack", color="#37A48D"
            ).scale(1.3).shift(LEFT*4.3)
        stack.shift(UP*0.2)
        title = SVGMobject("../images/HyperGI_2.svg")
        title.next_to(stack, RIGHT, buff=0.5).shift(DOWN*0.2)
        self.play(Write(stack))
        self.play(FadeIn(title))
        # group objects
        title_group = VGroup(stack, title)
        # add subtitle
        sub_title = Text(
            "Generative Intelligence Video Series",
            font = "Open Sans",
            color=BLACK,
            ).scale(0.7)
        sub_title.next_to(title_group, DOWN, buff=0.5)
        self.play(
            FadeIn(sub_title)
        )
        self.play(FadeOut(sub_title), run_time=1.9)
        # move title and stack to the topleft corner
        self.play(
            title_group.animate.shift(UP*3+LEFT*5.3).scale(0.3),
        )


        