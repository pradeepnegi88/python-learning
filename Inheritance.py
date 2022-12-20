class Animal:
    def __init__(self, age, color):
        self.age = age
        self.color = color

    def born(self):
        print("This animal has been born")

    def talk(self):
        print("This animal makes a sound")


class Bird(Animal):
    def __init__(self, age, color, altitude):
        # self.age = age
        # self.color = color
        super.__init__(age, color)
        self.altitude = altitude

    def talk(self):
        print("chirp")

    def fly(self, fleet):
        print(f'This bird flies {fleet}')



tweetie = Bird(1, "yellow")
tweetie.talk()
tweetie.fly(100)
