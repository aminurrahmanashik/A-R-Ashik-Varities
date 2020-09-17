
def t_shirt(size,adjective):
    print(f"Will this {adjective} shirt suit you,It's size is:{size}")

t_shirt(20,'Red colored')
# once you use keyword arguments, you need to specify it for all the arguments
# else, you'll get an Error
t_shirt(adjective='Blue',size=10)