n = int(input("Enter what range you want : "))

emp = []
ids = []

for i in range(n):
    li = input(f"Please enter {i} Employee : ").split()

    eid = int(li[0])
    work = int(li[2])
    present = int(li[3])

    if eid in ids:
        continue
    ids.append(eid)

    if work <= 0:
        
        continue

    if present > work:
        present = work

    att = (present / work) * 100

    if att >= 98:
        reward = "Platinum"
    elif att >= 95:
        reward = "Gold"
    elif att >= 90:
        reward = "Silver"
    elif att >= 80:
        reward = "Bronze"
    else:
        reward = "No Reward"

    emp.append([li[1], reward, att])

emp.sort(key=lambda x: (-x[2], x[0]))

for i in emp:
    print(i[0], i[1], "{:.2f}".format(i[2]))