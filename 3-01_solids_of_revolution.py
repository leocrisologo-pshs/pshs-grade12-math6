from re import L
from manim import *

class Solid01(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [0,4.1,1],
            x_length = 5,
            y_range = [-4, 4.1, 1],
            y_length = 5,
            z_range=[-4,4,1],
            z_length = 5,
        )

        trace = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[0,4], color = BLUE)
        function = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[1,3], color = YELLOW)
        bottom = ax.plot(lambda x: 0, x_range=[1,3], color = YELLOW)
        region = ax.get_area(function, x_range=[1,3], color = [BLUE_B, BLUE_D])

        e = ValueTracker(2 * PI)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * v ** 2 + 4) * np.cos(u), (-0.25 * v ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,3],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        floorbase = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1, v * np.cos(u), v*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,3.75],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        topbase = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    3, v * np.cos(u), v*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,1.75],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        s.play(Create(ax), Create(trace))
        s.wait(2)
        s.play(Create(function))
        s.wait(2)
        s.play(FadeOut(trace))
        s.play(Create(region))
        s.wait(2)
        s.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES)
        s.wait(2)
        s.begin_ambient_camera_rotation(rate=0.1)

        s.play(
            Rotating(
                VGroup(function, region),
                axis=RIGHT,
                radians=2 * PI,
                about_point=ax.c2p(0, 0, 0),
            ),
            e.animate.set_value(2 * PI),
            run_time=7,
            rate_func=linear,
        )
        s.wait(2)
#        s.begin_ambient_camera_rotation(rate=0.1)
        s.play(Create(surface), Create(floorbase), Create(topbase))
        s.wait(2)
        s.move_camera(phi=45 * DEGREES, theta=45 * DEGREES)
#        s.begin_ambient_camera_rotation(rate=0.1)
        s.move_camera(phi=-45 * DEGREES, theta=45 * DEGREES)
        s.wait(5)



######################


class Solid02(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [-4,4.1,5],
            x_length = 9,
            y_range = [-4, 4.1, 5],
            y_length = 5,
            z_range=[-4,4,5],
            z_length = 5,
        )#.add_coordinates()

        trace = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[0,4], color = BLUE)
        function = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[1,3], color = YELLOW)
        region = ax.get_area(function, x_range=[1,3], color = [BLUE_B, BLUE_D])

        e = ValueTracker(2 * PI)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    2 * (4 - v) ** 0.5 * np.cos(u), v, 2 * (4 - v) ** 0.5 * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1.75,3.75],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        floorbase = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v * np.cos(u),0, v*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,3],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        inner = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1 * np.cos(u),v, 1*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,3.75],
                checkerboard_colors = [GREEN_B, GREEN_D],
            )
        )

        outer = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    3 * np.cos(u),v, 3*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,1.75],
                checkerboard_colors = [BLUE_B, BLUE_D],
            )
        )

        s.play(Create(ax), Create(trace))
        s.wait(2)
        s.play(Create(function))
        s.wait(2)
        s.play(FadeOut(trace))
        s.play(Create(region))
        s.wait(2)
        s.move_camera(phi=-45 * DEGREES, theta=-60 * DEGREES)
        s.wait(2)
        s.begin_ambient_camera_rotation(rate=0.1)

        s.play(
            Rotating(
                VGroup(function, region),
                axis=UP,
                radians=2 * PI,
                about_point=ax.c2p(0, 0, 0),
            ),
            e.animate.set_value(2 * PI),
            run_time=7,
            rate_func=linear,
        )
        s.wait(2)
        s.play(Create(surface), Create(floorbase), Create(inner), Create(outer))
        s.wait(2)
        s.move_camera(phi=45 * DEGREES, theta=60 * DEGREES)
        s.wait(2)
        s.move_camera(phi=15 * DEGREES, theta = -75 * DEGREES)
        s.wait(5)
        s.move_camera(phi=-45 * DEGREES, theta=60 * DEGREES)
        s.wait(5)



###########

