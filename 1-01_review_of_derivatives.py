from manim import *

class Titles(Scene):
    def construct(self):
        pshslogo = ImageMobject("pshslogo.png")
        pshslogo.scale(1.2)
        pshslogo.to_edge(LEFT+UP, buff=1)
        with register_font("../Montserrat/Montserrat-Medium.ttf"):
            topText = Paragraph("Philippine Science High School Main Campus",
                                "Mathematics 6",
                                "First Quarter", font="Montserrat").scale(0.4)
            topText.next_to(pshslogo,RIGHT)
        with register_font("../Montserrat/Montserrat-SemiBold.ttf"):
            titleText = Text("Review of Derivatives", font="Montserrat").scale(1.5)
        self.play(FadeIn(pshslogo),FadeIn(topText))
        self.wait(1)
        self.play(Write(titleText))
        self.wait(1)
        self.play(FadeOut(pshslogo,topText,titleText))
        self.wait(1)

class DeriveTangent(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-1, 7.2, 1],
            y_range = [-1, 7.2, 1],
            x_length = 6,
            y_length = 6,
            axis_config={
                #"numbers_to_include":[2,4,6],
                "color": GREEN},
                tips=False
        )
        #  Define hyperbolic function y = 3/x
        def func(x):
            return 3 / x

        # Create the axes and the function f(x) = 3/x
        curve_1 = axes.get_graph(func, x_range=[0.43, 7], color=RED)
        curve_1_label = axes.get_graph_label(curve_1, label="f(x)=\\frac{3}{x}",x_val=0.5 )
        plot_1 = VGroup(curve_1,curve_1_label.scale(0.65)) # VGroup groups objects together

        # Define the location of the fixed reference point at x = 4
        xFixed = 4
        yFixed = func(xFixed)

        # ValueTracker is the changing x-value to animate the components
        p = ValueTracker(0.43)

        # Plot the fixed reference point and its labels
        fixed_dot = Dot()
        fixed_dot.move_to(axes.coords_to_point(xFixed,yFixed))
        fixed_dot_label = Tex(r"$P(x,f(x))$").scale(0.65)
        always(fixed_dot_label.next_to, fixed_dot, RIGHT+UP*0.5)

        # Create the moving Dot, the initial coordinates are given by ValueTracker
        moving_dot = Dot()
        moving_dot.move_to(axes.coords_to_point(p.get_value(), func(p.get_value())))
        moving_dot_label_Q = Tex(r'$Q$').scale(0.6)
        moving_dot_label = Tex(r'$Q(x + \Delta x, f(x + \Delta x))$').scale(0.6)
        always(moving_dot_label.next_to, moving_dot, RIGHT)
        always(moving_dot_label_Q.next_to, moving_dot, RIGHT)

        # Create the secant line that will become the tangent line using the 2-pt form of a linear equation
        secantLine = axes.get_graph(
            lambda x: ((yFixed - func(p.get_value()))/(xFixed-p.get_value()))*(x-xFixed) + yFixed,
            color = BLUE,
            x_min = 0.43,
            x_max = 6
        )

        # The add_updater modifies the values of the objects. This will move the Dot as the x-value changes.
        moving_dot.add_updater(
            lambda m: m.become(
                moving_dot.move_to(axes.coords_to_point(p.get_value(), func(p.get_value())))
                )
            )

        # add_updater to animate the secant line
        secantLine.add_updater(
            lambda m: m.become(
                axes.get_graph(
                    # lambda x: -1 * p.get_value() * x + p.get_value(),
                    lambda x: ((yFixed - func(p.get_value()))/(xFixed-p.get_value()))*(x-xFixed) + yFixed,
                    color = BLUE,
                    x_min = 0.43,
                    x_max = 6
                )
            )
        )

        # Drop two vertical lines to illustrate delta_x
        drop1 = axes.get_vertical_line(axes.i2gp(4, curve_1), color=YELLOW, line_func=Line)
        drop2 = axes.get_vertical_line(axes.i2gp(0.93, curve_1), color=YELLOW, line_func=Line)
        drop1.shift(LEFT*3)
        drop2.shift(LEFT*3)
        # Draw brace to demonstrate length of delta_x
        distLine = Line(axes.c2p(0.93,0), axes.c2p(4,0))
        brace_dx = Brace(distLine).shift(LEFT*3)
        brace_dx_text = brace_dx.get_tex("\Delta x").scale(0.6)

        # Define the legs of the right triangle to demonstrate the slope computation.
        hLine = Line(axes.c2p(xFixed,yFixed), axes.c2p(p.get_value(),yFixed),color = YELLOW)
        vLine = Line(axes.c2p(p.get_value(),yFixed), axes.c2p(p.get_value(),func(p.get_value())),color = YELLOW)

        # Label the legs as delta x and delta y. The always() makes sure that the labels follow the lines.
        delta_x_label = Tex(r"$\Delta x$").scale(0.6)
        always(delta_x_label.next_to,hLine,DOWN)

        delta_y_label = Tex(r"$f(x+\Delta x) - f(x)$").scale(0.6)
        always(delta_y_label.next_to,vLine,LEFT)

        # hLine and vLine updaters to animate the slope indicator
        hLine.add_updater(
            lambda m: m.become(
                hLine.put_start_and_end_on(axes.c2p(xFixed,yFixed), axes.c2p(p.get_value(),yFixed))
            )
        )

        vLine.add_updater(
            lambda m: m.become(
                vLine.put_start_and_end_on(axes.c2p(p.get_value(),yFixed), axes.c2p(p.get_value(),func(p.get_value())))
            )
        )

        # Discussion Text
        #text01 = Text("Goal: Find the slope of the tangent line to f(x) on P", font="Montserrat", color = BLUE).scale(0.6)
        text01 = Paragraph(
            "Find the slope of the",
            "tangent line to f(x) on P",
            font="Montserrat",
            color=BLUE
        ).scale(0.65)
        text01.shift(RIGHT*3 + UP*3)
        text02 = MathTex("m","="," ","\dfrac{f(x + \Delta x) - f(x)}{\Delta x}")
        text02.shift(RIGHT*3 + UP)
        text03 = MathTex("m","=","\displaystyle\lim_{\Delta x \Rightarrow 0}","\dfrac{f(x + \Delta x) - f(x)}{\Delta x}")
        text03.shift(RIGHT*3 + UP)
        text04 = MathTex("f'(x)","=","\displaystyle\lim_{\Delta x \Rightarrow 0}","\dfrac{f(x + \Delta x) - f(x)}{\Delta x}")
        text04.shift(RIGHT*3 + UP)

        # Issue: I cannot get \to or \rightarrow to render.

        # Animate initial drawing of axes and graph, then shifts them left
        self.play(Create(axes))
        self.play(Create(plot_1))
        self.add(fixed_dot, fixed_dot_label)
        self.wait(1)

        # Shift axis and graph to the left
        self.play(axes.animate.shift(LEFT * 3), plot_1.animate.shift(LEFT*3), fixed_dot.animate.shift(LEFT*3))

        # Text: Finding the slope of the tangent line
        self.play(FadeIn(text01))
        self.wait(3)

        # Show the secant line and prepare to move it to the first Q location
        #self.add(secantLine, moving_dot,hLine,vLine)
        self.add(moving_dot)

        # Move dot to first location
        self.play(
            ApplyMethod(p.increment_value,0.5),
            run_time=2
        )

        # Label moving point as Q, no coordinates yet
        self.add(moving_dot_label_Q)
        self.wait(2)

        # Drop vertical lines to axis to denote horizontal distance of delta x
        self.play(FadeIn(drop1, drop2, brace_dx, brace_dx_text))
        self.wait(2)

        # Update Q label to include coordinates
        self.remove(moving_dot_label_Q)
        self.add(moving_dot_label)

        # Having made the point, remove drop lines and brace
        self.wait(2)
        self.play(FadeOut(drop1, drop2, brace_dx, brace_dx_text))

        # Draw the secant line
        self.play(Create(secantLine))
        self.wait(1)

        # Draw the triangle to denote slope
        self.play(Create(hLine))
        self.play(Create(vLine))
        self.play(FadeIn(delta_x_label, delta_y_label))
        self.wait(2)

        # Show slope formula
        self.play(FadeIn(text02))
        self.wait(2)

        # Transform to limit of difference quotient
        self.play(
            ReplacementTransform(text02, text03),
        )

        # Move Q closer to  P
        self.play(
            ApplyMethod(p.increment_value,1),
            #MoveAlongPath(moving_dot, curve_1, rate_func=linear ),
            run_time=2
        )
        self.wait(1)

        # Move Q to P
        self.play(FadeOut(delta_x_label, delta_y_label, moving_dot_label))
        self.play(
            ApplyMethod(p.increment_value,2.069),
            #MoveAlongPath(moving_dot, curve_1, rate_func=linear ),
            run_time=2
        )
        self.wait(1)
        self.play(
            ReplacementTransform(text03, text04),
        )
        self.wait(2)
        self.play(FadeOut(text01, text04, fixed_dot_label))
        self.wait(1)

        # I wanted to change the colors of "\Delta x to 0" to highlight but I can't figure it out yet.


