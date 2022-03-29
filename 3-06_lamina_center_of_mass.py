from re import L
from manim import *

class ThreeDSurfacePlot(ThreeDScene):
    def construct(s):
        resolution_fa = 42
        s.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        ax = ThreeDAxes()
        flat = Surface(
            lambda u, v: ax.c2p(
                u, v, 0
            ),
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        sphere1 = Surface(
            lambda u, v: ax.c2p(
                0.4*np.cos(u)*np.sin(v)+1,
                0.4*np.sin(u)*np.sin(v)+2,
                0.4*np.cos(v)+0.4
            ),
            u_range = [0, 360*DEGREES],
            v_range = [0, 180*DEGREES],
            checkerboard_colors = [RED_C, RED_E],
        )

        sphere2 = Surface(
            lambda u, v: ax.c2p(
                0.3*np.cos(u)*np.sin(v)+2,
                0.3*np.sin(u)*np.sin(v)-1,
                0.3*np.cos(v)+0.3
            ),
            u_range = [0, 360*DEGREES],
            v_range = [0, 180*DEGREES],
            checkerboard_colors = [GREEN_C, GREEN_E],
        )

        sphere3 = Surface(
            lambda u, v: ax.c2p(
                0.2*np.cos(u)*np.sin(v)-3,
                0.2*np.sin(u)*np.sin(v)+1,
                0.2*np.cos(v)+0.2
            ),
            u_range = [0, 360*DEGREES],
            v_range = [0, 180*DEGREES],
            checkerboard_colors = [BLUE_C, BLUE_E],
        )

        flat.scale(2, about_point=ORIGIN)
        flat.set_style(fill_opacity=1,stroke_color=BLUE_E)
        flat.set_fill_by_checkerboard(GRAY_E, GRAY_E,opacity=0.5)

        s.add(ax)
        s.play(Create(flat))
        s.wait(2)
        s.play(Create(VGroup(sphere1, sphere2, sphere3)))

        s.begin_ambient_camera_rotation(rate=0.1)
        s.wait(7)

class Discrete2D(Scene):
    def construct(s):
        numberplane = NumberPlane(x_range=[-4.05,4.05,1], y_range=[-4,4,1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 0.8,
                "stroke_opacity": 0.7
            }
        )
        dot8 = Dot([1,2,0],color=RED).scale(2)
        dot3 = Dot([2,-1,0], color=GREEN).scale(1.5)
        dot2 = Dot([-3,1,0],color=BLUE)
        dot8_l = Text('8kg').next_to(dot8,RIGHT)
        dot3_l = Text('3kg').next_to(dot3,DOWN)
        dot2_l = Text('2kg').next_to(dot2,LEFT)

        s.add(numberplane)
        s.add(dot8, dot3, dot2)
        s.add(dot8_l, dot3_l, dot2_l)

        d8_x = Line(dot8.get_center(), [1,0,0], color=RED)
        d3_x = Line(dot3.get_center(), [2,0,0], color=GREEN)
        d2_x = Line(dot2.get_center(), [-3,0,0], color=BLUE)

        d8_y = Line(dot8.get_center(), [0,2,0], color=RED)
        d3_y = Line(dot3.get_center(), [0,-1,0], color=GREEN)
        d2_y = Line(dot2.get_center(), [0,1,0], color=BLUE)

        c_mass = Dot([8/13, 15/13, 0])
        c_label = MathTex(r"(\overline{x},\overline{y})").next_to(c_mass, RIGHT)
        s.play(Create(VGroup(d8_x, d3_x, d2_x)))
        s.wait(3)
        s.play(FadeOut(VGroup(d8_x, d3_x, d2_x)))
        s.wait(3)
        s.play(Create(VGroup(d8_y, d3_y, d2_y)))
        s.wait(3)
        s.play(FadeOut(VGroup(d8_y, d3_y, d2_y)))
        s.wait(3)
        s.play(FadeIn(c_mass), Create(c_label))
        s.wait(3)


class Lamina(Scene):
    def construct(s):

        ax = Axes(
            x_range=[-1,12,1],
            x_length=13,
            y_range=[-1,10,2],
            y_length=11/2
        )

        def f1(x):
            return (x / 4) * np.sin(x) + 7

        def f2(x):
            return (x + 2) ** (1/2)

        upper_f = ax.plot(f1, x_range = [-1,12], color = BLUE)
        lower_f = ax.plot(f2, x_range = [-1,12], color = GREEN)

        f1_label=ax.get_graph_label(upper_f, label = 'f(x)',x_val=1, direction=UP)
        f2_label=ax.get_graph_label(lower_f, label = 'g(x)',x_val=1, direction = UP)

        area = ax.get_area(upper_f, bounded_graph=lower_f, x_range=[2,10],color=(RED_B,RED_D))

        rect_area = ax.get_riemann_rectangles(
            upper_f, bounded_graph=lower_f,
            x_range=[5.75,6.25],dx=0.501,
            input_sample_type='center',
            color=YELLOW,fill_opacity=0.5
            )

        centroid_x = 6
        centroid_y = (f1(centroid_x) - f2(centroid_x)) / 2 + f2(centroid_x)
        pt = ax.c2p(centroid_x, centroid_y)
        centroid = Dot(pt)
        centroid_label = MathTex("(x_i,y_i)").next_to(centroid, RIGHT)
        dx_label = MathTex(r"\Delta x").next_to(Dot(ax.c2p(centroid_x,f1(centroid_x))), UP)
        pt_top = Dot(ax.c2p(centroid_x, f1(centroid_x)))
        pt_down = Dot(ax.c2p(centroid_x, f2(centroid_x)))
        pt_top_label = MathTex(r"(x_i,f(x_i))").next_to(pt_top, LEFT)
        pt_down_label = MathTex(r"(x_i,g(x_i))").next_to(pt_down, LEFT)
        x_label = MathTex("x_i").next_to(Dot(ax.c2p(centroid_x,0)),DOWN)
        y_label = MathTex("y_i").next_to(Dot(ax.c2p(0,4.705)),LEFT)
        a_line = ax.get_vertical_lines_to_graph(upper_f, x_range=[2,10], num_lines=2)
        a_label = MathTex("a").next_to(Dot(ax.c2p(2,0)),DOWN)
        b_label = MathTex("b").next_to(Dot(ax.c2p(10,0)),DOWN)
        #a_line = ax.get_vertical_line(Dot(ax.c2p(2, f1(2))))
        #b_line = ax.get_vertical_line(Dot(ax.c2p(10, f1(10))))

        coord_lines = ax.get_lines_to_point(pt)

        s.add(ax)
        s.play(Create(VGroup(upper_f, lower_f)))
        s.play(FadeIn(VGroup(f1_label, f2_label)))
        s.wait(3)
        s.add(a_label,b_label)
        s.play(Create(a_line))
        s.wait(1)
        s.play(FadeIn(area))
        s.wait(3)
        s.play(FadeIn(rect_area))
        s.wait(1)
        s.play(Create(VGroup(pt_top,pt_down, pt_top_label, pt_down_label)))
        s.wait(3)
        s.play(FadeIn(dx_label))
        s.wait(3)
        s.play(FadeIn(centroid), FadeIn(coord_lines))
        s.play(Create(VGroup(x_label, y_label)))
        s.wait(1)
        s.play(Create(centroid_label))
        s.wait(3)
