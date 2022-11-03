def validStartingCity(distances, fuel, mpg):
    def helper(idx, start, remaining, cycle=False):
        if idx >= len(distances):
            idx = 0
            cycle = True
        if cycle and idx == start:
            return True
        remaining += fuel[idx] * mpg
        remaining -= distances[idx]
        if remaining < 0:
            return False
        return helper(idx + 1, start, remaining, cycle)
    for i in range(len(distances)):
        if helper(i, i, 0):
            return i
    return -1