class Solid03(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [0,4.1,5],
            x_length = 5,
            y_range = [-4, 4.1, 5],
            y_length = 5,
            z_range=[-4,4,5],
            z_length = 5,
        )#.add_coordinates()

        trace = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[0,4], color = BLUE)
        function = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[1,3], color = YELLOW)
        region = ax.get_area(function, x_range=[1,3], color = [BLUE_B, BLUE_D])
        rect = ax.plot(lambda x: 3.0975, x_range=[1.8,2], color = RED)
        rectarea = ax.get_area(rect, x_range=[1.8,2], color = [RED_B, RED_C])

        e = ValueTracker(2 * PI)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, 3.0975 * np.cos(u), 3.0975 * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1.8,2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        floorbase = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1.8, v * np.cos(u), v*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,3.0975],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        topbase = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    2, v * np.cos(u), v*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,3.0975],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s.add(ax,trace)
        s.wait(2)
        s.play(Create(function),Create(region))
        s.wait(2)
        s.play(FadeOut(trace))
        s.play(Create(rect),Create(rectarea))
        s.wait(2)
        s.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES)
        s.wait(2)
        s.begin_ambient_camera_rotation(rate=0.1)

        s.play(
            Rotating(
                VGroup(rect,rectarea),
                axis=RIGHT,
                radians=2 * PI,
                about_point=ax.c2p(0, 0, 0),
            ),
            e.animate.set_value(2 * PI),
            run_time=7,
            rate_func=linear,
        )
        s.wait(2)
#        s.begin_ambient_camera_rotation(rate=0.1)
        s.play(Create(surface), Create(floorbase), Create(topbase))
        s.wait(2)
        s.move_camera(phi=45 * DEGREES, theta=45 * DEGREES)
#        s.begin_ambient_camera_rotation(rate=0.1)
        s.move_camera(phi=-45 * DEGREES, theta=45 * DEGREES)
        s.wait(5)

#######################

class Solid04(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [0,4.1,5],
            x_length = 5,
            y_range = [-4, 4.1, 5],
            y_length = 5,
            z_range=[-4,4,5],
            z_length = 5,
        )#.add_coordinates()



        trace = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[0,4], color = BLUE)
        function = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[1,3], color = YELLOW)
        region = ax.get_area(function, x_range=[1,3], color = [BLUE_B, BLUE_D])
#        rect = ax.get_riemann_rectangles(lambda x: -0.25 * x ** 2 + 4, x_range=[1.8,2], dx=0.2, color=(TEAL, BLUE_B, DARK_BLUE), input_sample_type="right",)
        rect = ax.get_riemann_rectangles(function, x_range=[1,3], dx=0.2, input_sample_type="center")


        e = ValueTracker(2 * PI)

