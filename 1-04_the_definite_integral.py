from manim import *

class AreaUnderCurve(Scene):
    def construct(s):

        pshslogo = ImageMobject("pshslogo.png")
        pshslogo.scale(1.2)
        pshslogo.to_edge(LEFT+UP, buff=1)
        topText = Paragraph("Philippine Science High School Main Campus",
                            "Mathematics 6",
                            "First Quarter", font="Montserrat").scale(0.4)
        topText.next_to(pshslogo,RIGHT)
        titleText = Text("The Area Under A Curve", font="Montserrat").scale(1.2)
        s.play(FadeIn(pshslogo),FadeIn(topText))
        s.wait(1)
        s.play(Write(titleText))
        s.wait(1)
        s.play(FadeOut(pshslogo,topText,titleText))
        s.wait(1)

        ax = Axes(
            x_range = [-1, 6],
            y_range = [-2, 16, 20],
            x_length = 6,
            y_length = 6,
            axis_config={
                #"numbers_to_include":[1,3,5],
                "color": GREEN},
                #tips=False
        ).shift(LEFT*3)

        s.play(Create(ax))
        #s.add(ax)

        # Define the function
        def func(x):
            return -(x-0.7)*(x-3)*(x-4)*(x-5) + 4

        # Draw the curve
        curve = ax.get_graph(func, x_range=[0.55,5.4], color=RED)
        curve_label = ax.get_graph_label(curve, label="f(x)",x_val=2 )
        plot = VGroup(curve, curve_label.scale(0.7))
        s.add_foreground_mobject(curve)
        s.play(Create(plot))
        #s.add(plot)

        # Drop the boundaries at x=1 and x=5
        drop = ax.get_vertical_lines_to_graph(curve, x_range=[1.2,4.5], num_lines=2, stroke_width=3, color=YELLOW)
        label_a = Tex("$a$").scale(0.7).next_to(Dot().move_to(ax.c2p(1.2,0)),DOWN)
        label_b = Tex("$b$").scale(0.7).next_to(Dot().move_to(ax.c2p(4.5,0)),DOWN)
        s.play(Create(VGroup(drop,label_a,label_b)))
        #s.add(VGroup(drop,label_a,label_b))

        # Show text: We want to approximate etc.
        t0 = Paragraph('We want to find the', 'exact area of the region', 'bounded by f(x), the lines', 'x=a, x=b, and the x-axis.',font="Montserrat", line_spacing=1.2).scale(0.5)
        t0.set_alignment('left')
        t0.shift(RIGHT*3)
        s.play(Create(t0))

        # Briefly flash area of interest
        area = ax.get_area(curve, x_range=[1.2,4.5], opacity=0.3)
        s.play(FadeIn(area))
        s.play(FadeOut(area))
        s.wait(1)

        # Show text: We can use approximating rectangles
        s.play(FadeOut(t0))
        t0 = Paragraph('We can use rectangles ', 'of width Δx to approximate', 'the area of this region.',font="Montserrat", line_spacing=1.2).scale(0.5)
        t0.set_alignment('left')
        t0.shift(RIGHT*3)
        s.play(Create(t0))

        # Draw one of the Riemann rectangles, mark the tag and the corresponding point
        r1 = ax.get_riemann_rectangles(curve, x_range=[1.2,4.5], dx=0.55, input_sample_type='center')
        s.play(Create(r1))
        brace_dx = Brace(r1[2])
        brace_dx_text = brace_dx.get_tex("\Delta x").scale(0.6)
        brace_grp = VGroup(brace_dx, brace_dx_text)
        s.add(brace_grp)
        s.wait(1)

        # We can use rectangles to approximate the area

        # Fade out other get_riemann_rectangles
        s.play(FadeOut(VGroup(r1[0],r1[1],r1[3],r1[4],r1[5],brace_grp,t0)))
        drop_xi = ax.get_T_label(2.575, curve, label=Tex("$x^*_i$").scale(0.7), triangle_size=0.15, line_color=PURPLE)
        marker_dot = Dot().move_to(ax.c2p(2.575, func(2.575)))
        marker_label = MathTex("(x^*_i, f(x^*_i))").scale(0.5).next_to(marker_dot)
        s.add_foreground_mobject(marker_dot)
        s.play(Create(drop_xi))
        s.add(VGroup(marker_dot,marker_label))

        # Show text: We can use approximating rectangles
        t0 = Paragraph('The area of the ith ', 'approximating rectangle is', 'given by:',font="Montserrat", line_spacing=1.2).scale(0.5).shift(RIGHT*3+UP).set_alignment('left')
        t1 = MathTex("A_i", "=", r"f(x^*_i)", "\cdot", "\Delta x").next_to(t0, DOWN*2)
        s.play(Create(VGroup(t0,t1)))
        s.wait(1)

        # Show other rectangles and use summation
        s.play(FadeOut(VGroup(t0,t1)))
        s.play(FadeIn(VGroup(r1[0],r1[1],r1[3],r1[4],r1[5])))

        # Show text: The approximate area
        t0 = Paragraph('The approximate area of the ', 'region is given by the sum of', 'the areas of the rectangles:',font="Montserrat", line_spacing=1.2).scale(0.5).shift(RIGHT*3+UP*2).set_alignment('left')
        t1 = MathTex(" ", " ", "R_n", "=", " ", r"\sum", r"_{i=1}","^n", r"f(x^*_i) \cdot \Delta x").next_to(t0, DOWN*2)
        s.play(Create(t0))
        s.play(FadeIn(t1))
        s.wait(1)
        t2 = Text('This is called the Riemann Sum',font="Montserrat", color=RED).scale(0.5).next_to(t1,DOWN*2).set_alignment('left')
        s.play(Create(t2))
        s.wait(1)

        # Increase the number of rectangles
        s.remove_foreground_mobject(marker_dot)
        s.play(FadeOut(VGroup(t0,t2,marker_dot,marker_label,drop_xi)))
        r2 = ax.get_riemann_rectangles(curve, x_range=[1.2,4.5], dx=0.165, input_sample_type='center')
        s.play(ReplacementTransform(r1,r2))
        t0 = Paragraph('We can improve the approximation', 'by increasing the number of', 'rectangles.',font="Montserrat", line_spacing=1.2).scale(0.5).shift(RIGHT*3).set_alignment('left')
        t1a = MathTex(" ", " ", "R_n", "=", " ", r"\sum", r"_{i=1}","^n", r"f(x^*_i) \cdot \Delta x").next_to(t0, UP*2)
        s.play(ReplacementTransform(t1,t1a))
        s.play(Create(t0))
        s.wait(1)

        # Make the area exact
        s.play(FadeOut(t0))
        s.play(ReplacementTransform(r2,area))
        t0 = Paragraph('We can get the exact area', 'by allowing n to approach infinity:',font="Montserrat", line_spacing=1.2).scale(0.5).shift(RIGHT*3+UP).set_alignment('left')
        t1 = MathTex(" ", " ", "R_n", "=", " ", r"\sum", r"_{i=1}","^n", r"f(x^*_i) \cdot \Delta x").next_to(t0, DOWN*2)
        s.play(ReplacementTransform(t1a,t1))
        s.play(Create(t0))
        t2 = MathTex("A = ", r"\displaystyle\lim_{n \to \infty}", "R_n", "=", r"\displaystyle\lim_{n \to \infty}", r"\sum", r"_{i=1}","^n", r"f(x^*_i) \cdot \Delta x").next_to(t0, DOWN*2).scale(0.75)
        for i_ in (0, 1, 4):
            t2[i_].set_color(YELLOW)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)

        # The Definite Integral
        s.play(FadeOut(t0))
        t0 = Paragraph('We define this limit of', 'the Riemann sum as', 'the Definite Integral',font="Montserrat", line_spacing=1.2).scale(0.5).shift(RIGHT*3+UP).set_alignment('left')
        s.play(FadeIn(t0))
        #t2 = MathTex("A = ", r"\displaystyle\lim_{n \to \infty}", "R_n", "=", r"\displaystyle\lim_{n \to \infty}", r"\sum", r"_{i=1}","^n", r"f(x^*_i) \cdot \Delta x").next_to(t0, DOWN*2).scale(0.75)
        t2a= MathTex(" ", "A = ", r"\displaystyle\lim_{n \to \infty}", "R_n", "=", r"\displaystyle\lim_{n \to \infty}", r"\sum", r"_{i=1}","^n", r"f(x^*_i) \cdot \Delta x").next_to(t0, DOWN*2).scale(0.75)
        s.remove(t2)
        s.add(t2a)
        t1= MathTex(r"\int_a^b f(x) \cdot dx", " ", " ", " ", "=", r"\displaystyle\lim_{n \to \infty}", r"\sum", r"_{i=1}","^n", r"f(x^*_i) \cdot \Delta x").next_to(t0, DOWN*2).scale(0.85)
        s.play(ReplacementTransform(t2a,t1))
        s.wait(1)
