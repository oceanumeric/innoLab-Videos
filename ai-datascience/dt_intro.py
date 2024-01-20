from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path
import pandas as pd


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

        # add 'programming = data structures + algorithms' text
        text = Tex("programming = data structures + algorithms")
        # add 'this is also true for data science' text
        text2 = Tex("This is also ture for", " data science")
        # set color '#DF5868' for text2
        text2[1].set_color("#DF5868")
        # scale it up to 1.2
        text.scale(1.2)
        # make text2 be below text
        text2.next_to(text, DOWN * 2)
        self.play(Write(text))
        self.wait(1)
        # text2 animation
        text2_anims = [FadeIn(text2[0]), FadeIn(text2[1], shift=DOWN)]
        self.play(*text2_anims)

        # move it to the top of the screen
        text.generate_target()
        text.target.move_to(3 * UP)
        # move text2 to the top of the screen
        text2.generate_target()
        text2.target.move_to(2 * UP)
        self.play(MoveToTarget(text), MoveToTarget(text2))

        # introduce three data structures
        # table, json, and unstructured data like text-file
        table = BootstrapSVGMobject("table", color="#2cb67d")
        table.scale(0.7)
        table.move_to(3 * LEFT)
        json = BootstrapSVGMobject("filetype-json", color="#2cb67d")
        json.scale(0.7)
        text_file = BootstrapSVGMobject("body-text", color="#2cb67d")
        text_file.scale(0.7)
        text_file.move_to(3 * RIGHT)
        # add table, json, and text to the screen one by one
        self.play(GrowFromPoint(table, table.get_center()))
        self.play(GrowFromPoint(json, json.get_center()))
        self.play(GrowFromPoint(text_file, text_file.get_center()))

        # remove text and text2
        self.play(FadeOut(text), FadeOut(text2))

        # rearraange the three data structures from top to bottom
        # on the left side of the screen
        table.generate_target()
        table.target.move_to(UP * 2.5 + LEFT * 3)
        json.generate_target()
        json.target.move_to(UP * 0.5 + LEFT * 3)
        text_file.generate_target()
        text_file.target.move_to(DOWN * 1.5 + LEFT * 3)
        self.play(
            MoveToTarget(table),
            MoveToTarget(json),
            MoveToTarget(text_file),
        )

        # add text 'Structed Data - Easy' to the left of table
        text_table = Tex("Structured Data - ", "Easy")
        # set color '#DF5868' for text_table[1]
        text_table[1].set_color("#DF5868")
        text_table.next_to(table, RIGHT * 3)
        # play text_table animation
        self.play(FadeIn(text_table))

        # add text 'Semistructured Data - Medium' to the left of json
        text_json = Tex("Semistructured Data - ", "Medium")
        # set color '#DF5868' for text_json[1]
        text_json[1].set_color("#DF5868")
        text_json.next_to(json, RIGHT * 3)
        # play text_json animation with fade in
        self.play(FadeIn(text_json))

        # add text 'Unstructured Data - Hard' to the left of text_file
        text_text_file = Tex("Unstructured Data - ", "Hard")
        # set color '#DF5868' for text_text_file[1]
        text_text_file[1].set_color("#DF5868")
        text_text_file.next_to(text_file, RIGHT * 3)
        # play text_text_file animation with fade in
        self.play(FadeIn(text_text_file))

        # remove everything
        self.play(FadeOut(text_table), FadeOut(text_json), FadeOut(text_text_file))
        # add a 3 by 3 random matrix with random numbers (int)
        matrix = Matrix([[3, 2, 3], [1, 7, 6], [7, 4, 2]])
        # move matrix to the right of the screen
        matrix.move_to(RIGHT * 3)
        # add to the screen
        self.play(GrowFromCenter(matrix), run_time=3)

        # add arrow from table to matrix and arrow from json to matrix
        # and arrow from text_file to matrix (lef edge of matrix)
        arrow_table = Arrow(table.get_right(), matrix.get_left())
        arrow_json = Arrow(json.get_right(), matrix.get_left())
        arrow_text_file = Arrow(text_file.get_right(), matrix.get_left())

        # play arrow_table, arrow_json, and arrow_text_file animations
        self.play(
            GrowArrow(arrow_table), GrowArrow(arrow_json), GrowArrow(arrow_text_file),
            run_time=3
        )

        # remove everything
        # add image from './images/movie_matrix.jpg'
        # and move it to the right of the screen
        self.play(
            FadeOut(matrix),
            FadeOut(arrow_table),
            FadeOut(arrow_json),
            FadeOut(arrow_text_file)
        )

        # add image from './images/movie_matrix.jpg'
        # and move it to the right of the screen
        image = ImageMobject("./images/movie_matrix.jpg")
        image.scale(0.3)
        image.move_to(RIGHT * 3)
        # add to the screen
        self.play(GrowFromCenter(image), FadeOut(table), FadeOut(json), FadeOut(text_file))


        # add text 'With my 10 years of experience' to the left of image
        text_image = Tex("With my 10 years of experience")
        text_image.next_to(image, LEFT * 3)
        # add text 'THINK In Matrices' to below text_image
        text_image2 = Tex("THINK In Matrices")
        # set color '#DF5868' for text_image2
        text_image2.set_color("#DF5868")
        # scale it up to 1.2
        text_image2.scale(1.2)
        text_image2.next_to(text_image, DOWN * 2.5)

        # play text_image and text_image2 animations
        self.play(FadeIn(text_image))
        self.play(FadeIn(text_image2))


        # remove everything
        self.play(FadeOut(image), FadeOut(text_image), FadeOut(text_image2))

        # add image './images/movie_matrix2.png'
        # and keep it in the center of the screen
        image2 = ImageMobject("./images/movie_matrix2.png")
        image2.scale(0.7)
        # add to the screen
        self.play(GrowFromCenter(image2))

        # add text 'SEE IT IN MATRICES' on the top of the screen
        text_image3 = Tex("SEE IT IN MATRICES")
        # set color '#DF5868' for text_image3
        text_image3.set_color("#DF5868")
        # scale it up to 1.2
        text_image3.scale(1.5)
        # play text_image3 animation
        self.play(FadeIn(text_image3))

    


