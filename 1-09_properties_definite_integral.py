from manim import *
import scipy.integrate as  integrate

class prop1(Scene):
    def construct(s):

        prop1Title = Text("Property 1", font="Montserrat").shift(UP*3)
        prop1DescA = MathTex(r"\text{If }", "\int_a^b f(x) \, dx", r"\text{ exists, then }", "\int","_a","^b", "f(x)\, dx = -\int","_b","^a", "f(x) \, dx").shift(UP)
        for i in range(3,10):
            prop1DescA[i].set_color(YELLOW)
        prop1DescA[4].set_color(BLUE)
        prop1DescA[5].set_color(RED)
        prop1DescA[8].set_color(BLUE)
        prop1DescA[7].set_color(RED)
        s.play(Write(prop1Title))
        s.play(Write(prop1DescA))
        s.wait(1)

        t1 = MathTex(r"\int","_a","^b", r"f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i)\,", "\Delta x").scale(0.5).shift(DOWN+LEFT*3)
        t1[4].set_color(YELLOW)
        t1[1].set_color(BLUE)
        t1[2].set_color(RED)
        t2 = MathTex("\Delta x =  {b-a \over n }").scale(0.5).next_to(t1,RIGHT*3).set_color(YELLOW)

        t3 = MathTex(r"\int","_b","^a", r"f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i)\,", "\Delta x").scale(0.5).next_to(t1,DOWN)
        t3[4].set_color(GREEN)
        t3[1].set_color(RED)
        t3[2].set_color(BLUE)
        t4 = MathTex("\Delta x =  {a-b \over n }","=-","{b-a \over n}").scale(0.5).next_to(t3,RIGHT*3).set_color(GREEN)
        t4[2].set_color(YELLOW)

        #t2 = MathTex("\Delta x = {b - a \over n}").scale(0.6).next_to(t1,DOWN)

        s.play(Write(t1))
        s.play(Write(t2))
        s.wait(2)
        s.play(Write(t3))
        s.play(Write(t4))
        s.wait(2)

class prop2(Scene):
    def construct(s):

        propTitle = Text("Property 2", font="Montserrat").shift(UP*3)
        propDescA = MathTex(r"\text{If }", "f(a)", r"\text{ exists, then }", "\int_a^a f(x)\, dx = 0").shift(UP)
        propDescA[3].set_color(YELLOW)
        s.play(Write(propTitle))
        s.play(Write(propDescA))
        s.wait(2)

        ax = Axes(
            x_range = [-0.8, 6, 10],
            y_range = [-0.8, 6, 10],
            x_length = 6,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=True
        ).shift(DOWN*2+LEFT*3)
        ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        func = ax.get_graph(lambda x: np.sin(3*x-3)/(x-1) + 2, color = RED)
        func_label = ax.get_graph_label(func, "f(x)", x_val = 4, direction=UP).scale(0.5)

        t_label  = ax.get_T_label(x_val=1.1,graph=func,label=MathTex("a").scale(0.6),triangle_size=0.15)

        s.play(Create(ax),FadeIn(ax_label))
        s.play(Create(func), FadeIn(func_label))
        s.play(Create(t_label))

        s.wait(1)

