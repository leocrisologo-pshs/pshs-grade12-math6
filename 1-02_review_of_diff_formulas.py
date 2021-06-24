from manim import *

class Scratch(Scene):
    def construct(self):

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "{", " ", " ", " ", "{", "f(x+ \Delta x)", "\over", "g(x+\Delta x)", "}", " ", " ", " ", " ", "-", "{", "f(x)", " ", "\over", " ", "g(x)","}", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\over", "\Delta x", "}")

class ProductRule(Scene):
    def construct(s):

        text1 = Text("The Product Rule of Differentiation", font="Montserrat").shift(UP*2)
        text2 = Text("If f and g are differentiable, then", color=YELLOW, font="Montserrat").scale(0.7)
        text3 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "f(x)", "\cdot",  "g'(x)",  "+", "g(x)", "\cdot", "f'(x)").scale(1.3)
        text3.shift(DOWN)
        uptext = VGroup(text1, text2)
        s.play(Write(uptext))
        s.play(FadeIn(text3))
        s.wait(1)
        s.play(FadeOut(uptext))
        s.play(FadeOut(text3))

        e0 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", "{", "f(x+\Delta x)", "\cdot", "g(x+\Delta x)", " ", " ", " ", " ", " ", " ", " ", " ", "-", "f(x)","\cdot","g(x)", "\over", "\Delta x", "}")
        s.play(FadeIn(e0))
        s.wait(1)
        t0 = Text("Add two convenient terms that cancel each other out",font="Montserrat").scale(0.5)
        t0.shift(DOWN*3)
        s.play(FadeIn(t0))
        s.wait(1)

        # Insert +/- f(x + dx)g(x)
        e1 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", "{", "f(x+\Delta x)", "\cdot", "g(x+\Delta x)", "-", "f(x+\Delta x)", "\cdot", "g(x)", "+", "f(x+\Delta x)", "\cdot", "g(x)", "-", "f(x)","\cdot","g(x)", "\over", "\Delta x", "}").scale(0.6)
        for i_ in range(7,15):
            e1[i_].set_color(BLUE)
        s.play(ReplacementTransform(e0,e1))
        s.wait(1)
        s.play(FadeOut(t0))
        for i_ in range(7,15):
            e1[i_].set_color(WHITE)
        e1[4].set_color(BLUE)
        e1[8].set_color(BLUE)
        t0 = Text("Factor out",font="Montserrat").scale(0.5)
        t0.shift(DOWN*3)
        s.play(FadeIn(t0))
        s.wait(1)

        # Add space for square brackets
        e0 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", "{", "f(x+\Delta x)", "\cdot", " ", "g(x+\Delta x)", "-", "f(x+\Delta x)", "\cdot", "g(x)", " ", "+", "f(x+\Delta x)", "\cdot", "g(x)", "-", "f(x)","\cdot","g(x)", "\over", "\Delta x", "}").scale(0.6)
        s.remove(e1)
        s.add(e0)

        # Factor out common f(x + dx)
        e1 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", "{", "f(x+\Delta x)", "\cdot", "\left[", "g(x+\Delta x)", "-", " ", " ", "g(x)", r"\right] ", "+", "f(x+\Delta x)", "\cdot", "g(x)", "-", "f(x)","\cdot","g(x)", "\over", "\Delta x", "}").scale(0.7)
        e1[6].set_color(YELLOW)
        e1[12].set_color(YELLOW)
        s.play(ReplacementTransform(e0,e1))
        s.wait(1)
        s.play(FadeOut(t0))
        s.wait(1)
        e1[16].set_color(BLUE)
        e1[20].set_color(BLUE)
        t0 = Text("Factor out",font="Montserrat").scale(0.5)
        t0.shift(DOWN*3)
        s.play(FadeIn(t0))
        s.wait(1)

        # Add space for square brackets
        e0 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", "{", "f(x+\Delta x)", "\cdot", "\left[", "g(x+\Delta x)", "-", "g(x)", r"\right] ", "+", " ", " ", " ", "f(x+\Delta x)", "\cdot", "g(x)", "-", "f(x)","\cdot","g(x)", " ", "\over", "\Delta x", "}").scale(0.7)
        s.remove(e1)
        s.add(e0)

        # Factor out common g(x)
        e1 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", "{", "f(x+\Delta x)", "\cdot", "\left[", "g(x+\Delta x)", "-", "g(x)", r"\right] ", "+", "g(x)", "\cdot", "\left[", "f(x+\Delta x)", " ", " ", "-", "f(x)"," "," ", r"\right]", "\over", "\Delta x", "}").scale(0.7)
        e1[14].set_color(YELLOW)
        e1[22].set_color(YELLOW)
        s.play(ReplacementTransform(e0,e1))
        s.play(FadeOut(t0))
        e1[24].set_color(BLUE)
        t0 = Text("Distribute",font="Montserrat").scale(0.5)
        t0.shift(DOWN*3)
        s.play(FadeIn(t0))
        s.wait(1)

        # Add space for distributed dx denominators
        e0 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", " ", "{", "f(x+\Delta x)", "\cdot", "{", "\left[", "g(x+\Delta x)", "-", "g(x)", r"\right] ", "}", " ", " ", " ", "+", "g(x)", " ","\cdot", "{", "\left[", "f(x+\Delta x)", "-", "f(x)", r"\right]", "}" , "\over", "\Delta x", "}"," ").scale(0.7)
        s.remove(e1)
        s.add(e0)

        # Distribute dxs
        e1 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", "\left[", " ", "f(x+\Delta x)", "\cdot", "{", "\left[", "g(x+\Delta x)", "-", "g(x)", r"\right] ", " ", "\over", "\Delta x", "}", "+", "g(x)", " ", "\cdot", "{", "\left[", "f(x+\Delta x)", "-", "f(x)", r"\right]", " " , "\over", "\Delta x", "}", r"\right]").scale(0.75)
        s.play(ReplacementTransform(e0,e1))
        s.play(FadeOut(t0))
        e1[1].set_color(BLUE)
        e1[2].set_color(BLUE)
        t0 = Text("Apply limits to  all factors",font="Montserrat").scale(0.5)
        t0.shift(DOWN*3)
        s.play(FadeIn(t0))
        s.wait(1)

        # Add space for limits
        e0 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", "\left[", " ", "f(x+\Delta x)", "\cdot", " ", "{",  "\left[", "g(x+\Delta x)", "-", "g(x)", r"\right] ", " ", "\over", "\Delta x", "}", "+", " ", "g(x)", " ", "\cdot", " ","{",  "\left[", "f(x+\Delta x)", "-", "f(x)", r"\right]", " " , "\over", "\Delta x", "}", r"\right]").scale(0.75)
        s.remove(e1)
        s.add(e0)

        # Distribute limits
        e1 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", " ", " ", "f(x+\Delta x)", "\cdot", r"\displaystyle\lim_{\Delta x \to 0} ","{",  "\left[", "g(x+\Delta x)", "-", "g(x)", r"\right] ", " ", "\over", "\Delta x", "}", "+", r"\displaystyle\lim_{\Delta x \to 0}", "g(x)", " ", "\cdot", r"\displaystyle\lim_{\Delta x \to 0}", "{", "\left[", "f(x+\Delta x)", "-", "f(x)", r"\right]", " " , "\over", "\Delta x", "}", " ").scale(0.6)
        s.play(ReplacementTransform(e0,e1))
        s.play(FadeOut(t0))
        for i_ in (1, 2, 5):
            e1[i_].set_color(BLUE)
        t0 = Text("Evaluate each limit",font="Montserrat").scale(0.5)
        t0.shift(DOWN*3)
        s.play(FadeIn(t0))

        # Insert some blanks
        e0 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "\displaystyle\lim_", r"{\Delta x \to 0}", " ", " ", "f(x", " ", "+\Delta x)", "\cdot", r"\displaystyle\lim_{\Delta x \to 0} ","{",  "\left[", "g(x+\Delta x)", "-", "g(x)", r"\right] ", " ", "\over", "\Delta x", "}", "+", r"\displaystyle\lim_{\Delta x \to 0}", "g(x)", " ", "\cdot", r"\displaystyle\lim_{\Delta x \to 0}", "{", "\left[", "f(x+\Delta x)", "-", "f(x)", r"\right]", " " , "\over", "\Delta x", "}", " ").scale(0.6)
        s.remove(e1)
        s.add(e0)

        # Evaluate limit of f(x + dx)
        e1 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", " ", " ", " ", " ", "f(x", ")", " ", "\cdot", r"\displaystyle\lim_{\Delta x \to 0} ","{",  "\left[", "g(x+\Delta x)", "-", "g(x)", r"\right] ", " ", "\over", "\Delta x", "}", "+", r"\displaystyle\lim_{\Delta x \to 0}", "g(x)", " ", "\cdot", r"\displaystyle\lim_{\Delta x \to 0}", "{", "\left[", "f(x+\Delta x)", "-", "f(x)", r"\right]", " " , "\over", "\Delta x", "}", " ").scale(0.65)
        s.play(ReplacementTransform(e0,e1))

        # Insert some blanks
        e0 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "f(x)", "\cdot", r"\displaystyle\lim_{\Delta x \to 0} ","{",  "\left[", "g(x+\Delta x)", "-", "g", " ", "(x)", r"\right] ", " ", "\over", "\Delta x", "}", "+", r"\displaystyle\lim_{\Delta x \to 0}", "g(x)", "\cdot", r"\displaystyle\lim_{\Delta x \to 0}", "{", "\left[", "f(x+\Delta x)", "-", "f", " ", "(x)", r"\right]", " " , "\over", "\Delta x", "}", " ").scale(0.65)
        for i_ in range(3, 15):
            e0[i_].set_color(BLUE)
        s.remove(e1)
        s.add(e0)

        # Evaluate limit to g'(x)
        e1 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "f(x)", "\cdot", " ","{",  " ", " ", " ", "g", "' ", "(x)", "  ", " ", " ", " ", "}", "+", r"\displaystyle\lim_{\Delta x \to 0}", "g(x)", "\cdot", r"\displaystyle\lim_{\Delta x \to 0}", "{", "\left[", "f(x+\Delta x)", "-", "f", "  ", "(x)", r"\right]", " " , "\over", "\Delta x", "}", " ").scale(0.75)
        s.wait(1)
        s.play(ReplacementTransform(e0,e1))
        e1[17].set_color(BLUE)
        e1[18].set_color(BLUE)
        s.wait(1)

        # Evaluate limit of g(x)
        e0 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "f(x)", "\cdot", " ","{",  " ", " ", " ", "g", "' ", "(x)", "  ", " ", " ", " ", "}", "+", " ", "g(x)", "\cdot", r"\displaystyle\lim_{\Delta x \to 0}", "{", "\left[", "f(x+\Delta x)", "-", "f", " ", "(x)", r"\right]", " " , "\over", "\Delta x", "}", " ").scale(0.85)
        s.play(ReplacementTransform(e1,e0))
        for i_ in range(20, 32):
            e0[i_].set_color(BLUE)
        s.wait(1)

        # Evaluate limit to g'(x)
        e1 = MathTex(r"\dfrac{d}{dx} \left[ f(x) \cdot g(x) \right] = ", "f(x)", "\cdot", " ","{",  " ", " ", " ", "g", "' ", "(x)", "  ", " ", " ", " ", "}", "+", " ", "g(x)", "\cdot", " ", "{", " ", " ", " ", "f", "' ", "(x)", " ", " " , " ", " ", "}", " ").scale(1.3)
        s.play(ReplacementTransform(e0,e1))
        s.play(FadeOut(t0))
        s.wait(1)

        # Close with opening scene
        s.play(ApplyMethod(e1.shift,DOWN))
        s.play(FadeIn(uptext))
        s.wait(1)

