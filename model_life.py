

class Bike:

    def __init__(self, color, wheel_size, frame_material):
        self.color = color
        self.wheel_size = wheel_size
        self.frame_material = frame_material


class RoadBike(Bike):

    def __init__(self):
        self.color = "red"
        self.wheel_size = 700
        self.frame_material = "carbon"


class MountainBike(Bike):

    def __init__(self):
        self.color = "grey"
        self.wheel_size = 29
        self.frame_material = "aluminum"


class Riders(RoadBike, MountainBike):

    def __init__(self, name, style):
        self.name = []
        self.style = style
        self.road_bike = 0
        self.mountain_bike = 0

    def get_info(self):
        name = input("What's your name? ").lower()
        style = input("Do you prefer [R]oad or [M]ountain biking? ").lower()

        self.name.append(name)
        print(self.name)
        if style == "r":
            self.road_bike += 1
        else:
            self.mountain_bike += 1

        print(self.road_bike)
        print(self.mountain_bike)


rider = Riders(RoadBike, MountainBike)
rider.get_info()
bike = Bike("red", 29, "aluminum")
# print(bike.color)
# print(bike.wheel_size)
# print(bike.frame_material)
danielle_bike = bike
road_bike = RoadBike()
mountain_bike = MountainBike()
# print(danielle_bike.color)
# print(road_bike.color)
# print(mountain_bike.color)
john_bike = road_bike
# print(john_bike)
