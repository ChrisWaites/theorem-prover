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
              conjunction, resolution, constructiveDilemma]
ntEquivalencies = [quantifierInterchange, quantifierNegation, symmetryOfEquality, addition, subtraction, doubleNegationIntroduction]

# Peano's Axioms
theorems = set([parse("Aa(~((S(a))=(0)))"),
                parse("Aa(((a)+(0))=(a))"),
                parse("Aa(Ab(((a)+(S(b)))=(S((a)+(b)))))"),
                parse("Aa(((a)*(0))=(0))"),
                parse("Aa(Ab(((a)*(S(b)))=(((a)*(b))+(a))))")])
# Unused Theorems
currTheorems = set(theorems)

for i in range(2):
    # Derivations
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
        absorbed = absorption(theorem)
        if absorbed != None:
            newTheorems.add(absorbed)
    theorems.update(newTheorems)
    currTheorems = newTheorems

q = PriorityQueue()
for theorem in theorems:
    q.put(theorem)
for i in range(15):
    print q.get()
