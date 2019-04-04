#id __name__
#PEP8
#generator
#dont print in methods
#logger
#show usecase
#Events as class
#Car as class
#Multiprocessing
#environment class
#env -> event -> car -> event -> enviro



from math import cos, sin
from random import choice, randrange
from time import sleep


class Object:
    def __init__(self, name):
        self.name = name

class Environment:
    def __init__(self, cars, objects):
        self.cars = cars
        self.objects = objects
        self.log = []
    def do_actions(self):
        object_msg = Event.encounter_object(choice(self.cars), choice(self.objects), randrange(1,5))
        steer_msg = Event.steer(choice(self.cars))
        move_msg = Event.move(choice(self.cars))
        self.log.append(object_msg)
        self.log.append(steer_msg)
        self.log.append(move_msg)
        return "\n" + object_msg + "\n" + steer_msg + "\n" + move_msg

class Car:
    def __init__(self, angle, speed, model):
        self.angle = angle
        self.speed = speed
        self.model = model
        self.x = 0
        self.y = 0

    def move(self):
        self.x = self.x+self.speed*cos(self.angle % 180)
        self.y = self.y+self.speed*sin(self.angle % 180)
    def turn(self, angle):
        self.angle = self.angle + angle
        while self.angle>180:
            self.angle=self.angle-360
        while self.angle<-180:
            self.angle=self.angle+360
        return self.angle
    def slow(self, speed):
        self.speed = self.speed - speed
        if self.speed < 0:
            self.speed=0
        return self.speed
    def accelerate(self, speed):
        self.speed = self.speed + speed
        return self.speed


class Event:
    @staticmethod
    def encounter_object(car, object, duration):
        sleep(duration)
        return car.model + " enountered " + object.name + "\nRestarted after " + str(duration) + " seconds"
    @staticmethod
    def steer(car):
        speed_change = randrange(-25, 25)
        if speed_change<0:
            car.slow(abs(speed_change))
        if speed_change>0:
            car.accelerate(speed_change)
        car.turn(randrange(-180, 180))
        return car.model + " is moving " + str(car.speed) + " km/h "
    @staticmethod
    def move(car):
        car.move()
        return "The car is now at " + str(car.x) + ", " + str(car.y)

def main():
    car1 = Car(45, 100, "fiat")
    car2 = Car(0, 30, "maluch")
    object1 = Object("rock")
    object2 = Object("tree")
    object3 = Object("crossroad")
    object_list = [object1, object2, object3]
    car_list = [car1, car2]
    environment = Environment(car_list, object_list)
    counter = 10;
    while counter>0:
        print(environment.do_actions())
        counter=counter-1

main()
