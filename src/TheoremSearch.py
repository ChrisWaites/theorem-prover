import PropositionalLogic
import NumberTheory
import Inference
from Expr import *
from Search import *

propositional_logic_equivalencies = [f for _, f in PropositionalLogic.__dict__.iteritems() if callable(f) and f != Expr]
number_theory_equivalencies = [f for _, f in NumberTheory.__dict__.iteritems() if callable(f) and f != Expr]
inference_equivalencies = [f for _, f in Inference.__dict__.iteritems() if callable(f) and f != Expr and f != Inference.conjunction]

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
            newExpr = Expr(expr.op, *newArgs)
            equivalencies.add(newExpr)
    return equivalencies

def apply_equivalencies(fs, expr):
    equivalencies = set()
    for f in fs:
        equivalencies.update(apply_equivalency(f, expr))
    return equivalencies

def get_neighboring_expressions(state):
    return apply_equivalencies(equivalency_functions, state)

def find_theorem(axioms, theorem, heuristic=trivial_heuristic):
    """
    Given an iterable of axioms and a heuristic (optional),
    attempts to find a theorem or its negation using A* search.
    """
    return a_star_search(Graph(get_neighboring_expressions), axioms, lambda x: (x == theorem) or (x == ~theorem), heuristic)

if __name__ == "__main__":
    peanos_axioms = set([parse("Aa(~(((a)+(1))=(0)))"),
                        parse("Aa(((a)+(0))=(a))"),
                        parse("Aa(Ab(((a)+((b)+(1)))=(((a)+(b))+(1))))"),
                        parse("Aa(((a)*(0))=(0))"),
                        parse("Aa(Ab(((a)*((b)+(1)))=(((a)*(b))+(a))))")])

    print find_theorem(peanos_axioms, ~~parse("Aa(~(((a)+(1))=(0)))"))