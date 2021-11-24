class CarDetails():
    def __init__(self,brand,chasis_no,year):
        self.brand = brand
        self.chasis_no = chasis_no
        self.year = year

    def car_details(self):
        print(f'Brand = {self.brand}, Chasis.no = {self.chasis_no} and Year = {self.year}')

    def car_brand(self):
        print(f"Your car brand is {self.brand}")

    def valid_chasis_no(self):
        if  int(self.chasis_no) > 20000000 and int(self.chasis_no) < 30000000 :
            print(f"{self.chasis_no} is valid")
        else:
            print(f"{self.chasis_no} is not valid")
        

car1 = CarDetails(brand = 'Hundia', chasis_no ='21323244', year = '2015')
car2 = CarDetails(brand = 'Maruti', chasis_no ='32311234', year = '2012')

"""car1.car_details()
print(car1.brand)
print(car1.chasis_no)
print(car1.year)
car1.brand = "Honda"
print(car1.brand)"""

car1.car_brand()
car2.car_brand()

car1.valid_chasis_no()
car2.valid_chasis_no()


