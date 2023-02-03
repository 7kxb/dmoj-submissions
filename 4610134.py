days = int(input())
swifts = input().split()
semaphores = input().split()
swifts_runs = 0
semaphores_runs = 0
toggle = True
for i in range(days):
    swifts_runs += int(swifts[i])
    semaphores_runs += int(semaphores[i])
    if swifts_runs == semaphores_runs:
        toggle = False
        pointer = i+1
if swifts_runs != semaphores_runs and toggle:
    print(0)
else:
    print(pointer)