def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file

    Args:
        n: repetitions of H
    Returns:
        number of operations (Copy & Paste) to reach n Hs
    """
    operations = 0
    current_sum = 1

    while current_sum < n:
        current_sum *= 2
        operations += 1

    if current_sum > n: # Subtract the remaining steps from the final operation count
        remaining_steps = 0
        while current_sum > n:
            current_sum -= current_sum // 2
            remaining_steps += 1
        operations -= remaining_steps

    return operations
