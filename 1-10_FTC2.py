from manim import *
import scipy.integrate as  integrate

class FTC2b(Scene):
    def construct(s):

        t1 = Text("The Fundamental Theorem of Calculus (2)", color=YELLOW, font="Montserrat").shift(UP*3).scale(0.8)
        t2 = MathTex(r"\text{If a }",  r"\text{function }",  "f", r"\text{ is continuous}", r"\text{ on the }", r"\text{closed interval }","[a,b],", r"\text{then}").shift(UP*2).scale(0.65)
        formula = MathTex(r"\int_a", "^b", "f(x)", "dx", "=", "F(b)-F(a)").next_to(t2,DOWN).scale(0.75)
        s.add(t1,formula.shift(UP))

        ax1 = Axes(
            x_range = [-2, 3, 10],
            y_range = [-2, 4, 10],
            x_length = 5.5,
            y_length = 3,
            axis_config={
                "color": GREEN},
                tips=False
        ).shift(LEFT*3+DOWN)
        ax1_label = ax1.get_axis_labels(x_label="t", y_label="y")

        ax2 = Axes(
            x_range = [-2, 3, 10],
            y_range = [-2, 4, 10],
            x_length = 5.5,
            y_length = 3,
            axis_config={
                "color": GREEN},
                tips=False
        ).shift(RIGHT*3+DOWN)
        ax2_label = ax2.get_axis_labels(x_label="x", y_label="y")

        curve1 = ax1.get_graph(lambda x: x**3 - 2*x**2 - x + 2, x_range=[-1.7,2.8],color=BLUE)
        c1_label = ax1.get_graph_label(curve1, label="f(t)",x_val=1.5).scale(0.6).shift(UP,LEFT)
        curve1z = ax1.get_graph(lambda x: (x**3 - 2*x**2 - x + 2)*1.06, x_range=[-1.7,2.8],color=BLUE)
        curve1z2 = ax1.get_graph(lambda x: ((x+0.1)**3 - 2*(x+0.1)**2 - (x+0.1) + 2), x_range=[-1.7,2.8],color=BLUE)
        curve1z3 = ax1.get_graph(lambda x: ((x+0.1)**3 - 2*(x+0.1)**2 - (x+0.1) + 2)*.85, x_range=[-1.7,2.8],color=BLUE)


        curve2b = ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x + 1.6, x_range=[-1.6,2.8],color=BLUE)
        c2b_label = ax2.get_graph_label(curve2b, label="F_2(x)",x_val=2.8).scale(0.6)
        c_limit = ax1.get_T_label(-1,curve1,label=MathTex("c=-1", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)


        s.add(ax1,ax2,ax1_label,ax2_label,curve1,c1_label,curve2b,c2b_label,c_limit)

####### Stage set #######

        t3 = MathTex("F_2(x) = \int_{-1}^x f(t)\, dt").scale(0.6).shift(DOWN*2)
        s.play(FadeIn(t3))
        s.wait(1)

        a_limit = ax1.get_T_label(-0.5,curve1,label=MathTex("a", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)
        b_limit = ax1.get_T_label(0.6,curve1z,label=MathTex("b", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)
        s.play(Create(a_limit),Create(b_limit))
        s.wait(1)

        t4 = MathTex(r" ", r"F_2(b) = ", r"\int_{-1}^b f(t)\, dt", r" ", r" ", r" ").scale(0.6).next_to(t3,DOWN)
        s.play(FadeIn(t4))
        s.wait(1)

        b_area1 = ax1.get_area(curve1z,x_range=[-1,-0.5], dx_scaling=0.5, color=GREEN)
        b_area2 = ax1.get_area(curve1z,x_range=[-0.5,0.6], dx_scaling=0.5, color=GREEN)
        b2_limit = ax2.get_T_label(0.6,curve2b,label=MathTex("b", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)
        s.play(Create(b_area1))
        s.play(Create(b_area2))
        s.play(Create(b2_limit))
        bDot = Dot().move_to(ax2.coords_to_point(0.6,2.5))
        s.add(bDot)
        s.wait(1)

        t5 = MathTex(r" ", r"F_2(b) =", r"\int_{-1}^b f(t)\, dt", r" \, , \,", r"F_2(a)=", r"\int_{-1}^a f(t)\, dt").scale(0.6).next_to(t3,DOWN)
        s.play(ReplacementTransform(t4,t5))

        a_area = ax1.get_area(curve1z,x_range=[-1,-0.5], dx_scaling=0.5, color=RED)
        a2_limit = ax2.get_T_label(-0.5,curve2b,label=MathTex("b", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)
        s.play(Create(a_area))
        s.play(Create(a2_limit))
        aDot = Dot().move_to(ax2.coords_to_point(-0.5,0.4))
        s.add(aDot)
        s.wait(1)

        t4 = MathTex(r"\int_a^b f(t)\, dt =", r" ", r"\int_{-1}^b f(t)\, dt", r"-", r" ", r"\int_{-1}^a f(t)\, dt").scale(0.6).next_to(t3,DOWN)
        s.play(ReplacementTransform(t5,t4))
        s.wait(1)
        s.play(FadeOut(b_area1),FadeOut(a_area))
        s.wait(1)

        t5 = MathTex(r"\int_a^b f(t)\, dt =", r" ", r"F_2(b)", r"-", r" ", r"F_2(a)").scale(0.6).next_to(t3,DOWN)
        s.play(ReplacementTransform(t4,t5))
        s.wait(1)



class FTC2(Scene):
    def construct(s):

        t1 = Text("The Fundamental Theorem of Calculus (2)", color=YELLOW, font="Montserrat").shift(UP*3).scale(0.8)
        t2 = MathTex(r"\text{If a }",  r"\text{function }",  "f", r"\text{ is continuous}", r"\text{ on the }", r"\text{closed interval }","[a,b],", r"\text{then}").shift(UP*2).scale(0.65)
        formula = MathTex(r"\int_a", "^b", "f(x)", "dx", "=", "F(b)-F(a)").next_to(t2,DOWN).scale(0.75)
        t4 =  MathTex(r"\text{where }", "F(x)", r"\text{ is any antiderivative of }", "f(x).").next_to(formula,DOWN).scale(0.65)
        s.play(FadeIn(t1))
        s.play(Create(t2))
        s.play(Create(formula))
        s.play(Create(t4))
        s.wait(1)
        s.play(FadeOut(t2),FadeOut(t4))
        s.play(ApplyMethod(formula.shift,UP))
        s.wait(1)

        ax1 = Axes(
            x_range = [-2, 3, 10],
            y_range = [-2, 4, 10],
            x_length = 5.5,
            y_length = 3,
            axis_config={
                "color": GREEN},
                tips=False
        ).shift(LEFT*3+DOWN)
        ax1_label = ax1.get_axis_labels(x_label="t", y_label="y")

        ax2 = Axes(
            x_range = [-2, 3, 10],
            y_range = [-2, 4, 10],
            x_length = 5.5,
            y_length = 3,
            axis_config={
                "color": GREEN},
                tips=False
        ).shift(RIGHT*3+DOWN)
        ax2_label = ax2.get_axis_labels(x_label="x", y_label="y")

        s.play(Create(ax1), Create(ax1_label))
        s.play(Create(ax2), Create(ax2_label))

        curve1 = ax1.get_graph(lambda x: x**3 - 2*x**2 - x + 2, x_range=[-1.7,2.8],color=BLUE)
        c1_label = ax1.get_graph_label(curve1, label="f(t)",x_val=1.5).scale(0.6).shift(UP,LEFT)
        curve1z = ax1.get_graph(lambda x: (x**3 - 2*x**2 - x + 2)*1.06, x_range=[-1.7,2.8],color=BLUE)
        curve1z2 = ax1.get_graph(lambda x: ((x+0.1)**3 - 2*(x+0.1)**2 - (x+0.1) + 2), x_range=[-1.7,2.8],color=BLUE)
        curve1z3 = ax1.get_graph(lambda x: ((x+0.1)**3 - 2*(x+0.1)**2 - (x+0.1) + 2)*.85, x_range=[-1.7,2.8],color=BLUE)


        #curve2a = ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x, x_range=[-2,3],color=YELLOW)

        #s.play(Create(curve1),Create(curve2a))
        s.play(Create(curve1), FadeIn(c1_label))
        s.wait(1)

        t0 = MathTex("c = 0").shift(DOWN*2).scale(0.7)
        t1 = MathTex("\int","_{c=0}","^x f(t)\, dt = F_1(x)").scale(0.7).next_to(t0,DOWN)
        s.play(Create(t0))
        s.play(Create(t1))
        s.wait(1)

        a=0
        x1=-1.6
        x2=-1
        x3=0
        x4=1
        x5=1.9
        p1 = ValueTracker(x1)
        p2 = ValueTracker(x2)
        p3 = ValueTracker(x3)
        p4 = ValueTracker(x4)
        p5 = ValueTracker(x5)

        a_limit = ax1.get_T_label(a,curve1,label=MathTex("c=0", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)
        x_limit = ax1.get_T_label(p1.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)

        s.play(Create(a_limit),Create(x_limit))

        # Show definite integral from negative values to 0
        area1p = ax1.get_area(curve1z,x_range=[p1.get_value(),-1], dx_scaling=0.5, color=GREEN)
        area1n = ax1.get_area(curve1z,x_range=[p2.get_value(),a], dx_scaling=1,color=RED)
        s.play(FadeIn(area1p),FadeIn(area1n))

        curve2a = ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x, x_range=[-1.6,p1.get_value()],color=YELLOW)
        c2_label = ax2.get_graph_label(curve2a, label="F_1(x)",x_val=2.8).scale(0.6)
        s.add(curve2a)

        area1p.add_updater(lambda m: m.become(ax1.get_area(curve1z,x_range=[p1.get_value(),-1], dx_scaling=0.5, color=GREEN)))
        area1n.add_updater(lambda m: m.become(ax1.get_area(curve1z,x_range=[p2.get_value(),a], dx_scaling=0.5,color=RED)))
        curve2a.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x, x_range=[-1.6,p1.get_value()],color=YELLOW)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p1.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.wait(1)
        s.play(
            ApplyMethod(p1.increment_value,0.6),
            run_time=1
        )

        curve2a.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x, x_range=[-1.6,p2.get_value()],color=YELLOW)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p2.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.play(
            ApplyMethod(p2.increment_value,1),
            run_time=4
        )
        s.wait(1)

        area2p1 = ax1.get_area(curve1,x_range=[0,p3.get_value()], dx_scaling=0.5, color=GREEN)
        area2n =  ax1.get_area(curve1z2,x_range=[1,p4.get_value()], dx_scaling=0.5, color=RED)
        area2p2 = ax1.get_area(curve1z3,x_range=[1.9,p5.get_value()], dx_scaling=0.5, color=GREEN)
        s.add(area2p1, area2n, area2p2)

        area2p1.add_updater(lambda m: m.become(ax1.get_area(curve1,x_range=[0,p3.get_value()], dx_scaling=0.5, color=GREEN)))
        area2n.add_updater(lambda m: m.become(ax1.get_area(curve1z2,x_range=[1,p4.get_value()], dx_scaling=0.5, color=RED)))
        area2p2.add_updater(lambda m: m.become(ax1.get_area(curve1z3,x_range=[1.9,p5.get_value()], dx_scaling=0.5, color=GREEN)))

        curve2a.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x, x_range=[-1.6,p3.get_value()],color=YELLOW)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p3.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.play(
            ApplyMethod(p3.increment_value,1),
            run_time=2
        )

        curve2a.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x, x_range=[-1.6,p4.get_value()],color=YELLOW)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p4.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.play(
            ApplyMethod(p4.increment_value,0.9),
            run_time=2
        )

        curve2a.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x, x_range=[-1.6,p5.get_value()],color=YELLOW)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p5.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.play(
            ApplyMethod(p5.increment_value,0.9),
            run_time=2
        )
        s.play(FadeIn(c2_label))
        s.wait(1)
        curve2aFINAL = ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x, x_range=[-1.6,2.8],color=YELLOW)



        # Repeat for a  = -1

        s.play(FadeOut(area2p1),FadeOut(area2n),FadeOut(area2p2),FadeOut(area1p),FadeOut(area1n))
        s.play(FadeOut(x_limit,a_limit))
        s.play(ReplacementTransform(curve2a,curve2aFINAL))
        s.wait(1)

        t0a = MathTex("c = -1").shift(DOWN*2).scale(0.7)
        t1a = MathTex("\int","_{c=-1}","^x f(t)\, dt = F_2(x)").scale(0.7).next_to(t0,DOWN)
        s.play(ReplacementTransform(t0,t0a),ReplacementTransform(t1,t1a))
        s.wait(1)

        a = -1
        x1=-1.6
        x2=-1
        x3=0
        x4=1
        x5=1.9
        p1 = ValueTracker(x1)
        p2 = ValueTracker(x2)
        p3 = ValueTracker(x3)
        p4 = ValueTracker(x4)
        p5 = ValueTracker(x5)


        a_limit = ax1.get_T_label(a,curve1,label=MathTex("c=-1", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)
        x_limit = ax1.get_T_label(p1.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)

        area1p = ax1.get_area(curve1z,x_range=[p1.get_value(),-1], dx_scaling=0.5, color=GREEN)
        area1n = ax1.get_area(curve1z,x_range=[a,p2.get_value()], dx_scaling=1,color=GREEN)

        s.play(Create(a_limit),Create(x_limit))
        s.wait(1)

        s.play(FadeIn(area1p),FadeIn(area1n))

        curve2b = ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x + 1.6, x_range=[-1.6,p1.get_value()],color=BLUE)
        c2b_label = ax2.get_graph_label(curve2b, label="F_2(x)",x_val=2.8).scale(0.6)
        s.add(curve2b)

        area1p.add_updater(lambda m: m.become(ax1.get_area(curve1z,x_range=[p1.get_value(),-1], dx_scaling=0.5, color=GREEN)))
        area1n.add_updater(lambda m: m.become(ax1.get_area(curve1z,x_range=[a,p2.get_value()], dx_scaling=0.5,color=GREEN)))
        curve2b.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x + 1.6, x_range=[-1.6,p1.get_value()],color=BLUE)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p1.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.wait(1)
        s.play(
            ApplyMethod(p1.increment_value,0.6),
            run_time=1
        )

        curve2b.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x+1.6, x_range=[-1.6,p2.get_value()],color=BLUE)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p2.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.play(
            ApplyMethod(p2.increment_value,1),
            run_time=4
        )
        s.wait(1)

        area2p1 = ax1.get_area(curve1,x_range=[0,p3.get_value()], dx_scaling=0.5, color=GREEN)
        area2n =  ax1.get_area(curve1z2,x_range=[1,p4.get_value()], dx_scaling=0.5, color=RED)
        area2p2 = ax1.get_area(curve1z3,x_range=[1.9,p5.get_value()], dx_scaling=0.5, color=GREEN)
        s.add(area2p1, area2n, area2p2)

        area2p1.add_updater(lambda m: m.become(ax1.get_area(curve1,x_range=[0,p3.get_value()], dx_scaling=0.5, color=GREEN)))
        area2n.add_updater(lambda m: m.become(ax1.get_area(curve1z2,x_range=[1,p4.get_value()], dx_scaling=0.5, color=RED)))
        area2p2.add_updater(lambda m: m.become(ax1.get_area(curve1z3,x_range=[1.9,p5.get_value()], dx_scaling=0.5, color=GREEN)))

        curve2b.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x+1.6, x_range=[-1.6,p3.get_value()],color=BLUE)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p3.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.play(
            ApplyMethod(p3.increment_value,1),
            run_time=2
        )

        curve2b.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x+1.6, x_range=[-1.6,p4.get_value()],color=BLUE)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p4.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.play(
            ApplyMethod(p4.increment_value,0.9),
            run_time=2
        )

        curve2b.add_updater(lambda m: m.become(ax2.get_graph(lambda x: (x**4)/4 - (2*x**3)/3 - (x**2)/2 + 2*x+1.6, x_range=[-1.6,p5.get_value()],color=BLUE)))
        x_limit.add_updater(lambda m:m.become(ax1.get_T_label(p5.get_value(),curve1,label=MathTex("x", color=ORANGE).scale(0.4),triangle_size=0.15, line_color=ORANGE)))

        s.play(
            ApplyMethod(p5.increment_value,0.9),
            run_time=2
        )
        s.play(FadeIn(c2b_label))
        s.wait(1)

        s.play(FadeOut(curve2aFINAL),FadeOut(c2_label),FadeOut(t0a), FadeOut(t1a), FadeOut(area2p1), FadeOut(area2n), FadeOut(area1n), FadeOut(area2p2))
        s.wait(2)