class prop3(Scene):
    def construct(s):

        propTitle = Text("Property 3", font="Montserrat").shift(UP*3)
        propDescA = MathTex("\int_a^b c \cdot dx = c\cdot(b-a)").shift(UP)
        #propDescA[3].set_color(YELLOW)
        s.play(Write(propTitle))
        s.play(Write(propDescA))
        s.wait(2)

        ax = Axes(
            x_range = [-0.8, 6, 10],
            y_range = [-0.8, 6, 10],
            x_length = 4,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=True
        ).shift(DOWN*2+LEFT*4)
        ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        func = ax.get_graph(lambda x: 4, color = BLUE)
        func_label = ax.get_graph_label(func, "f(x)=c", x_val = 4, direction=UP).scale(0.5)

        a_label  = ax.get_T_label(x_val=1.1,graph=func,label=MathTex("a").scale(0.6),triangle_size=0.15)
        b_label  = ax.get_T_label(x_val=5,graph=func,label=MathTex("b").scale(0.6),triangle_size=0.15)
        area = ax.get_area(func, x_range=[1.1,5], opacity=0.3)

        s.play(Create(ax),FadeIn(ax_label))
        s.play(Create(func), FadeIn(func_label))
        s.play(Create(a_label), Create(b_label))
        s.wait(0.5)
        s.play(Create(area))
        s.wait(2)
        s.play(FadeOut(ax),FadeOut(ax_label),FadeOut(func),FadeOut(func_label),FadeOut(a_label),FadeOut(b_label),FadeOut(area))

        ax = Axes(
            x_range = [-0.8, 6, 10],
            y_range = [-6, 0.8, 10],
            x_length = 4,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=False
        ).shift(DOWN*2+LEFT*4)
        ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        func = ax.get_graph(lambda x: -4, color = BLUE)
        func_label = ax.get_graph_label(func, "f(x)=c,c<0", x_val = 4, direction=DOWN).scale(0.5)

        a_label  = ax.get_graph_label(ax.get_graph(lambda x:0), "a", x_val = 1.1, direction=UP).scale(0.5)
        b_label  = ax.get_graph_label(ax.get_graph(lambda x:0), "b", x_val = 5, direction=UP).scale(0.5)

        a_line  = ax.get_T_label(x_val=1.1,graph=func,triangle_size=0)
        b_line  = ax.get_T_label(x_val=5,graph=func,triangle_size=0.)
        area = ax.get_area(func, x_range=[1.1,5], opacity=0.3, color=RED)

        s.play(Create(ax),FadeIn(ax_label))
        s.play(Create(func), FadeIn(func_label))
        s.play(Create(a_label), Create(b_label), Create(a_line),Create(b_line))
        s.wait(0.5)
        s.play(Create(area))

        s.wait(1)

class prop4(Scene):
    def construct(s):

        propTitle = Text("Property 4", font="Montserrat").shift(UP*3)
        propDescA = MathTex(r"\int_a^b","c", "\cdot f(x) \, dx = ", "c", "\int_a^b f(x) \, dx").shift(UP)
        propDescA[1].set_color(RED)
        propDescA[3].set_color(RED)
        s.play(Write(propTitle))
        s.play(Write(propDescA))
        s.wait(1)

        t1 = MathTex(r"\int_a^b","c","\cdot f(x) \, dx =", " ", r"\lim_{n\to\infty}", "  ", "\sum_{i=1}^n", r"c \cdot", "f(x) \, \Delta x").scale(0.7).shift(DOWN+LEFT*3)
        t1[1].set_color(RED)
        t1[7].set_color(RED)
        s.play(FadeIn(t1))
        s.wait(1)

        t2 = MathTex(r"\int_a^b","c","\cdot f(x) \, dx =", " ", r"\lim_{n\to\infty}", "c \cdot", "\sum_{i=1}^n", " ", "f(x) \, \Delta x").scale(0.7).shift(DOWN+LEFT*3)
        t2[1].set_color(RED)
        t2[5].set_color(RED)
        s.play(ReplacementTransform(t1,t2))
        s.wait(1)

        t1 = MathTex(r"\int_a^b","c","\cdot f(x) \, dx =", "c \cdot", r"\lim_{n\to\infty}", " ", "\sum_{i=1}^n", " ", "f(x) \, \Delta x").scale(0.7).shift(DOWN+LEFT*3)
        t1[1].set_color(RED)
        t1[3].set_color(RED)
        s.play(ReplacementTransform(t2,t1))
        s.wait(1)

        t2 = MathTex(r"\int_a^b","c","\cdot f(x) \, dx =", "c \cdot", " ", "\int_a^b f(x)\, dx", " ", " ", " ").scale(0.8).shift(DOWN+LEFT*3)
        t2[1].set_color(RED)
        t2[3].set_color(RED)
        s.play(ReplacementTransform(t1,t2))

        s.wait(2)

