
def convert_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    reamining_seconds = seconds - hours * 3600 - minutes * 60
    return hours,minutes,reamining_seconds

ans = convert_seconds(3423421)
print(ans)
ans = convert_seconds(5000)
print(ans)