from manim import *
import scipy.integrate as  integrate

class Example1DefInt(Scene):
    def construct(s):

        ax = Axes(
            x_range = [0, 1.1, 1],
            y_range = [0, 1.1, 1],
            x_length = 8,
            y_length = 5,
            axis_config={
                "numbers_to_include":[1],
                "color": GREEN},
                tips=True
        )
        ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        func = ax.get_graph(lambda x: x**2, color = RED)
        func_label = ax.get_graph_label(func, "f(x)=x^2", x_val = 0.7, direction=UP*6)
        rectarea = ax.get_riemann_rectangles(func, x_range=[0,1], dx=0.05, fill_opacity=0.8, color=BLUE, input_sample_type='right')

        s.add(rectarea,func, func_label)
        s.add(ax, ax_label)


class Example2DefInt(Scene):
    def construct(s):

        ax = Axes(
            x_range = [-3, 3, 1],
            y_range = [-7, 3, 1],
            x_length = 8,
            y_length = 8,
            axis_config={
                "numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=True
        )
        ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        func = ax.get_graph(lambda x: 2*x - 2, color = RED)
        func_label = ax.get_graph_label(func, "f(x)=2x-2", x_val = 1, direction=UP+LEFT)
        rectarea = ax.get_riemann_rectangles(func, x_range=[-2,2], dx=0.25, fill_opacity=0.8, color=BLUE, input_sample_type='center')

        s.add(rectarea,func)
        s.add(ax, ax_label)


class Example3DefInt(Scene):
    def construct(s):

        ax = Axes(
            x_range = [-1, 3, 1],
            y_range = [-2, 4, 1],
            x_length = 8,
            y_length = 5,
            axis_config={
                "numbers_to_include":[-2, -1,1,2],
                "color": GREEN},
                tips=True
        )
        ax_label = ax.get_axis_labels(x_label="x", y_label="y")

        func = ax.get_graph(lambda x: x**3 - 3*x**2 + 3, color = RED)
        func_label = ax.get_graph_label(func, "f(x)=2x-2", x_val = 1, direction=UP+LEFT)
        rectarea = ax.get_riemann_rectangles(func, x_range=[0,2], dx=0.05, fill_opacity=0.8, color=BLUE, input_sample_type='right')

        s.add(rectarea,func)
        s.add(ax, ax_label)
