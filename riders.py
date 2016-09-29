# from model_life import Bike, RoadBike, MountainBike


class Riders(RoadBike, MountainBike):

    def __init__(self, name, style):
        self.name = name
        self.style = style

    def get_info(self):
        name = input("What's your name? ").lower()
        style = input("Do you prefer [R]oad or [M]ountain biking? ").lower()
        if style == "r":
            roadbike += 1
        else:
            mountain_bike += 1
        print(name)
        print(style)

rider = Riders()
rider.get_info()
