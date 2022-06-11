from base.important_variables import keyboard


def key_is_pressed(pygame_key_index):
    return keyboard.get_key_event(pygame_key_index).happened_this_cycle


def key_is_hit(pygame_key_index):
    return not keyboard.get_key_event(pygame_key_index).happened_last_cycle() and key_is_pressed(pygame_key_index)


def key_has_been_released(pygame_key_index):
    return keyboard.get_key_event(pygame_key_index).happened_last_cycle() and not key_is_pressed(pygame_key_index)


def get_time_of_key_being_held_in(pygame_key_index):
    return keyboard.get_timed_event(pygame_key_index).current_time


def mouse_is_clicked():
    return keyboard.mouse_clicked_event.is_click()