from base.colors import pleasing_green, white
from base.utility_functions import key_is_hit
from gui_components.screen import Screen
from gui_components.text_box import TextBox


class NavigationScreen(Screen):
    buttons = []
    screens = []
    selected_screen = None

    def __init__(self, screens, screen_names):
        self.buttons = []

        for screen_name in screen_names:
            self.append(TextBox(screen_name, 25, pleasing_green, white, True))

        self.screens = screens
        self.selected_screen = self

    def run(self):
        for x in range(len(self.buttons)):
            button = self.buttons[x]

            if button.got_clicked() and self.selected_screen == self:
                self.selected_screen = self.screens[x]

        if key_is_hit(pygame.K_ESCAPE):
            self.selected_screen = self

        if self.selected_screen != self:
            self.selected_screen.run()

    def get_components(self):
        return self.components if self.selected_screen == self else self.selected_screen.get_components()