class prop5(Scene):
    def construct(s):

        propTitle = Text("Property 5/6: Sums and differences", font="Montserrat").shift(UP*3)
        propDescA = MathTex(r"\int_a^b \left[ f(x) \pm g(x) \right] \, dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx").shift(UP)
        s.play(Write(propTitle))
        s.play(Write(propDescA))
        s.wait(1)

        ax1 = Axes(
            x_range = [-0.8, 6.5, 10],
            y_range = [-0.8, 6.5, 10],
            x_length = 3,
            y_length = 2,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=False
        ).shift(DOWN*2+LEFT*5)

        ax2 = Axes(
            x_range = [-0.8, 6.5, 10],
            y_range = [-0.8, 6.5, 10],
            x_length = 3,
            y_length = 2,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=False
        ).shift(DOWN*2+LEFT)

        ax3 = Axes(
            x_range = [-0.8, 6.5, 10],
            y_range = [-0.8, 6.5, 10],
            x_length = 3,
            y_length = 2,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=False
        ).shift(DOWN*2+RIGHT*3)

        func = ax1.get_graph(lambda x: (x * np.sin(2*x)) /3 + 2, color=BLUE)
        func_label = ax1.get_graph_label(func, "f(x)", x_val = 4, direction=UP).scale(0.5)
        a_f  = ax1.get_T_label(x_val=1,graph=func,label=MathTex("a").scale(0.6),triangle_size=0.15)
        b_f  = ax1.get_T_label(x_val=5,graph=func,label=MathTex("b").scale(0.6),triangle_size=0.15)
        rect_f = ax1.get_riemann_rectangles(func, x_range=[1,5], dx=0.5, input_sample_type='center',color=BLUE)
        area_f = ax1.get_area(func,x_range=[1,5],color=BLUE,opacity=1)

        gunc = ax3.get_graph(lambda x: (x -3)**2 /3 + 1, color=PURPLE)
        gunc_label = ax3.get_graph_label(gunc, "g(x)", x_val = 4, direction=UP).scale(0.5)
        a_g  = ax3.get_T_label(x_val=1,graph=gunc,label=MathTex("a").scale(0.6),triangle_size=0.15)
        b_g  = ax3.get_T_label(x_val=5,graph=gunc,label=MathTex("b").scale(0.6),triangle_size=0.15)
        rect_g = ax3.get_riemann_rectangles(gunc, x_range=[1,5], dx=0.5, input_sample_type='center',color=PURPLE)
        area_g = ax3.get_area(gunc,x_range=[1,5],color=PURPLE,opacity=1)

        sumfunc = ax2.get_graph(lambda x: (x * np.sin(2*x)) /3 +(x -3)**2 /3 + 3, color=RED)
        sumfunc_label = ax2.get_graph_label(sumfunc, "f(x)+g(x)", x_val = 4, direction=UP).scale(0.5)
        a_s  = ax2.get_T_label(x_val=1,graph=sumfunc,label=MathTex("a").scale(0.6),triangle_size=0.15)
        b_s  = ax2.get_T_label(x_val=5,graph=sumfunc,label=MathTex("b").scale(0.6),triangle_size=0.15)
        f_in_sum = ax2.get_graph(lambda x: (x * np.sin(2*x)) /3 + 2, color=BLUE)
        rect_g_in_sum = ax2.get_riemann_rectangles(sumfunc, x_range=[1,5], dx=0.5, input_sample_type='center',color=PURPLE)
        rect_f_in_sum = ax2.get_riemann_rectangles(f_in_sum, x_range=[1,5], dx=0.5, input_sample_type='center',color=BLUE)
        area_g_in_sum = ax2.get_area(sumfunc,x_range=[1,5],color=PURPLE,opacity=1)
        area_f_in_sum = ax2.get_area(f_in_sum,x_range=[1,5],color=BLUE,opacity=1)

        s.play(Create(ax1), Create(ax2),Create(ax3))
        s.play(Create(func), Create(gunc), FadeIn(func_label),FadeIn(gunc_label))
        s.wait(1)
        s.play(Create(sumfunc), FadeIn(sumfunc_label))
        s.wait(1)
        s.play(Create(a_f), Create(b_f), Create(a_g), Create(b_g), Create(a_s), Create(b_s))
        s.wait(1)
        s.play(Create(rect_f),Create(rect_f_in_sum))
        s.wait(1)
        # Rearrange objects
        s.mobjects = [rect_f, rect_f_in_sum, rect_g, rect_g_in_sum] + s.mobjects
        s.play(Create(rect_g), Create(rect_g_in_sum))
        s.wait(1)

        s.play(ReplacementTransform(rect_g,area_g), ReplacementTransform(rect_g_in_sum,area_g_in_sum))
        s.remove(rect_f_in_sum)
        s.add(rect_f_in_sum)
        s.wait(1)
        #s.mobjects = [area_f_in_sum, rect_f_in_sum,area_g_in_sum] + s.mobjects
        s.play(ReplacementTransform(rect_f,area_f), ReplacementTransform(rect_f_in_sum,area_f_in_sum))

        s.wait(1)



