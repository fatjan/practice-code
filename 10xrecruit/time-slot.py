def min_time(q, num_machines, second_1, second_q):
    """
    :param q: time to complete longer batches
    :param num_machines: number of machines
    :param second_1: amount of 1-second slot purchased
    :param second_q: amount of q-second slot purchased
    :return: minimum time to process all jobs
    """
    time = 0

    if not second_q:
        if not second_1:
            return time
        time = second_1 // num_machines
        remainder = second_1 % num_machines
        if remainder:
            time += 1
        return time

    if not second_1:
        if not second_q:
            return time
        time = second_q // num_machines
        remainder = second_q % num_machines
        if remainder:
            time += q
        return time
    
    remaining_machines = num_machines

    while remaining_machines > 0 and (second_q > 0 or second_1 > 0):
        if second_q > 0:
            q_batches, remaining_machines = divmod(second_q, remaining_machines)
            second_q -= num_machines * q_batches
            time += q_batches * q
            if remaining_machines == 0:
                remaining_machines = num_machines

        if second_1 > 0:
            if second_q:
                time += q 
                remaining_machines -= second_q
                if remaining_machines != 0:
                    second_1 -= remaining_machines
                    if remaining_machines == 0:
                        remaining_machines = num_machines
            else:
                one_batches, remaining_machines = divmod(second_1, remaining_machines)
                second_1 -= num_machines * one_batches
                time += one_batches

    return time


line = input().split()
q = int(line[0])
num_machines = int(line[1])
second_1 = int(line[2])
second_q = int(line[3])
print(min_time(q, num_machines, second_1, second_q))