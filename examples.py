from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(circle), Create(square))


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square, circle))
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(LEFT * 2.)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(RIGHT * 2.)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()
