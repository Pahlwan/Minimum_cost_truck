import pandas as pd 
from datetime import datetime,timedelta

status_options=["LOADIG","WAITING","UNLOADING"]

class Truck:
    def __init__(self,name,rate,minimum_run,already_ran,cycle,status="Waiting"):
        self.name=name
        self.rate=rate
        self.minmum_run=minimum_run
        self.cycle=cycle
        self.alread_ran=already_ran
        self.status=status
    
    def days_reamining_in_cycle(self):
        return (self.cycle[1]-datetime(2020,4,27))


# This calculate eficiency for each truck
def min_cost(truck_list,asssignment_distance,status_consideration=False):
    
    # pay_after_pick_list=[] 
    # cost_func=[]
    # min_cost_func=[]
    # for t in truck_list:
    #     pay=0
    #     if(t.alread_ran+distance>t.minmum_run):
    #         pay=t.rate*t.minmum_run+(t.alread_ran+distance-t.minmum_run)*(t.rate*120/100)
    #     else:
    #         pay=t.rate*t.minmum_run
    #     pay_after_pick_list.append(pay)

    #     #more to impliment
    #     if(t.minmum_run-t.alread_ran==0):
    #         cost_func.append(t.days_reamining_in_cycle().days/1)
    #     else:
    #         cost_func.append(t.days_reamining_in_cycle().days/(t.minmum_run-t.alread_ran))

    # for i in range(len(truck_list)):
    #     min_cost_func.append(cost_func[i]*pay_after_pick_list[i])

    # return min_cost_func
    if status_consideration==True:
        for t in truck_list:
            if t.status=="Unloading":
                truck_list.remove(t)
    
    cost_efficiency=[]
    for i in truck_list:

        total_run_after_assignment=i.alread_ran+asssignment_distance

        if total_run_after_assignment>i.minmum_run and (i.minmum_run-i.alread_ran)!=0:
            cost_efficiency.append(((i.rate*i.minmum_run)+(i.rate*120/100)*(total_run_after_assignment-i.minmum_run))*((i.minmum_run-i.alread_ran)/i.minmum_run)*i.days_reamining_in_cycle().days)

        elif (i.minmum_run-i.alread_ran)!=0 and total_run_after_assignment<=i.minmum_run:
            # Main formula
            cost_efficiency.append((i.rate*i.minmum_run)*((i.minmum_run-i.alread_ran)/i.minmum_run)*i.days_reamining_in_cycle().days)

        else:
            cost_efficiency.append((i.rate*i.minmum_run)*(1)*i.days_reamining_in_cycle().days)

    return cost_efficiency


# Create Own truck list
def my_own_trucks():
    truck_list=[]
        
    print("Enter truck details 'PLZ FILL' all details")
    for _ in range(int(input("Input number of trucks : "))):
        print("\n"+"Enter Truck Detail".center(60,'-'))
        print("\n")
        name=input("Truck number or name : ")
        rate=int(input("Rate per km : "))
        minimum_run=int(input("Mininumum run every month :"))
        already_ran=int(input("How much km's already used :"))
        while(1):
            try:
                cycle=list(map(lambda x:datetime.strptime(x,'%Y/%m/%d'),input("Enter cycle in Format YYYY/MM/DD-YYYY/MM/DD : ").strip().split('-')))
                if ((cycle[1]-cycle[0]).days<=0):
                    print("Invailid cycle try again input date again")
                    continue
            except:
                print("Invailid date format input date again")
                continue

            else:
                break
        status=input().upper   
           
        tepm_t=Truck(name,rate,minimum_run,already_ran,cycle,status)
        truck_list.append(tepm_t)
        print()
    return truck_list

truck_list=[]

# Sample data
truck_list.append(Truck("l1",30,3000,2500,[datetime(2020,4,7),datetime(2020,5,6)]))
truck_list.append(Truck("l2",25,2400,2400,[datetime(2020,4,10),datetime(2020,5,9)],"Unloading"))
truck_list.append(Truck("l3",34,2700,2300,[datetime(2020,4,10),datetime(2020,5,9)]))
truck_list.append(Truck("l4",25,2400,100,[datetime(2020,4,26),datetime(2020,5,25)]))
truck_list.append(Truck("l5",30,2800,2000,[datetime(2020,4,1),datetime(2020,4,30)]))

while(1):
    print("1: Use sample date")
    print("2: Input your own data")
    print("3: For exit")
    print("   \nPRESS 1 OR 2 OR 3")
    i=int(input())

    # Custom input
    if i==2:
        truck_list=my_own_trucks()
        print("".center(80,"-"))

    if i==3:
        print("Sad! Plzzz try me once")
        exit()   
        
        
    list1=min_cost(truck_list,600,True)

    # Printing efficiency of each truck
    print("Cost efficiency for each truck :")
    for ind,i in enumerate(list1):
        print("\t{} : {:.2f}".format(truck_list[ind].name,i))

    print("\n")

    print("Best pick for us is : ",end="")   
   
    #next line is important
    print(truck_list[list1.index(min(list1))].name)

    print()
    if(input("Test more Y/N").upper()=="N"):
        print("Thank you for using me")
        exit()




    