#        surface = []
#        for i in range(0,10):
#            t = always_redraw(
#                lambda: Surface(
#                    lambda u, v: ax.c2p(
#                        v, (-0.25 * (0.2 * i + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * i + 1.1) ** 2 + 4) * np.sin(u)
#                    ),
#                    u_range = [0, e.get_value()],
#                    v_range=[1 + 0.2 * i, 1.2 + 0.2 * i],
#                    checkerboard_colors = [RED_B, RED_D],
#                )
#            )
#            surface.append(t)

        s0 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 0 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 0 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 0, 1.2 + 0.2 * 0],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 1 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 1 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 1, 1.2 + 0.2 * 1],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s2 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 2 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 2 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 2, 1.2 + 0.2 * 2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s3 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 3 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 3 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 3, 1.2 + 0.2 * 3],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s4 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 4 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 4 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 4, 1.2 + 0.2 * 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s5 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 5 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 5 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 5, 1.2 + 0.2 * 5],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s6 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 6 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 6 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 6, 1.2 + 0.2 * 6],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s7 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 7 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 7 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 7, 1.2 + 0.2 * 7],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s8 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 8 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 8 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 8, 1.2 + 0.2 * 8],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s9 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * (0.2 * 9 + 1.1) ** 2 + 4) * np.cos(u), (-0.25 * (0.2 * 9 + 1.1) ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1 + 0.2 * 9, 1.2 + 0.2 * 9],
                checkerboard_colors = [RED_B, RED_D],
            )
        )




        f0 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*0+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 0 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*1+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 1 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f2 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*2+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 2 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f3 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*3+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 3 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f4 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*4+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 4 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f5 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*5+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 5 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f6 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*6+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 6 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f7 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*7+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 7 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f8 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*8+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 8 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f9 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*9+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 9 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        f10 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.2*10+1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0, -0.25 * (0.2 * 10 + 1) ** 2 + 4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s.add(ax,function,region)
        s.play(Create(rect))
        s.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES)
        s.wait(1)
        s.play(FadeOut(rect,region))

        s.play(Create(s0),Create(f1))
        s.play(Create(s1),Create(f2))
        s.play(Create(s2),Create(f3))
        s.play(Create(s3),Create(f4))
        s.play(Create(s4),Create(f5))
        s.play(Create(s5),Create(f6))
        s.play(Create(s6),Create(f7))
        s.play(Create(s7),Create(f8))
        s.play(Create(s8),Create(f9))
        s.play(Create(s9),Create(f10))
        s.add(f0)
        s.begin_ambient_camera_rotation(rate=0.1)
        s.wait()
        s.move_camera(phi=45 * DEGREES, theta=0 * DEGREES)
        s.wait()
        s.move_camera(phi=-45 * DEGREES, theta=45 * DEGREES)

#######################

class Solid05(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [0,4.1,5],
            x_length = 5,
            y_range = [-4, 4.1, 5],
            y_length = 5,
            z_range=[-4,4,5],
            z_length = 5,
        )#.add_coordinates()

        tracetop = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[0,4], color = BLUE)
        tracebottom = ax.plot(lambda x: -0.125 * x ** 2 + 2.5, x_range=[0,4], color = GREEN)
        functiontop = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[1,3.46], color = YELLOW)
        functionbottom = ax.plot(lambda x: -0.125 * x ** 2 + 2.5, x_range=[1,3.46], color = GREEN)

        region = ax.get_area(functiontop, x_range=[1,3.46], bounded_graph=functionbottom, color = [BLUE_B, GREEN_D])

        rtop = ax.plot(lambda x: 3.0975, x_range=[1.8,2], color = RED)
        rbot = ax.plot(lambda x: 2.04875 , x_range=[1.8,2], color = RED)

        rect = ax.get_area(rtop, x_range = [1.8,2], bounded_graph = rbot, color = [RED_B, RED_D])

        e = ValueTracker(2 * PI)

        surface1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.25 * v ** 2 + 4) * np.cos(u), (-0.25 * v ** 2 + 4) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,3.46],
                checkerboard_colors = [GREEN_B, GREEN_D],
            )
        )


        surface2 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (-0.125 * v ** 2 + 2.5) * np.cos(u), (-0.125 * v ** 2 + 2.5) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,3.46],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        floorbase = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1, v * np.cos(u), v*np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[2.375,3.75],
                checkerboard_colors = [RED_B, RED_D],
            )
        )


        disctop = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, 3.0975 * np.cos(u), 3.0975 * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1.8, 2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        discbottom = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, 2.04875 * np.cos(u), 2.04875 * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1.8, 2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1.8, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[2.04875, 3.0975],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side2 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    2, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[2.04875, 3.0975],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s.play(Create(ax),Create(tracetop),Create(tracebottom))
        s.wait(3)
        s.add(region)
        s.wait(3)
        s.add(rect)
        s.wait(3)
        s.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES)
        s.play(Create(disctop), Create(discbottom), Create(side1), Create(side2))
        s.wait(3)
        s.play(Create(floorbase), Create(surface1), Create(surface2), FadeOut(disctop), FadeOut(discbottom), FadeOut(side1), FadeOut(side2))
        s.wait(3)
        s.begin_ambient_camera_rotation(rate=0.1)
        s.wait(3)
        s.move_camera(phi=45 * DEGREES, theta=45 * DEGREES)
        s.wait(3)
        s.move_camera(phi=-45 * DEGREES, theta=45 * DEGREES)
        s.wait(5)

