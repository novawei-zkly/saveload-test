
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} is eating {food}')

    def run(self):
        print(f'{self.name} is running')