class QuotientRule(Scene):
    def construct(self):

        text1 = Text("The Quotient Rule of Differentiation", font="Montserrat").shift(UP*2)
        text2 = Text("If f and g are differentiable, then", color=YELLOW, font="Montserrat").scale(0.7)
        text3 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=", "{", "g(x)", "\cdot", "{", "f'(x)", "}", "-", "f(x)", "\cdot", "{", "g'(x)", "}", "\over", "\left[", "g(x)" , " ", r"\right] ", "^2"," ", "}").scale(1.3)
        text3.next_to(text2,DOWN)
        uptext = VGroup(text1, text2)
        self.play(Write(uptext))
        self.play(FadeIn(text3))
        self.wait(1)
        self.play(FadeOut(uptext))
        self.play(FadeOut(text3))

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "{", " ", " ", " ", "{", "f(x+ \Delta x)", "\over", "g(x+\Delta x)", "}", " ", " ", " ", " ", "-", "{", "f(x)", " ", "\over", " ", "g(x)","}", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\over", "\Delta x", "}")
        self.play(FadeIn(s0))
        self.wait(1)
        s0[37].set_color(BLUE)
        t0 = Text("Let's relocate the denominator for clarity", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)
        self.play(FadeOut(t0))


        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "\left[", " ", " ", " ", "{", "f(x+ \Delta x)", "\over", "g(x+\Delta x)", "}", " ", " ", " ", " ", "-", "{", "f(x)", " ", "\over", " ", "g(x)","}", " ", " ", " ", " ", " ", " ", " ", " ", r"\right]", "\cdot", "{", "1", "\over", "\Delta x", "}")
        self.play(ReplacementTransform(s0,s1))
        self.wait(1)
        for i_ in (3, 8, 9, 10, 16, 18, 20, 22, 32):
            s1[i_].set_color(BLUE)
        t0 = Text("Combine these into one fractional expression", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)
        self.play(FadeOut(t0))

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "{", "g(x)", "\cdot", " ", "      ", "f(x+ \Delta x)", " ", " ", " ", " ", " ", " ", " ", " ", "-", "f(x)", "\cdot", "      ", "g(x+\Delta x)", " "," ", " ", " ", " ", " ", "\over", "g(x+ \Delta x)", "\cdot", "g(x)", "}", "\cdot", "{", "1", "\over", "\Delta x", "}")
        self.play(ReplacementTransform(s1,s0))
        self.wait(1)
        t0 = Text("Add these terms that add up to zero", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)


        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "{", "g(x)", "\cdot", " ", "      ", "f(x+ \Delta x)", "-", " ", " ", "f(x)", "\cdot", "g(x)", " ", " ", "-", "f(x)", "\cdot", "      ", "g(x+\Delta x)", "+"," ", "f(x)", "\cdot", "g(x)", " ", "\over", "g(x+ \Delta x)", "\cdot", "g(x)", "}", "\cdot", "{", "1", "\over", "\Delta x", "}").scale(0.7)
        for i_ in (9, 12, 13, 14, 22, 24, 25, 26):
            s1[i_].set_color(BLUE)
        self.play(ReplacementTransform(s0,s1))
        self.wait(1)
        self.play(FadeOut(t0))
        self.wait(1)
        for i_ in (9, 12, 13, 14, 22, 24, 25, 26):
            s1[i_].set_color(WHITE)
        s1[4].set_color(BLUE)
        s1[14].set_color(BLUE)
        t0 = Text("Factor out g(x)", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)


        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "{", "g(x)", "\cdot", "{", "\left[", "f(x+ \Delta x)", "-", " ", " ", "f(x)", "     ", " ",r"\right]", "}", "-", "f(x)", "\cdot", "      ", "g(x+\Delta x)", "+"," ", "f(x)", "\cdot", "g(x)", " ", "\over", "g(x+ \Delta x)", "\cdot", "g(x)", "}", "\cdot", "{", "1", "\over", "\Delta x", "}").scale(0.7)
        s0[4].set_color(YELLOW)
        self.play(ReplacementTransform(s1,s0))
        self.play(FadeOut(t0))
        self.wait(1)

        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "{", "g(x)", "\cdot", "{", "\left[", "f(x+ \Delta x)", "-", "f(x)", r"\right]", "}", "-", "f(x)", "\cdot", "      ", "g(x+\Delta x)", "+"," ", "f(x)", "\cdot", "g(x)", " ", "\over", "g(x+ \Delta x)", "\cdot", "g(x)", "}", "\cdot", "{", "1", "\over", "\Delta x", "}").scale(0.7)
        self.remove(s0)
        self.add(s1)
        s1[14].set_color(BLUE)
        s1[20].set_color(BLUE)
        t0 = Text("Factor out f(x)", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)
        self.play(FadeOut(t0))

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", "{", "g(x)", "\cdot", "{", "\left[", "f(x+ \Delta x)", "-", "f(x)", r"\right]", "}", "-", "f(x)", "\cdot", "\left[", "g(x+\Delta x)", " ","-", " ", " ", "g(x)",r"\right] ", "\over", "g(x+ \Delta x)", "\cdot", "g(x)", "}", "\cdot", "{", "1", "\over", "\Delta x", "}").scale(0.8)
        self.play(ReplacementTransform(s1,s0))
        s0[14].set_color(YELLOW)
        self.wait(1)

        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", " ", " ", " ", "{", "\left[", "f(x+ \Delta x)", "-", "f(x)", r"\right]", "    ", "        ", "}", "-", " "," "," ", "f(x)", "\cdot", " ", " ", " ","{", "\left[", "g(x+\Delta x)", "-", "g(x)",r"\right] ", "     ", "       " "}", "\over", " ", " ","g(x+ \Delta x)", "\cdot", " ", " ","g(x)", "}", "\cdot", "{", "1", "\over", "\Delta x", "}").scale(0.8)
        self.remove(s0)
        self.add(s1)
        for i_ in (54, 52, 53):
            s1[i_].set_color(BLUE)
        t0 = Text("Distribute", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)
        self.play(FadeOut(t0))


        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", " ", " ", " ", "{", "      ", "f(x+ \Delta x)", "-", "f(x)",  "      ", "\over", "\Delta x", "}", "-", " "," "," ", "f(x)", "\cdot", " ", " ", " ","{", "      ", "g(x+\Delta x)", "-", "g(x)","         ", "\over", "\Delta x" "}", "\over", " ", " ","g(x+ \Delta x)", "\cdot", " ", " ","g(x)", "}", " ", " ", " ", " ", " ", " ")
        self.play(ReplacementTransform(s1,s0))
        self.wait(1)
        t0 = Text("Apply the limit to all factors", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)
        self.play(FadeOut(t0))

        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=",r"\displaystyle\lim_{\Delta x \to 0}", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", " ", " ", " ", "{", "f(x+ \Delta x)", "-", "f(x)", "\over", "\Delta x", "}", "-", " "," "," ", "f(x)", "\cdot", " ", " ", " ","{","g(x+\Delta x)", "-", "g(x)", "\over", "\Delta x" "}", "\over", " ", " ","g(x+ \Delta x)", "\cdot", " ", " ","g(x)", "}")
        self.remove(s0)
        self.add(s1)

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","="," ", " ", " ", " ", "{", "\displaystyle\lim", "_", r"{\Delta x \to 0}", "g(x)", "\cdot", "\displaystyle\lim", "_", r"{\Delta x \to 0}", "{", "f(x+ \Delta x)", "-", "f(x)", "\over", "\Delta x", "}", "-", "\displaystyle\lim","_",r"{\Delta x \to 0}", "f(x)", "\cdot", "\displaystyle\lim", "_", r"{\Delta x \to 0}","{","g(x+\Delta x)", "-", "g(x)", "\over", "\Delta x" "}", "\over", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x+ \Delta x)", "\cdot", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x)", "}").scale(0.7)
        self.play(ReplacementTransform(s1,s0))
        self.wait(1)
        for i_ in (7, 9, 10):
            s0[i_].set_color(BLUE)
        self.wait(1)
        t0 = Text("Evaluate each limit", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)

        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","="," ", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", "\displaystyle\lim", "_", r"{\Delta x \to 0}", "{", "f(x+ \Delta x)", "-", "f(x)", "\over", "\Delta x", "}", "-", "\displaystyle\lim","_",r"{\Delta x \to 0}", "f(x)", "\cdot", "\displaystyle\lim", "_", r"{\Delta x \to 0}","{","g(x+\Delta x)", "-", "g(x)", "\over", "\Delta x" "}", "\over", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x+ \Delta x)", "\cdot", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x)", "}").scale(0.75)
        self.play(ReplacementTransform(s0,s1))
        self.wait(1)
        for i_ in (12, 14, 16, 17, 18, 19, 20):
            s1[i_].set_color(BLUE)
        self.wait(1)

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","="," ", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", " ", " ", " ", "{", " ", " ", "f'(x)", " ", " ", "}", "-", "\displaystyle\lim","_",r"{\Delta x \to 0}", "f(x)", "\cdot", "\displaystyle\lim", "_", r"{\Delta x \to 0}","{","g(x+\Delta x)", "-", "g(x)", "\over", "\Delta x" "}", "\over", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x+ \Delta x)", "\cdot", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x)", "}").scale(0.8)
        s0[18].set_color(YELLOW)
        self.play(ReplacementTransform(s1,s0))
        self.wait(1)
        for i_ in (23, 25, 26):
            s0[i_].set_color(BLUE)
        self.wait(1)

        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","="," ", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", " ", " ", " ", "{", " ", " ", "f'(x)", " ", " ", "}", "-", " "," "," ", "f(x)", "\cdot", "\displaystyle\lim", "_", r"{\Delta x \to 0}","{","g(x+\Delta x)", "-", "g(x)", "\over", "\Delta x" "}", "\over", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x+ \Delta x)", "\cdot", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x)", "}").scale(0.9)
        self.play(ReplacementTransform(s0,s1))
        self.wait(1)
        for  i_ in (28, 30, 32, 33, 34, 35, 36):
            s1[i_].set_color(BLUE)
        self.wait(1)

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","="," ", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", " ", " ", " ", "{", " ", " ", "f'(x)", " ", " ", "}", "-", " "," "," ", "f(x)", "\cdot", " ", " ", " ","{"," ", " ", "g'(x)", " ", " ", "}", "\over", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x+ \Delta x)", "\cdot", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x)", "}")
        s0[34].set_color(YELLOW)
        self.play(ReplacementTransform(s1,s0))
        self.wait(1)
        s0[39].set_color(BLUE)
        s0[40].set_color(BLUE)
        s0[41].set_color(BLUE)
        self.wait(1)

        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","="," ", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", " ", " ", " ", "{", " ", " ", "f'(x)", " ", " ", "}", "-", " "," "," ", "f(x)", "\cdot", " ", " ", " ","{"," ", " ", "g'(x)", " ", " ", "}", "\over", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x" , " ", "+ \Delta x)", "\cdot", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x)", "}")
        self.remove(s0)
        self.add(s1)

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","="," ", " ", " ", " ", "{", " ", " ", " ", "g(x)", "\cdot", " ", " ", " ", "{", " ", " ", "f'(x)", " ", " ", "}", "-", " "," "," ", "f(x)", "\cdot", " ", " ", " ","{"," ", " ", "g'(x)", " ", " ", "}", "\over", " ", " ","g(x" , ")", " ", "\cdot", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x)", "}")
        self.play(ReplacementTransform(s1,s0))
        self.wait(1)
        s0[45].set_color(BLUE)
        s0[46].set_color(BLUE)
        s0[47].set_color(BLUE)
        self.wait(1)

        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=", "{", "g(x)", "\cdot", "{", "f'(x)", "}", "-", "f(x)", "\cdot", "{", "g'(x)", "}", "\over", " ", "g(x)" , "\cdot", "\displaystyle\lim_", r"{\Delta x \to 0}","g(x)", "}")
        self.remove(s0)
        self.add(s1)

        s0 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=", "{", "g(x)", "\cdot", "{", "f'(x)", "}", "-", "f(x)", "\cdot", "{", "g'(x)", "}", "\over", " ", "g(x)" , "\cdot", " ", " ","g(x)", "}")
        self.play(ReplacementTransform(s1,s0))
        self.play(FadeOut(t0))
        self.wait(1)
        s0[16].set_color(BLUE)
        s0[17].set_color(BLUE)
        s0[20].set_color(BLUE)
        t0 = Text("Combine", font="Montserrat").shift(DOWN*3)
        t0.scale(0.5)
        self.play(FadeIn(t0))
        self.wait(1)
        self.play(FadeOut(t0))

        s1 = MathTex(r"\dfrac{d}{dx} \left[\dfrac{f(x)}{g(x)} \right]","=", "{", "g(x)", "\cdot", "{", "f'(x)", "}", "-", "f(x)", "\cdot", "{", "g'(x)", "}", "\over", "\left[", "g(x)" , " ", r"\right] ", "^2"," ", "}").scale(1.3)
        self.play(ReplacementTransform(s0,s1))
        self.wait(1)

        # Last Scene
        self.play(ApplyMethod(s1.next_to,text2, DOWN))
        self.play(FadeIn(uptext))
        self.wait(1)


