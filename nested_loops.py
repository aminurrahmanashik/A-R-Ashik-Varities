
for left in range(7):
    for right in range(left,7):
        print("[", str(left), "|", str(right), "]",end=" ")
    print()

teams = ['Dragons','Wolves','Pandas','Unicorns']
count = 0
for home in teams:
    for away in teams:
        if home != away:
            count += 1
            print(home, "vs", away)
print(f"Total {count} games need to be arranged")