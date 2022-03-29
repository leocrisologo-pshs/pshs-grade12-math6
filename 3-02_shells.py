from re import L
from manim import *

class ShellsIntro(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=-30*DEGREES, theta = -PI/2)

        scale = 0.5
        waitdelay = 2

        ax = ThreeDAxes(
            x_range = [-7,7,1],
            x_length = 14 * scale,
            y_range = [-1, 6, 1],
            y_length = 7 * scale,
            z_range=[-2,2,1],
            z_length = 4 * scale,
        )

        def func(x):
            return 0.5 * x * np.sin(x) + (7/2)

        trace = ax.plot(func, x_range=[0,7], color = BLUE)
        function = ax.plot(func, x_range=[1,6], color = YELLOW)
        region = ax.get_area(function,x_range=[1,6], color = [BLUE_B, BLUE_D])
        bound_left = ax.get_T_label(x_val=1, graph=function, label=Tex("a").scale(0.7), triangle_size=0.1)
        bound_right = ax.get_T_label(x_val=6, graph=function, label=Tex("b").scale(0.7), triangle_size=0.1)

        e = ValueTracker(2 * PI)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), 0.5*v*np.sin(v) + 3.5, v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,6],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        outside = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    6*np.cos(u), v, 6*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,2.66],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        inside = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1*np.cos(u), v, 1*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,3.92],
                checkerboard_colors = [GREEN_B, GREEN_D],
            )
        )

#        s.add(ax, trace, function, region, bound_left, bound_right)
        s.play(LaggedStart(Create(ax), Create(trace), Create(bound_left),Create(bound_right), Create(function)))
        s.wait(waitdelay)
        s.add(region)
        s.wait(waitdelay)

        s.move_camera(phi=-30*DEGREES)

        s.play(
            Rotating(
                VGroup(function, region),
                axis=DOWN,
                radians=2 * PI,
                about_point=ax.c2p(0, 0, 0),
            ),
            e.animate.set_value(2 * PI),
            run_time=5,
            rate_func=linear,
        )

        s.wait(waitdelay)
        s.play(Create(surface),Create(outside), Create(inside))
        s.wait(waitdelay)

        s.move_camera(phi=0*DEGREES)
        s.wait(waitdelay)
        s.play(FadeOut(surface), FadeOut(outside), FadeOut(inside))
        s.wait(waitdelay)

######################

class ShellsDiff(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        scale = 0.5
        waitdelay = 2

        ax = ThreeDAxes(
            x_range = [-7,7,1],
            x_length = 14 * scale,
            y_range = [-1, 6, 1],
            y_length = 7 * scale,
            z_range=[-2,2,1],
            z_length = 4 * scale,
        )

        def func(x):
            return 0.5 * x * np.sin(x) + (7/2)

        trace = ax.plot(func, x_range=[0,7], color = BLUE)
        function = ax.plot(func, x_range=[1,6], color = YELLOW)
        region = ax.get_area(function,x_range=[1,6], color = [BLUE_B, BLUE_D])
        bound_left = ax.get_T_label(x_val=1, graph=function, label=Tex("a").scale(0.7), triangle_size=0.1)
        bound_right = ax.get_T_label(x_val=6, graph=function, label=Tex("b").scale(0.7), triangle_size=0.1)

        diffrect = ax.get_riemann_rectangles(function, x_range=[2.8,3], dx=0.21, input_sample_type="center",color=[RED_B,RED_D])

        e = ValueTracker(2 * PI)

        top = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), 3.847, v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[2.8,3],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        outside = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    3*np.cos(u), v, 3*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,3.847],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        inside = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    2.8*np.cos(u), v, 2.8*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,3.847],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s.add(ax, trace, function, region, bound_left, bound_right)
        s.play(Create(diffrect))
        s.wait(waitdelay)

        s.move_camera(phi=-30*DEGREES)

        s.play(Create(top), Create(inside), Create(outside))
        s.wait(waitdelay)
        s.play(FadeOut(diffrect))
        s.wait(waitdelay)
        s.move_camera(phi=0*DEGREES)
        s.wait(waitdelay)
        s.play(FadeOut(top, inside, outside))
        s.wait(waitdelay)

######################

