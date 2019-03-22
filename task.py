    from math import cos, sin
    from random import choice, randrange
    from time import sleep
    
    
    class Car:
        def _init_(self, angle, speed, model)
            self.angle = angle
            self.speed = speed
            self.x = 0
            self.y = 0
        def handle_event(self, event):
            print("The car enountered ", event.object, "\n Restarting in ", event.duration, " seconds")
            sleep(event.duration)
        def move(self):
            self.x = x+self.speed*cos(self.angle % 180)
            self.y = y+self.speed*sin(self.angle % 180)
            print("The car is now at ", self.x, ", ", self.y)
        def turn(self, angle):
            self.angle = self.angle + angle
        def slow(self, speed):
            self.speed = self.speed - speed
        def accelerate(self, speed):
            self.speed = self.speed + speed
            
            
        
    class Event:
        def _init_(self, event_object, duration):
            self.object = event_object
            self.duration = duration
        
    def main():
        car1 = Car(45, 100)
        event1 = Event("other car", 1)
        event2 = Event("tree", 5)
        event3 = Event("other car", 3)
        event_list = [event1, event2, event3]
            while True:
                car1.handle_event(choice(event_list))
                car1.move()
                car1.turn(randrange(0, 360))
                car1.slow(randrange(0, 100))
                car1.accelerate(randrange(0, 100))
         
                
        
