import pandas as pd 
from datetime import datetime,timedelta

class Truck:
    def __init__(self,name,rate,minimum_run,already_ran,cycle):
        self.name=name
        self.rate=rate
        self.minmum_run=minimum_run
        self.cycle=cycle
        self.alread_ran=already_ran
    
    def days_reamining_in_cycle(self):
        return (self.cycle[1]-datetime(2020,4,27))


def min_cost(truck_list,distance):
    
    pay_after_pick_list=[] 
    cost_func=[]
    min_cost_func=[]
    for t in truck_list:
        pay=0
        if(t.alread_ran+distance>t.minmum_run):
            pay=t.rate*t.minmum_run+(t.alread_ran+distance-t.minmum_run)*(t.rate*120/100)
        else:
            pay=t.rate*t.minmum_run
        pay_after_pick_list.append(pay)

        #more to impliment
        if(t.minmum_run-t.alread_ran==0):
            cost_func.append(t.days_reamining_in_cycle().days/1)
        else:
            cost_func.append(t.days_reamining_in_cycle().days/(t.minmum_run-t.alread_ran))

    for i in range(len(truck_list)):
        min_cost_func.append(cost_func[i]*pay_after_pick_list[i])

    return min_cost_func



truck_list=[]

truck_list.append(Truck("l1",30,3000,2500,[datetime(2020,4,7),datetime(2020,5,6)]))
truck_list.append(Truck("l2",25,2400,2400,[datetime(2020,4,10),datetime(2020,5,9)]))
truck_list.append(Truck("l3",34,2700,2300,[datetime(2020,4,10),datetime(2020,5,9)]))
truck_list.append(Truck("l4",25,3400,2500,[datetime(2020,4,26),datetime(2020,5,25)]))
truck_list.append(Truck("l5",29,2800,2000,[datetime(2020,4,1),datetime(2020,4,30)]))


list1=min_cost(truck_list,600)

print(truck_list[list1.index(min(min_cost(truck_list,600)))].name)

# dif=t1.days_reamining_in_cycle().days



    




