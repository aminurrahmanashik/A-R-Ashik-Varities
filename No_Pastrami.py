
print("Deli has run out of pastrami")
sandwich_orders  = ['pastrami','lolli','pastrami','nalaita','pastrami','alaika','nabla','utra']
print(f"Before removal:{sandwich_orders}")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"After removal:{sandwich_orders}")
