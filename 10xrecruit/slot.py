def min_time(q, num_machines, second_1, second_q):
    if second_1 == 0 and second_q == 0:
        return 0

    q_batches, second_q = divmod(second_q, num_machines)
    time = q_batches * q

    one_batches, second_1 = divmod(second_1, num_machines)
    time += one_batches

    if second_q > 0:
        remaining_machines = num_machines - second_q
        time += (remaining_machines // num_machines) * q
        if remaining_machines % num_machines != 0:
            time += q

    return time

# Input
line = input().split()
q = int(line[0])
num_machines = int(line[1])
second_1 = int(line[2])
second_q = int(line[3])

# Output
print(min_time(q, num_machines, second_1, second_q))
