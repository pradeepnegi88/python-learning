class Human:
    def __init__(self, name):
        self.name = name

    @classmethod
    def class_can_access_directly(cls):
        print("class_can_access_directly")

    @staticmethod
    def static_method_call():
        print("static_method_call")


h = Human("Pradeep")
h.class_can_access_directly()
Human.class_can_access_directly()
Human.static_method_call()