class CloseUp(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=-30*DEGREES, theta = -PI/2)

        scale = 1.2
        waitdelay = 2

        ax = ThreeDAxes(
            x_range = [-0.1,0.1,2],
            x_length = 0.2 * scale,
            y_range = [-3, 2, 5],
            y_length = 5 * scale,
            z_range=[-1,1,2],
            z_length = 2 * scale,
        )

        e = ValueTracker(2 * PI)

        top = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), 0, v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        outside = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    2*np.cos(u), v, 2*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[-2,0],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        inside = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    np.cos(u), v, np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[-2,0],
                checkerboard_colors = [PURPLE_B, PURPLE_E],
            )
        )

        point_1 = Dot(ax.c2p(1,0))
        point_2 = Dot(ax.c2p(1.5,0))
        point_3 = Dot(ax.c2p(2,0))
        point_4a = Dot(ax.c2p(2.5, -2))
        point_4b = Dot(ax.c2p(2.5, 0))
        y_axis = ax.get_vertical_line(ax.c2p(0,5),line_config={"dashed_ratio": 1}, color=RED_A, stroke_width=5)
        inner_v_line = ax.get_vertical_line(ax.c2p(1,1.3),line_config={"dashed_ratio": 0.9})
        mid_v_line = ax.get_vertical_line(ax.c2p(1.5,1.9),line_config={"dashed_ratio": 0.9})
        outer_v_line = ax.get_vertical_line(ax.c2p(2,2.3),line_config={"dashed_ratio": 0.9})
        h_line = ax.get_vertical_line(ax.c2p(2.5,-2),line_config={"dashed_ratio": 0.9})
        r_in = ax.plot(lambda x: 1, x_range=[0,1])
        r_mid = ax.plot(lambda x: 1.5, x_range=[0,1.5])
        r_out = ax.plot(lambda x: 2, x_range=[0,2])

#        label_a = Tex("$a$").scale(0.7).next_to(Dot().move_to(ax.c2p(1.2,0)),DOWN)

        label_r_in = Tex("$r_I$").scale(0.5).next_to(Dot(ax.c2p(0.5,0.8)), UP)
        label_r_mid = Tex("$m$").scale(0.5).next_to(Dot(ax.c2p(0.75,1.3)), UP)
        label_r_out = Tex("$r_O$").scale(0.5).next_to(Dot(ax.c2p(1,1.8)), UP)
        label_h = Tex("$h$").scale(0.5).next_to(Dot(ax.c2p(2.35,-1)), RIGHT)

        s.play(Create(top), Create(outside), Create(inside))
        s.wait(waitdelay)
        s.move_camera(phi=0)
        s.wait(waitdelay)
        s.play(FadeIn(VGroup(inner_v_line, mid_v_line, outer_v_line, point_1, point_2, point_3,y_axis)))
        s.play(FadeIn(VGroup(r_in, r_mid, r_out)))
        s.play(FadeIn(VGroup(point_4a, point_4b, h_line)))
        s.play(FadeIn(VGroup(label_r_in, label_r_mid, label_r_out, label_h)))
        s.wait(waitdelay)
        s.move_camera(phi=-30*DEGREES)


######################

class ManyShells1(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0*DEGREES, theta = -PI/2)

        scale = 0.5
        waitdelay = 2

        ax = ThreeDAxes(
            x_range = [-7,7,1],
            x_length = 14 * scale,
            y_range = [-1, 6, 1],
            y_length = 7 * scale,
            z_range=[-2,2,1],
            z_length = 4 * scale,
        )

        def func(x):
            return 0.5 * x * np.sin(x) + (7/2)

        trace = ax.plot(func, x_range=[0,7], color = BLUE)
        function = ax.plot(func, x_range=[1,6], color = YELLOW)
        region = ax.get_area(function,x_range=[1,6], color = [BLUE_B, BLUE_D])
        bound_left = ax.get_T_label(x_val=1, graph=function, label=Tex("a").scale(0.7), triangle_size=0.1)
        bound_right = ax.get_T_label(x_val=6, graph=function, label=Tex("b").scale(0.7), triangle_size=0.1)

        diffrect = ax.get_riemann_rectangles(function, x_range=[1,6], dx=0.5, input_sample_type="center",color=[RED_A,RED_D], fill_opacity=0.5)


        s.add(ax, trace, function, region, bound_left, bound_right)
        s.play(Create(diffrect))
        s.wait(waitdelay)
        s.move_camera(phi=-30*DEGREES)
        s.wait(waitdelay)


########


