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


class Intro(Scene):
    def construct(self):
        # set background color
        self.camera.background_color = WHITE
        # create moving objects
        em = BootstrapSVGMobject("stack", color="#37A48D").scale(1.3).shift(LEFT*3.7)
        em.shift(UP*0.1)
        title = Text("HyperGI", font = "Open Sans", color="#37A48D").scale(3).shift(RIGHT*2)
        self.play(Write(em))
        self.play(FadeIn(title))