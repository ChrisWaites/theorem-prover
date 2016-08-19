from LogicalEquivalence import *
from NumberTheory import *
from Inference import *
from Node import *
from Queue import PriorityQueue

equivalencies = [truth, identity, domination, idempotent, doubleNegationIntroduction,
                 doubleNegationElimination, commutative, association, distribution,
                 demorgans, absorption, negation, materialImplication, contraposition,
                 biconditional, biconditionalElimination]
inferences = [modusPonens, modusTollens, hypotheticalSyllogism, disjunctiveSyllogism,
              conjunction, resolution, constructiveDilemma, absorption]
ntEquivalencies = [quantifierInterchange, quantifierNegation, symmetryOfEquality, addition, subtraction, doubleNegationIntroduction]

theorems = set([parse("(p)->(q)"), parse("(q)->(r)"), parse("(r)->(p)")])
currTheorems = set(theorems)

for i in range(3):
    newTheorems = set()
    for theorem in currTheorems:
        for equivalence in equivalencies:
            newTheorems.update(theorem.apply(equivalence))
        for equivalence in ntEquivalencies:
            newTheorems.update(theorem.apply(equivalence))
        for otherTheorem in currTheorems:
            for inference in inferences:
                inf = inference(theorem, otherTheorem)
                if inf != None:
                    newTheorems.add(inf)
        simplified = simplification(theorem)
        if simplified != None:
            newTheorems.add(simplified)
    theorems.update(newTheorems)
    currTheorems = newTheorems

q = PriorityQueue()
for theorem in theorems:
    q.put(theorem)
for i in range(15):
    print q.get()
