import pandas as pd 
from datetime import datetime,timedelta

class Truck:
    def __init__(self,name,rate,minimum_run,cycle):
        self.name=name
        self.rate=rate
        self.minmum_run=minimum_run
        self.cycle=cycle
    
    def days_reamining_in_cycle(self):
        return (self.cycle[1]-datetime.today())


truck_list=[]

truck_list.append(Truck("l1",30,3000,[datetime(2020,4,7),datetime(2020,5,6)]))
truck_list.append(Truck("l2",25,2400,[datetime(2020,4,10),datetime(2020,5,9)]))
truck_list.append(Truck("l3",34,2700,[datetime(2020,4,10),datetime(2020,5,9)]))
truck_list.append(Truck("l2",25,3400,[datetime(2020,4,26),datetime(2020,5,25)]))
truck_list.append(Truck("l2",29,2800,[datetime(2020,4,1),datetime(2020,4,30)]))


# dif=t1.days_reamining_in_cycle().days
print(truck_list)

    




