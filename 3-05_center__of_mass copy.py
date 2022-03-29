from re import L
from manim import *

class center_1(Scene):
    def construct(s):

        wd = 3
        # change this to 3 before final compile

        d1,d2 = Dot([-5.5,0,0]),Dot([5.5,0,0])
        theta_tracker = ValueTracker(0)
        line = Line(d1.get_center(), d2.get_center())
        line_moving = Line(d1.get_center(), d2.get_center())
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point = line.get_center()
        )

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value()*DEGREES, about_point=line.get_center()
            )
        )

        dotP1start = Dot([0,-4,0], color = RED).scale(1.5)
        dotP1end = Dot([0,0,0])
        s.play(Create(line))
        s.add(line_moving)
        s.add(dotP1start)
        s.play(dotP1start.animate.shift(dotP1end.get_center() - dotP1start.get_center()))
        s.wait(wd)
        s.remove(line)

        P1label = MathTex("P").next_to(dotP1end,DOWN)
        s.add(P1label)

        s.play(theta_tracker.animate.set_value(40))
        s.play(theta_tracker.animate.set_value(-40))
        s.play(theta_tracker.animate.set_value(0))
        s.wait(wd)

        numline = NumberLine(
            x_range=[-6,6,1],
            length=12,
            numbers_with_elongated_ticks=[-4,-2, 1, 5],
            include_numbers=True,
        ).shift(DOWN)
        numline_label = MathTex(r"\text{meters from }P").next_to(numline,DOWN).scale(0.7)

        s.play(FadeIn(VGroup(numline,numline_label)))

        dot10kg_start = Dot([5,4,0], color = BLUE).scale(3)
        dot10kg_end = Dot([5,0,0])
        label10kg = MathTex(r"10\text{kg}",color=BLUE).next_to(dot10kg_end,UP)
        s.add(dot10kg_start)
        s.play(dot10kg_start.animate.shift(dot10kg_end.get_center() - dot10kg_start.get_center()))
        s.add(label10kg)
        s.wait(wd)

        dot7kg_start = Dot([-2,4,0], color = GREEN).scale(2.1)
        dot7kg_end = Dot([-2,0,0])
        label7kg = MathTex(r"7\text{kg}",color=GREEN).next_to(dot7kg_end,UP)
        s.add(dot7kg_start)
        s.play(dot7kg_start.animate.shift(dot7kg_end.get_center() - dot7kg_start.get_center()))
        s.add(label7kg)
        s.wait(wd)

        dot2kg_start = Dot([1,4,0], color = YELLOW).scale(1.5)
        dot2kg_end = Dot([1,0,0])
        label2kg = MathTex(r"2\text{kg}",color=YELLOW).next_to(dot2kg_end,UP)
        s.add(dot2kg_start)
        s.play(dot2kg_start.animate.shift(dot2kg_end.get_center() - dot2kg_start.get_center()))
        s.add(label2kg)
        s.wait(wd)

        dot1kg_start = Dot([-4,4,0], color = PINK)
        dot1kg_end = Dot([-4,0,0])
        label1kg = MathTex(r"1\text{kg}",color=PINK).next_to(dot1kg_end,UP)
        s.add(dot1kg_start)
        s.play(dot1kg_start.animate.shift(dot1kg_end.get_center() - dot1kg_start.get_center()))
        s.add(label1kg)
        s.wait(wd)

        s.play(FadeOut(dotP1start,P1label))
        s.wait(wd)

        arrow = Arrow([1.7,-1,0],[1.7,0,0],buff=0,color=RED)
        arrowlabel=Text('1.7',color=RED).next_to(arrow,DOWN).scale(0.5)
        dot_P2 = Dot([2,0,0])
        P2label = MathTex("P_2", color=RED).scale(0.75).next_to(dot_P2,DOWN)

        s.play(FadeIn(VGroup(arrow,arrowlabel,P2label)))
        s.wait(wd)


class center_2(Scene):
    def construct(s):

        wd = 2.5
        # change this to 3 before final compile

        density = ImageMobject("densityfunction.png").scale(0.7).shift(UP)
        #density.to_edge(RIGHT,buff=1)

        s.add(density)

        d1,d2 = Dot([-4,-2.2,0]),Dot([4,-2.2,0])
        line = Line(d1.get_center(), d2.get_center())

        dot0 = Dot([-3.1,-2.2,0])
        dotL = Dot([3.15,-2.2,0])
        d0label = Tex('0').scale(0.7).next_to(dot0, DOWN)
        dLlabel = Tex('L').scale(0.7).next_to(dotL, DOWN)
        rod = Line(dot0.get_center(), dotL.get_center(), color=BLUE, stroke_width=10)

        dotxi_1 = Dot([0,-2.2,0])
        dotxi = Dot([1,-2.2,0])
        dxi_1_label = MathTex("x_{i-1}").scale(0.65).next_to(dotxi_1,DOWN)
        dxi_label = MathTex("x_i").scale(0.65).next_to(dotxi,DOWN)

        portion = Line(dotxi_1.get_center(), dotxi.get_center(), color=RED, stroke_width=10)

        arrow = Arrow([0.6,-2.6,0],[0.6,-2.2,0],buff=0,color=YELLOW)
        arrowlabel=MathTex("x_i^*",color=YELLOW).next_to(Dot([0.6,-2.2,0]),DOWN).scale(0.6)

        b1 = Brace(Line([0,-2.7,0],[1,-2.7,0]))
        b1text = MathTex("\Delta x").scale(0.6).next_to(Dot([0.5,-2.9,0]),DOWN)

        dotm1 = Dot([-3.1,-1.8,0])
        dotm2 = Dot([0.6,-1.8,0])
        m_line = DashedLine(dotm1.get_center(), dotm2.get_center())

        m_text = MathTex(r"m_i = \rho(x_i^*)\cdot \Delta x ").scale(0.7).next_to(Dot([0.25,-1.5,0],UP))
        m2_text = MathTex(r"M_i = \left[\rho(x_i^*)\cdot \Delta x\right] \cdot x_i^* ").scale(0.7).next_to(Dot([0.25,-1.5,0],UP))

        s.play(Create(line))
        s.play(FadeIn(dot0, dotL, d0label, dLlabel))
        s.wait(wd)
        s.play(Create(rod))
        s.wait(wd)
        s.add(dotxi_1, dotxi, dxi_1_label, dxi_label)
        s.play(Create(portion))
        s.wait(wd)
        s.play(Create(arrow))
        s.add(arrowlabel)
        s.wait(wd)
        s.play(Create(VGroup(b1, b1text)))
        s.wait(wd)
        s.play(FadeOut(density))
        s.wait(wd)
        s.play(Create(VGroup(m_line, dotm1,dotm2)))
        s.wait(wd)
        s.play(Create(m_text))
        s.wait(wd)
        s.play(FadeOut(m_text))
        s.wait(wd)
        s.play(Create(m2_text))
        s.wait(wd)
