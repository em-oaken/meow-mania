"""
Amuse your pet
"""

from random import randint

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HomeScreen(toga.Box):
    def __init__(self, on_goto_press, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_goto_press = on_goto_press

        # Elements
        title = toga.Label('Meow Mania', style=Pack(padding=5, flex=2))

        self.duration_slider = toga.Slider(
            min=1, max=10, value=3, tick_count=10
        )

        btn_game1 = toga.Button (
            text="Game 1",
            on_press = self.goto_game1,
            style=Pack(padding=5)
        )
        btn_game2 = toga.Button (
            text="Game 2",
            on_press = self.goto_game2,
            style=Pack(padding=5)
        )

        parameters_box = toga.Box(
            style=Pack(direction=COLUMN, flex=3),
            children=[
                toga.Box(
                    style=Pack(direction=ROW),
                    children=[btn_game1, btn_game2]
                )
            ]
        )


        # Layout assembly
        self.style.update(direction=COLUMN)
        self.add(title)
        self.add(toga.Box(style=Pack(flex=1), children=[self.duration_slider]))
        self.add(parameters_box)
    
    def goto_game1(self, widget):
        self.on_goto_press('game1')
    
    def goto_game2(self, widget):
        self.on_goto_press('game2')


class PlayScreen(toga.Box):
    def __init__(self, on_goto_press, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_goto_press = on_goto_press

        button = toga.Button(
            text="Back to home screen",
            on_press = self.goto_home,
            style=Pack(padding=5)
        )

        background_img = toga.Image('resources/background1.png')
        image_view = toga.ImageView(background_img)
        self.box_background = toga.Box(children=[image_view])

        target = toga.Button(
            icon=toga.Icon(path='i want the default icon'),
            on_press=self.on_press_target,
            style=Pack(background_color='#000000')
        )
        self.target_box = toga.Box(children=[target], style=Pack(padding=(-300, 100, 0, 0)))

        self.style.update(direction=COLUMN, padding=0)
        self.add(button)
        self.add(self.box_background)
        self.add(self.target_box)

    async def on_press_target(self, widget):
        self.target_box.style.update(padding=(randint(-500, 0), 0, 0, randint(0, 400)))
        self.playground_size = (self.box_background.layout.width, self.box_background.layout.height)

    def goto_home(self, widget):
        self.on_goto_press('home')


class MeowMania(toga.App):
    def startup(self):
        self.homescreen = HomeScreen(on_goto_press=self.goto)
        self.playscreen = PlayScreen(on_goto_press=self.goto)

        self.main_window = toga.Window(resizable=False)
        self.main_window.content = self.homescreen
        self.main_window.show()

        self.app_size = self.main_window.size  # width, height

    
    def goto(self, whereto):
        match whereto:
            case 'game1':
                self.main_window.content = self.playscreen
                # self.playscreen.label.text = 'Game1'
            
            case 'game2':
                self.main_window.content = self.playscreen
                # self.playscreen.label.text = 'Game2'
            
            case 'home':
                self.main_window.content = self.homescreen


def main():
    return MeowMania()
