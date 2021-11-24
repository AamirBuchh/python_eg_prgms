class Person():

    def __init__(self, name, address, cell): # class construtor funtion
        self.name =name
        self.address= address
        self.cell=cell


    def get_name(self):# method function
        return self.name

    def set_name(self,new_name):# method function
        self.name=new_name


    def display_details(self):# method function
        print(f"Details: {self.name}, {self.address} and {self.cell}")


" different ways of entering data in class"
person1 = Person(name='Amir', address= 'Rawlapora', cell=1234567)
person2 = Person(name="Sqib", address= 'Soura', cell =3456798)
person3 = Person("Hamid","Budgam",980809808)

print("Name = " + person3.name)
person4 = Person(person1.name,person2.address,person3.cell)
print("Name = ",person4.name)