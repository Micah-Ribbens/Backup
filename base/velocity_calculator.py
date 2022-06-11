class VelocityCalculator:
    time = 0

    def get_velocity(self, unit_of_measurement, how_much):
        return (unit_of_measurement / 1000) * how_much

    def get_meausurement(self, unit_of_measurement, how_much):
        return (unit_of_measurement / 100) * how_much

    def calculate_distance(self, velocity):
        return velocity * self.time

