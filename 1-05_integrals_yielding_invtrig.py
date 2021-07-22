from manim import *

class Scratch(Scene):
    def construct(self):

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "{", " ", " ", " ", "{", "f(x+ \Delta x)", "\over", "g(x+\Delta x)", "}", " ", " ", " ", " ", "-", "{", "f(x)", " ", "\over", " ", "g(x)","}", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\over", "\Delta x", "}")

class ArcSin(Scene):
    def construct(s):
        text1 = Text("Integrals yielding inverse sines", font="Montserrat", color=YELLOW).shift(UP)
        eqn = MathTex(r"\int {du \over \sqrt{a^2-u^2}} = \sin^{-1} {u  \over a} + C").scale(1.3).shift(DOWN)
        s.play(Write(text1))
        s.play(FadeIn(eqn))
        #s.wait(1)
        s.play(FadeOut(text1))
        s.play(FadeOut(eqn))

        e0 = MathTex(r"\text{Let }", " ",  "y", "=", r"\sin^{-1}", "{", "u", "\over", "a", "}").scale(1.3)
        s.play(FadeIn(e0))
        #s.wait(1)

        reminder0 = MathTex(r"\text{Let }", " ",  "y", "=", r"\sin^{-1}", "{", "u", "\over", "a", "}").set_color(RED).shift(LEFT*5,UP*2).scale(0.8)
        s.play(FadeIn(reminder0))
        #s.wait(1)

        e1 = MathTex(" ", "\sin",  "y", "=", " ", "{", "u", "\over", "a", "}").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        #s.wait(1)

        e0 = MathTex("a", "\sin",  "y", "=", " ", "{", "u", " ", " ", "}").scale(1.3)
        s.play(ReplacementTransform(e1,e0))


        reminder1 = MathTex("a", "\sin",  "y", "=", " ", "{", "u", " ", " ", "}").shift(UP*2).set_color(BLUE).scale(0.8)
        s.play(FadeIn(reminder1))
        #s.wait(1)

        e1 = MathTex(" ", " ", " ", " ", "a", "\sin",  "y", " ", "=", " ", " ", "u", " ", " ", " ").scale(1.3)
        s.remove(e0)
        s.add(e1)

        e0 = MathTex(" ", " ", "{d \over du}", "(", "a", "\sin",  "y", ")", "=", "{d \over du}", "(", "u", ")", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        #s.wait(1)

        e1 = MathTex("a", "\cdot", "{d \over du}", "(", " ", "\sin",  "y", ")", "=", "{d \over du}", "(", "u", ")", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        #s.wait(1)

        e0 = MathTex("a", "\cdot", "{d \over du}", "(", " ", "\sin",  "y", ")", "=", "1", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        #s.wait(1)

        e1 = MathTex("a", "\cdot", "{d \over du}", " ","(", " ", "\sin", " ", "y", ")", "=", "1", " ", " ", " ", " ", " ").scale(1.3)
        s.remove(e0)
        #s.add(e1)

        e0 = MathTex("a", " ", " ", "\cos y", " ", "\cdot", " ", "{dy ",  "\over", "du}", "=", "1", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        #s.wait(1)

        e1 = MathTex(" ", " ", " ", " ", " ", " ", " ", "{dy ",  "\over", "du}", "=", "{1", "\over", "a\cos y", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        #s.wait(1)

        side1 = MathTex("\sin^2  y", "+", "\cos", "^2", "y", "=", " ", " ", " ", "1", " ", " ", " ").shift(RIGHT*4,UP*2).set_color(YELLOW).scale(0.8)
        s.play(FadeIn(side1))
        #s.wait(1)

        side2 = MathTex(" ", " ", "\cos", "^2", "y", "=", " ", " ", " ", "1", "-", "\sin^2 y", " ").shift(RIGHT*4,UP*2).set_color(YELLOW).scale(0.8)
        s.play(ReplacementTransform(side1, side2))
        #s.wait(1)

        side1 = MathTex(" ", " ", "\cos", " ", "y", "=", " ", "\pm", "\sqrt{", "1", "-", "\sin^2 y", "}").shift(RIGHT*4,UP*2).set_color(YELLOW).scale(0.8)
        s.play(ReplacementTransform(side2, side1))
        #s.wait(1)

        side2 = MathTex(" ", " ", "\cos", " ", "y", "=", " ", " ", "\sqrt{", "1", "-", "\sin^2 y", "}").shift(RIGHT*4,UP*2).set_color(YELLOW).scale(0.8)
        s.play(ReplacementTransform(side1, side2))
        #s.wait(1)

        e0 = MathTex("{dy ",  "\over", "du}", "=", "{1", "\over", " ", "a"," ", " ", " ", "\cos", " ", "y", "}", " ", " ").scale(1.3)
        s.remove(e1)
        s.add(e0)
        #s.wait(1)

        e1 = MathTex("{dy ",  "\over", "du}", "=", "{1", "\over", " ", "a","\sqrt{ ", "1", "-", "\sin", "^2", "y", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        #s.wait(1)
        s.play(FadeOut(side2))
        #s.wait(1)

        e0 = MathTex("{dy ",  "\over", "du}", "=", "{1", "\over", " ", "a","\sqrt{ ", " ", " ", "1", "-", " ", "\sin", "^2", "y", " ", "}", " ", " ").scale(1.3)
        s.remove(e1)
        s.add(e0)

        e1 = MathTex("{dy ",  "\over", "du}", "=", "{1", "\over", " ", " ","\sqrt{", "a^2", "(", "1", "-", " ", "\sin", "^2", "y", ")", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        #s.wait(1)

        e0 = MathTex("{dy ",  "\over", "du}", "=", "{1", "\over", " ", " ","\sqrt{", " ", "(", "a^2", "-", "a^2", "\sin", "^2", "y", ")", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        #s.wait(1)
        s.play(Indicate(reminder1))

        e1 = MathTex("{dy ",  "\over", "du}", "=", "{1", "\over", " ", " ","\sqrt{", " ", "(", "a^2", "-", "u^2", " ", " ", " ", ")", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        #s.wait(1)
        s.play(FadeOut(reminder1))

        e0 = MathTex("{dy ",  " ", " }", "=", "{du", "\over", " ", " ","\sqrt{", " ", "(", "a^2", "-", "u^2", " ", " ", " ", ")", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        #s.wait(1)

        e1 = MathTex(" ", " ",  " ", "dy", " ", "=", " ", " ", "{du", "\over","\sqrt{", " ", "(", "a^2", "-", "u^2", " ", " ", " ", ")", "}", " ", " ").scale(1.3)
        s.remove(e0)
        s.add(e1)

        e0 = MathTex(" ", "\int",  "d", "y", " ", "=", " ", "\int", "{du", "\over","\sqrt{", " ", "(", "a^2", "-", "u^2", " ", " ", " ", ")", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        #s.wait(1)

        e1 = MathTex(" ", " ",  "y", "+ C", "=", " ", "\int", "{du", "\over","\sqrt{", " ", "(", "a^2", "-", "u^2", " ", " ", " ", ")", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        #s.wait(1)
        s.play(Indicate(reminder0))

        e0 = MathTex("\sin^{-1}", "{ u \over a}",  " ", "+ C", "=", " ", "\int", "{du", "\over","\sqrt{", " ", "(", "a^2", "-", "u^2", " ", " ", " ", ")", "}", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        s.wait(1)
        s.play(FadeOut(reminder0))

        e1 = MathTex(" ", " ",  " ", " ", " ", " ", "\int", "{du", "\over","\sqrt{", " ", "(", "a^2", "-", "u^2", " ", " ", " ", ")", "}", "}", "= \sin^{-1} {u \over a} + C").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        s.wait(1)

        # Close with opening scene
        s.play(ApplyMethod(e1.shift(DOWN)))
        s.play(FadeIn(text1))
        s.wait(1)

class ArcTan(Scene):
    def construct(s):
        text1 = Text("Integrals yielding inverse tangents", font="Montserrat", color=YELLOW).shift(UP)
        eqn = MathTex(r"\int {du \over a^2+u^2} = {1 \over a}\tan^{-1} {u  \over a} + C").scale(1.3).shift(DOWN)
        s.play(Write(text1))
        s.play(FadeIn(eqn))
        #s.wait(1)
        s.play(FadeOut(text1))
        s.play(FadeOut(eqn))

        e0 = MathTex(" ", " ", " ", " ", " ", r"\text{Let }", " ",  "y", " ", " ","=", " ", " ", "{1", "\over", "a}", r"\tan^{-1}", "{", "u", "\over", "a", "}", " ", " ", " ", " ", " ").scale(1.3)
        s.play(FadeIn(e0))
        #s.wait(1)

        reminder0 = MathTex(r"\text{Let } y = {1 \over a} \tan^{-1} { u \over a }").set_color(RED).shift(LEFT*5,UP*2).scale(0.8)
        s.play(FadeIn(reminder0))
        #s.wait(1)

        e1 = MathTex(" ", " ", " ", " ", " ", " ", "a",  "y", " ", " ","=", " ", " ", " ", " ", " ", r"\tan^{-1}", "{", "u", "\over", "a", "}", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        #s.wait(1)

        e0 = MathTex(" ", " ", " ", " ", r"\tan", "(", "a",  "y", ")", " ","=", " ", " ", " ", " ", " ", " ", "{", "u", "\over", "a", "}", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))

        e1 = MathTex(" ", " ", " ", "a", r"\tan", "(", "a",  "y", ")", " ","=", " ", " ", " ", " ", " ", " ", " ", "u", " ", " ", " ", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))

        reminder1 = MathTex(r"a \tan  ( a y ) = u").set_color(BLUE).shift(UP*2).scale(0.8)
        s.play(FadeIn(reminder1))

        e0 = MathTex(" ", r"{d \over du}", "(", "a", r"\tan", "(", "a",  "y", ")", ")","=", "{d \over du}", "( ", " ", " ", " ", " ", " ", "u", ")", " ", " ", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))

        e1 = MathTex("a", r"{d \over du}", "(", " ", r"\tan", "(", "a",  "y", ")", ")","=", " ", " ", "1", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))

        e0 = MathTex("a", r"{d \over du}", "(", " ", r"\tan", "(", "a",  "y", ")", ")"," ", " ", " "," "," ", "=", " ", " ", "1", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ").scale(1.3)
        s.remove(e1)
        s.add(e0)

        e1 = MathTex("a", " ", " ", "\sec^2(ay) ", " ", " ", " ",  " ", " ", " ","\cdot", "a", "{dy", "\over", "du}","=", " ", " ", "1", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))

        e0 = MathTex(" ", "a^2", " ", "\sec^2(ay) ", " ", " ", " ",  " ", " ", " "," ", " ", "{dy", "\over", "du}","=", " ", " ", "1", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))

        e1 = MathTex(" ", " ", " ", " ", " ", " ", " ",  " ", " ", " "," ", " ", "{dy", "\over", "du}","=", " ", "{", "1", "\over", "a^2", " ", "\sec^2(ay)", " ", " ", " ", " ", " ", " ", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))

        reminder3 = MathTex(r"\sec^2x=1+\tan^2x").set_color(YELLOW).shift(RIGHT*4,UP*2).scale(0.8)
        s.play(FadeIn(reminder3))

        e0 = MathTex(" ", " ", " ", " ", " ", " ", " ",  " ", " ", " "," ", " ", "{dy", "\over", "du}","=", " ", "{", "1", "\over", "a^2", "(", " ", " ","1", "+", " ",r"\tan^2(ay)", " ", ")", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        s.play(FadeOut(reminder3))

        e1 = MathTex(" ", " ", " ", " ", " ", " ", " ",  " ", " ", " "," ", " ", "{dy", "\over", "du}","=", " ", "{", "1", "\over", " ", "(", " ", "a^2"," ", "+", "a^2",r"\tan^2(ay)", " ", ")", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        s.play(Indicate(reminder1))

        e0 = MathTex(" ", " ", " ", " ", " ", " ", " ",  " ", " ", " "," ", " ", "{dy", "\over", "du}","=", " ", "{", "1", "\over", " ", " ", " ", "a^2"," ", "+", " "," ", "u^2", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        s.play(FadeOut(reminder1))

        e1 = MathTex(" ", " ", " ", " ", " ", " ", " ",  " ", " ", " "," ", " ", "{dy", " ", " ","=", "{du", " ", " ", "\over", " ", " ", " ", "a^2"," ", "+", " "," ", "u^2", " ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))

        e0 = MathTex(" ", " ", " "," ", " ", "{dy", " ", " ","=", " ",r"{du \over a^2 + u^2}").scale(1.3)
        s.remove(e1).add(e0)

        e1 = MathTex(" ", " ", " "," ", "\int", "dy", " ", " ","=", "\int",r"{du \over a^2 + u^2}").scale(1.3)
        s.play(ReplacementTransform(e0,e1))

        e0 = MathTex(" ", " ", " "," ", " ", " ", "y", "+C","=", "\int",r"{du \over a^2 + u^2}").scale(1.3)
        s.play(ReplacementTransform(e1,e0))
        s.play(Indicate(reminder0))

        e1 = MathTex(" ", " ", " "," ", " ", r"{1 \over a} \tan^{-1} { u \over a }", " ", "+C","=", "\int",r"{du \over a^2 + u^2}").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        s.play(FadeOut(reminder0))

        e0 = MathTex(" ", " ", " ",r"\int {du \over a^2 + u^2}", "=", r"{1 \over a} \tan^{-1} { u \over a }", " ", "+C"," ", " ", " ").scale(1.3)
        s.play(ReplacementTransform(e1,e0))

        # Close with opening scene
        s.play(ApplyMethod(e0.shift,DOWN))
        s.play(FadeIn(text1))
        s.wait(1)
