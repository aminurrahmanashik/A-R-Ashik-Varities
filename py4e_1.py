fname = input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count += 1
    add += float(line[21:])

print("Average spam confidence:", add / count)

