import random

class StadiumEnvironment:
    def __init__(self):
        self.gate_a_occupancy = 0
        self.gate_b_occupancy = 0
        self.pitch_moisture = 50 
        self.weather_condition = "Sunny"

    def update(self):
        self.gate_a_occupancy = random.randint(0, 100)
        self.gate_b_occupancy = random.randint(0, 100)

        self.weather_condition = random.choice(["Sunny", "Cloudy", "Rainy"])


        if self.weather_condition == "Sunny":
            # Sun dries the pitch a bit
            self.pitch_moisture -= random.randint(1, 5)
        elif self.weather_condition == "Cloudy":
            # Cloudy, small decrease
            self.pitch_moisture -= random.randint(0, 2)
        elif self.weather_condition == "Rainy":
            # Rain increases moisture
            self.pitch_moisture += random.randint(5, 15)

        # Keep moisture within 0-100%
        if self.pitch_moisture < 0:
            self.pitch_moisture = 0
        elif self.pitch_moisture > 100:
            self.pitch_moisture = 100

    def get_data(self):
        return (
            self.gate_a_occupancy,
            self.gate_b_occupancy,
            self.pitch_moisture
        )

    def get_weather(self):
        return self.weather_condition