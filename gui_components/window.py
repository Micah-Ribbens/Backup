import pygame


class Window:
    screens = []
    window = None
    background_color = None
    title = None

    def __init__(self, length, height, background_color, title):
        self.window = pygame.display.set_mode((length, height))
        pygame.display.set_title(title)
        self.background_color = background_color

    def add_screen(self, screen):
        self.screens.append(screen)

    def display_screen(self, screen):
        for screen in self.screens:
            screen.is_visible = False

        screen.is_visible = True

    def run(self):
        for screen in self.screens:
            if screen.is_visible:
                screen.run()
                screen.display_background()

            else:
                continue

            for component in screen.get_components():
                component.run()
                component.render()

    def get_window(self):
        return self.window
