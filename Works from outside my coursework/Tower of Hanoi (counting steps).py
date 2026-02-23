def hanoi(n, source, target, auxiliary, t = 0):
    """
    :param n: number of plates
    :param source: starting pillar
    :param target: target pillar
    :param auxiliary: helper pillar
    """
    t = t + 1
    if n == 1:
        print(f"Move from {source} to {target}")
        return t
    t = hanoi(n - 1, source, auxiliary, target, t)
    print(f"Move from {source} to {target}")
    t = hanoi(n - 1, auxiliary, target, source, t)
    return t

n = 6  # number of plates
source = 'A'  # starting pillar
target = 'C'  # target pillar
auxiliary = 'B'  # helper pillar

count = hanoi(n, source, target, auxiliary)
print('Count：'+str(count))