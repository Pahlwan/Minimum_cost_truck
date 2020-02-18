# Minimum_cost_truck
 Finding maximum profit truck for company

language of code: Python

We define Minimum cost function.

**************************************************************************************************************************
Minimum cost function :  (Total pay factor)*1/(Reamaining time factor)

Total pay factor = If truck will selected how much company pay to truck owner after current cycle 

Formula: 
            [extra_km * (rate*120/100) + monthly cycle pay]
            Higher pay less chance to pick



Reamaining time factor = If reamaing Km s devided by reamaing days. if this increase we increase the total pay factor strength
but if Total pay already high we dont want to increase Totala pay factor strength.
we can normalize total pay factor by mutiply it with [remaning time/reamaing distance] for example

    we hacce 2 trucks:
                            Truck 1 has 2 days left in his cycle and 500 km remaining in its cycle then = 500/2=250
                            Truck 2 has 5 days left in his cycle and 500 km remaining in its cycle then = 500/5=100

                            Higher km/days means more chance to pick


Now our optimum selection formula is====>

                            [extra_km * (rate*120/100) + monthly cycle pay]*[remaining days/remaining distance]

************************************************************************************************************************