class PowerRule(Scene):
    def construct(self):

        text1 = Text("The Power Rule of Differentiation", font="Montserrat").shift(UP*2)
        title2 = Text("If n is a  positive integer, then", color=YELLOW, font="Montserrat").scale(0.7)
        text3 = MathTex("\dfrac{d}{dx}(x^n) = nx^{n-1}").scale(1.3)
        text3.next_to(title2,DOWN)
        uptext = VGroup(text1, title2)
        self.play(Write(uptext))
        self.play(FadeIn(text3))
        self.wait(1)
        self.play(FadeOut(uptext))
        self.play(FadeOut(text3))


        step0 = MathTex("\dfrac{d}{dx} (x^n) = ", "\displaystyle\lim_", r"{\Delta x  \to 0}", "{","(x", " ", " "," ", " ", "+", " "," "," "," "," "," "," ","\Delta x)^n","-","x^n", "\over", "\Delta x","}")
        #step0.shift(UP*2)
        self.play(FadeIn(step0))
        self.wait(1)
        step0[4].set_color(BLUE)
        step0[9].set_color(BLUE)
        step0[17].set_color(BLUE)
        #self.wait(1)

        text1 = Text("Apply binomial expansion to this term", font="Montserrat").shift(DOWN*3)
        text1.scale(0.7)
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(FadeOut(text1))

        step1 = MathTex("\dfrac{d}{dx} (x^n) = ", "\displaystyle\lim_", r"{\Delta x  \to 0}", "{","x^n", "+", "{n \choose 1}","x^{n-1}", "\Delta x", "+", "{n \choose 2}","x^{n-2}","(\Delta x)^2","+","\cdots","+","{n \choose n}","(\Delta x)^n","-","x^n", "\over", "\Delta x","}").scale(0.7)
        self.play(ReplacementTransform(step0,step1))
        self.wait(1)
        step1[4].set_color(BLUE)
        step1[18].set_color(BLUE)
        step1[19].set_color(BLUE)
        #self.wait(1)

        text2 = Text("These two terms will cancel each other out", font="Montserrat").shift(DOWN*3)
        text2.scale(0.7)
        self.play(FadeIn(text2))
        self.wait(1)
        self.play(FadeOut(text2))

        step2 = MathTex("\dfrac{d}{dx} (x^n) = ", "\displaystyle\lim_", r"{\Delta x  \to 0}", "{","   ", " ", "{n \choose 1}","x^{n-1}", "\Delta x", "+", "{n \choose 2}","x^{n-2}","(\Delta x)^2","+","\cdots","+","{n \choose n}","(\Delta x)^n"," ","   ", "\over", "\Delta x","}").scale(0.8)
        self.play(ReplacementTransform(step1, step2))
        self.wait(1)

        step3 = MathTex("\dfrac{d}{dx} (x^n) = ", "\displaystyle\lim_", r"{\Delta x  \to 0}", "{", "{n \choose 1}","x^{n-1}", "\Delta x", "+", "{n \choose 2}","x^{n-2}","(\Delta x)","^","2","+","\cdots","+","{n \choose n}","(\Delta x)","^","n"," ", "\over", "\Delta x","}").scale(0.8)
        self.remove(step2)
        self.add(step3)
        for i_ in (6, 10, 12, 17, 19, 22):
            step3[i_].set_color(BLUE)

        text3 = Text("Divide each term in the numerator by Δx", font="Montserrat").shift(DOWN*3)
        text3.scale(0.7)
        self.play(FadeIn(text3))
        self.wait(1)
        self.play(FadeOut(text3))

        step4 = MathTex("\dfrac{d}{dx} (x^n) = ", "\displaystyle\lim_", r"{\Delta x  \to 0}", "{", "{n \choose 1}","x^{n-1}", "        ", "+", "{n \choose 2}","x^{n-2}","(\Delta x)"," "," ","+","\cdots","+","{n \choose n}","(\Delta x)","^","{n-1}"," ", "\over", " ","}").scale(0.8)
        self.play(ReplacementTransform(step3, step4))

        step5 = MathTex("\dfrac{d}{dx} (x^n) = ", "\displaystyle\lim_", r"{\Delta x  \to 0}", "\left[", "{n \choose 1}","x^{n-1}", "        ", "+", "{n \choose 2}","x^{n-2}","(\Delta x)"," "," ","+","\cdots","+","{n \choose n}","(\Delta x)","^","{n-1}"," ", " ", " ",r"\right]").scale(0.8)
        self.play(ReplacementTransform(step4, step5))
        self.wait(1)

        step6 = MathTex("\dfrac{d}{dx} (x^n) = ", "\displaystyle\lim_", r"{\Delta x  \to 0}", "\left[", "{n \choose 1}","x^{n-1}",  "+ {n \choose 2} x^{n-2} (\Delta x) + \cdots + {n \choose n} (\Delta x)^ {n-1}",r"\right]").scale(0.8)
        self.remove(step5)
        self.add(step6)
        step6[2].set_color(BLUE)
        step6[6].set_color(BLUE)
        #self.wait(1)

        text4 = Text("These terms will approach zero as Δx approaches zero", font="Montserrat").shift(DOWN*3)
        text4.scale(0.7)
        self.play(FadeIn(text4))
        self.wait(1)
        self.play(FadeOut(text4))

        step7 = MathTex("\dfrac{d}{dx} (x^n) = ", " ", " ", " ", "{n \choose 1}","x^{n-1}", " ", " ")
        self.play(ReplacementTransform(step6, step7))
        self.wait(1)
        step7[4].set_color(BLUE)
        #self.wait(1)

        text5 = Text("This factor is simply n", font="Montserrat").shift(DOWN*3)
        text5.scale(0.7)
        self.play(FadeIn(text5))
        self.wait(1)
        self.play(FadeOut(text5))

        step8 = MathTex("\dfrac{d}{dx} (x^n) = ", " ", " ", " ", "n","x^{n-1}", " ", " ").scale(1.3)
        self.play(ReplacementTransform(step7, step8))
        self.wait(1)

        self.play(ApplyMethod(step8.next_to,title2, DOWN))
        self.play(FadeIn(uptext))
        self.wait(1)
