
# **toppings will return the whole as a list
def sandwitches(**toppings):
    return toppings


summery = sandwitches(a = 'big',b = 'medium',c = 'small')
print(summery)
sandwitches(a='big')
print(summery)
summery = sandwitches(c1 = 'big',c2 = 'small')
print(summery)
