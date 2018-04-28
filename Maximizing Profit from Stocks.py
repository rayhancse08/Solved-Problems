def max_profit(prices):
    profit=0
    max_sofar=0
    length=len(prices)
    prices=prices[-1::-1]
    for item in prices:
        
        if item >= max_sofar:
               max_sofar=item
        profit+=max_sofar-item

    return profit

test_number=int(input("Number of Test: "))
profit_list=[]
for i in range(test_number):
    input_time=int(input("Time: "))
    prices=[]
    
    for j in range(input_time):
        price=int(input())
        prices.insert(j,price)
        
    result=max_profit(prices)
    profit_list.insert(j,result)

for item in profit_list:
    print(item)
