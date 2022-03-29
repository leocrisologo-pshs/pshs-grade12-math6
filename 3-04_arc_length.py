from re import L
from manim import *

class A01(Scene):
    def construct(s):

        scale = 1
        wt = 2    #wait time

        ax = Axes(
            x_range = [-0.5,8.5,9],
            x_length = 8.5 * scale,
            y_range = [-0.5, 8,9],
            y_length = 5.5 * scale*0.75,
        )

        def func(x):
            return 0.5 * x * np.sin(x-1) + 5

        x_1 = 0.5
        x_2 = 7.5

        trace = ax.plot(func, x_range=[-1,8.4], color = BLUE)
        arc = ax.plot(func, x_range=[x_1,x_2], color = RED)
        ptA = Dot(ax.c2p(x_1,func(x_1)))
        ptB = Dot(ax.c2p(x_2,func(x_2)))
        endptA = ax.get_T_label(x_val=x_1, graph=arc, label=Tex("a").scale(0.7), triangle_size=0.1)
        endptB = ax.get_T_label(x_val=x_2, graph=arc, label=Tex("b").scale(0.7), triangle_size=0.1)
        labelA = Tex("$A$").scale(0.5).next_to(Dot(ax.c2p(x_1,func(x_1))), LEFT)
        labelB = Tex("$B$").scale(0.5).next_to(Dot(ax.c2p(x_2,func(x_2))), RIGHT)
        f_label = Tex("$f(x)$").scale(0.7).next_to(Dot(ax.c2p(8,func(8))), RIGHT)

        s.play(Create(ax), Create(trace), FadeIn(f_label))
        s.wait(wt)
        s.play(Create(endptA), Create(endptB))
        s.play(FadeIn(VGroup(ptA, ptB)))
        s.wait(wt)
        s.play(Create(arc))
        s.wait(wt)
        s.play(FadeOut(VGroup(ax,trace, endptA, endptB, f_label)))
        s.wait(wt)
        s.play(FadeIn(VGroup(labelA, labelB)))
        s.wait(wt)

