from manim import *

class MerkleTreeScene(Scene):
    def setup(self):
        self.data1, self.box_data1 = self._node("d1", DOWN * 3 + LEFT * 3)
        self.data2, self.box_data2 = self._node("d2", DOWN * 3 + LEFT * 1)
        self.data3, self.box_data3 = self._node("d3", DOWN * 3 + RIGHT * 1)
        self.data4, self.box_data4 = self._node("d4", DOWN * 3 + RIGHT * 3)

        self.hash_data1, self.box_hash_data1 = self._node("h(d1)", DOWN * 1 + LEFT * 3)
        self.hash_data2, self.box_hash_data2 = self._node("h(d2)", DOWN * 1 + LEFT * 1)
        self.hash_data3, self.box_hash_data3 = self._node("h(d3)", DOWN * 1 + RIGHT * 1)
        self.hash_data4, self.box_hash_data4 = self._node("h(d4)", DOWN * 1 + RIGHT * 3)

        self.hash_left, self.box_hash_left = self._node("h( h(d1) + h(d2) )", UP * 1 + LEFT * 2)
        self.hash_right, self.box_hash_right = self._node("h( h(d3) + h(d4) )", UP * 1 + RIGHT * 2)

        self.hash_root, self.box_hash_root = self._node("h( h( h(d1) + h(d2) ) + h( h(d3) + h(d4) )", UP * 3)

        self.line1 = self._line_between(self.data1, self.hash_data1)
        self.line2 = self._line_between(self.data2, self.hash_data2)
        self.line3 = self._line_between(self.data3, self.hash_data3)
        self.line4 = self._line_between(self.data4, self.hash_data4)

        self.line5 = self._line_between(self.hash_data1, self.hash_left)
        self.line6 = self._line_between(self.hash_data2, self.hash_left)
        self.line7 = self._line_between(self.hash_data3, self.hash_right)
        self.line8 = self._line_between(self.hash_data4, self.hash_right)

        self.line9 = self._line_between(self.hash_left, self.hash_root)
        self.line10 = self._line_between(self.hash_right, self.hash_root)

    def _node(self, text, position):
        data = Text(text).scale(0.6).shift(position)
        box = BackgroundRectangle(data, color=self._node_color(), buff=0.2, fill_opacity=1)
        data.set_z_index(2)
        box.set_z_index(1)
        return data, box

    def _line_between(self, starting_element, ending_element):
        return Line(starting_element.get_center(), ending_element.get_center(), color=self._line_and_text_color())

    def _line_and_text_color(self):
        return WHITE

    def _node_color(self):
        return BLUE

    def _first_highlight_color(self):
        return "#FFA500"

    def _second_highlight_color(self):
        return "#800080"

class MerkleTreeConstruction(MerkleTreeScene):
    def construct(self):
        self.play(Create(self.box_data1), Create(self.box_data2), Create(self.box_data3), Create(self.box_data4))
        self.play(Write(self.data1), Write(self.data2), Write(self.data3), Write(self.data4))
        self.wait(1)

        self.play(Create(self.line1), Create(self.line2), Create(self.line3), Create(self.line4), Create(self.box_hash_data1), Create(self.box_hash_data2), Create(self.box_hash_data3), Create(self.box_hash_data4))
        self.play(Write(self.hash_data1), Write(self.hash_data2), Write(self.hash_data3), Write(self.hash_data4))
        self.wait(3)

        self.play(Create(self.line5), Create(self.line6), Create(self.line7), Create(self.line8), Create(self.box_hash_left), Create(self.box_hash_right))
        self.play(Write(self.hash_left), Write(self.hash_right))
        self.wait(3)

        self.play(Create(self.line9), Create(self.line10), Create(self.box_hash_root))
        self.play(Write(self.hash_root))
        self.wait(5)

class MerkleTreeAuthentication(MerkleTreeScene):
    def construct(self):
        self.add(self.box_data1, self.box_data2, self.box_data3, self.box_data4)
        self.add(self.data1, self.data2, self.data3, self.data4)
        self.add(self.line1, self.line2, self.line3, self.line4, self.box_hash_data1, self.box_hash_data2, self.box_hash_data3, self.box_hash_data4)
        self.add(self.hash_data1, self.hash_data2, self.hash_data3, self.hash_data4)
        self.add(self.line5, self.line6, self.line7, self.line8, self.box_hash_left, self.box_hash_right)
        self.add(self.hash_left, self.hash_right)
        self.add(self.line9, self.line10, self.box_hash_root)
        self.add(self.hash_root)
        self.wait(3)

        self.play(self._fade_to_first_highlight_color(self.box_data2))
        self.wait(1)

        self.play(self._fade_to_first_highlight_color(self.line2))
        self.play(self._fade_to_first_highlight_color(self.box_hash_data2))
        self.wait(1)

        self.play(self._fade_to_second_highlight_color(self.box_hash_data1))
        self.play(self._fade_to_second_highlight_color(self.line5), self._fade_to_first_highlight_color(self.line6))
        self.play(self._fade_to_first_highlight_color(self.box_hash_left))
        self.wait(1)

        self.play(self._fade_to_second_highlight_color(self.box_hash_right))
        self.play(self._fade_to_first_highlight_color(self.line9), self._fade_to_second_highlight_color(self.line10))
        self.play(self._fade_to_first_highlight_color(self.box_hash_root))
        self.wait(5)

    def _fade_to_first_highlight_color(self, movable_object):
        return FadeToColor(movable_object, color=self._first_highlight_color())

    def _fade_to_second_highlight_color(self, movable_object):
        return FadeToColor(movable_object, color=self._second_highlight_color())
