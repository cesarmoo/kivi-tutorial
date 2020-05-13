from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.base import runTouchApp
from kivy.lang import Builder

Builder.load_string('''
<RootWidget>:
    text: 'the background'
    font_size: 150
    Image:
        pos: root.pos
        size: root.width * 0.5, root.height
        source: 'pic.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        pos: 200, 300
        size: root.width * 0.5, root.height
        source: 'pic.png'
        allow_stretch: True
        keep_ratio: False
''')

class RootWidget(Label):
    def do_layout(self, *args):
        num_children = len(self.children)
        width = self.width
        child_width = width / num_children

        positions = range(0, width, child_width)
        for position, child in zip(positions, self.children):
            child.height = self.height
            child.width = child_width
            child.x = self.x + position
            child.y = self.y

    def on_size(self, *args):
        self.do_layout()

    def on_pos(self, *args):
        self.do_layout()

    def add_widget(self, widget):
        super(RootWidget, self).add_widget(widget)
        self.do_layout()

    def remove_widget(self, widget):
        super(RootWidget, self).add_widget(widget)
        self.do_layout()

runTouchApp(RootWidget())