class PlotDerivative(Scene):
    def construct(self):

        # This the original axis from the previous animation and is on the left side
        ax1 = Axes(
            x_range = [-1, 7.2, 1],
            y_range = [-1, 7.2, 1],
            x_length = 6,
            y_length = 6,
            axis_config={
                #"numbers_to_include":[2,4,6],
                "color": GREEN},
                tips=False
        )
        ax1.shift(LEFT * 3)

        #  Define hyperbolic function y = 3/x
        def func(x):
            return 3 / x

        curve_1 = ax1.get_graph(func, x_range=[0.43, 7], color=RED)
        curve_1_label = ax1.get_graph_label(curve_1, label="f(x)=\\frac{3}{x}",x_val=0.5 )
        plot_1 = VGroup(curve_1,curve_1_label.scale(0.65)) # VGroup groups objects together

        self.add(ax1, plot_1)

        # Valuetracker to control movement of tangent line
        p = ValueTracker(0)

        # Create moving dot. The starting x-value is 4.
        movingDot = Dot().shift(LEFT * 3)
        movingDot.move_to(ax1.coords_to_point(4 - p.get_value(), func(4 - p.get_value()) ))
        self.add(movingDot)

        # Define the tangent line that will move
        tangentLine = ax1.get_graph(
            lambda x: ax1.slope_of_tangent(4 - p.get_value(),curve_1) * (x - (4 - p.get_value())) + func(4 - p.get_value()),
            color = BLUE,
            x_min = 0.43,
            x_max = 6
        )
        self.add(tangentLine)

        # The add_updater modifies the values of the objects. This will move the Dot as the x-value changes.
        movingDot.add_updater(
            lambda m: m.become(
                movingDot.move_to(ax1.coords_to_point(4 - p.get_value(), func(4 - p.get_value())))
                )
            )
        # This add_updater moves the tangent line
        tangentLine.add_updater(
            lambda m: m.become(
                ax1.get_graph(
                    lambda x: ax1.slope_of_tangent(4 - p.get_value(),curve_1) * (x - (4 - p.get_value())) + func(4 - p.get_value()),
                    color = BLUE,
                    x_min = 0.43,
                    x_max = 6
                )
            )
        )

        # Second pair of axes to plot the derivative of 3/x
        ax2 = Axes(
            x_range = [-1, 7.2, 1],
            y_range = [-7, 1.2, 1],
            x_length = 6,
            y_length = 6,
            axis_config={
                #"numbers_to_include":[2,4,6],
                "color": GREEN},
                tips=False
        )
        ax2.shift(RIGHT * 3)
        self.play(Create(ax2))

        # Create dot which will not be shown, to bind label
        invisiDot = Dot()
        testvalue = 0.7

        # Create anchors for x-value and slope labels
        x_anchor = Dot().move_to(ax1.coords_to_point(2, 4.5))
        x_anchor_2= Dot().move_to(ax1.coords_to_point(2, 4))

        # Define Dot for derivative function  - I brute forced this
        plotPoint0 = Dot(color=YELLOW).move_to(ax2.coords_to_point(0.7,ax1.slope_of_tangent(0.7,curve_1)))
        plotPoint1 = Dot(color=YELLOW).move_to(ax2.coords_to_point(1,ax1.slope_of_tangent(1,curve_1)))
        plotPoint2 = Dot(color=YELLOW).move_to(ax2.coords_to_point(2,ax1.slope_of_tangent(2,curve_1)))
        plotPoint3 = Dot(color=YELLOW).move_to(ax2.coords_to_point(3,ax1.slope_of_tangent(3,curve_1)))
        plotPoint4 = Dot(color=YELLOW).move_to(ax2.coords_to_point(4,ax1.slope_of_tangent(4,curve_1)))
        plotPoint5 = Dot(color=YELLOW).move_to(ax2.coords_to_point(5,ax1.slope_of_tangent(5,curve_1)))
        pp0 = MathTex("(0.7, -6.12)").scale(0.5)
        pp1 = MathTex("(1, -3)").scale(0.5)
        pp2 = MathTex("(2, -0.75)").scale(0.5)
        pp3 = MathTex("(3, -0.33)").scale(0.5)
        pp4 = MathTex("(4, -0.19)").scale(0.5)
        pp5 = MathTex("(5, -0.12)").scale(0.5)
        always(pp0.next_to,plotPoint0,DOWN)
        always(pp1.next_to,plotPoint1,DOWN)
        always(pp2.next_to,plotPoint2,DOWN)
        always(pp3.next_to,plotPoint3,DOWN)
        always(pp4.next_to,plotPoint4,UP)
        always(pp5.next_to,plotPoint5,DOWN)


        for i_ in (3.3, 3, 2, 1, 0, -1):
            # Set one second as the duration between steps
            self.play(p.animate.set_value(i_),run_time=1)
            # Set-up the x-axis label of the x-value
            invisiDot.move_to(ax1.coords_to_point(4-i_, 0))
            invisiDot_label = Variable(4-i_,"x").scale(0.6)
            always(invisiDot_label.next_to, invisiDot, DOWN)
            #Label x-value and slope  as reference for other graph
            text_x = Variable(4-i_,"x", color=YELLOW).scale(0.6)
            always(text_x.next_to, x_anchor, RIGHT)
            text_slope = Variable(ax1.slope_of_tangent(4 - i_,curve_1),Text("slope",font="Montserrat", color=YELLOW).scale(0.6), color=YELLOW).scale(0.6)
            always(text_slope.next_to, x_anchor_2, RIGHT)
            # Define dropped vertical lines to the axis.
            drop1 = ax1.get_vertical_line(ax1.i2gp(4 - i_ ,  curve_1), color=YELLOW, line_func=Line)
            # Plot on opposite axis
            #plotPoint.move_to(ax2.coords_to_point(4-i_,ax1.slope_of_tangent(4 - i_,curve_1)))
            self.play(FadeIn(drop1, invisiDot_label, text_x, text_slope))
            if i_ == 3.3:
                self.play(FadeIn(plotPoint0, pp0))
            elif i_ == 3:
                self.play(FadeIn(plotPoint1, pp1))
            elif i_ == 2:
                self.play(FadeIn(plotPoint2, pp2))
            elif i_ == 1:
                self.play(FadeIn(plotPoint3, pp3))
            elif i_ == 0:
                self.play(FadeIn(plotPoint4, pp4))
            else:
                self.play(FadeIn(plotPoint5, pp5))

            self.wait(1)
            self.play(FadeOut(drop1, invisiDot_label, text_x, text_slope))

        self.wait(1)
        self.play(FadeOut(pp0, pp1, pp2, pp3, pp4, pp5))
        def func_prime(x):
            return -3 / (x**2)
        curve_2 = ax2.get_graph(
            func_prime,
            color = YELLOW,
            x_range = [0.65,7],
        )
        curve_2_label = ax2.get_graph_label(curve_2, label="f'(x)=-\\frac{3}{x^2}",x_val=1.5 )
        curve_2_label.scale(0.65)
        self.play(Create(curve_2))
        self.play(FadeOut(plotPoint0,plotPoint1,plotPoint2,plotPoint3,plotPoint4,plotPoint5 ))
        self.play(Write(curve_2_label))
        self.wait(2)
        self.play(FadeOut(ax1, ax2, curve_1, curve_2, curve_1_label, curve_2_label, tangentLine, movingDot))
        self.wait(1)

