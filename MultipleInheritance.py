class Father:
    def talk(self):
        print("Hello")


class Mother:
    def laugh(self):
        print("ha ha ha ha..... he he he ")

    def talk(self):
        print("How are you ? ")


class Child(Mother, Father ):
    pass


class GrandChild(Child):
    pass


myGrandChild = GrandChild()
myGrandChild.talk()
myGrandChild.laugh()
print(GrandChild.__mro__)
print(Child.__bases__)
print(Mother.__subclasses__())