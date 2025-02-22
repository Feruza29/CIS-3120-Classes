class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self):
        print("hi")

from Animal import Animal

# Creating an Animal instance
x = Animal("Leo", "Lion")

x.talk()
x.eat("meat")
x.sleep(5)
x.walk(2)
x.describe()
x.set_name("Kile")
x.descibe()
x.make_sound("Roar")
x.play("chasing a butterfly")
x.age(4)
x.run(20)
x.jump(3)
