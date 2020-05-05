class Cs:
    
    @staticmethod
    def static_method():
        print("Static method")
    
    @Classmethod
    def class_method(cls):
        print("Class method")

    def instance_method(self):
        print("Instance method")

i = Cs()

# ! python에서는 Class method가
# * static method
# * class method
# 두가지로 존재한다고 할 수 있다.

Cs.static_method()
Cs.class_method()
i.instance_method()