########

class Pic1(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [0,5.2,1],
            x_length = 5.2,
            y_range = [-1.5, 1.5, 1],
            y_length = 3,
            z_range=[-1,1,2],
            z_length = 2,
        ).add_coordinates()

        trace = ax.plot(lambda x: 1 / x, x_range=[0.5,3.1], color = BLUE)
        function = ax.plot(lambda x: 1 / x, x_range=[1,4], color = YELLOW)
        region = ax.get_area(function, x_range=[1,4], color = [BLUE_B, BLUE_D])
        rectarea = ax.get_riemann_rectangles(function, x_range = [2, 2.18], dx=0.2, color = [RED_D, RED_B])

        s.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)

        e = ValueTracker(2 * PI)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (0.476) * np.cos(u), (0.476) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[2,2.2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    1, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,1],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side2 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    4, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,0.25],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        surface1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (1 / v) * np.cos(u), (1  / v) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,4],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s.add(ax, trace, function, surface1, side1, side2)
        s.begin_ambient_camera_rotation(rate=2*PI/12)
        s.wait(12)


#######################

class Pic2(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [-6.5,6.5,3],
            x_length = 6.5,
            y_range = [-1, 10, 3],
            y_length = 5.5,
            z_range=[-1,1,2],
            z_length = 1,
        ).add_coordinates()

        trace = ax.plot(lambda x: 0.25 * x**2, x_range=[-0.5,6.5], color = BLUE)
        function = ax.plot(lambda x: 0.25 * x ** 2, x_range=[0,6], color = YELLOW)
        toplimit = ax.plot(lambda x: 9, x_range=[-0.5,6.5], color=RED)
        region = ax.get_area(toplimit, bounded_graph=function, x_range=[0,6], color = [BLUE_B, BLUE_D])

        recttop = ax.plot(lambda x: 4.4, x_range=[0, 6])
        rectbottom = ax.plot(lambda x: 4, x_range=[0, 6])

        rectarea = ax.get_riemann_rectangles(recttop, bounded_graph = rectbottom, x_range = [0, 4.1], dx=4.2, color = [RED_D, RED_B], input_sample_type="center")

        s.set_camera_orientation(phi=-45 * DEGREES, theta=-100 * DEGREES)

        e = ValueTracker(2 * PI)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    (2 * v ** 0.5) * np.cos(u), v, (2 * v ** 0.5) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0.05,9],
                checkerboard_colors = [GREEN_B, GREEN_D],
            )
        )

        disctop = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    4.1 * np.cos(u), v, 4.1 * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[4,4.2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), 9, v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,6],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side2 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), 4, v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,4.1],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s.add(ax, region, trace, function, toplimit)
        s.add(side1,surface)
        s.begin_ambient_camera_rotation(rate=2*PI/12)
        s.wait(12)

#######################


#######################

class Pic3(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [-0.5,1.5,1],
            x_length = 4,
            y_range = [-1.5, 1.5, 1],
            y_length = 6,
            z_range=[-0.5,0.5,2],
            z_length = 2,
        ).add_coordinates()

        tracetop = ax.plot(lambda x: x, x_range=[-0.3,1.3], color = BLUE)
        tracebottom = ax.plot(lambda x: x ** 3, x_range=[-0.3,1.1], color = GREEN)
        region = ax.get_area(tracetop, bounded_graph=tracebottom, x_range=[0,1], color = [BLUE_B, BLUE_D])
        rectarea = ax.get_riemann_rectangles(tracetop, bounded_graph = tracebottom, x_range = [0.5, 0.59], dx=0.1, color = [RED_D, RED_B], input_sample_type="center")

        s.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)

        e = ValueTracker(2 * PI)

        surfaceout = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (v) * np.cos(u), (v) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,1],
                checkerboard_colors = [GREEN_B, GREEN_D],
            )
        )

        washerout = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, 0.55 * np.cos(u), 0.55 * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0.5,0.6],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        washerin = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, 0.166 * np.cos(u), 0.166 * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0.5,0.6],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.5, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0.166,0.55],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side2 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    0.6, v * np.cos(u), v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0.166,0.55],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        surfacein = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v, (v**3) * np.cos(u), (v**3) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,1],
                checkerboard_colors = [RED_B, RED_D],
            )
        )


        s.add(ax, region, tracetop, tracebottom)
        s.add(surfacein, surfaceout)
        s.begin_ambient_camera_rotation(rate=2*PI/12)
        s.wait(12)

