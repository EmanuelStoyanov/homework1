
def calculate_coins(sum):
    dict = { 100 : 0, 50 : 0, 20 : 0, 10 : 0, 5 : 0, 1 : 0, 2 : 0 }
    return calculate_coins2(sum*100,dict)

    

def calculate_coins2(sum,dict):
    if sum>=100.0:
        dict[100]+=1
        return calculate_coins2(sum-100.0,dict)
    elif sum>=50.0:
        dict[50]+=1
        return calculate_coins2(sum-50.0,dict)
    elif sum>=20.0:
        dict[20]+=1
        return calculate_coins2(sum-20.0,dict)
    elif sum>=10.0:
        dict[10]+=1
        return calculate_coins2(sum-10.0,dict)
    elif sum>=5.0:
        dict[5]+=1
        return calculate_coins2(sum-5.0,dict)
    elif sum>=2.0:
        dict[2]+=1
        return calculate_coins2(sum-2.0,dict)
    elif sum==1.0:
        dict[1]+=1
        return dict
    else:
        return dict
