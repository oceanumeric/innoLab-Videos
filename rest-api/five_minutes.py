from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


theme_color = "#37CB8F"
theme_color_light = "#83EDBC"
theme_color_gray = "#3b3a3a"
theme_color_blue = "#2F7ED0"
theme_color_blue_light = "#7fb3eb"
theme_color_gray_light = "#616060"
theme_color_turquoise = "#26e8ff"


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
            "cloudy-fill", color=theme_color_light,
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
            fill_color= theme_color_light,
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

        def _abb_text(text1, text2, shift_x, shift_y):

            abbr = Text(
                text1,
                font = "Roboto",
                color = theme_color,
                weight = BOLD
            ).shift(LEFT*shift_x + UP*shift_y)

            t2c_dict = {}
            for i in text1:
                t2c_dict[i] = theme_color

            expl = Text(
                text2,
                font = "Roboto",
                t2c = t2c_dict,
                color = theme_color_gray,
                weight = BOLD
            ).next_to(abbr, RIGHT, buff=0.2).shift(DOWN*0.05)

            vertical_bar2.next_to(abbr, LEFT, buff=0.16)

            return VGroup(vertical_bar2, abbr, expl)

        # move up the api_group
        self.play(api_group.animate.shift(UP*1.3))

        # pc image
        pc_icon = BootstrapSVGMobject(
            "pc-display-horizontal", color=theme_color_blue
        ).scale(0.8).shift(LEFT*4+DOWN*0.2)

        # sever image
        sever_image = SVGMobject("../assets/server.svg").scale(0.8).shift(RIGHT*4+DOWN*0.2)

        pc_sever_group = VGroup(pc_icon, sever_image)

        self.play(Write(pc_sever_group))

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

        # move out the api_group
        self.play(FadeOut(api_group))

        # move out the request_group and response_group
        self.play(
            FadeOut(request_group),
            FadeOut(response_group),
        )

        # scale up pc_icon and sever_image
        self.play(
            pc_icon.animate.scale(1.1).shift(RIGHT*0.2+UP*0.1),
            sever_image.animate.scale(1.1).shift(LEFT*0.2+UP*0.1),
        )

        # cloudy fill
        cloudy_fill2 = BootstrapSVGMobject(
            "cloud-fill", color=theme_color_blue_light,
        ).scale(0.7).shift(DOWN*0.1)

        # play
        self.play(Create(cloudy_fill2))

        # add text
        cloud_text = Text(
            "{...}",
            font = "Roboto",
            color=theme_color_gray,
            weight = BOLD
        ).scale(0.4).shift(DOWN*0.1)
        rest_api_text = Text(
            "REST API",
            font = "Roboto",
            color=theme_color_gray
        ).scale(0.4).next_to(cloud_text, DOWN, buff=0.1)

        # group cloud_text and rest_api_text
        cloud_group = VGroup(cloud_text, rest_api_text)

        # add arrow
        cloud_arrow1 = Arrow(
            start=pc_icon.get_right(),
            end=cloudy_fill2.get_left(),
            color=theme_color_gray_light,
        ).shift(UP*0.2)
        cloud_arrow1.tip.scale(0.7)

        cloud_arrow2 = Arrow(
            start=cloudy_fill2.get_left(),
            end=pc_icon.get_right(),
            color=theme_color_gray_light,
        ).shift(DOWN*0.2)
        cloud_arrow2.tip.scale(0.7)

        cloud_arrow3 = Arrow(
            start = cloudy_fill2.get_right(),
            end = sever_image.get_left(),
            color=theme_color_gray_light,
        ).shift(UP*0.2)
        cloud_arrow3.tip.scale(0.7)

        cloud_arrow4 = Arrow(
            start = sever_image.get_left(),
            end = cloudy_fill2.get_right(),
            color=theme_color_gray_light,
        ).shift(DOWN*0.2)
        cloud_arrow4.tip.scale(0.7)

        self.play(
            FadeIn(cloud_group), 
            cloud_group.animate.shift(UP*0.1),
            Write(cloud_arrow1),
            Write(cloud_arrow2),
            Write(cloud_arrow3),
            Write(cloud_arrow4)
            )
        
        rest_exp = _abb_text("REST", "stands for REpresentational State Transfer", 6.2, 1)

        self.play(rest_exp.animate.shift(UP*1).scale(0.7), run_time=1.5)

        # clear the screen
        self.play(
            FadeOut(pc_sever_group),
            FadeOut(cloud_group),
            FadeOut(cloudy_fill2),
            FadeOut(cloud_arrow1),
            FadeOut(cloud_arrow2),
            FadeOut(cloud_arrow3),
            FadeOut(cloud_arrow4),
            FadeOut(rest_exp)
        )

        # add document
        document_svg = SVGMobject("../assets/document.svg")
        document_svg.scale(1.2).shift(UP*0.5)

        # add text
        not_specification = Text(
            "Not a specification",
            font = "Roboto",
            color=theme_color_gray)
        not_specification.next_to(document_svg, DOWN, buff=0.2)
        not_specification.scale(0.7)

        self.play(
            FadeIn(document_svg),
            Write(not_specification),
            run_time=0.7
        )

        self.play(
            FadeOut(document_svg),
            FadeOut(not_specification)
        )

        # rectangle
        rest_api_rules = Text(
            "REST API Rules",
            font = "Roboto",
            weight = BOLD
        ).scale(0.5)

        rectangle_txt1 = RoundedRectangle(
            corner_radius = 0.2,
            width = rest_api_rules.width+0.3,
            height = rest_api_rules.height+0.3)
        
        # fill color
        rectangle_txt1.set_fill(color=theme_color_turquoise, opacity=0.8)
        
        rest_api_rules_group = VGroup(rectangle_txt1, rest_api_rules)

        self.play(
            Write(rest_api_rules_group),
            rest_api_rules_group.animate.shift(LEFT*3.5+UP*0.7),
            )
        
        def _text_box(text):
            text = Text(
                text,
                font = "Roboto",
                color=theme_color_blue,
                weight = BOLD)
            text_box = RoundedRectangle(
                corner_radius = 0.2,
                stroke_color = theme_color_turquoise,
                width = text.width+0.3,
                height = text.height+0.3)
    
            return VGroup(text, text_box)
        
        uniform_interface = _text_box("Uniform Interface").scale(0.5)
        client_server = _text_box("Client-Server").scale(0.5)
        state_less = _text_box("Stateless").scale(0.5)
        cache = _text_box("Cacheable").scale(0.5)
        layered_system = _text_box("Layered System").scale(0.5)
        code_on_demand = _text_box("Code on Demand (Optional)").scale(0.5)

        # arrange group
        uniform_interface.shift(RIGHT*1.7+UP*2.1)
        client_server.next_to(uniform_interface, DOWN, buff=0.2, aligned_edge=LEFT)
        state_less.next_to(client_server, DOWN, buff=0.2, aligned_edge=LEFT)
        cache.next_to(state_less, DOWN, buff=0.2, aligned_edge=LEFT)
        layered_system.next_to(cache, DOWN, buff=0.2, aligned_edge=LEFT)
        code_on_demand.next_to(layered_system, DOWN, buff=0.2, aligned_edge=LEFT)


        # add curved arrow
        start_point_coord = rest_api_rules_group.get_right()
        curved_arrow1 = CurvedArrow(
            start_point = [start_point_coord[0]-0.4, start_point_coord[1]+0.25, 0],
            end_point = uniform_interface.get_left(),
            color = theme_color_turquoise,
            stroke_width = 2,
            tip_length = 0.0,
            radius = -9,
        )

        grp1 = VGroup(curved_arrow1, uniform_interface)

        curved_arrow2 = CurvedArrow(
            start_point = [start_point_coord[0]-0.2, start_point_coord[1]+0.25, 0],
            end_point = client_server.get_left(),
            color = theme_color_turquoise,
            stroke_width = 2,
            tip_length = 0.0,
            radius = -8,
        )

        grp2 = VGroup(curved_arrow2, client_server)

        curved_arrow3 = CurvedArrow(
            start_point = [start_point_coord[0], start_point_coord[1], 0],
            end_point = state_less.get_left(),
            color = theme_color_turquoise,
            stroke_width = 2,
            tip_length = 0.0,
            radius = -7,
        )

        grp3 = VGroup(curved_arrow3, state_less)

        curved_arrow4 = CurvedArrow(
            start_point = [start_point_coord[0], start_point_coord[1], 0],
            end_point = cache.get_left(),
            color = theme_color_turquoise,
            stroke_width = 2,
            tip_length = 0.0,
            radius = 7,
        )

        grp4 = VGroup(curved_arrow4, cache)

        curved_arrow5 = CurvedArrow(
            start_point = [start_point_coord[0]-0.2, start_point_coord[1]-0.25, 0],
            end_point = layered_system.get_left(),
            color = theme_color_turquoise,
            stroke_width = 2,
            tip_length = 0.0,
            radius = 8,
        )

        grp5 = VGroup(curved_arrow5, layered_system)

        curved_arrow6 = CurvedArrow(
            start_point = [start_point_coord[0]-0.4, start_point_coord[1]-0.25, 0],
            end_point = code_on_demand.get_left(),
            color = theme_color_turquoise,
            stroke_width = 2,
            tip_length = 0.0,
            radius = 9,
        )

        grp6 = VGroup(curved_arrow6, code_on_demand)


        self.play(Write(grp1), run_time=0.9)
        self.play(Write(grp2), run_time=0.9)
        self.play(Write(grp3), run_time=0.9)
        self.play(Write(grp4), run_time=0.9)
        self.play(Write(grp5), run_time=0.9)
        self.play(Write(grp6), run_time=0.9)    

    




    



class MainScene(Scene):
    def construct(self):
        intro_scene = Intro3()
        intro_scene.render()
        chapter1_scene = Ch1()
        chapter1_scene.render()


if __name__ == "__main__":
    scene = MainScene()
    scene.render()
