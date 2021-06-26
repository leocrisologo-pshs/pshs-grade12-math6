from manim import *

class RiemannApproximation(Scene):
    def construct(s):

        pshslogo = ImageMobject("pshslogo.png")
        pshslogo.scale(1.2)
        pshslogo.to_edge(LEFT+UP, buff=1)
        topText = Paragraph("Philippine Science High School Main Campus",
                            "Mathematics 6",
                            "First Quarter", font="Montserrat").scale(0.4)
        topText.next_to(pshslogo,RIGHT)
        titleText = Text("Introduction to Riemann Sums", font="Montserrat").scale(1.2)
        s.play(FadeIn(pshslogo),FadeIn(topText))
        s.wait(1)
        s.play(Write(titleText))
        s.wait(1)
        s.play(FadeOut(pshslogo,topText,titleText))
        s.wait(1)

        ax = Axes(
            x_range = [0, 6, 1],
            y_range = [0, 22, 5],
            x_length = 6,
            y_length = 4,
            axis_config={
                #"numbers_to_include":[1,3,5],
                "color": GREEN},
                tips=False
        ).shift(LEFT*3)
        ax.add_coordinates(x_values=[1,5], y_values=[5,10,15,20])

        s.play(Create(ax))

        # Define the curve to approximate y = (x-1)^2 + 1
        def func(x):
            return (x - 1) ** 2 + 1

        # Draw the curve
        curve = ax.get_graph(func, x_range=[-0.5,5.5], color=RED)
        curve_label = ax.get_graph_label(curve, label="f(x)=(x-1)^2 + 1",x_val=4 ).shift(UP*3+LEFT*4)
        plot = VGroup(curve, curve_label.scale(0.7))
        s.add_foreground_mobject(curve)
        s.play(Create(plot))

        # Drop the boundaries at x=1 and x=5
        drop = ax.get_vertical_lines_to_graph(curve, x_range=[1,5], num_lines=2, stroke_width=3, line_func=Line)
        s.play(Create(drop))
        s.wait(1)

        # Show text: We want to approximate etc.
        t0 = Paragraph('We want to approximate', 'the area of the region', 'bounded by f(x), the lines', 'x=1, x=5, and the x-axis.',font="Montserrat", line_spacing=1.2).scale(0.6)
        t0.set_alignment('left')
        t0.shift(RIGHT*3)
        s.play(Create(t0))

        # Briefly flash area of interest
        area = ax.get_area(curve, x_range=[1,5], opacity=0.3)
        s.play(FadeIn(area))
        s.play(FadeOut(area))
        s.wait(1)

        # Draw Riemann rectangles where dx = 1, so four rectangles
        r1 = ax.get_riemann_rectangles(curve, x_range=[1,5], dx=1, input_sample_type='left')

        # Show text: We want to approximate etc.
        s.play(FadeOut(t0))
        t0 = Paragraph("Let's use n=4 rectangles", "of equal width to" , "approximate the area.",font="Montserrat", line_spacing=1.2).scale(0.6)
        t0.set_alignment('left')
        t0.shift(RIGHT*3)
        v0 = MathTex("n", "=", "4").shift(LEFT*5+ UP*2)
        grp = VGroup(r1,t0,v0.scale(0.75))
        s.play(Create(grp))
        s.wait(1)

        # Show text: Denote the width by dx
        s.play(FadeOut(t0))
        t0 = Paragraph("Denote the width of each", "rectangle by Δx." , "In our example:",font="Montserrat", line_spacing=1.2).scale(0.6)
        t0.shift(RIGHT*3+UP)
        t1 = MathTex(r"\Delta x", "=", r"\frac{5 - 1}{4} = 1").scale(0.8)
        t1.next_to(t0, DOWN)
        tgrp = VGroup(t0,t1)
        s.play(Write(tgrp))

        # Create braces to illustrate rectangle width and label with dx
        brace_dx =  Brace(r1[0])
        brace_dx_text = brace_dx.get_tex("\Delta x").scale(0.6)
        brace_grp = VGroup(brace_dx, brace_dx_text)
        s.play(Write(brace_grp))
        for i_ in (1, 2, 3, 0):
            brace_grp_old = brace_grp
            brace_dx = Brace(r1[i_])
            brace_dx_text = brace_dx.get_tex("\Delta x").scale(0.6)
            brace_grp = VGroup(brace_dx, brace_dx_text)
            s.play(ReplacementTransform(brace_grp_old,brace_grp))
        s.wait(1)

        # Write delta x on top of get_graph
        v1 = MathTex(r"\Delta x", "=", "1").scale(0.75)
        v1.next_to(v0,DOWN)
        s.play(ReplacementTransform(t1,v1))
        s.play(FadeOut(tgrp))

        # Show text: We use the left endpoints of the subinterval
        t0 = Paragraph("Here we use the left endpoint", "of each subinterval to find" , "the heights of the rectangles.",font="Montserrat", line_spacing=1.2).scale(0.6)
        t0.shift(RIGHT*3)
        s.play(Create(t0))
        s.wait(1)

        # Show text: We could use other points to set the height
        s.play(FadeOut(t0))
        t0 = Paragraph("We could also use other points", "in the subinterval to find" , "the heights of the rectangles.",font="Montserrat", line_spacing=1.2).scale(0.6)
        t0.shift(RIGHT*3)
        s.play(Write(t0))
        s.wait(1)
        r2 = ax.get_riemann_rectangles(curve, x_range=[1,5], dx=1, input_sample_type='center')
        s.play(ReplacementTransform(r1,r2))
        s.wait(1)
        r3 = ax.get_riemann_rectangles(curve, x_range=[1,5], dx=1, input_sample_type='right')
        s.play(ReplacementTransform(r2,r3))
        r1 = ax.get_riemann_rectangles(curve, x_range=[1,5], dx=1, input_sample_type='left')
        s.wait(1)
        s.play(ReplacementTransform(r3,r1))
        s.wait(1)

        # Show only first rectangle
        r_grp = VGroup(r1[1], r1[2], r1[3], t0)
        s.play(FadeOut(r_grp))
        hline = ax.get_horizontal_line(ax.i2gp(1,curve),color=YELLOW, stroke_width=2, line_func=Line)
        hline_label = MathTex("f(1)").scale(0.6)
        hline_label.next_to(hline, LEFT*2)
        hgrp = VGroup(hline, hline_label.set_color(YELLOW))
        s.play(Create(hgrp))
        t0 = Paragraph("The approximate area is given", "by the sum of the areas of" , "the rectangles.",font="Montserrat", line_spacing=1.2).scale(0.6)
        t0.shift(RIGHT*3+UP*2)
        t1 = MathTex(r"A_\text{approx}", "=", "f(1)", "\cdot", "\Delta x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
        t1.next_to(t0,DOWN)
        s.play(Write(t0))
        s.play(Write(t1))
        s.wait(1)

        # Show next 2nd rectangle
        s.play(FadeOut(hgrp))
        s.play(FadeIn(r1[1]))
        brace_grp_old = brace_grp
        brace_dx = Brace(r1[1])
        brace_dx_text = brace_dx.get_tex("\Delta x").scale(0.7)
        brace_grp = VGroup(brace_dx, brace_dx_text)
        hline = ax.get_horizontal_line(ax.i2gp(2,curve),color=YELLOW, stroke_width=2, line_func=Line)
        hline_label = MathTex("f(2)").scale(0.6)
        hline_label.next_to(hline, LEFT*2)
        hgrp = VGroup(hline, hline_label.set_color(YELLOW))
        s.play(Create(hgrp))
        s.play(ReplacementTransform(brace_grp_old,brace_grp))
        t2 = MathTex(r"A_\text{approx}", "&=", "f(1)", "\cdot", r"\Delta x \\", "&+", "f(2)", "\cdot", "\Delta x", " ", " ", " ", " ", " ", " ", " ", " " ).scale(0.8)
        t2.next_to(t0,DOWN)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)

        # Show next 3rd rectangle
        s.play(FadeOut(hgrp))
        s.play(FadeIn(r1[2]))
        brace_grp_old = brace_grp
        brace_dx = Brace(r1[2])
        brace_dx_text = brace_dx.get_tex("\Delta x").scale(0.7)
        brace_grp = VGroup(brace_dx, brace_dx_text)
        hline = ax.get_horizontal_line(ax.i2gp(3,curve),color=YELLOW, stroke_width=2, line_func=Line)
        hline_label = MathTex("f(3)").scale(0.6)
        hline_label.next_to(hline, LEFT*2)
        hgrp = VGroup(hline, hline_label.set_color(YELLOW))
        s.play(Create(hgrp))
        s.play(ReplacementTransform(brace_grp_old,brace_grp))
        t1 = MathTex(r"A_\text{approx}", "&=", "f(1)", "\cdot", r"\Delta x \\", "&+", "f(2)", "\cdot", r"\Delta x \\", "&+", "f(3)", "\cdot", "\Delta x", " ", " ", " ", " " ).scale(0.8)
        t1.next_to(t0,DOWN)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)

        # Show next 4th rectangle
        s.play(FadeOut(hgrp))
        s.play(FadeIn(r1[3]))
        brace_grp_old = brace_grp
        brace_dx = Brace(r1[3])
        brace_dx_text = brace_dx.get_tex("\Delta x").scale(0.7)
        brace_grp = VGroup(brace_dx, brace_dx_text)
        hline = ax.get_horizontal_line(ax.i2gp(4,curve),color=YELLOW, stroke_width=2, line_func=Line)
        hline_label = MathTex("f(4)").scale(0.6)
        hline_label.next_to(hline, LEFT+UP)
        hgrp = VGroup(hline, hline_label.set_color(YELLOW))
        s.play(Create(hgrp))
        s.play(ReplacementTransform(brace_grp_old,brace_grp))
        t2 = MathTex(r"A_\text{approx}", "&=", "f(1)", "\cdot", r"\Delta x \\", "&+", "f(2)", "\cdot", r"\Delta x \\", "&+", "f(3)", "\cdot", r"\Delta x \\", "&+", "f(4)", "\cdot", "\Delta x" ).scale(0.8)
        t2.next_to(t0,DOWN)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)

        # Remove lines and delta x bracket under x-axis
        s.play(FadeOut(VGroup(hgrp,brace_grp)))
        s.wait(1)

        # Solve the areas
        t1 = MathTex(r"A_\text{approx}", "&=", "f(1)", "\cdot", r"1 \\", "&+", "f(2)", "\cdot", r"1 \\", "&+", "f(3)", "\cdot", r"1 \\", "&+", "f(4)", "\cdot", "1" ).scale(0.8)
        t1.next_to(t0,DOWN)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)
        t2 = MathTex(r"A_\text{approx}", "&=", "f(1)", " ", r"  \\", "&+", "f(2)", " ", r"  \\", "&+", "f(3)", " ", r"  \\", "&+", "f(4)", " ", " " ).scale(0.8)
        t2.next_to(t0,DOWN)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)
        t1 = MathTex(r"A_\text{approx}", "&=", "(1-1)^2+1", " ", r"  \\", "&+", "(2-1)^2+1", " ", r"  \\", "&+", "(3-1)^2+1", " ", r"  \\", "&+", "(4-1)^2+1", " ", " " ).scale(0.8)
        t1.next_to(t0,DOWN)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)
        t2 = MathTex(r"A_\text{approx}", "&=", "1", " ", r"  \\", "&+", "2", " ", r"  \\", "&+", "5", " ", r"  \\", "&+", "10", " ", " " ).scale(0.8)
        t2.next_to(t0,DOWN)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)
        t1 = MathTex(r"A_\text{approx}", "=", "1", "8", r"\text{ sq. units} ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " ).scale(0.8)
        t1.next_to(t0,DOWN)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)

        # Show text: This is an under approximation
        t3 = Text("This is an underapproximation!",font="Montserrat", color=RED).scale(0.6)
        t3.next_to(t1,DOWN*2)
        s.play(Create(t3))
        s.wait(1)

        # Clear existing text and show text: We can take better approximations by increasing n
        s.play(FadeOut(VGroup(t3, t1, t0)))
        t0 = Paragraph("We can improve our", " approximation by increasing" , "the number of subintervals,", "denoted by n.",font="Montserrat", line_spacing=1.2).scale(0.6).shift(RIGHT*3)
        s.play(Create(t0))
        r2 = ax.get_riemann_rectangles(curve, x_range=[1,5], dx=0.5, input_sample_type='left')
        v0a = MathTex("n", "=", "8").shift(LEFT*5+ UP*2).scale(0.75)
        v1a = MathTex(r"\Delta x", "=", "0.5").scale(0.75)
        v1a.next_to(v0a,DOWN)
        s.play(ReplacementTransform(r1,r2))
        s.play(ReplacementTransform(VGroup(v0,v1),VGroup(v0a,v1a)))
        s.wait(1)

        r3 = ax.get_riemann_rectangles(curve, x_range=[1,5], dx=0.2, input_sample_type='left')
        v0 = MathTex("n", "=", "20").shift(LEFT*5+ UP*2).scale(0.75)
        v1 = MathTex(r"\Delta x", "=", "0.2").scale(0.75)
        v1.next_to(v0,DOWN)
        s.play(ReplacementTransform(r2,r3))
        s.play(ReplacementTransform(VGroup(v0a,v1a),VGroup(v0,v1)))
        s.wait(1)

        # Parting question
        s.play(FadeOut(t0))
        t_0 = Text("Before you go: ", font="Montserrat", color=RED).scale(0.6).shift(UP*2 + RIGHT*3)
        t0 = Paragraph("How can we make the", " approximation exact?" ,font="Montserrat", line_spacing=1.2, color=YELLOW).scale(0.6)
        t0.next_to(t_0,DOWN*2)
        s.play(Create(t_0))
        s.play(Create(t0))
        s.wait(1)