### next scene, show lines

        labelA_1 = Tex("$A(a,f(a))=P_0$").scale(0.6).next_to(Dot(ax.c2p(x_1,func(x_1))), LEFT)
        labelB_1 = Tex("$B(b,f(b))=P_n$").scale(0.6).next_to(Dot(ax.c2p(x_2,func(x_2))), RIGHT)

        s.play(ReplacementTransform(labelA, labelA_1), ReplacementTransform(labelB, labelB_1))

        ptTracker=[]
        points=[]
        for i in range(0,10):
            pt_track=ValueTracker(x_2)
            ptTracker.append(pt_track)
            point_temp = Dot(ax.c2p(ptTracker[i].get_value(), func(ptTracker[i].get_value())))
            points.append(point_temp)

        points[1].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[1].get_value(), func(ptTracker[1].get_value()))))
        )

        points[2].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[2].get_value(), func(ptTracker[2].get_value()))))
        )

        points[3].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[3].get_value(), func(ptTracker[3].get_value()))))
        )

        points[4].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[4].get_value(), func(ptTracker[4].get_value()))))
        )

        points[5].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[5].get_value(), func(ptTracker[5].get_value()))))
        )

        points[6].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[6].get_value(), func(ptTracker[6].get_value()))))
        )

        points[7].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[7].get_value(), func(ptTracker[7].get_value()))))
        )

        points[8].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[8].get_value(), func(ptTracker[8].get_value()))))
        )

        points[9].add_updater(
            lambda m: m.become(Dot(ax.c2p(ptTracker[9].get_value(), func(ptTracker[9].get_value()))))
        )

        l1 = DashedLine(ptA, points[1], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(ptA, points[1],dashed_ratio=0.7)))
        l2 = DashedLine(points[1], points[2], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[1], points[2], dashed_ratio=0.7)))
        l3 = DashedLine(points[2], points[3], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[2], points[3], dashed_ratio=0.7)))
        l4 = DashedLine(points[3], points[4], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[3], points[4], dashed_ratio=0.7)))
        l5 = DashedLine(points[4], points[5], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[4], points[5], dashed_ratio=0.7)))

        l6 = DashedLine(points[5], points[6], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[5], points[6], dashed_ratio=0.7)))
        l7 = DashedLine(points[6], points[7], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[6], points[7], dashed_ratio=0.7)))
        l8 = DashedLine(points[7], points[8], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[7], points[8], dashed_ratio=0.7)))
        l9 = DashedLine(points[8], points[9], dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[8], points[9], dashed_ratio=0.7)))
        l0 = DashedLine(points[9], ptB, dashed_ratio=0.7).add_updater(lambda m: m.become(DashedLine(points[9], ptB, dashed_ratio=0.7)))


        s.wait(wt)
        s.play(Create(l1))
        s.wait(wt)
        t0 = MathTex(r"L \approx", r"\left|P_0P_n \right|").shift(DOWN*2)
        s.play(Create(t0))
        s.wait(wt)

        s.add(points[1], points[2], points[3], points[4], points[5], points[6], points[7], points[8], points[9],
            l2, l3, l4, l5, l6, l7, l8, l9, l0)

        mid = x_2 - x_1

        s.play(ptTracker[1].animate.set_value(x_1 + mid/2))
        s.wait(wt)

        ptlabel1 = Tex("$P_1$").scale(0.6).next_to(points[1],UP).add_updater(lambda m: m.become(Tex("$P_1$").scale(0.6).next_to(points[1],UP)))

        s.add(ptlabel1)
        t1 = MathTex(r"L \approx", r"\left|P_0P_1 \right|", r"+ \left| P_1P_n \right|").shift(DOWN*2)
        s.play(ReplacementTransform(t0,t1))
        s.wait(wt)

        s.play(ptTracker[1].animate.set_value(x_1 + mid/3), ptTracker[2].animate.set_value(x_1 + 2 * mid/3))
        s.wait(wt)

        ptlabel2 = Tex("$P_2$").scale(0.6).next_to(points[2],UP).add_updater(lambda m: m.become(Tex("$P_2$").scale(0.6).next_to(points[2],UP)))

        s.add(ptlabel2)
        t0 = MathTex(r"L \approx", r"\left|P_0P_1 \right|", r"+\left|P_1P_2\right|",r"+ \left| P_2P_n \right|").shift(DOWN*2)
        s.play(ReplacementTransform(t1,t0))

        s.wait(wt)

        s.play(ptTracker[1].animate.set_value(x_1 + mid/4),
            ptTracker[2].animate.set_value(x_1 + 2 * mid/4),
            ptTracker[3].animate.set_value(x_1 + 3 * mid/4))
        s.wait(wt)
        ptlabel3 = Tex("$P_3$").scale(0.6).next_to(points[3],UP).add_updater(lambda m: m.become(Tex("$P_3$").scale(0.6).next_to(points[3],UP)))
        s.add(ptlabel3)
        t1 = MathTex(r"L \approx", r"\left|P_0P_1 \right|", r"+\left|P_1P_2\right|","+\cdots +",r" \left| P_{n-1}P_n \right|").shift(DOWN*2)
        s.play(ReplacementTransform(t0,t1))
        s.wait(wt)

        s.play(ptTracker[1].animate.set_value(x_1 + mid/5),
            ptTracker[2].animate.set_value(x_1 + 2 * mid/5),
            ptTracker[3].animate.set_value(x_1 + 3 * mid/5),
            ptTracker[4].animate.set_value(x_1 + 4 * mid/5),)
        s.wait(wt)
        ptlabel4 = Tex("$P_4$").scale(0.6).next_to(points[4],UP).add_updater(lambda m: m.become(Tex("$P_4$").scale(0.6).next_to(points[4],UP)))
        s.add(ptlabel4)
        t0 = MathTex(r"L \approx", r"\left|P_0P_1 \right|", r"+\left|P_1P_2\right|","+\cdots +",r"\left|P_{n-2}P_{n-1}\right|", r"+ \left| P_{n-1}P_n \right|").shift(DOWN*2)
        s.play(ReplacementTransform(t1,t0))
        s.wait(wt)

        s.play(ptTracker[1].animate.set_value(x_1 + mid/6),
            ptTracker[2].animate.set_value(x_1 + 2 * mid/6),
            ptTracker[3].animate.set_value(x_1 + 3 * mid/6),
            ptTracker[4].animate.set_value(x_1 + 4 * mid/6),
            ptTracker[5].animate.set_value(x_1 + 5 * mid/6),)
        s.wait(wt)
        ptlabel5 = Tex("$P_5$").scale(0.6).next_to(points[5],UP).add_updater(lambda m: m.become(Tex("$P_5$").scale(0.6).next_to(points[5],UP)))
        s.add(ptlabel5)
        s.wait(wt)

        s.play(ptTracker[1].animate.set_value(x_1 + mid/7),
            ptTracker[2].animate.set_value(x_1 + 2 * mid/7),
            ptTracker[3].animate.set_value(x_1 + 3 * mid/7),
            ptTracker[4].animate.set_value(x_1 + 4 * mid/7),
            ptTracker[5].animate.set_value(x_1 + 5 * mid/7),
            ptTracker[6].animate.set_value(x_1 + 6 * mid/7),)
        s.wait(wt)
        ptlabel6 = Tex("$P_{n-1}$").scale(0.6).next_to(points[6],UP).add_updater(lambda m: m.become(Tex("$P_{n-1}$").scale(0.6).next_to(points[6],UP)))
        s.add(ptlabel6)
        s.wait(wt)

        s.remove(ptlabel6)
        s.play(ptTracker[1].animate.set_value(x_1 + mid/8),
            ptTracker[2].animate.set_value(x_1 + 2 * mid/8),
            ptTracker[3].animate.set_value(x_1 + 3 * mid/8),
            ptTracker[4].animate.set_value(x_1 + 4 * mid/8),
            ptTracker[5].animate.set_value(x_1 + 5 * mid/8),
            ptTracker[6].animate.set_value(x_1 + 6 * mid/8),
            ptTracker[7].animate.set_value(x_1 + 7 * mid/8),)
        s.wait(wt)
        ptlabel6 = Tex("$P_{n-2}$").scale(0.6).next_to(points[6],UP).add_updater(lambda m: m.become(Tex("$P_{n-2}$").scale(0.6).next_to(points[6],UP)))
        ptlabel7 = Tex("$P_{n-1}$").scale(0.6).next_to(points[7],UP).add_updater(lambda m: m.become(Tex("$P_{n-1}$").scale(0.6).next_to(points[7],UP)))
        s.add( ptlabel6, ptlabel7)
        s.wait(wt)

        s.remove(ptlabel6, ptlabel7)
        s.play(ptTracker[1].animate.set_value(x_1 + mid/9),
            ptTracker[2].animate.set_value(x_1 + 2 * mid/9),
            ptTracker[3].animate.set_value(x_1 + 3 * mid/9),
            ptTracker[4].animate.set_value(x_1 + 4 * mid/9),
            ptTracker[5].animate.set_value(x_1 + 5 * mid/9),
            ptTracker[6].animate.set_value(x_1 + 6 * mid/9),
            ptTracker[7].animate.set_value(x_1 + 7 * mid/9),
            ptTracker[8].animate.set_value(x_1 + 8 * mid/9),)
        s.wait(wt)
        ptlabel6 = Tex("$P_{n-3}$").scale(0.6).next_to(points[6],UP).add_updater(lambda m: m.become(Tex("$P_{n-3}$").scale(0.6).next_to(points[6],UP)))
        ptlabel7 = Tex("$P_{n-2}$").scale(0.6).next_to(points[7],UP).add_updater(lambda m: m.become(Tex("$P_{n-2}$").scale(0.6).next_to(points[7],UP)))
        ptlabel8 = Tex("$P_{n-1}$").scale(0.6).next_to(points[8],UP).add_updater(lambda m: m.become(Tex("$P_{n-1}$").scale(0.6).next_to(points[8],UP)))

        s.add( ptlabel6, ptlabel7, ptlabel8)
        s.wait(wt)

        s.remove(ptlabel6, ptlabel7,ptlabel8)
        s.play(ptTracker[1].animate.set_value(x_1 + mid/11),
            ptTracker[2].animate.set_value(x_1 + 2 * mid/11),
            ptTracker[3].animate.set_value(x_1 + 3 * mid/11),
            ptTracker[4].animate.set_value(x_1 + 4 * mid/11),
            ptTracker[5].animate.set_value(x_1 + 5 * mid/11),
            ptTracker[6].animate.set_value(x_1 + 6 * mid/11),
            ptTracker[7].animate.set_value(x_1 + 8 * mid/11),
            ptTracker[8].animate.set_value(x_1 + 9 * mid/11),
            ptTracker[9].animate.set_value(x_1 + 10 * mid/11),)
        s.wait(wt)
        ptlabel6 = Tex("$P_{i-1}$").scale(0.75).next_to(points[6],UP).add_updater(lambda m: m.become(Tex("$P_{i-1}$").scale(0.75).next_to(points[6],UP).set_color(YELLOW)))
        ptlabel7 = Tex("$P_{i}$").scale(0.75).next_to(points[7],UP).add_updater(lambda m: m.become(Tex("$P_{i}$").scale(0.75).next_to(points[7],UP).set_color(YELLOW)))
        ptlabel8 = Tex("$P_{n-2}$").scale(0.6).next_to(points[8],UP).add_updater(lambda m: m.become(Tex("$P_{n-2}$").scale(0.6).next_to(points[8],UP)))
        ptlabel9 = Tex("$P_{n-1}$").scale(0.6).next_to(points[9],UP).add_updater(lambda m: m.become(Tex("$P_{n-1}$").scale(0.6).next_to(points[9],UP)))
        s.add( ptlabel6, ptlabel7, ptlabel8, ptlabel9)
        t1 = MathTex(r"L \approx", r"\left|P_0P_1 \right|", r"+\left|P_1P_2\right|","+\cdots +",r"\left|P_{i-1}P_i\right|","+\cdots +",r"\left|P_{n-2}P_{n-1}\right|", r"+ \left| P_{n-1}P_n \right|").shift(DOWN*2).scale(0.7)
        s.play(ReplacementTransform(t0,t1))
        s.wait(wt)

        t0 = MathTex(r"L \approx", r" ", r"\displaystyle\sum_{i=1}^n"," ",r"\left|P_{i-1}P_i\right|"," ",r" ", r" ").shift(DOWN*2)
        s.play(ReplacementTransform(t1,t0))
        s.wait(wt)

        t1 = MathTex(r"L =", r" \lim_{n \to +\infty}", r"\displaystyle\sum_{i=1}^n"," ",r"\left|P_{i-1}P_i\right|"," ",r" ", r" ").shift(DOWN*2)
        s.play(ReplacementTransform(t0,t1))
        s.wait(wt)



