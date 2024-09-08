class Transport:
    state = 'На земле'
    def show_state(self):
        print(self.state)

class Flying(Transport):
    # state = 'на земле'
    def fly(self):
        self.state = 'В небе'
    
class Swimming(Transport):
    # state = 'на земле'
    def swim(self):
        self.state = 'В воде'

class Amphibian(Flying, Swimming):
    def land(self):
        self.state = 'На земле'

amphibian = Amphibian()
amphibian.show_state()
amphibian.fly()
amphibian.show_state()
amphibian.swim()
amphibian.show_state()