class Computations(Scene):
    def construct(self):

        given = MathTex("f(x)","=","\dfrac{3}{x}").shift(LEFT*4)
        self.play(Write(given))
        #self.add(given)

        step00 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            " ",                                 #3
            "{f(x + \Delta x)",                 #4
            "-",                                #5
            "f(x)",                             #6
            " ",
            "\\over",                           #8
            "\Delta x}"                         #9
        ).shift(RIGHT*2)
        self.play(FadeIn(step00))
        #self.add(step00)
        self.wait(1)
        self.play(Indicate(step00[4]))
        self.play(Indicate(step00[6]))
        self.play(Indicate(given))
        self.wait(1)

        step01 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            " ",
            "{{3 \over x + \Delta x}",          #4
            "-",                                #5
            "{3 \over x}",                      #6
            " ",
            "\\over",                           #8
            "\Delta x}"                         #9
        ).shift(RIGHT*2)

        self.play(ReplacementTransform(step00,step01))
        self.wait(1)
        self.play(Indicate(step01[9]))
        self.wait()

        step02 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            "\left(",
            "{3 \over x + \Delta x}",           #4
            "-",                                #5
            "{3 \over x}",
            r"\right)",                         #7
            "\cdot",                            #8
            "{1 \over \Delta x}"                #9
        ).shift(RIGHT*2)
        self.play(ReplacementTransform(step01,step02))
        self.wait(1)
        self.play(Indicate(step02[4]))
        self.play(Indicate(step02[6]))

        step03 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            "\left(",
            "{3x - 3(x + \Delta x)",           #4
            r"\over",                                #5
            "(x + \Delta x)x}",
            r"\right)",                         #7
            "\cdot",                            #8
            "{1 \over \Delta x}"                #9
        ).shift(RIGHT*2)
        self.play(ReplacementTransform(step02,step03))
        self.wait()

        step04 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            "\left(",
            "{3x - 3x - 3\Delta x",           #4
            r"\over",                                #5
            "(x + \Delta x)x}",
            r"\right)",                         #7
            "\cdot",                            #8
            "{1 \over \Delta x}"                #9
        ).shift(RIGHT*2)
        self.play(ReplacementTransform(step03,step04))
        self.wait()

        step05 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            "\left(",
            "{3x - 3x - 3\Delta x",           #4
            r"\over",                                #5
            "x^2 + x \Delta x}",
            r"\right)",                         #7
            "\cdot",                            #8
            "{1 \over \Delta x}"                #9
        ).shift(RIGHT*2)
        self.play(ReplacementTransform(step04,step05))
        self.play(Indicate(step05[4]))
        self.wait()

        step06 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            "\left(",
            "{- 3\Delta x",           #4
            r"\over",                                #5
            "x^2 + x \Delta x}",
            r"\right)",                         #7
            "\cdot",                            #8
            "{1 \over \Delta x}"                #9
        ).shift(RIGHT*2)
        self.play(ReplacementTransform(step05,step06))
        self.wait()

        step06b = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            "\left(",
            "{-3",
            "\Delta x",           #4
            r"\over",                                #5
            "x^2 + x \Delta x}",
            r"\right)",                         #7
            "\cdot",                            #8
            "{1 \over ",
            "\Delta x}"                #9
        ).shift(RIGHT*2)
        self.remove(step06)
        self.add(step06b)
        self.play(Indicate(step06b[5]))
        self.play(Indicate(step06b[11]))
        self.wait()

        step07 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            "\left(",
            "{-3",
            " ",           #4
            r"\over",                                #5
            "x^2 + x \Delta x}",
            r"\right)",                         #7
            " ",                            #8
            " ",
            " "                #9
        ).shift(RIGHT*2)
        self.play(ReplacementTransform(step06b, step07))
        self.wait()

        step07b = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            r"\displaystyle\lim_{\Delta x \to 0 }",    #2
            "\left(",
            "{-3",
            r"\over",                                #5
            "x^2",
            "+",
            "x",
            "\Delta x}",
            r"\right)"                         #7
        ).shift(RIGHT*2)
        self.remove(step07)
        self.add(step07b)
        self.play(Indicate(step07b[2]))
        self.play(Indicate(step07b[9]))

        step08 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            " ",    #2
            " ",
            "{-3",
            r"\over",                                #5
            "x^2",
            " ",
            " ",
            " ",
            " "                         #7
        ).shift(RIGHT*2)
        self.play(ReplacementTransform(step07b, step08))

        step09 = MathTex(
            "f'(x)",                            #0
            "=",                                #1
            " ",    #2
            "-",
            "{3",
            r"\over",                                #5
            "x^2",
            " ",
            " ",
            " ",
            " "                         #7
        ).shift(RIGHT*2)
        self.play(ReplacementTransform(step08, step09))

        self.wait(1)
        self.play(FadeOut(given,step09))
        self.wait(1)
