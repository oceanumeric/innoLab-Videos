from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


theme_color = "#37CB8F"
theme_color_weak = "#83EDBC"
theme_color_gray = "#3b3a3a"
theme_color_blue = "#2F7ED0"


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
        title.next_to(stack, RIGHT, buff=0.5).shift(DOWN*0.3)
        self.play(Write(stack))
        self.play(FadeIn(title))
        # group objects
        title_group = VGroup(stack, title)
        # add subtitle
        sub_title = Text(
            "Generative Intelligence Video Series",
            font = "Open Sans",
            color=BLACK,
            ).scale(0.77)
        sub_title.next_to(title_group, DOWN, buff=0.5)
        self.play(
            FadeIn(sub_title)
        )
        self.play(FadeOut(sub_title), run_time=1.9)
        # move title and stack to the topleft corner
        self.play(
            title_group.animate.shift(UP*3.2+RIGHT*5.6).scale(0.17),
        )


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

        # remove vertical bar
        self.play(FadeOut(vertical_bar), run_time=0.3)

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
            color = theme_color_blue,
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

        # move out the rest_text_group
        self.play(FadeOut(rest_text_group))

        # add explanation text
        api_abbr = Text(
            "API",
            font = "Roboto",
            color = theme_color,
            weight = BOLD
        ).shift(LEFT*7 + UP*0.5)

        # vertical bar2
        vertical_bar2 = Rectangle(
            height=0.7,
            width=0.11,
            fill_color= theme_color_weak,
            fill_opacity=1.6,
            stroke_width=0.5,
        )

        vertical_bar2.next_to(api_abbr, LEFT, buff=0.16)

        api_expl = Text(
            "Stands for Application Programming Interface",
            t2c = {
                "A": theme_color,
                "P": theme_color,
                "I": theme_color,
            },
            color = theme_color_gray,
            font = "Roboto",
            weight = BOLD
        )

        api_expl.next_to(api_abbr, RIGHT, buff=0.2).shift(DOWN*0.05)

        api_group = VGroup(vertical_bar2, api_abbr, api_expl).scale(0.7)

        self.play(Write(api_group))

        # move up the api_group
        self.play(api_group.animate.shift(UP*1.3))

        # pc image
        pc_icon = BootstrapSVGMobject(
            "pc-display-horizontal", color=theme_color_blue
        ).scale(0.8).shift(LEFT*4+DOWN*0.2)

        self.play(FadeIn(pc_icon), run_time=0.3)

        # sever image
        sever_image = SVGMobject("../assets/server.svg").scale(0.8).shift(RIGHT*4+DOWN*0.2)

        self.play(DrawBorderThenFill(sever_image))

        # add arrow
        client_to_server = Arrow(
            start=pc_icon.get_right(),
            end=sever_image.get_left(),
            buff=0.2,
            color=theme_color_gray,
            stroke_width=3,
        ).shift(UP*0.2)
        # add text
        request_text = Text(
            "Request",
            font = "Roboto",
            color = theme_color_blue,
            weight = BOLD
        ).scale(0.4).shift(UP*0.2)

        # group request_text and client_to_server
        request_group = VGroup(client_to_server, request_text).shift(UP*0.15)

        self.play(Write(request_group), run_time=1.5)

        # add arrow
        server_to_client = Arrow(
            start=sever_image.get_left(),
            end=pc_icon.get_right(),
            buff=0.2,
            color=theme_color_gray,
            stroke_width=3,
        ).shift(DOWN*0.2)
        # add text
        response_text = Text(
            "Response",
            font = "Roboto",
            color = theme_color_blue,
            weight = BOLD
        ).scale(0.4).shift(DOWN*0.2)

        # group response_text and server_to_client
        response_group = VGroup(server_to_client, response_text).shift(DOWN*0.15)

        self.play(Write(response_group), run_time=1.5)


    



class MainScene(Scene):
    def construct(self):
        intro_scene = Intro3()
        intro_scene.render()
        chapter1_scene = Ch1()
        chapter1_scene.render()


if __name__ == "__main__":
    scene = MainScene()
    scene.render()
