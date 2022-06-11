class Screen:
    components = []
    background_file = ""

    def __init__(self, background_file):
        self.background_file = background_file

    def run(self):
        pass

    def get_components(self):
        return self.components

    def render_background(self):
        pass