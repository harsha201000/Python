from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer

class App(MDApp):
    title = "Media Player"
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        player = VideoPlayer(source = "4d9f0f3d-35a0-4c3b-8fbf-8e6df02353f3.mp4")
        
        player.state = 'stop'
        
        return player
    
App().run()