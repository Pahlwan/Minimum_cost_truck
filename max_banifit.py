import pandas as pd 
from datetime import datetime

class Truck:

    

    def __init__(self,name,rate,minimum_run,cycle):
        self.name=name
        self.rate=rate
        self.minmum_run=minimum_run
        self.cycle=cycle
    
    def days_reamining_in_cycle(self):
        pass


truck_list=[]

t1=Truck("l1",30,3000,[datetime.now,datetime(2010-5-6)])

print(t1)

    