# new chapter ch1
class Ch1(Scene):
    def construct(self):
        # set background color
        self.camera.background_color = "#0f0e17"

        # add hypergi logo on the top right
        stack = (
            BootstrapSVGMobject("stack", color="#37A48D").scale(1.2).shift(LEFT * 4.3)
        )
        stack.shift(UP * 0.2)
        title = SVGMobject("../images/HyperGI_2.svg")
        title.next_to(stack, RIGHT, buff=0.5).shift(DOWN * 0.3)
        # group objects
        title_group = VGroup(stack, title)
        title_group.shift(UP * 3.2 + RIGHT * 6.1).scale(0.17)
        # add to the screen
        self.add(title_group)

        # add text 'Chapter 1' on the top of the screen
        text_ch1 = Tex("Chapter 1 - data.table basics")
        # set color '#7f5af0' for text_ch1
        text_ch1.set_color("#7f5af0")
        # scale it up to 1.2
        text_ch1.scale(1.5)
        # play text_ch1 animation
        self.play(FadeIn(text_ch1))

        # add text ad code '[i, j, by]' under text_ch1
        text_ch1_code = Tex("[i, j, by]")
        # scale it up to 1.2
        text_ch1_code.scale(1.5)
        # make text_ch1_code be below text_ch1
        text_ch1_code.next_to(text_ch1, DOWN * 2)
        # add underline for text_ch1_code
        underline = Underline(text_ch1_code, buff=0.3, color="#7f5af0")
        # play text_ch1_code animation
        self.play(FadeIn(text_ch1_code), Create(underline))

        # remove everything
        self.play(FadeOut(text_ch1), FadeOut(text_ch1_code), FadeOut(underline))

        # add data.table logo on the top of the screen
        data_table_logo = ImageMobject("./images/data-table-logo.png")
        data_table_logo.shift(UP * 3.2 + LEFT * 6.3).scale(0.4)
        # add to the screen
        self.add(data_table_logo)

        # read data from './data/demo_dt.csv'
        df = pd.read_csv("./data/demo_dt.csv")
        # add table from df
        row1 = df.columns[:5].to_list()
        row2 = df.iloc[0, :5].to_list()
        # convert row2 to string
        row2 = [str(i) for i in row2]

        row3 = df.iloc[1, :5].to_list()
        # convert row3 to string
        row3 = [str(i) for i in row3]

        row4 = df.iloc[2, :5].to_list()
        # convert row4 to string
        row4 = [str(i) for i in row4]

        # add table from df
        table = Table([row1, row2, row3, row4])
        # scale down table to 0.7
        table.scale(0.7)
        # move table to center of the screen
        table.move_to(ORIGIN)
        # play table animation
        self.play(GrowFromCenter(table))

        # add brace for table
        # add on top of table
        brace_table = Brace(table, UP)
        # add on left of table
        brace_table2 = Brace(table, LEFT)

        # play brace_table and brace_table2 animations
        self.play(GrowFromCenter(brace_table), GrowFromCenter(brace_table2))

        # group table, brace_table, and brace_table2 together
        table_group = VGroup(table, brace_table, brace_table2)

        # create animation for table_group by scaling it down to 0.7
        table_group.generate_target()
        table_group.target.scale(0.8)
        # move table_group to right of the screen
        table_group.target.move_to(RIGHT * 0.5)
        # play table_group animation
        self.play(MoveToTarget(table_group))

        # add text 'data.table' on the top of the screen
 
    
