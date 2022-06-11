import pygame

from base.history_keeper import HistoryKeeper
from base.keyboard import Keyboard
from gui_components.window import Window
from base.velocity_calculator import VelocityCalculator

pygame.init()

screen_length = 300
screen_height = 300

keyboard = Keyboard()
game_window = Window(screen_length, screen_height, (200, 200, 200), "Game Basics")
history_keeper = HistoryKeeper()
velocity_calculator = VelocityCalculator()

