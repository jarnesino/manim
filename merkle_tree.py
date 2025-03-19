from manim import *

class MerkleTreeAssembly(Scene):
    def construct(self):
        data1, box_data1 = self._node("d1", DOWN * 3 + LEFT * 3)
        data2, box_data2 = self._node("d2", DOWN * 3 + LEFT * 1)
        data3, box_data3 = self._node("d3", DOWN * 3 + RIGHT * 1)
        data4, box_data4 = self._node("d4", DOWN * 3 + RIGHT * 3)

        hash_data1, box_hash_data1 = self._node("h(d1)", DOWN * 1 + LEFT * 3)
        hash_data2, box_hash_data2 = self._node("h(d2)", DOWN * 1 + LEFT * 1)
        hash_data3, box_hash_data3 = self._node("h(d3)", DOWN * 1 + RIGHT * 1)
        hash_data4, box_hash_data4 = self._node("h(d4)", DOWN * 1 + RIGHT * 3)

        hash_left, box_hash_left = self._node("h( h(d1) + h(d2) )", UP * 1 + LEFT * 2)
        hash_right, box_hash_right = self._node("h( h(d3) + h(d4) )", UP * 1 + RIGHT * 2)

        hash_root, box_hash_root = self._node("h( h( h(d1) + h(d2) ) + h( h(d3) + h(d4) )", UP * 3)

        line1 = self._line_between(data1, hash_data1)
        line2 = self._line_between(data2, hash_data2)
        line3 = self._line_between(data3, hash_data3)
        line4 = self._line_between(data4, hash_data4)

        line5 = self._line_between(hash_data1, hash_left)
        line6 = self._line_between(hash_data2, hash_left)
        line7 = self._line_between(hash_data3, hash_right)
        line8 = self._line_between(hash_data4, hash_right)

        line9 = self._line_between(hash_left, hash_root)
        line10 = self._line_between(hash_right, hash_root)

        self.play(Create(box_data1), Create(box_data2), Create(box_data3), Create(box_data4))
        self.play(Write(data1), Write(data2), Write(data3), Write(data4))
        self.wait(1)

        self.play(Create(line1), Create(line2), Create(line3), Create(line4), Create(box_hash_data1), Create(box_hash_data2), Create(box_hash_data3), Create(box_hash_data4))
        self.play(Write(hash_data1), Write(hash_data2), Write(hash_data3), Write(hash_data4))
        self.wait(3)

        self.play(Create(line5), Create(line6), Create(line7), Create(line8), Create(box_hash_left), Create(box_hash_right))
        self.play(Write(hash_left), Write(hash_right))
        self.wait(5)

        self.play(Create(line9), Create(line10), Create(box_hash_root))
        self.play(Write(hash_root))
        self.wait(5)

    def _node(self, text, position):
        data = Text(text).scale(0.6).shift(position)
        box = BackgroundRectangle(data, color=BLUE_D, buff=0.2, fill_opacity=1)
        data.set_z_index(2)
        box.set_z_index(1)
        return data, box

    def _line_between(self, starting_element, ending_element):
        return Line(starting_element.get_center(), ending_element.get_center(), color=WHITE)
