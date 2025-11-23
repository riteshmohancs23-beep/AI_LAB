import itertools

def remove_implications(expr):
    if isinstance(expr, str):
        return expr
    
    op = expr[0]

    if op == 'implies':
        return ['or', ['not', remove_implications(expr[1])], remove_implications(expr[2])]
    
    if op == 'iff':
        A = remove_implications(expr[1])
        B = remove_implications(expr[2])
        return ['and',
            ['or', ['not', A], B],
            ['or', A, ['not', B]]
        ]
    
    return [op] + [remove_implications(e) for e in expr[1:]]

def move_negation_inward(expr):
    if isinstance(expr, str):
        return expr

    op = expr[0]

    if op == 'not':
        sub = expr[1]
        if isinstance(sub, list):
            if sub[0] == 'not':
                return move_negation_inward(sub[1])
            if sub[0] == 'and':
                return ['or'] + [move_negation_inward(['not', x]) for x in sub[1:]]
            if sub[0] == 'or':
                return ['and'] + [move_negation_inward(['not', x]) for x in sub[1:]]
        return ['not', move_negation_inward(sub)]

    return [op] + [move_negation_inward(e) for e in expr[1:]]

var_counter = itertools.count()

def standardize(expr, mapping=None):
    if mapping is None:
        mapping = {}

    if isinstance(expr, str):
        if expr[0].islower():
            if expr not in mapping:
                mapping[expr] = f"v{next(var_counter)}"
            return mapping[expr]
        return expr

    return [expr[0]] + [standardize(e, mapping) for e in expr[1:]]

skolem_counter = itertools.count()

def skolemize(expr, context=None):
    if context is None:
        context = []

    if isinstance(expr, str):
        return expr

    op = expr[0]

    if op == 'forall':
        return skolemize(expr[2], context + [expr[1]])
    
    if op == 'exists':
        var = expr[1]
        name = f"S{next(skolem_counter)}"
        if context:
            return skolemize(replace(expr[2], var, [name] + context), context)
        else:
            return skolemize(replace(expr[2], var, name), context)
    
    return [op] + [skolemize(e, context) for e in expr[1:]]

def replace(expr, old, new):
    if isinstance(expr, str):
        return new if expr == old else expr
    return [expr[0]] + [replace(e, old, new) for e in expr[1:]]

def drop_quantifiers(expr):
    if isinstance(expr, str):
        return expr
    if expr[0] in ('forall', 'exists'):
        return drop_quantifiers(expr[2])
    return [expr[0]] + [drop_quantifiers(e) for e in expr[1:]]

def distribute(expr):
    if isinstance(expr, str):
        return expr

    if expr[0] == 'or':
        A = distribute(expr[1])
        B = distribute(expr[2])
        if isinstance(A, list) and A[0] == 'and':
            return ['and', distribute(['or', A[1], B]), distribute(['or', A[2], B])]
        if isinstance(B, list) and B[0] == 'and':
            return ['and', distribute(['or', A, B[1]]), distribute(['or', A, B[2]])]
        return ['or', A, B]

    if expr[0] == 'and':
        return ['and'] + [distribute(e) for e in expr[1:]]

    return [expr[0]] + [distribute(e) for e in expr[1:]]

def fol_to_cnf(expr):
    expr = remove_implications(expr)
    expr = move_negation_inward(expr)
    expr = standardize(expr)
    expr = skolemize(expr)
    expr = drop_quantifiers(expr)
    expr = distribute(expr)
    return expr

formula = ['implies', ['and', 'P(x)', 'Q(x)'], ['exists', 'y', 'R(y)']]
print(fol_to_cnf(formula))
