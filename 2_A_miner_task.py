line = input()
miner_task = {}

while line != "stop":
    resource = line
    quantity = int(input())
    if resource not in miner_task.keys():
        miner_task[resource] = quantity
    else :
        miner_task[resource] += quantity

    line = input()

for resource, quantity in miner_task.items():
    print(f"{resource} -> {quantity}")
