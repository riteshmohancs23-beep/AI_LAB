import itertools
import pandas as pd

vars = ['P', 'Q', 'R']

def implies(a, b):
    return (not a) or b

def KB(P, Q, R):
    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R
    return s1, s2, s3, (s1 and s2 and s3)

def entails_R(P, Q, R):
    return R

def entails_R_implies_P(P, Q, R):
    return implies(R, P)

def entails_Q_implies_R(P, Q, R):
    return implies(Q, R)

data = []
models_KB_true = []

for P, Q, R in itertools.product([False, True], repeat=3):
    s1, s2, s3, kb = KB(P, Q, R)
    r = entails_R(P, Q, R)
    r_imp_p = entails_R_implies_P(P, Q, R)
    q_imp_r = entails_Q_implies_R(P, Q, R)
    data.append({
        'P': P, 'Q': Q, 'R': R,
        'Q→P': s1, 'P→¬Q': s2, 'Q∨R': s3,
        'KB': kb, 'R': r, 'R→P': r_imp_p, 'Q→R': q_imp_r
    })
    if kb:
        models_KB_true.append((P, Q, R))

df = pd.DataFrame(data)

def entails(KB_true_models, query_func):
    for P, Q, R in KB_true_models:
        if not query_func(P, Q, R):
            return False
    return True

print("\nModels where KB is TRUE:")
for m in models_KB_true:
    print(f"P={m[0]}, Q={m[1]}, R={m[2]}")

print("\nEntailment Results:")
print("KB ⊨ R:", entails(models_KB_true, entails_R))
print("KB ⊨ (R → P):", entails(models_KB_true, entails_R_implies_P))
print("KB ⊨ (Q → R):", entails(models_KB_true, entails_Q_implies_R))
print("TRUTH TABLE")
df


# OUTPUT:





#     P     Q     R   Q→P  P→¬Q   Q∨R    KB   R→P   Q→R
# False False False  True  True False False  True  True
# False False  True  True  True  True  True False  True
# False  True False False  True  True False  True False
# False  True  True False  True  True False False  True
#  True False False  True  True False False  True  True
#  True False  True  True  True  True  True  True  True
#  True  True False  True False  True False  True False
#  True  True  True  True False  True False  True  True

# Models where KB is TRUE:
# P=False, Q=False, R=True
# P=True, Q=False, R=True

# Entailment Results:
# KB ⊨ R: True
# KB ⊨ (R → P): False
# KB ⊨ (Q → R): True