class ManyShells2(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=-30*DEGREES, theta = -PI/2)

        scale = 0.5
        waitdelay = 2

        ax = ThreeDAxes(
            x_range = [-7,7,1],
            x_length = 14 * scale,
            y_range = [-1, 6, 1],
            y_length = 7 * scale,
            z_range=[-2,2,1],
            z_length = 4 * scale,
        )

        def func(x):
            return 0.5 * x * np.sin(x) + (7/2)

        trace = ax.plot(func, x_range=[0,7], color = BLUE)
        function = ax.plot(func, x_range=[1,6], color = YELLOW)
        region = ax.get_area(function,x_range=[1,6], color = [BLUE_B, BLUE_D])
        bound_left = ax.get_T_label(x_val=1, graph=function, label=Tex("a").scale(0.7), triangle_size=0.1)
        bound_right = ax.get_T_label(x_val=6, graph=function, label=Tex("b").scale(0.7), triangle_size=0.1)

        diffrect = ax.get_riemann_rectangles(function, x_range=[1,6], dx=0.5, input_sample_type="center",color=[RED_A,RED_D], fill_opacity=0.5)

        e = ValueTracker(2 * PI)

        top01 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(1.25), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,1.5],
                checkerboard_colors = [RED_B, MAROON_D],
            )
        )

        top02 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(1.75), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1.5,2],
                checkerboard_colors = [PURPLE_D,PURPLE_D],
            )
        )

        top03 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(2.25), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[2,2.5],
                checkerboard_colors = [RED_B, MAROON_D],
            )
        )

        top04 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(2.75), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[2.5,3],
                checkerboard_colors = [RED_B, MAROON_D],
            )
        )

        top05 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(3.25), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[3,3.5],
                checkerboard_colors = [PURPLE_D,PURPLE_D],
            )
        )

        top06 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(3.75), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[3.5,4],
                checkerboard_colors = [RED_B, MAROON_D],
            )
        )

        top07 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(4.25), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[4,4.5],
                checkerboard_colors = [PURPLE_D,PURPLE_D],
            )
        )

        top08 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(4.75), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[4.5,5],
                checkerboard_colors = [RED_B, MAROON_D],
            )
        )

        top09 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(5.25), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[5,5.5],
                checkerboard_colors = [PURPLE_D,PURPLE_D],
            )
        )

        top10 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), func(5.75), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[5.5,6],
                checkerboard_colors = [MAROON_D,MAROON_D],
            )
        )

        s01 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1*np.cos(u), v, 1*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(1.25)],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        s02 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1.5*np.cos(u), v, 1.5*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(1.25)],
                checkerboard_colors = [GREEN_B,GREEN_D],
            )
        )

        s03 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    2*np.cos(u), v, 2*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(1.75)],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        s04 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    2.5*np.cos(u), v, 2.5*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(2.25)],
                checkerboard_colors = [GREEN_B,GREEN_D],
            )
        )

        s05 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    3*np.cos(u), v, 3*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(2.75)],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        s06 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    3.5*np.cos(u), v, 3.5*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(3.25)],
                checkerboard_colors = [GREEN_B,GREEN_D],
            )
        )

        s07 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    4*np.cos(u), v, 4*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(3.75)],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        s08 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    4.5*np.cos(u), v, 4.5*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(4.25)],
                checkerboard_colors = [GREEN_B,GREEN_D],
            )
        )

        s09 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    5*np.cos(u), v, 5*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(4.75)],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        s10 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    5.5*np.cos(u), v, 5.5*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(5.25)],
                checkerboard_colors = [GREEN_B,GREEN_D],
            )
        )

        s11 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    6*np.cos(u), v, 6*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,func(5.75)],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )



        s.add(ax, trace, function, region, bound_left, bound_right)
        s.add(top01, top02, top03, top04, top05, top06, top07, top08, top09, top10,
            s01,s02,s03,s04,s05,s06,s07,s08,s09,s10,s11)


