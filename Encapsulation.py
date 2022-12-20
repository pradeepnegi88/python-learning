class Person:
    public_attribute = "Show"  # Accessible from outside
    __private_attribute = "Hidden"  # Not accessible

    # Not accessible from outside
    def __hidden_method(self):
        print("This method is hidden")
        self.__variable = 0

    # Accessible from outside
    def normal_method(self):
        # The method is accessible from inside
        self.__hidden_method()


student = Person()
# student.__hidden_method()  # This method is not accessible from outside
# student.hidden_method()
student.normal_method()

# There is a little trick (not recommended) to access hidden attributes and methods. These methods are to be called
# with a somewhat different name: instance + _ + ClassName + hidden method/attribute


# student._Person__hidden_method()
print(student._Person__private_attribute)