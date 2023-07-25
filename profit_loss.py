import csv 
 
def profit_and_loss(fp): 
    with open(fp,mode="r", newline="") as file: 
        reader = csv.reader(file) 
 
        next(reader) 
        next(reader) 
        days = [] 
        net_profit = [] 
        for row in reader: 
            days.append(row[0]) 
            net_profit.append(float(row[-1])) 
 
    max_net_profit = 0 
    max_day = "" 
    surplus = True 
    deficits = [] 
 
    for i in range(1, len(net_profit)): 
        difference = net_profit[i] - net_profit[i - 1] 
        if difference < 0: 
            surplus = False 
            deficits.append((days[i], abs(difference))) 
        else: 
            if difference > max_net_profit: 
                max_net_profit = difference 
                max_day = days[i] 
 
    if surplus: 
        return (surplus, (max_day, max_net_profit)) 
    else: 
        return (surplus, deficits)