from manim import *
import scipy.integrate as  integrate

class FTC1(Scene):
    def construct(s):

        text1 = Text("The Fundamental Theorem of Calculus (1)", color=YELLOW, font="Montserrat").shift(UP*3).scale(0.8)
        text2 = MathTex(r"\text{If a }",  r"\text{function }",  "f", r"\text{ is continuous}", r"\text{ on the }", r"\text{closed interval }","[a,b],", r"\text{then}").shift(UP*2).scale(0.65)
        #text3 = MathTex(r"\text{closed interval }","[a,b],", r"\text{then}").next_to(text2,DOWN).scale(0.5)
        formula = MathTex("{d \over dx}",r"\int_a", "^x", "f(t)", "dt", "=", "f(x)").next_to(text2,DOWN).scale(0.75)
        text4 =  MathTex("a \leq x  \leq  b").next_to(formula,DOWN).scale(0.65)
        s.play(FadeIn(text1))
        s.play(Create(text2))
        #s.play(Create(text3))
        s.play(Create(formula))
        s.play(Create(text4))
        s.wait(1)

        ax = Axes(
            x_range = [0, 6, 10],
            y_range = [0, 6, 10],
            x_length = 3,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[1,3,5],
                "color": GREEN},
                tips=True
        ).next_to(text4, DOWN)
        ax_label = ax.get_axis_labels(x_label="t", y_label="").scale(0.6)

        s.play(Create(ax), Create(ax_label))
        s.wait(1)

        a = 1
        b = 4.5
        c = 2 #starting value for ValueTracker
        p = ValueTracker(c)

        def func(x):
            return 2.5 - (x / 2) * np.sin(x)

        for i in [1, 2, 3]:
            text2[i].set_color(RED)
        s.wait(1)

        curve = ax.get_graph(func, x_range=[-0.2,5.8], color=RED)
        curve_label = ax.get_graph_label(curve, label="y=f(t)",x_val=2).scale(0.6).shift(UP,LEFT)
        s.play(Create(curve))
        s.add(curve_label)
        s.wait(1)

        for i in [5, 6]:
            text2[i].set_color(BLUE)
        s.wait(1)

        drop = ax.get_vertical_lines_to_graph(curve, x_range=[a,b], num_lines=2, stroke_width=3, color=BLUE)
        label_a = Tex("$a$").scale(0.6).next_to(Dot().move_to(ax.c2p(a,0)),DOWN).set_color(BLUE)
        label_b = Tex("$b$").scale(0.6).next_to(Dot().move_to(ax.c2p(b,0)),DOWN).set_color(BLUE)
        s.play(Create(VGroup(drop,label_a,label_b)))
        s.wait(1)

        text4.set_color(ORANGE)
        s.wait(1)

        x_val  = ax.get_T_label(p.get_value(),curve,label=MathTex("x", color=ORANGE).scale(0.6),triangle_size=0.15, line_color=ORANGE, line_func=DashedLine)
        s.play(Create(x_val))
        s.wait(1)

        for i in [1, 2, 3, 4]:
            formula[i].set_color(YELLOW)
        s.wait(1)

        area = ax.get_area(curve, x_range=[a,p.get_value()], dx_scaling=0.2, color=YELLOW)
        s.play(FadeIn(area))
        s.wait(1)

        area.add_updater(lambda m: m.become(ax.get_area(curve, x_range=[a,p.get_value()], dx_scaling=0.5, color=YELLOW)))
        x_val.add_updater(lambda m: m.become(ax.get_T_label(p.get_value(),curve,label=MathTex("x", color=ORANGE).scale(0.6),triangle_size=0.15, line_color=ORANGE, line_func=DashedLine)))

        ax2 = Axes(
            x_range = [0, 6, 10],
            y_range = [0, 20, 5],
            x_length = 3,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[1,3,5],
                "color": GREEN},
                tips=True
        ).next_to(ax, RIGHT*2)
        ax2_label = ax2.get_axis_labels(x_label="x",y_label="").scale(0.6)

        s.play(Create(ax2),Create(ax2_label))
        s.wait(1)

        curve3 = DashedVMobject(ax2.get_graph(lambda x: 2.5*x - 0.5*np.sin(x) + 0.5*x*np.cos(x) + 1.78,x_range=[0.1,5.2], color="#5c5e0c"))
        s.play(FadeIn(curve3))


        curve2 = ax2.get_graph(lambda x: 2.5*x - 0.5*np.sin(x) + 0.5*x*np.cos(x) + 1.78,x_range=[2,p.get_value()], color=YELLOW)
        s.add(curve2)
        curve2.add_updater(lambda m: m.become(ax2.get_graph(lambda x: 2.5*x - 0.5*np.sin(x) + 0.5*x*np.cos(x) + 1.78,x_range=[2,p.get_value()], color=YELLOW, stroke_width=5)))

        s.play(
            ApplyMethod(p.increment_value,2),
            run_time=3
        )


        s.wait(1)

