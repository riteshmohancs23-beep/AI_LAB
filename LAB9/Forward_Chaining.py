def fol_forward_chaining(kb, query):
    inferred = set()
    agenda = []
    count = {}

    for rule in kb:
        if isinstance(rule, tuple):
            premises, conclusion = rule
            count[rule] = len(premises)
            for p in premises:
                if p in kb:
                    agenda.append(p)
        else:
            agenda.append(rule)

    while agenda:
        p = agenda.pop(0)
        if p == query:
            return True
        if p not in inferred:
            inferred.add(p)
            for rule in kb:
                if isinstance(rule, tuple):
                    premises, conclusion = rule
                    if p in premises:
                        count[rule] -= 1
                        if count[rule] == 0:
                            if conclusion == query:
                                return True
                            agenda.append(conclusion)
    return False

kb = [
    "A",
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D")
]

print(fol_forward_chaining(kb, "D"))