class ClosingShot(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=-30*DEGREES, theta = -PI/2)

        scale = 0.5
        waitdelay = 2

        ax = ThreeDAxes(
            x_range = [-7,7,1],
            x_length = 14 * scale,
            y_range = [-1, 6, 1],
            y_length = 7 * scale,
            z_range=[-2,2,1],
            z_length = 4 * scale,
        )

        def func(x):
            return 0.5 * x * np.sin(x) + (7/2)

        trace = ax.plot(func, x_range=[0,7], color = BLUE)
        function = ax.plot(func, x_range=[1,6], color = YELLOW)
        region = ax.get_area(function,x_range=[1,6], color = [BLUE_B, BLUE_D])
        bound_left = ax.get_T_label(x_val=1, graph=function, label=Tex("a").scale(0.7), triangle_size=0.1)
        bound_right = ax.get_T_label(x_val=6, graph=function, label=Tex("b").scale(0.7), triangle_size=0.1)

        e = ValueTracker(2 * PI)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), 0.5*v*np.sin(v) + 3.5, v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,6],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        outside = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    6*np.cos(u), v, 6*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,2.66],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        inside = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1*np.cos(u), v, 1*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,3.92],
                checkerboard_colors = [GREEN_B, GREEN_D],
            )
        )

        s.add(ax, trace, function, region, bound_left, bound_right,region)
        s.add(surface,outside,inside)


class ZoomTop(Scene):
    def construct(s):
        scale = 2
        waitdelay = 2

        ax = Axes(
            x_range = [-1,3,1],
            x_length = 4 * scale,
            y_range = [-1, 3, 1],
            y_length = 4 * scale,
        )

        def func(x):
            return (4/9) * x ** 2

        function = ax.plot(func, x_range=[0,2.1], color = YELLOW)
        top = ax.plot(lambda x: 1, x_range=[1,2], color = RED)
        meas = ax.plot(lambda x: 1.25, x_range=[1,2])
        region = ax.get_area(top,x_range=[1,2], color = [BLUE_B, BLUE_D])
        bound_left = ax.get_vertical_line(ax.c2p(1,1),line_config={"dashed_ratio": 0.9})
        bound_right = ax.get_vertical_line(ax.c2p(2,1),line_config={"dashed_ratio": 0.9})
        mid = ax.get_vertical_line(ax.c2p(1.5,1),line_config={"dashed_ratio": 0.9})

        label_x1 = Tex("$x_{i-1}$").scale(0.8).next_to(Dot(ax.c2p(1,0)), DOWN)
        label_x2 = Tex("$m_i$").scale(0.8).next_to(Dot(ax.c2p(1.5,0)), DOWN)
        label_x3 = Tex("$x_i$").scale(0.8).next_to(Dot(ax.c2p(2,0)), DOWN)

        d1 = Dot(ax.c2p(1,1.25))
        d2 = Dot(ax.c2p(2,1.25))
        d3 = Dot(ax.c2p(1.5,1))
        label_meas = Tex("$\Delta x$").scale(0.8).next_to(Dot(ax.c2p(1.5,1.25)),UP)
        h = Tex("$f(m_i)$").scale(0.8).next_to(Dot(ax.c2p(0,1)),LEFT)
        f_label = Tex("$f(x)$").scale(0.8).next_to(Dot(ax.c2p(2,func(2))),RIGHT)

        s.add(ax, top, function, region, bound_left, bound_right, mid)
        s.add(label_x1, label_x2, label_x3)
        s.add(meas,d1,d2, label_meas,h,f_label)


class BrokeRect(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0*DEGREES, theta = -PI/2)

        scale = 0.5
        waitdelay = 2

        ax = ThreeDAxes(
            x_range = [-7,7,1],
            x_length = 14 * scale,
            y_range = [-1, 6, 1],
            y_length = 7 * scale,
            z_range=[-2,2,1],
            z_length = 4 * scale,
        )

        def func(x):
            return 0.5 * x * np.sin(x) + (7/2)

        trace = ax.plot(func, x_range=[0,7], color = BLUE)
        function = ax.plot(func, x_range=[1,6], color = YELLOW)
        region = ax.get_area(function,x_range=[1,6], color = [BLUE_B, BLUE_D])
        bound_left = ax.get_T_label(x_val=1, graph=function, label=Tex("a").scale(0.7), triangle_size=0.1)
        bound_right = ax.get_T_label(x_val=6, graph=function, label=Tex("b").scale(0.7), triangle_size=0.1)

        box_top = ax.plot(lambda x: 1.58, color=RED, x_range=[1, 4.3])
        box_bottom = ax.plot(lambda x: 1.48, color=RED, x_range=[1, 4.3])

        box2_top = ax.plot(lambda x: 1.58, color=RED, x_range=[5.48, 6])
        box2_bottom = ax.plot(lambda x: 1.48, color=RED, x_range=[5.48, 6])

        s.add(ax, trace, function, region, bound_left, bound_right,
            box_top, box_bottom, box2_top, box2_bottom)
