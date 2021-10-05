from manim import *
import scipy.integrate as  integrate

class AreaVerticalRects(Scene):
    def construct(s):

        t1 = Text("Area Between Curves", color=YELLOW, font="Montserrat").shift(UP*3).scale(0.8)

        s.play(Create(t1))
        s.wait(1)
#        s.add(t1)

        ax1 = Axes(
            x_range = [-3, 6, 10],
            y_range = [-4, 5, 10],
            x_length = 8,
            y_length = 4,
            axis_config={
                "color": GREEN},
                tips=False
        )#.shift(LEFT*3)
        ax1_label = ax1.get_axis_labels(x_label="x", y_label="y")
        s.play(Create(ax1))
        s.add(ax1_label)
        s.wait(1)

        curve1 = ax1.get_graph(lambda x: 0.05*x*(x-2)*(x-7) +4, x_range=[-2.5,5.7],color=BLUE)
        c1_label = ax1.get_graph_label(curve1, label="f(x)",x_val=5.5).scale(0.6)
        curve2 = ax1.get_graph(lambda x: 0.4*(x+1)*(x-4), x_range=[-2.5,5.7],color=RED)
        c2_label = ax1.get_graph_label(curve2, label="g(x)",x_val=5.7).scale(0.6)

        s.play(Create(curve1),Create(curve2))
        s.add(c1_label,c2_label)
        s.wait(1)

        lines1 = ax1.get_vertical_lines_to_graph(curve1, x_range=[0.5,3.5], num_lines=2,color=BLUE)
        lines2 = ax1.get_vertical_lines_to_graph(curve2, x_range=[0.5,3.5], num_lines=2,color=BLUE)
        a_label = MathTex("a").next_to(Dot().move_to(ax1.coords_to_point(-0.2, 0.4))).scale(0.5)
        b_label = MathTex("b").next_to(Dot().move_to(ax1.coords_to_point(3.2, 0.4))).scale(0.5)


        s.play(Create(lines1),Create(lines2))
        s.add(a_label,b_label)
        s.wait(1)

        area1 = ax1.get_area(curve1,x_range=[0.5,3.5], dx_scaling=0.5, color=GREEN)
        area2 = ax1.get_area(curve2,x_range=[0.5,3.5], dx_scaling=0.5, color=GREEN)
        s.mobjects = [curve1,curve2,area1,area2] + s.mobjects
        s.play(FadeIn(area1),FadeIn(area2))
        s.wait(1)
        s.play(FadeOut(area1),FadeOut(area2))
        s.wait(1)

        rect = ax1.get_riemann_rectangles(curve1, bounded_graph=curve2, dx=0.5, x_range=[1,1.5], color=PURPLE, input_sample_type="center")
        s.mobjects = [curve1,curve2,ax1,rect] + s.mobjects
        s.play(Create(rect))
        s.wait(1)

        pointF = Dot().move_to(ax1.coords_to_point(1.25, 4.27)).scale(0.75)
        pointG = Dot().move_to(ax1.coords_to_point(1.25, -2.475)).scale(0.75)
        s.add(pointF, pointG)

        xtag1 = ax1.get_T_label(1.25,curve1,triangle_size=0, line_color=WHITE)
        xtag2 = ax1.get_T_label(1.25,curve2,triangle_size=0, line_color=WHITE)
        s.play(Create(xtag1),Create(xtag2))

        x_label = MathTex("x_i").next_to(Dot().move_to(ax1.coords_to_point(0.9, -0.5))).scale(0.7)
        f_label = MathTex("(x_i,f(x_i))").next_to(Dot().move_to(ax1.coords_to_point(0.7, 5))).scale(0.6)
        g_label = MathTex("(x_i,g(x_i))").next_to(Dot().move_to(ax1.coords_to_point(0.7, -3))).scale(0.6)
        s.add(x_label)
        s.wait(1)
        s.play(FadeIn(f_label),FadeIn(g_label))
        s.wait(1)

        t1 = MathTex("A_i", "=", " ", " ", r"\left[f\left(x_i\right) - g\left(x_i\right)\right]", "\cdot", r"\left({b-a \over n}\right)").scale(0.8).shift(DOWN*3)
        s.play(FadeIn(t1))
        s.wait(1)

        s.play(FadeOut(x_label, f_label, g_label, rect, xtag1, xtag2, pointF, pointG))
        s.wait(1)

        area = ax1.get_riemann_rectangles(curve1, bounded_graph=curve2, dx=0.25, x_range=[0.5,3.5], color=(RED_A, BLUE_B, PURPLE_D), input_sample_type="center")
        s.mobjects = [curve1,curve2,ax1,area] + s.mobjects
        s.play(Create(area))
        s.wait(1)

        t2 = MathTex("A", r"\approx", " ", "\sum_{i=1}^n", r"\left[f\left(x_i\right) - g\left(x_i\right)\right]", "\cdot", "\Delta x").scale(0.8).shift(DOWN*3)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)

        s.play(FadeOut(area))
        #area = ax1.get_riemann_rectangles(curve1, bounded_graph=curve2, dx=0.05, x_range=[0.5,3.5], color=(RED_A, BLUE_B, PURPLE_D), input_sample_type="center")
        area = ax1.get_area(curve1,x_range=[0.5,3.5], dx_scaling=0.5, color=(RED_A, BLUE_B, PURPLE_D))
        area2 = ax1.get_area(curve2,x_range=[0.5,3.5], dx_scaling=0.5, color=(RED_A, BLUE_B, PURPLE_D))
        s.mobjects = [curve1,curve2,ax1,area] + s.mobjects
        s.play(Create(area),Create(area2))
        s.wait(1)

        t1 = MathTex("A", "=", r"\lim_{n\to\infty}", "\sum_{i=1}^n", r"\left[f\left(x_i\right) - g\left(x_i\right)\right]", "\cdot", "\Delta x").scale(0.8).shift(DOWN*3)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)

        t2 = MathTex("A", "=", " ", "\int_a^b", r"\left[f\left(x\right) - g\left(x\right)\right]", "\,", "dx").scale(0.8).shift(DOWN*3)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)

        s.wait(2)
