from manim import *

class MeanValueTheorem(Scene):
    def construct(s):

        text1 = Text("The Mean Value Theorem", color=YELLOW, font="Montserrat").shift(RIGHT*3,UP*3).scale(0.7)
        text2 = MathTex(r"\text{If a function }",  "f", r"\text{ is continuous on the closed interval}").shift(RIGHT*3,UP*2).scale(0.6)
        text3 = MathTex("[a,b],", r"\text{ there exists a number }", "c" r"\text{ in }", "[a,b]", r"\text{ such that}").next_to(text2,DOWN).scale(0.6)
        formula = MathTex(r"\int_a^b f(x) dx", "=", "f(c)(b-a)").shift(RIGHT*3)
        s.play(FadeIn(text1))
        s.play(Create(text2))
        s.play(Create(text3))
        s.play(Create(formula))
        s.wait(1)

        ax = Axes(
            x_range = [0, 6, 10],
            y_range = [0, 6, 10],
            x_length = 5,
            y_length = 5,
            axis_config={
                #"numbers_to_include":[1,3,5],
                "color": GREEN},
                tips=True
        ).shift(LEFT*3,UP)

        s.play(Create(ax))

        a = 1
        b = 4.5
        c = 2.69
        x_at_max=1.46
        x_at_min=3.87

        def func(x):
            return ((x-1)*(x-2)*(x-5))/5 + 4

        curve = ax.get_graph(func, x_range=[-0.2,4.8], color=RED)
        curve_label = ax.get_graph_label(curve, label="y=f(x)",x_val=2.5).scale(0.85).shift(UP)
        s.play(Create(curve))
        s.add(curve_label)
        s.wait(1)

        drop = ax.get_vertical_lines_to_graph(curve, x_range=[a,b], num_lines=2, stroke_width=3, color=YELLOW)
        label_a = Tex("$a$").scale(0.7).next_to(Dot().move_to(ax.c2p(a,0)),DOWN)
        label_b = Tex("$b$").scale(0.7).next_to(Dot().move_to(ax.c2p(b,0)),DOWN)
        s.play(Create(VGroup(drop,label_a,label_b)))
        s.wait(1)

        f0 = MathTex(r"\int_a^b f(x) dx", "=", "f(c)(b-a)").shift(RIGHT*3)
        s.add(f0)
        s.play(ApplyMethod(f0.shift,DOWN*2))
        f1 = MathTex(r"\int_a^b f(x) dx", "=", "f(c)(b-a)").shift(RIGHT*3,DOWN*2)
        f1[0].set_color(RED)
        f1[1].set_color(BLACK)
        f1[2].set_color(BLACK)
        s.play(ReplacementTransform(f0,f1))

        area = ax.get_area(curve, x_range=[a,b], dx_scaling=0.2, color='#ab4f5c')
        s.play(FadeIn(area))
        s.wait(1)

        p = ValueTracker(x_at_max)

        drop_c  = ax.get_T_label(p.get_value(),curve,label=MathTex(r"x_{\text{M}}").scale(0.65),triangle_size=0.15, line_color=BLACK, line_func=DashedLine)
        s.play(Create(drop_c))
        s.wait(1)

        moving_dot = Dot().move_to(ax.coords_to_point(p.get_value(), func(p.get_value())))
        s.add(moving_dot)

        rectbox = ax.get_graph(
            lambda x: func(p.get_value()),
            #lambda x: 2,
            color = BLUE,
            x_range=[a,b]
        )
        s.play(FadeIn(rectbox))

        rectarea = ax.get_riemann_rectangles(rectbox, x_range=[a,b-a], dx=b-a, fill_opacity=0.4, color=YELLOW)
        s.play(FadeIn(rectarea))

        f2 = MathTex(r"\int_a^b f(x) dx", "<", r"f(x_{\text{M}})(b-a)").shift(RIGHT*3,DOWN*2)
        f2[0].set_color(RED)
        f2[1].set_color(BLUE)
        f2[2].set_color(YELLOW)
        s.play(ReplacementTransform(f1,f2))
        s.wait(1)
        f1 = MathTex(r"\int_a^b f(x) dx", "<", r"f(x_{\text{M}})(b-a)").shift(RIGHT*3,DOWN*2)
        f1[0].set_color(RED)
        f1[1].set_color(BLACK)
        f1[2].set_color(BLACK)
        s.play(ReplacementTransform(f2,f1))
        s.wait(1)

        moving_dot.add_updater(
            lambda m: m.become(
                moving_dot.move_to(ax.coords_to_point(p.get_value(), func(p.get_value())))
                )
            )

        rectbox.add_updater(
            lambda m: m.become(
                ax.get_graph(
                    lambda x: func(p.get_value()),
                    #lambda x: 2,
                    color = BLUE,
                    x_range=[a,b]
                    )
                )
            )

        rectarea.add_updater(lambda m: m.become(ax.get_riemann_rectangles(rectbox, x_range=[a,b-a], dx=b-a, fill_opacity=0.4, color=YELLOW)))

        drop_c.add_updater(lambda m: m.become(ax.get_T_label(p.get_value(),curve, triangle_size=0.15, line_color=BLACK, line_func=DashedLine)))

        #

        s.play(
            ApplyMethod(p.increment_value,x_at_min-x_at_max),
            run_time=3
        )

        drop_c  = ax.get_T_label(p.get_value(),curve,label=MathTex(r"x_{\text{m}}").scale(0.65),triangle_size=0.15, line_color=BLACK, line_func=DashedLine)
        s.add(drop_c)
        s.wait(1)

        f2 = MathTex(r"\int_a^b f(x) dx", ">", r"f(x_{\text{m}})(b-a)").shift(RIGHT*3,DOWN*2)
        f2[0].set_color(RED)
        f2[1].set_color(BLUE)
        f2[2].set_color(YELLOW)
        s.play(ReplacementTransform(f1,f2))
        s.wait(1)
        f1 = MathTex(r"\int_a^b f(x) dx", ">", r"f(x_{\text{m}})(b-a)").shift(RIGHT*3,DOWN*2)
        f1[0].set_color(RED)
        f1[1].set_color(BLACK)
        f1[2].set_color(BLACK)
        s.play(ReplacementTransform(f2,f1))
        s.wait(1)
        s.remove(drop_c)

        s.play(
            ApplyMethod(p.increment_value,c-x_at_min),
            run_time=3
        )

        drop_c  = ax.get_T_label(p.get_value(),curve,label=MathTex("c").scale(0.65),triangle_size=0.15, line_color=BLACK, line_func=DashedLine)
        s.add(drop_c)

        f2 = MathTex(r"\int_a^b f(x) dx", "=", r"f(c)(b-a)").shift(RIGHT*3,DOWN*2)
        f2[0].set_color(RED)
        f2[1].set_color(BLUE)
        f2[2].set_color(YELLOW)
        s.play(ReplacementTransform(f1,f2))
        s.wait(1)

        s.play(ApplyMethod(f2.shift,UP*2),FadeOut(formula))

        s.wait(1)