class prop6(Scene):
    def construct(s):

        propTitle = Text("Property 7", font="Montserrat").shift(UP*3)
        propDescA = MathTex(r"\int", "_a", "^", "c", "f(x) \, dx + \int^b", "_c", "f(x) \, dx = \int_a^b f(x) \, dx").shift(UP)
        s.play(Write(propTitle))
        s.play(FadeIn(propDescA))
        s.wait(1)

        ax = Axes(
            x_range = [-0.8, 6, 10],
            y_range = [-0.8, 6, 10],
            x_length = 6,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=False
        ).shift(DOWN*2+LEFT*3)
        #ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        func = ax.get_graph(lambda x: (x * np.sin(2*x)) /3 + 3, color = RED)
        func_label = ax.get_graph_label(func, "f(x)", x_val = 4, direction=UP).scale(0.5)

        a_label  = ax.get_T_label(x_val=1.7,graph=func,label=MathTex("a").scale(0.6),triangle_size=0.15)
        b_label  = ax.get_T_label(x_val=4.3,graph=func,label=MathTex("b").scale(0.6),triangle_size=0.15)

        s.play(Create(ax))#,FadeIn(ax_label))
        s.play(Create(func), FadeIn(func_label))
        s.play(Create(a_label), Create(b_label))
        s.wait(1)

        # a < c < b
        c_label = ax.get_T_label(x_val=3.3,graph=func,label=MathTex("c").scale(0.6),triangle_size=0.15)
        s.play(Create(c_label))
        s.wait(1)

        ac_area = ax.get_area(func,x_range=[1.7,3.3],color=GREEN)
        s.play(Create(ac_area))
        s.wait(1)
        cb_area = ax.get_area(func,x_range=[3.3,4.3],color=BLUE)
        s.play(Create(cb_area))
        s.wait(1)

        s.play(FadeOut(ac_area),FadeOut(cb_area),FadeOut(c_label))
        s.wait(1)

        # c < a < b
        c_label = ax.get_T_label(x_val=1,graph=func,label=MathTex("c").scale(0.6),triangle_size=0.15)
        s.play(Create(c_label))
        s.wait(1)

        cb_area = ax.get_area(func,x_range=[1,4.3],color=BLUE)
        s.play(Create(cb_area))
        s.wait(1)
        ac_area = ax.get_area(func,x_range=[1,1.7],color=RED)
        s.play(Create(ac_area))
        s.wait(1)

        ab_area = ax.get_area(func,x_range=[1.7,4.3],color=BLUE)
        s.play(FadeOut(ac_area),ReplacementTransform(cb_area,ab_area),FadeOut(c_label))
        s.wait(1)
        s.play(FadeOut(ab_area))
        s.wait(1)

        # a < b < c
        c_label = ax.get_T_label(x_val=5.5,graph=func,label=MathTex("c").scale(0.6),triangle_size=0.15)
        s.play(Create(c_label))
        s.wait(1)

        ac_area = ax.get_area(func,x_range=[1.7,5.5],color=BLUE)
        s.play(Create(ac_area))
        s.wait(1)

        cb_area = ax.get_area(func,x_range=[4.3,5.5],color=RED)
        s.play(Create(cb_area))
        s.wait(1)

        ab_area = ax.get_area(func,x_range=[1.7,4.3],color=BLUE)
        s.play(FadeOut(cb_area),ReplacementTransform(ac_area,ab_area),FadeOut(c_label))
        s.wait(1)

        s.play(FadeOut(propTitle),FadeOut(propDescA))
        s.wait(1)

        propTitle = Text("Property 8", font="Montserrat").shift(UP*3)
        propDescA = MathTex(r"\text{If } f(x)>0 \text{ for } a \leq x \leq b \text{ then } \int_a^b f(x)\, dx \geq 0 ").shift(UP)
        s.play(Write(propTitle))
        s.play(FadeIn(propDescA))
        s.wait(1)



        s.wait(1)