######################

class A02(Scene):
    def construct(s):

        scale = 1
        wt = 2    #wait time

        ax = Axes(
            x_range = [-0.5,8.5,9],
            x_length = 8.5 * scale,
            y_range = [-0.5, 8,9],
            y_length = 5.5 * scale*0.75,
        )

        def func(x):
            return 0.5 * x * np.sin(x-1) + 5

        x_1 = 0.5
        x_2 = 7.5
        mid = x_2 - x_1

        trace = ax.plot(func, x_range=[-1,8.4], color = BLUE)
        arc = ax.plot(func, x_range=[x_1,x_2], color = RED)
        ptA = Dot(ax.c2p(x_1,func(x_1)))
        ptB = Dot(ax.c2p(x_2,func(x_2)))
        endptA = ax.get_T_label(x_val=x_1, graph=arc, label=Tex("a").scale(0.7), triangle_size=0.1)
        endptB = ax.get_T_label(x_val=x_2, graph=arc, label=Tex("b").scale(0.7), triangle_size=0.1)
        labelA = Tex("$A$").scale(0.5).next_to(Dot(ax.c2p(x_1,func(x_1))), LEFT)
        labelB = Tex("$B$").scale(0.5).next_to(Dot(ax.c2p(x_2,func(x_2))), RIGHT)
        f_label = Tex("$f(x)$").scale(0.7).next_to(Dot(ax.c2p(8,func(8))), RIGHT)


        s.add(arc, ptA, ptB)

        labelA_1 = Tex("$A(a,f(a))=P_0$").scale(0.6).next_to(Dot(ax.c2p(x_1,func(x_1))), LEFT)
        labelB_1 = Tex("$B(b,f(b))=P_n$").scale(0.6).next_to(Dot(ax.c2p(x_2,func(x_2))), RIGHT)

        s.add(labelA_1, labelB_1)

        points=[]
        for i in range(0,10):
            if i < 7:
                point_temp = Dot(ax.c2p(x_1 + i * mid/11, func(x_1 + i * mid/11)))
            else:
                point_temp = Dot(ax.c2p(x_1 + (i+1) * mid/11, func(x_1 + (i+1) * mid/11)))
            points.append(point_temp)

        l1 = DashedLine(ptA, points[1], dashed_ratio=0.7)
        l2 = DashedLine(points[1], points[2], dashed_ratio=0.7)
        l3 = DashedLine(points[2], points[3], dashed_ratio=0.7)
        l4 = DashedLine(points[3], points[4], dashed_ratio=0.7)
        l5 = DashedLine(points[4], points[5], dashed_ratio=0.7)

        l6 = DashedLine(points[5], points[6], dashed_ratio=0.7)
        l7 = DashedLine(points[6], points[7], dashed_ratio=0.7)
        l8 = DashedLine(points[7], points[8], dashed_ratio=0.7)
        l9 = DashedLine(points[8], points[9], dashed_ratio=0.7)
        l0 = DashedLine(points[9], ptB, dashed_ratio=0.7)

        ptlabel1 = Tex("$P_1$").scale(0.6).next_to(points[1],UP)
        ptlabel2 = Tex("$P_2$").scale(0.6).next_to(points[2],UP)
        ptlabel3 = Tex("$P_3$").scale(0.6).next_to(points[3],UP)
        ptlabel4 = Tex("$P_4$").scale(0.6).next_to(points[4],UP)
        ptlabel5 = Tex("$P_5$").scale(0.6).next_to(points[5],UP)

        ptlabel6 = Tex("$P_{i-1}$").scale(0.75).next_to(points[6],UP).set_color(YELLOW)
        ptlabel7 = Tex("$P_{i}$").scale(0.75).next_to(points[7],UP).set_color(YELLOW)
        ptlabel8 = Tex("$P_{n-2}$").scale(0.6).next_to(points[8],UP)
        ptlabel9 = Tex("$P_{n-1}$").scale(0.6).next_to(points[9],UP)



        s.add(points[1], points[2], points[3], points[4], points[5], points[6], points[7], points[8], points[9],
            l1, l2, l3, l4, l5, l6, l7, l8, l9, l0)

        s.add(ptlabel1, ptlabel2, ptlabel3, ptlabel4, ptlabel5, ptlabel6,
            ptlabel7, ptlabel8, ptlabel9,)


        t1 = MathTex(r"L =", r" \lim_{n \to +\infty}", r"\displaystyle\sum_{i=1}^n"," ",r"\left|P_{i-1}P_i\right|"," ",r" ", r" ").shift(DOWN*2)
        s.add(t1)

        s.play(FadeOut(t1))
        s.play(FadeOut(VGroup(ptlabel1, ptlabel2, ptlabel3, ptlabel4,
            ptlabel5, ptlabel8, ptlabel9, )))
        s.play(FadeOut(VGroup(points[1], points[2], points[3], points[4], points[5], points[8], points[9],
            l1, l2, l3, l4, l5, l6, l8, l9, l0)))

        arc2 = ax.plot(func, x_range=[x_1 + 6 * mid/11,x_1 + 8 * mid/11], color = RED)
        s.add(arc2)
        s.play(FadeOut(arc),FadeIn(VGroup(ax, trace, f_label)))
        s.add(arc2)
        s.add(ptlabel6, ptlabel7, labelA_1, labelB_1)
        s.wait(wt)

        xd1 = ax.get_T_label(x_val=x_1 + 6 * mid/11, graph=arc, label=Tex("$x_{i-1}$").scale(0.7), triangle_size=0.1)
        xd2 = ax.get_T_label(x_val=x_1 + 8 * mid/11, graph=arc, label=Tex("$x_i$").scale(0.7), triangle_size=0.1)

        s.play(Create(xd1), Create(xd2))

        Plabel_left = Tex("$P_{i-1}(x_{i-1}, f(x_{i-1}))$").scale(0.6).next_to(points[6],LEFT).set_color(YELLOW)
        Plabel_right = Tex("$P_i(x_i, f(x_i))$").scale(0.6).next_to(points[7],RIGHT+DOWN).set_color(YELLOW)

        s.play(ReplacementTransform(ptlabel6, Plabel_left))
        s.play(ReplacementTransform(ptlabel7, Plabel_right))
        s.wait(wt)

        t0 = MathTex(r"\left|P_{i-1}P_i\right|=\sqrt{(x_i-x_{i-1})^2 + (y_i-y_{i-1})^2}").shift(DOWN*3)
        s.play(Create(t0))
        s.wait(wt)


#####

class MVT(Scene):
    def construct(s):

        scale = 1
        wt = 2    #wait time

        x_1 = 3
        x_2 = 6.5
        x_p1 = 4.3182
        x_p2 = 5.5909
        print(x_p1)
        print(x_p2)


        ax = Axes(
            x_range = [2.5,7,9],
            x_length = 4.5 * scale*2,
            y_range = [1, 5,9],
            y_length = 5.5 * scale*0.8,
        )

        def func(x):
            return 0.5 * x * np.sin(x-1) + 5

        print(func(x_p1))
        print(func(x_p2))


        trace = ax.plot(func, x_range=[2.8,6.7], color = BLUE)
        arc2 = ax.plot(func, x_range=[x_p1, x_p2], color = RED)

        ptA = Dot(ax.c2p(x_p1,func(x_p1)))
        ptB = Dot(ax.c2p(x_p2,func(x_p2)))

        l_AB = DashedLine(ptA, ptB, dashed_ratio=0.7)

        s.add(ax,trace,arc2,ptA,ptB, l_AB)
