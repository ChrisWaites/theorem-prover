import propositional_logic
import number_theory
import inference
from expression import *
from search import *

propositional_logic_equivalencies = [f for _, f in propositional_logic.__dict__.iteritems() if callable(f) and f != Expression]
number_theory_equivalencies = [f for _, f in number_theory.__dict__.iteritems() if callable(f) and f != Expression]
inference_equivalencies = [f for _, f in inference.__dict__.iteritems() if callable(f) and f != Expression and f != inference.conjunction]

equivalency_functions = propositional_logic_equivalencies + number_theory_equivalencies + inference_equivalencies

def apply_equivalency(f, expr):
    """
    Applies a given equivalency rule exactly once to every
    node in an expression tree recursively and returns a set
    of the new deductions

    f -- An equivalency function
    expr -- An expression tree
    """
    equivalencies = set()
    application = f(expr)
    if application:
        equivalencies.add(application)
    for i in range(len(expr.args)):
        newIthArgs = apply_equivalency(f, expr.args[i])
        for newArg in newIthArgs:
            newArgs = [arg for arg in expr.args]
            newArgs[i] = newArg
            newExpression = Expression(expr.op, *newArgs)
            equivalencies.add(newExpression)
    return equivalencies

def apply_equivalencies(fs, expr):
    equivalencies = set()
    for f in fs:
        equivalencies.update(apply_equivalency(f, expr))
    return equivalencies

def get_neighboring_theorems(state):
    return apply_equivalencies(equivalency_functions, state)

def find_theorem(axioms, theorem, heuristic=trivial):
    """
    Given an iterable of axioms and a heuristic (optional),
    attempts to find a theorem or its negation using A* search.
    """
    return a_star_search(Graph(get_neighboring_theorems), axioms, lambda x: (x == theorem) or (x == ~theorem), heuristic)

if __name__ == "__main__":
    peanos_axioms = set([parse("Aa(~(((a)+(1))=(0)))"),
                        parse("Aa(((a)+(0))=(a))"),
                        parse("Aa(Ab(((a)+((b)+(1)))=(((a)+(b))+(1))))"),
                        parse("Aa(((a)*(0))=(0))"),
                        parse("Aa(Ab(((a)*((b)+(1)))=(((a)*(b))+(a))))")])

    print find_theorem(peanos_axioms, ~~parse("Aa(~(((a)+(1))=(0)))"))
