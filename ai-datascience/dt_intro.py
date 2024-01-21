from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path
import pandas as pd
import requests


class BootstrapSVGMobject(SVGMobject):
    def __init__(self, emoji, color=BLACK, **kwargs):
        url = f"https://raw.githubusercontent.com/twbs/icons/main/icons/{emoji}.svg"
        path_svg = Path.cwd() / f"{emoji}.svg"
        urllib.request.urlretrieve(url, path_svg)
        path_svg.write_text(path_svg.read_text().replace("currentColor", color))
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally


class EmojiImageMobject(ImageMobject):
    def __init__(self, emoji, is_code=False, **kwargs):
        if is_code:
            url = f"https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/618x618/{emoji}.png"
        else:
            emoji_code = "-".join(f"{ord(c):x}" for c in emoji)
            emoji_code = emoji_code.upper()  # <-  needed for openmojis
            url = f"https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/618x618/{emoji_code}.png"
        im = Image.open(requests.get(url, stream=True).raw)
        emoji_img = np.array(im.convert("RGBA"))
        ImageMobject.__init__(self, emoji_img, **kwargs)


class Intro(Scene):
    def construct(self):
        # set background color
        self.camera.background_color = "#0f0e17"

        # add 'programming = data structures + algorithms' text
        # text = Tex("programming = data structures + algorithms")
        # # add 'this is also true for data science' text
        # text2 = Tex("This is also ture for", " data science")
        # # set color '#DF5868' for text2
        # text2[1].set_color("#DF5868")
        # # scale it up to 1.2
        # text.scale(1.2)
        # # make text2 be below text
        # text2.next_to(text, DOWN * 2)
        # self.play(Write(text))
        # self.wait(1)
        # # text2 animation
        # text2_anims = [FadeIn(text2[0]), FadeIn(text2[1], shift=DOWN)]
        # self.play(*text2_anims)

        # # move it to the top of the screen
        # text.generate_target()
        # text.target.move_to(3 * UP)
        # # move text2 to the top of the screen
        # text2.generate_target()
        # text2.target.move_to(2 * UP)
        # self.play(MoveToTarget(text), MoveToTarget(text2))

        # # introduce three data structures
        # # table, json, and unstructured data like text-file
        # table = BootstrapSVGMobject("table", color="#2cb67d")
        # table.scale(0.7)
        # table.move_to(3 * LEFT)
        # json = BootstrapSVGMobject("filetype-json", color="#2cb67d")
        # json.scale(0.7)
        # text_file = BootstrapSVGMobject("body-text", color="#2cb67d")
        # text_file.scale(0.7)
        # text_file.move_to(3 * RIGHT)
        # # add table, json, and text to the screen one by one
        # self.play(GrowFromPoint(table, table.get_center()))
        # self.play(GrowFromPoint(json, json.get_center()))
        # self.play(GrowFromPoint(text_file, text_file.get_center()))

        # # clear everything
        # self.play(
        #     FadeOut(text),
        #     FadeOut(text2),
        #     FadeOut(table),
        #     FadeOut(json),
        #     FadeOut(text_file),
        # )

        # add a human svg
        human = BootstrapSVGMobject("person-fill", color="#F2EEF5").scale(0.7)
        # put it in the center of the screen
        human.move_to(ORIGIN)
        # add 'gender-female' svg
        woman_emoji = EmojiImageMobject("👩")
        banknote_emoji = EmojiImageMobject("💵")
        car_emoji = EmojiImageMobject("🚗")
        dog_emoji = EmojiImageMobject("🐕")
        avocado_emoji = EmojiImageMobject("🥑")
        linkedin_emoji = EmojiImageMobject("E046", is_code=True)
        features_group = [woman_emoji, banknote_emoji, car_emoji, dog_emoji,
                           avocado_emoji, linkedin_emoji]

        for idx, feature in enumerate(features_group):
            angle = idx * 2 * PI / len(features_group)
            x = 3 * np.cos(angle)   # radius = 3 for x
            y = 2.5 * np.sin(angle)   # radius = 2.5 for y
            feature.shift([x, y, 0]).scale(0.3)

        # create a human first
        self.play(GrowFromCenter(human))

        human_group = [human, *features_group]
        for feature in features_group:
            self.play(FadeIn(feature))
            # add line from human to feature
            line = DashedLine(human.get_center(), feature.get_center(), buff=0.7)
            self.play(Create(line), run_time=0.7)
            # append line to human_group
            human_group.append(line)

        
        # create group for human_group
        human_group = Group(*human_group)
        # move human_group to the top left of the screen with scale 0.7
        human_group.generate_target()
        human_group.target.scale(0.3)
        human_group.target.move_to(UP * 3 + LEFT * 5)
        # play human_group animation
        self.play(MoveToTarget(human_group))

        # create a table
        human_table = Table(
            [['int', 'str', 'int', 'str', 'str', 'str', 'bool'], # header
            ["id", "gender", "income", "car", "pet", "food", "linkedin"],
            ["1", "female", "1000", "BYD", "dog", "avocado", "yes"],
            ["2", "male", "2000", "BMW", "cat", "avocado", "no"],
            ["3", "male", "4000", "Audi", "dog", "noodles", "yes"],
            ['...', '...', '...', '...', '...', '...', '...'],
            ["42", "female", "5000", "Audi", "dog", "avocado", "yes"]]
        ).scale(0.4).shift(RIGHT * 0.8)

        # play human_table animation
        self.play(GrowFromCenter(human_table))

        # add surrounding rectangle for row 1
        row1_highlight = SurroundingRectangle(human_table.get_rows()[0])
        # play row1_highlight animation
        self.play(FadeIn(row1_highlight))

        # group human_table and row1_highlight together
        human_table_group = VGroup(human_table, row1_highlight)
        # move human_table_group to the top right of the screen with scale 0.7
        human_table_group.generate_target()
        human_table_group.target.scale(0.8)
        human_table_group.target.move_to(RIGHT * 2)
        # play human_table_group animation
        self.play(MoveToTarget(human_table_group))


        # add code 'str(data)' on the left of human_table
        code_snippet = """str(data)"""
        code_block = Code(
            code=code_snippet,
            background="window",
            language="R",
            font="Monospace",
            line_spacing=1,
        )
        # move code_block to the left of human_table
        code_block.next_to(human_table, LEFT*3)
        # play code_block animation
        self.play(FadeIn(code_block))


        # remove human_table_group and code_block
        self.play(FadeOut(human_table_group), FadeOut(code_block))

        # move human_group to the center of the screen with scale 0.7
        human_group.generate_target()
        human_group.target.scale(2)
        human_group.target.move_to(ORIGIN)
        # play human_group animation
        self.play(MoveToTarget(human_group))

        # get the postion for each feature
        feature_postions = []
        for feature in features_group:
            feature_postions.append(feature.get_center())
        
        feature_postions = feature_postions[1:] + feature_postions[:1]

        # change the position of each feature
        for idx, feature in enumerate(features_group):
            feature.generate_target()
            feature.target.move_to(feature_postions[idx])

        # lagged_start for features_group
        # move at the same time
        self.play(LaggedStart(*[MoveToTarget(feature) for feature in features_group], lag_ratio=0))

        # move human_group left
        self.play(human_group.animate.shift(LEFT * 3))

        # add new emojis
        linkedin_related_emojis = ['E303', 'E259', '260E', 'E063']
        postion_degree = [20, 60, 340, 300]
        postion_degree = [i * PI / 180 for i in postion_degree]

        linkedin_related_emojis_group = []
        # create new emojis
        for idx, emoji in enumerate(linkedin_related_emojis):
            emoji = EmojiImageMobject(emoji, is_code=True)
            emoji.scale(0.3)
            # get the center of linkedin emoji
            center = features_group[-1].get_center()
            # get the position for each emoji
            x = center[0] + 4 * np.cos(postion_degree[idx])
            y = center[1] + 3 * np.sin(postion_degree[idx])

            emoji.shift([x, y, 0])
            linkedin_related_emojis_group.append(emoji)
            

        # animate new emojis
        for emoji in linkedin_related_emojis_group:
            self.play(FadeIn(emoji))
            # add line from human to feature
            line = Line(features_group[-1].get_center(), emoji.get_center(), buff=0.7)
            self.play(Create(line), run_time=0.3)


        








        # remove text and text2
        # self.play(FadeOut(text), FadeOut(text2))

        # # rearraange the three data structures from top to bottom
        # # on the left side of the screen
        # table.generate_target()
        # table.target.move_to(UP * 2.5 + LEFT * 3)
        # json.generate_target()
        # json.target.move_to(UP * 0.5 + LEFT * 3)
        # text_file.generate_target()
        # text_file.target.move_to(DOWN * 1.5 + LEFT * 3)
        # self.play(
        #     MoveToTarget(table),
        #     MoveToTarget(json),
        #     MoveToTarget(text_file),
        # )

        # # add text 'Structed Data - Easy' to the left of table
        # text_table = Tex("Structured Data - ", "Easy")
        # # set color '#DF5868' for text_table[1]
        # text_table[1].set_color("#DF5868")
        # text_table.next_to(table, RIGHT * 3)
        # # play text_table animation
        # self.play(FadeIn(text_table))

        # # add text 'Semistructured Data - Medium' to the left of json
        # text_json = Tex("Semistructured Data - ", "Medium")
        # # set color '#DF5868' for text_json[1]
        # text_json[1].set_color("#DF5868")
        # text_json.next_to(json, RIGHT * 3)
        # # play text_json animation with fade in
        # self.play(FadeIn(text_json))

        # # add text 'Unstructured Data - Hard' to the left of text_file
        # text_text_file = Tex("Unstructured Data - ", "Hard")
        # # set color '#DF5868' for text_text_file[1]
        # text_text_file[1].set_color("#DF5868")
        # text_text_file.next_to(text_file, RIGHT * 3)
        # # play text_text_file animation with fade in
        # self.play(FadeIn(text_text_file))

        # # remove everything
        # self.play(FadeOut(text_table), FadeOut(text_json), FadeOut(text_text_file))
        # # add a 3 by 3 random matrix with random numbers (int)
        # matrix = Matrix([[3, 2, 3], [1, 7, 6], [7, 4, 2]])
        # # move matrix to the right of the screen
        # matrix.move_to(RIGHT * 3)
        # # add to the screen
        # self.play(GrowFromCenter(matrix), run_time=3)

        # # add arrow from table to matrix and arrow from json to matrix
        # # and arrow from text_file to matrix (lef edge of matrix)
        # arrow_table = Arrow(table.get_right(), matrix.get_left())
        # arrow_json = Arrow(json.get_right(), matrix.get_left())
        # arrow_text_file = Arrow(text_file.get_right(), matrix.get_left())

        # # play arrow_table, arrow_json, and arrow_text_file animations
        # self.play(
        #     GrowArrow(arrow_table),
        #     GrowArrow(arrow_json),
        #     GrowArrow(arrow_text_file),
        #     run_time=3,
        # )

        # # remove everything
        # # add image from './images/movie_matrix.jpg'
        # # and move it to the right of the screen
        # self.play(
        #     FadeOut(matrix),
        #     FadeOut(arrow_table),
        #     FadeOut(arrow_json),
        #     FadeOut(arrow_text_file),
        # )

        # # add image from './images/movie_matrix.jpg'
        # # and move it to the right of the screen
        # image = ImageMobject("./images/movie_matrix.jpg")
        # image.scale(0.3)
        # image.move_to(RIGHT * 3)
        # # add to the screen
        # self.play(
        #     GrowFromCenter(image), FadeOut(table), FadeOut(json), FadeOut(text_file)
        # )

        # # add text 'With my 10 years of experience' to the left of image
        # text_image = Tex("With my 10 years of experience")
        # text_image.next_to(image, LEFT * 3)
        # # add text 'THINK In Matrices' to below text_image
        # text_image2 = Tex("THINK In Matrices")
        # # set color '#DF5868' for text_image2
        # text_image2.set_color("#DF5868")
        # # scale it up to 1.2
        # text_image2.scale(1.2)
        # text_image2.next_to(text_image, DOWN * 2.5)

        # # play text_image and text_image2 animations
        # self.play(FadeIn(text_image))
        # self.play(FadeIn(text_image2))

        # # remove everything
        # self.play(FadeOut(image), FadeOut(text_image), FadeOut(text_image2))

        # # add image './images/movie_matrix2.png'
        # # and keep it in the center of the screen
        # image2 = ImageMobject("./images/movie_matrix2.png")
        # image2.scale(0.7)
        # # add to the screen
        # self.play(GrowFromCenter(image2))

        # # add text 'SEE IT IN MATRICES' on the top of the screen
        # text_image3 = Tex("SEE IT IN MATRICES")
        # # set color '#DF5868' for text_image3
        # text_image3.set_color("#DF5868")
        # # scale it up to 1.2
        # text_image3.scale(1.5)
        # # play text_image3 animation
        # self.play(FadeIn(text_image3))


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

        # add text 'row' on left of brace_table2
        text_row = Tex("row-i")
        # set color '#FD8927' for text_row
        text_row.set_color("#FD8927")
        # make it vertical
        text_row.rotate(PI / 2)
        # move text_row to left of brace_table2
        text_row.next_to(brace_table2, LEFT * 0.5)
        # play text_row animation
        self.play(FadeIn(text_row))

        # add text 'column' on top of brace_table
        text_column = Tex("column-j")
        # set color '#E1181D' for text_column
        text_column.set_color("#E1181D")
        # move text_column to top of brace_table
        text_column.next_to(brace_table, UP * 0.5)
        # play text_column animation
        self.play(FadeIn(text_column))

        # remove brace_table, brace_table2, text_row, and text_column
        self.play(
            FadeOut(brace_table),
            FadeOut(brace_table2),
            FadeOut(text_row),
            FadeOut(text_column),
        )

        # add text 'data[i, j, by]' on the top of the screen
        text_data = Tex("data[i, j, by]")
        # set color '#7f5af0' for text_data
        text_data.set_color("#7f5af0")
        # scale it up to 1.2
        text_data.scale(1.5)
        # move text_data to the top of the screen
        text_data.move_to(UP * 3)

        # scale table down to 0.7 and move it to the right of the screen
        table.generate_target()
        table.target.scale(0.7)
        table.target.move_to(RIGHT * 3 + UP * 0.5)
        # play table animation
        self.play(FadeIn(text_data), MoveToTarget(table))

        # add code block 'DT[i, j, by]' on the left of table
        code_snippet1 = """data[i, j, by]"""
        code_block = Code(
            code=code_snippet1,
            background="window",
            language="R",
            font="Monospace",
            line_spacing=1,
        )
        # move code_block to the left of table
        code_block.next_to(table, LEFT * 3)
        # play code_block animation
        self.play(FadeIn(code_block))

        # remove code_block
        self.play(FadeOut(code_block))
        # add new code block 'data[1:2,]' on the left of table
        code_snippet2 = """data[2,]"""
        code_block2 = Code(
            code=code_snippet2,
            background="window",
            language="R",
            font="Monospace",
            line_spacing=1,
        )
        # now highlight the third row of the table
        row2_highlight = SurroundingRectangle(table.get_rows()[2])
        # move code_block2 to the left of table
        code_block2.next_to(table, LEFT * 5)
        # play code_block2 animation
        self.play(FadeIn(code_block2), FadeIn(row2_highlight))

        # add text 'Using i position to select rows'
        # and move down to 1.5
        text_i = Tex("Using i position to select rows")
        # no need to set color for text_i
        text_i.scale(1.5)
        text_i.shift(DOWN * 2)
        # play text_i animation
        self.play(Write(text_i))

        # remove table, code_block2, and text_i
        self.play(
            FadeOut(table),
            FadeOut(code_block2),
            FadeOut(text_i),
            FadeOut(row2_highlight),
        )

        # print out elements of table

        # add table again
        self.play(GrowFromCenter(table))

        # add code block
        code_snippet = """
        data[, 2:3]
        data[, .(name, family_name)]"""

        code_block = Code(
            code=code_snippet,
            background="window",
            language="R",
            font="Monospace",
            line_spacing=1,
        )

        # scale down code_block to 0.7
        code_block.scale(0.85)

        # move code_block to the left of table
        code_block.next_to(table, LEFT * 2)

        # add highlight for columns 2 and 3
        col2_highlight = SurroundingRectangle(table.get_columns()[1:3])
        # play code_block animation
        self.play(FadeIn(code_block), FadeIn(col2_highlight))

        # add text 'Using j position to select columns'
        # and move down to 1.5
        text_j = Tex("Using j position to select columns")
        # no need to set color for text_j
        text_j.scale(1.5)
        text_j.shift(DOWN * 2)
        # play text_j animation
        self.play(Write(text_j))

        # remove table, code_block, and text_j
        self.play(
            FadeOut(table),
            FadeOut(code_block),
            FadeOut(text_j),
            FadeOut(col2_highlight),
        )

        # create a new table
        row1 = df.columns[[0, 1, 3, 6]].to_list()
        row2 = df.iloc[0, [0, 1, 3, 6]].to_list()
        # convert row2 to string
        row2 = [str(i) for i in row2]

        row3 = df.iloc[-2, [0, 1, 3, 6]].to_list()
        # convert row3 to string
        row3 = [str(i) for i in row3]

        row4 = df.iloc[2, [0, 1, 3, 6]].to_list()
        # convert row4 to string
        row4 = [str(i) for i in row4]

        row5 = df.iloc[3, [0, 1, 3, 6]].to_list()
        # convert row5 to string
        row5 = [str(i) for i in row5]

        # add table from df
        table = Table([row1, row2, row3, row4, row5])

        # scale down table to 0.7
        table.scale(0.7)

        # move table to center of the screen
        table.move_to(ORIGIN)

        # add highlight for cell(1, 2) and cell(3, 2)
        table.add_highlighted_cell((2, 3), color=GREEN)
        table.add_highlighted_cell((4, 3), color=GREEN)

        table[0].set_opacity(0)
        table[1].set_opacity(0)

        # add surrounding rectangle for row 2 and row 4
        row2_highlight = SurroundingRectangle(table.get_rows()[1])
        # move right
        row2_highlight.shift(RIGHT * 3)
        row3_highlight = SurroundingRectangle(table.get_rows()[3])
        # move left
        row3_highlight.shift(LEFT * 3)

        # play row2_highlight and row3_highlight animations
        self.play(FadeIn(table))

        # let row2_highlight and row3_highlight
        # fly in from the left side of the screen
        self.play(
            row2_highlight.animate.shift(LEFT * 3),
            row3_highlight.animate.shift(RIGHT * 3),
            run_time=2,
        )

        self.play(
            table[0].animate.set_opacity(0.7),
            table[1].animate.set_opacity(0.7),
            run_time=2,
        )

        # add code block
        code_snippet3 = """
        data %>%
            .[category == 'top'] %>%
            .[, .(age)] %>%
            sum()"""

        code_block3 = Code(
            code=code_snippet3,
            background="window",
            language="R",
            font="Monospace",
            line_spacing=1,
        ).scale(0.8)

        # remove row2_highlight and row3_highlight
        # and move table to the right of the screen with scale 0.7
        self.play(
            FadeOut(row2_highlight),
            FadeOut(row3_highlight),
            table.animate.scale(0.7).move_to(RIGHT * 3),
            run_time=2,
        )

        # move code_block3 to the left of table
        code_block3.next_to(table, LEFT * 1.7)

        # play code_block3 animation
        self.play(Write(code_block3), run_time=8)

        # remove everything
        self.play(FadeOut(table), FadeOut(code_block3))

        # create new table
        # category	age_sum
        # <chr>	<dbl>
        # top	90
        # middle	180
        # bottom	380
        table = Table(
            [
                ["category", "age_sum"],
                ["top", "90"],
                ["middle", "180"],
                ["bottom", "380"],
            ]
        )

        # scale down table to 0.7
        table.scale(0.7)

        # move table to center of the screen
        table.move_to(ORIGIN)

        self.play(GrowFromCenter(table))

        # move table to the right of the screen with scale 0.7
        table.generate_target()
        table.target.scale(0.7)
        table.target.move_to(RIGHT * 3)
        # play table animation
        self.play(MoveToTarget(table))

        # add code block
        code_snippet4 = """
        data %>%
            .[, .(age_sum = sum(age)), by = category]"""

        code_block4 = Code(
            code=code_snippet4,
            background="window",
            language="R",
            font="Monospace",
            line_spacing=1,
        ).scale(0.7)

        # move code_block4 to the left of table
        code_block4.next_to(table, LEFT * 1.7)

        # play code_block4 animation
        self.play(Write(code_block4), run_time=5)

        # add text 'Using by to group rows'
        # and move down to 1.5
        text_by = Tex("Using by to group rows")
        # no need to set color for text_by
        text_by.scale(1.5)
        text_by.shift(DOWN * 2)

        # play text_by animation
        self.play(Write(text_by))
