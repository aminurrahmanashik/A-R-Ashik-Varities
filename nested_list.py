

results = []
n = int(input())
for _ in range(n):
        name = input()
        score = float(input())
        results.append([name,score])

second_lowest = sorted(list(set([score for name,score in results])))[1]
#print('\n'.join([name for name,score in sorted(results) if score == second_lowest]))
for name,score in (results):
    if score == second_lowest:
        print(sorted(name))