class prop7(Scene):
    def construct(s):

        propTitle = Text("Property 9", font="Montserrat").shift(UP*3)
        propDescA = MathTex(r"\text{If } f(x)\geq g(x) \text{ for } a \leq x \leq b \text{ then }", "\int_a^b f(x)\,dx \geq \int_a^b g(x) \, dx").shift(UP).scale(0.9)
        propDescA[1].set_color(YELLOW)
        s.play(Write(propTitle))
        s.play(FadeIn(propDescA))
        s.wait(1)

        ax = Axes(
            x_range = [-0.8, 6.5, 10],
            y_range = [-0.8, 6.5, 10],
            x_length = 6,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=False
        ).shift(DOWN*2+LEFT*3)
        #ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        s.play(Create(ax))

        sumfunc = ax.get_graph(lambda x: (x * np.sin(2*x)) /3 +(x -3)**2 /3 + 3, color=RED)
        sumfunc_label = ax.get_graph_label(sumfunc, "f(x)", x_val = 1, direction=UP).scale(0.5)
        a_s  = ax.get_T_label(x_val=1,graph=sumfunc,label=MathTex("a").scale(0.6),triangle_size=0.15)
        b_s  = ax.get_T_label(x_val=5,graph=sumfunc,label=MathTex("b").scale(0.6),triangle_size=0.15)
        f_in_sum = ax.get_graph(lambda x: (x * np.sin(2*x)) /3 + 2, color=BLUE)
        f_label = ax.get_graph_label(f_in_sum, "g(x)", x_val = 0.5, direction=UP).scale(0.5)
        area_g_in_sum = ax.get_area(sumfunc,x_range=[1,5],color=RED)
        area_f_in_sum = ax.get_area(f_in_sum,x_range=[1,5],color=BLUE)

        s.play(Create(sumfunc), FadeIn(sumfunc_label))
        s.wait(1)
        s.play(Create(f_in_sum), FadeIn(f_label))
        s.play(Create(a_s),Create(b_s))
        s.wait(1)
        s.play(Create(area_g_in_sum))
        s.wait(1)
        s.play(Create(area_f_in_sum))

        s.wait(1)


class prop8(Scene):
    def construct(s):

        propTitle = Text("Property 10", font="Montserrat").shift(UP*3)
        propDescA = MathTex(r"\text{If } m \leq f(x) \leq M \text{ for } a \leq x \leq b \text{ then} ").next_to(propTitle,DOWN)
        propDescB = MathTex(r"m\cdot(b-a) \leq \int_a^b f(x)\, dx \leq M \cdot (b-a)").next_to(propDescA,DOWN).set_color(YELLOW)
        #propDescA[1].set_color(YELLOW)
        s.play(Write(propTitle))
        s.play(FadeIn(propDescA))
        s.play(Write(propDescB))
        s.wait(1)

        ax = Axes(
            x_range = [-0.2, 6.5, 10],
            y_range = [-0.2, 6.5, 10],
            x_length = 6,
            y_length = 3,
            axis_config={
                #"numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=False
        ).shift(DOWN*2+LEFT*3)
        #ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        s.play(Create(ax))

        bigMfunc = ax.get_graph(lambda x: 5.8, color=RED)
        smallMfunc = ax.get_graph(lambda x: 2, color=RED)
        bigMfunc_label = ax.get_graph_label(bigMfunc, "M", x_val = 0, direction=LEFT).scale(0.8)
        smallMfunc_label = ax.get_graph_label(smallMfunc, "m", x_val = 0, direction=LEFT).scale(0.8)
        s.play(FadeIn(bigMfunc_label), FadeIn(smallMfunc_label))
        s.play(Create(bigMfunc), Create(smallMfunc))
        s.wait(1)

        a_s  = ax.get_T_label(x_val=1,graph=bigMfunc,label=MathTex("a").scale(0.6),triangle_size=0.15)
        b_s  = ax.get_T_label(x_val=5,graph=bigMfunc,label=MathTex("b").scale(0.6),triangle_size=0.15)
        s.play(Create(a_s),Create(b_s))
        s.wait(1)

        func = ax.get_graph(lambda x: -(x-3)**2 / 3 + 4.5, color=GREEN)
        func_label = ax.get_graph_label(func, "f(x)", x_val = 5, direction=RIGHT*3).scale(0.8)
        s.play(Create(func),FadeIn(func_label))
        s.wait(1)

        bigMarea = ax.get_area(bigMfunc, x_range=[1,5], color = PURPLE)
        s.mobjects = [func] + s.mobjects
        s.play(Create(bigMarea))
        s.wait(1)

        area = ax.get_area(func, x_range=[1,5], color = GREEN)
        s.mobjects = [smallMfunc] + s.mobjects
        s.play(Create(area))
        s.wait(1)

        smallMarea = ax.get_area(smallMfunc, x_range=[1,5], color = BLUE)
        s.play(Create(smallMarea))
        s.wait(1)
