from collections import defaultdict
import propositional_logic
import number_theory
import inference
from expression import *
from search import *

def get_fns(module):
    return [f for _, f in module.__dict__.iteritems() if callable(f) and f != Expression]

equivalency_functions = get_fns(propositional_logic) + get_fns(number_theory) + get_fns(inference)
equivalency_functions.remove(inference.conjunction)

peanos_axioms = set(map(parse, [
    "Aa(~(((a)+(1))=(0)))",
    "Aa(((a)+(0))=(a))",
    "Aa(Ab(((a)+((b)+(1)))=(((a)+(b))+(1))))",
    "Aa(((a)*(0))=(0))",
    "Aa(Ab(((a)*((b)+(1)))=(((a)*(b))+(a))))"
]))

def apply_equivalency(f, expr):
    """
    Applies a given equivalency rule exactly once to every
    node in an expression tree recursively and returns a set
    of the new deductions

    f (Callable) -- An equivalency function
    expr (Expression) -- an expression tree
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


def neighboring_theorems(state):
    return apply_equivalencies(equivalency_functions, state)


def edit_distance(a, b):
    """
    a -- Anything capable of being converted to a string via str(a)
    b -- Anything capable of being converted to a string via str(b)
    """
    str_a, str_b = str(a), str(b)
    cache = defaultdict(lambda: defaultdict(int)) # two dimensional default dict
    for i in range(len(str_a) + 1):
        for j in range(len(str_b) + 1):
            if i == 0:
                cache[i][j] = j
            elif j == 0:
                cache[i][j] = i
            elif str_a[i-1] == str_b[j-1]:
                cache[i][j] = cache[i-1][j-1]
            else:
                cache[i][j] = 1 + min(
                    cache[i][j-1],
                    cache[i-1][j],
                    cache[i-1][j-1]
                )
    return cache[len(str_a)][len(str_b)]



def find_theorem(theorem, axioms=peanos_axioms, heuristic=None):
    """
    Given an iterable of axioms and a heuristic (optional),
    attempts to find a theorem or its negation using A* search.
    """
    if heuristic == None:
        heuristic = lambda t: edit_distance(t, theorem)
    return a_star(Graph(neighboring_theorems), axioms, lambda t: (t == theorem) or (t == ~theorem), heuristic)

