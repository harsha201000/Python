from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color, Line
import random

# RGBA = Red,Green,Blue, Opacity
Window.clearcolor = (1,1,1,1)

class PaintWindow(Widget):
    def on_touch_down(self, touch):
        color_red = random.randint(0,255)
        color_green = random.randint(0,255)
        color_blue = random.randint(0,255)
        self.canvas.add(Color(rgb=(color_red/255.0,color_green/255.0,color_blue/255.0)))
        d = 30
        self.canvas.add(Ellipse(pos=(touch.x - d/2, touch.y), size=(d,d)))
        touch.ud['line'] = Line(points=(touch.x,touch.y))
        self.canvas.add(touch.ud['line'])
        
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x,touch.y]

# Root Window = Paint Window + Button
class MSPaintApp(App):
    def build(self):
        self.icon = "paint.png"
        rootWindow = Widget()
        self.painter = PaintWindow()
        clear_btn = Button(text="Clear")
        clear_btn.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clear_btn)
        
        return rootWindow
    
    def clear_canvas(self,object):
        self.painter.canvas.clear()
    
if __name__ == "__main__":
    app = MSPaintApp()
    app.run()
    
# 1) Import Line Graphics
# 2) Create a Touch dictionary -> Store the initial touch point in it
# 3) When the moose is dragged to extend the line store the next points inside dictionary
# 4) Store it inside the canvas
# 5) Random colours
