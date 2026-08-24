from manim import *
import numpy as np


# The scene is designed for a YouTube Short. The render script also passes the
# pixel resolution explicitly so the output stays vertical if Manim defaults change.
config.frame_width = 9
config.frame_height = 16
config.background_color = "#F3EBDD"


class ByrneIII31(Scene):
    """Euclid III.31: an angle subtended by a diameter stays right."""

    def construct(self):
        ink = "#171717"
        red = "#D64035"
        blue = "#2457A6"
        yellow = "#E6A817"
        paper = "#F3EBDD"

        center = np.array([0.0, 0.65, 0.0])
        radius = 3.15
        left = center + radius * LEFT
        right = center + radius * RIGHT
        theta = ValueTracker(145 * DEGREES)

        def moving_point():
            t = theta.get_value()
            return center + radius * np.array([np.cos(t), np.sin(t), 0.0])

        def angle_basis():
            a = moving_point()
            toward_left = left - a
            toward_right = right - a
            toward_left /= np.linalg.norm(toward_left)
            toward_right /= np.linalg.norm(toward_right)
            return a, toward_left, toward_right

        title = Text("Byrne III.31", font_size=52, color=ink).move_to([0, 6.75, 0])
        statement = Text("angle in a semicircle", font_size=34, color=ink).move_to([0, 5.85, 0])

        circle = Circle(radius=radius, color=ink, stroke_width=5).move_to(center)
        diameter = Line(left, right, color=ink, stroke_width=8)

        left_dot = Dot(left, radius=0.085, color=ink)
        right_dot = Dot(right, radius=0.085, color=ink)
        moving_dot = Dot(moving_point(), radius=0.12, color=yellow)
        moving_dot.set_stroke(ink, width=2)
        moving_dot.add_updater(lambda m: m.move_to(moving_point()))

        left_leg = Line(moving_point(), left, color=red, stroke_width=10)
        left_leg.add_updater(lambda m: m.put_start_and_end_on(moving_point(), left))
        right_leg = Line(moving_point(), right, color=blue, stroke_width=10)
        right_leg.add_updater(lambda m: m.put_start_and_end_on(moving_point(), right))

        marker_size = 0.42
        right_marker = VMobject(color=ink, stroke_width=6)

        def update_right_marker(m):
            a, u, v = angle_basis()
            p1 = a + marker_size * u
            p2 = a + marker_size * (u + v)
            p3 = a + marker_size * v
            m.set_points_as_corners([p1, p2, p3])
            return m

        right_marker.add_updater(update_right_marker)
        update_right_marker(right_marker)

        angle_text = Text("90°", font_size=46, color=ink)

        def update_angle_text(m):
            a, u, v = angle_basis()
            inward = u + v
            inward /= np.linalg.norm(inward)
            return m.move_to(a + 0.95 * inward)

        angle_text.add_updater(update_angle_text)
        update_angle_text(angle_text)

        # A small neutral plate keeps the moving readout legible over either colored leg.
        angle_plate = RoundedRectangle(
            corner_radius=0.12,
            width=1.35,
            height=0.72,
            fill_color=paper,
            fill_opacity=0.92,
            stroke_opacity=0,
        )
        angle_plate.add_updater(lambda m: m.move_to(angle_text.get_center()))

        source = Text(
            "Euclid III.31 · Oliver Byrne, 1847",
            font_size=26,
            color=ink,
        ).move_to([0, -6.95, 0])

        self.add(
            title,
            statement,
            circle,
            diameter,
            left_leg,
            right_leg,
            left_dot,
            right_dot,
            moving_dot,
            angle_plate,
            right_marker,
            angle_text,
            source,
        )

        self.wait(0.4)
        self.play(theta.animate.set_value(35 * DEGREES), run_time=4.8, rate_func=linear)
        self.play(theta.animate.set_value(105 * DEGREES), run_time=2.0, rate_func=linear)
        self.wait(1.6)