class FTC1Proof(Scene):
    def construct(s):

        text1 = Text("Proof of The Fundamental Theorem of Calculus (1)", color=YELLOW, font="Montserrat").shift(UP*3).scale(0.7)
        text2 = MathTex(r"\text{If a }",  r"\text{function }",  "f", r"\text{ is continuous}", r"\text{ on the }", r"\text{closed interval }","[a,b],", r"\text{then }", "{d \over dx}",r"\int_a", "^x", "f(t)", "\,dt", "=", "f(x)", r"\text{ for }", "a  \leq x \leq b").shift(UP*2).scale(0.6).set_color(PURPLE)

        s.play(FadeIn(text1))
        s.play(Create(text2))
        s.wait(1)

        t0 = MathTex(r"\text{Let }", "F(x)", "=", "\int_a^x", "f(t)\,dt", ", \, a \leq x \leq b").scale(0.7).shift(RIGHT*2,UP)
        s.play(Create(t0))
        s.wait(1)

        ax = Axes(
            x_range = [0, 6, 10],
            y_range = [0, 6, 10],
            x_length = 3,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[1,3,5],
                "color": GREEN},
                tips=True
        ).next_to(text2, DOWN).shift(LEFT*4)
        ax_label = ax.get_axis_labels(x_label="t", y_label="").scale(0.6)



        a = 1
        b = 4.5
        x = 2.5
        dx = 1

        def func(x):
            return 2.5 - (x / 2) * np.sin(x)

        s.play(Create(ax), Create(ax_label))

        curve = ax.get_graph(func, x_range=[-0.2,5.8], color=RED)
        curve_label = ax.get_graph_label(curve, label="y=f(t)",x_val=2).scale(0.6).shift(UP,LEFT)
        s.play(Create(curve))
        s.add(curve_label)
        drop = ax.get_vertical_lines_to_graph(curve, x_range=[a,b], num_lines=2, stroke_width=3, color=YELLOW)
        label_a = Tex("$a$").scale(0.6).next_to(Dot().move_to(ax.c2p(a,0)),DOWN)
        label_b = Tex("$b$").scale(0.6).next_to(Dot().move_to(ax.c2p(b,0)),DOWN)
        s.play(Create(VGroup(drop,label_a,label_b)))
        x_val  = ax.get_T_label(x,curve,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE, line_func=DashedLine)
        s.play(Create(x_val))
        area1 = ax.get_area(curve,x_range=[a,x], dx_scaling=0.5, color="#32a852")
        s.play(FadeIn(area1))
        s.wait(1)
        s.play(FadeOut(area1), FadeOut(x_val))

        t2 = MathTex("{d \over dx}", "F(x)", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ").scale(0.7).next_to(t0,DOWN)
        s.play(Create(t2))
        s.wait(1)

        t1 = MathTex("{d \over dx}", "F(x)", "=", r"\displaystyle\lim_{\Delta x \to 0}", " ", " ", "{", "F(x + \Delta x )", " ", "-", "F(x)", " ", "\over", "\Delta x", "}", " ").scale(0.7).next_to(t0,DOWN)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)

        t2 = MathTex("{d \over dx}", "F(x)", "=", r"\displaystyle\lim_{\Delta x \to 0}", "\, {1 \over \Delta x}", "\left(", " ", "F(x + \Delta x )", " ", "-", "F(x)", " ", " ", " ", " ", r"\right)").scale(0.7).next_to(t0,DOWN)
        s.play(ReplacementTransform(t1,t2))
        t2[7].set_color(BLUE)
        s.wait(1)

        t1 = MathTex("{d \over dx}", "F(x)", "=", r"\displaystyle\lim_{\Delta x \to 0}", "\, {1 \over \Delta x}", "\left(", "\displaystyle\int_a^{x + \Delta x} f(t) \, dt", " ", " ", "-", "F(x)", " ", " ", " ", " ", r"\right)").scale(0.7).next_to(t0,DOWN)
        s.play(ReplacementTransform(t2,t1))
        s.wait(0.5)
        t1[10].set_color(GREEN)
        s.wait(1)

        t2 = MathTex("{d \over dx}", "F(x)", "=", r"\displaystyle\lim_{\Delta x \to 0}", "\, {1 \over \Delta x}", "\left(", "\displaystyle\int_a^{x + \Delta x} f(t) \, dt", " ", " ", "-", " ", "\displaystyle\int_a^x f(t) \, dt", " ", " ", " ", r"\right)").scale(0.7).next_to(t0,DOWN)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)
        t2[6].set_color(BLUE)
        s.wait(0.5)

        xdx_val  = ax.get_T_label(x +  dx,curve,label=MathTex("x+\Delta x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE, line_func=DashedLine)
        area2 = ax.get_area(curve,x_range=[a,x+dx], dx_scaling=0.5, color="#325ea8")
        s.play(Create(xdx_val),Create(area2))
        s.wait(1)

        t2[11].set_color(GREEN)
        s.wait(0.5)
        s.play(Create(x_val))
        area3 = ax.get_area(curve,x_range=[a,x], dx_scaling=0.5, color="#32a852")
        s.play(Create(area3))
        s.wait(1)

        area4 = ax.get_area(curve,x_range=[x,x+dx], dx_scaling=0.5, color="#325ea8")
        s.add(area4)
        s.play(FadeOut(area2),FadeOut(area3))
        s.wait(1)

        t1 = MathTex("{d \over dx}", "F(x)", "=", r"\displaystyle\lim_{\Delta x \to 0}", "\, {1 \over \Delta x}", "\,", "\displaystyle\int_x^{x + \Delta x} f(t) \, dt", " ", " ", " ", " ", " ", " ", " ", " ", " ").scale(0.7).next_to(t0,DOWN)
        t1[6].set_color(BLUE)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)

        recalltext =  MathTex(r"\text{Recall MVT: }", "\exists \,c \in [x, x+ \Delta x]", r"\text{ s.t. }", "\,f(c)\Delta x = \displaystyle\int_x^{x+\Delta x} f(t) \, dt").scale(0.6).next_to(t1,DOWN)
        recalltext[0].set_color(YELLOW)
        s.play(Create(recalltext))
        s.wait(1)

        c_val  = ax.get_T_label(x+0.5,curve,label=MathTex("c").scale(0.4),triangle_size=0.15, line_color=ORANGE, line_func=DashedLine)
        s.play(Create(c_val))
        s.wait(1)
        rectarea = ax.get_riemann_rectangles(curve, x_range=[x,x+0.5], dx=1, fill_opacity=0.3, color=YELLOW, input_sample_type='center')
        s.play(FadeIn(rectarea))
        s.wait(1)

        t2 = MathTex("{d \over dx}", "F(x)", "=", r"\displaystyle\lim_{\Delta x \to 0}", "\, {1 \over \Delta x}", "\,", " ", "f(c) \,", "\Delta x", " ", " ", " ", " ", " ", " ", " ").scale(0.7).next_to(t0,DOWN)
        t2[7].set_color(BLUE)
        t2[8].set_color(BLUE)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)

        s.play(FadeOut(rectarea),FadeOut(recalltext))

        t2[4].set_color(YELLOW)
        t2[8].set_color(YELLOW)
        t2[7].set_color(WHITE)
        s.wait(1)

        t1 = MathTex("{d \over dx}", "F(x)", "=", r"\displaystyle\lim_{\Delta x \to 0}", " ", "\,", " ", "f(c) \,", " ", " ", " ", " ", " ", " ", " ", " ").scale(0.7).next_to(t0,DOWN)
        t1[3].set_color(YELLOW)
        s.play(ReplacementTransform(t2,t1),FadeOut(area4))
        s.wait(1)


        p = ValueTracker(dx)

        xdx_val.add_updater( lambda m: m.become(ax.get_T_label(x+p.get_value(),curve,label=MathTex("x+\Delta x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE, line_func=DashedLine)))
        c_val.add_updater(lambda m: m.become(ax.get_T_label(x+0.5*p.get_value(),curve,label=MathTex("c").scale(0.4),triangle_size=0.15, line_color=WHITE)))
        move_c = Dot().move_to(ax.coords_to_point(x+0.5*p.get_value(), func(x+0.5*p.get_value() )))
        move_c.add_updater(lambda m: m.become(Dot().move_to(ax.coords_to_point(x+0.5*p.get_value(), func(x+0.5*p.get_value())))))
        s.add(move_c)

        s.play(
            ApplyMethod(p.increment_value,-1),
            run_time=5
        )
        s.remove(x_val)
        x_val  = ax.get_T_label(x,curve,label=MathTex("x", color=WHITE).scale(0.6),triangle_size=0.15)
        s.add(x_val)
        s.play(FadeOut(c_val),FadeOut(xdx_val))
        s.wait(1)

        t2 = MathTex("{d \over dx}", "F(x)", "=", " ", " ", "\,", "f(x)", " ", " ", " ", " ", " ", " ", " ", " ", " ").scale(0.7).next_to(t0,DOWN)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)

        t1 = MathTex("{d \over dx}", "F(x)", "=", " ", " ", "\,", "f(x)", " ", " ", " ", " ", " ", " ", " ", " ", " ").next_to(t0,DOWN).set_color(YELLOW)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)

        t2 = MathTex("{d \over dx}", " ", " ", "\displaystyle\int_a^x \, f(t)\, dt", "=", "\,", "f(x)", " ", " ", " ", " ", " ", " ", " ", " ", " ").next_to(t0,DOWN).set_color(YELLOW)
        s.play(ReplacementTransform(t1,t2))

        s.wait(1)
