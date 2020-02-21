# Minimum_cost_truck
 Finding maximum profit truck for company

language of code: Python
Virsion control : Github

I have private repository for this project on my github account.


**************************************************************************************************************************
Truck class to hold information about single truck
Input : name,rate (per Km), minimum_run, already_ran, cycle, status="WAITING"
it has a function to return the number of days left in cycle

input : to_day(can be custom)
Output : days reamaining in cycle

**************************************************************************************************************************
We defined a min_costfunction which calculate eficient cost for each truck present with us. and return a array

Inputs : truck_list,assingment_distance,to_day,status_cosideration=False)
Output : Efficiency list

************************************************************************************************************************

One more function my_own_trucks to create your own list of trucks

Input : none
output : truck_list

*************************************************************************************************************************

Formula we used for calculation of efficient cost :

if ratio of km left and minimum run dont have 0 as denominator:
        
        (fix_pay + addintion pay(if applicable)) * (ratio of km left and minimum run) * days remaining in cycle

if denominator is 0 then
        (fix_pay)+addition pay( if applicable ) * 1 * days remaining in cycle

**************************************************************************************************************************

I tried to cover all aspects of problem 

And testing is dont on lost of data

May be it still have some buggs plz forgive me this is becoz of my busy schedule from 4 to 5 days.

I believe this can be futher optimize for performance.

# NOTE:Plz re-run after testing with status_consideration = Y (True)

 Thank you.

 Date : 21-02-2020
 Place : Noida, Uttar Pradesh (India)