#######################


class Pic4(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [-4.5,4.5,2],
            x_length = 4.5*1.5,
            y_range = [-0.5, 2.5, 2],
            y_length = 1.5*1.5,
            z_range=[-1,1,2],
            z_length = 1.5,
        ).add_coordinates()

        tracetop = ax.plot(lambda x: x ** 0.5, x_range=[0,4.4], color = BLUE)
        tracebottom = ax.plot(lambda x: 0.5 * x, x_range=[0,4.4], color = GREEN)
        region = ax.get_area(tracetop, bounded_graph=tracebottom, x_range=[0,4], color = [BLUE_B, BLUE_D])

        recttop = ax.plot(lambda x: 1.1, x_range=[0, 6])
        rectbottom = ax.plot(lambda x: 0.9, x_range=[0, 6])

        rectarea = ax.get_riemann_rectangles(recttop, bounded_graph = rectbottom, x_range = [1,2], dx=1.1, color = [RED_D, RED_B], input_sample_type="center")

        s.set_camera_orientation(phi=-45 * DEGREES, theta=-100 * DEGREES)

        e = ValueTracker(2 * PI)

        outer = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    (2 * v) * np.cos(u), v, (2 * v) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,2],
                checkerboard_colors = [GREEN_B, GREEN_D],
            )
        )

        inner = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    (v ** 2) * np.cos(u), v, (v ** 2) * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        washouter = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    2 * np.cos(u), v, 2 * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0.9,1.1],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        washinner = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    np.cos(u), v, np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0.9,1.1],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side1 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), 1.1, v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[1,2],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        side2 = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    v*np.cos(u), 4, v * np.sin(u)
                ),
                u_range = [0, e.get_value()],
                v_range=[0,4.1],
                checkerboard_colors = [RED_B, RED_D],
            )
        )

        s.add(ax, tracetop, tracebottom, region)
        s.add(outer, inner)
#        s.add(washinner,washouter,side1)
        s.begin_ambient_camera_rotation(rate=2*PI/12)
        s.wait(12)#######################

class CamAngle(ThreeDScene):
    def construct(s):
        s.set_camera_orientation(phi=0, theta = -PI/2)

        ax = ThreeDAxes(
            x_range = [0,4.1,5],
            x_length = 5,
            y_range = [-4, 4.1, 5],
            y_length = 5,
            z_range=[-1,1,2],
            z_length = 2.5,
        )#.add_coordinates()

        trace = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[0,4], color = BLUE)
        function = ax.plot(lambda x: -0.25 * x ** 2 + 4, x_range=[1,3], color = YELLOW)
        region = ax.get_area(function, x_range=[1,3], color = [BLUE_B, BLUE_D])
        rect = ax.plot(lambda x: 3.0975, x_range=[1.8,2], color = RED)
        rectarea = ax.get_area(rect, x_range=[1.8,2], color = [RED_B, RED_C])



        s.add(ax,function,region)
        s.play(Create(rect), Create(rectarea))
        s.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES)
        s.wait(5)
        s.move_camera(phi=-45 * DEGREES, theta=-60 * DEGREES)
        s.wait(5)
        s.move_camera(phi=-45 * DEGREES, theta=60 * DEGREES)
        s.wait(5)
