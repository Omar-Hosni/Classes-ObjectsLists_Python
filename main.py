class Car:
    def __init__(self, car_details_list):
        self.car_details_list = car_details_list

    def insurance_cost(self):
        model_year = self.car_details_list[0]
        price = self.car_details_list[1]
        model_name = self.car_details_list[2]

        if 2020>= model_year >=2010 and 60000 <= price <= 20000:
            insurance = price*0.05
            return insurance
        else:
            insurance2 = price*0.07
            return insurance2

    def doors_status(self):
        door_status = self.car_details_list[3]
        if door_status == True:
            return True
        else:
            return False

    def get_car_details(self):
        print('car model is ', self.car_details_list[2], 'it was released in ',self.car_details_list[0])



#List of Tesla
Tesla_Details = [2020,19000,"Tesla Model X",True]

#Tesla Object
Tesla = Car(Tesla_Details)
Tesla.insurance_cost()


#List of BMW
BMW_Details = [2005 , 5000 , "MG" , False]

#BMW Object
BMW = Car(BMW_Details)
