class Aircon:
    def __init__(self, name, ac_type, horsepower):
        self.name = name
        self.ac_type = ac_type
        self.horsepower = horsepower

    def details(self):
        return (
            f"Aircon Name: {self.name}\n"
            f"Aircon Type: {self.ac_type}\n"
            f"Horse Power: {self.horsepower} HP"
        )
