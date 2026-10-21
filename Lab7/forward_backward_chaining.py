def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for condition, conclusion in rules:
            if conclusion in inferred:
                continue
            if all(item in inferred for item in condition):
                inferred.add(conclusion)
                changed = True

    return inferred


def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        return True
    if goal in visited:
        return False

    visited.add(goal)
    for condition, conclusion in rules:
        if conclusion == goal:
            return all(backward_chaining(item, facts, rules, visited) for item in condition)

    return False


facts = {'A', 'B'}
rules = [
    (['A', 'B'], 'C'),
    (['C'], 'D'),
    (['D'], 'E')
]

result = forward_chaining(facts, rules)
print('Forward chaining facts:', sorted(result))

print('Goal E is supported:', backward_chaining('E', facts, rules))
