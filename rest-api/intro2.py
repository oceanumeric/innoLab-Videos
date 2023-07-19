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


class Intro2(Scene):
    def construct(self):
        # set background color
        self.camera.background_color = WHITE
        # create moving objects
        stack = BootstrapSVGMobject("stack", color="#37A48D").scale(1.3).shift(LEFT*3.7)
        stack.shift(UP*0.1)
        title = Text("HyperGI", font = "Open Sans", color="#37A48D").scale(3)
        title.next_to(stack, RIGHT, buff=0.5).shift(DOWN*0.2)
        self.play(Write(stack))
        self.play(FadeIn(title))
        # group objects
        title_group = VGroup(stack, title)
        
        # move title and stack to the topleft corner
        self.play(
            title_group.animate.shift(UP*3+LEFT*5.3).scale(0.3),
        )


        