## Automated Theorem Prover


### Motivation

Many would agree that Kurt G÷del's [incompleteness theorems](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems)
set some of the most unintuitive and limiting retrictions upon our ability to
understand nontrivial formal systems like number theory or graph theory.
To be brief, it states that the ideal of ever constructing an automated system which is
fully capable of finding only and all true theorems given a finite set of axioms is
fundamentally impossible.

Despite this, many attempt to develop systems capable of proving
more conventional mathematical theorems rather than paradoxical ones. This is such an
attempt.


### Approach

The idea is to encode the mathematical process as an unambiguous procedure
which can computationally executed. That is, we define a formal mathematical system to be
a graph in which true theorems are vertices, laws of deduction are edges,
and a proof is essentially a search problem.  

Although from a theoretical perspective this is sufficient, the goal is to also
provide practical efficiency through means of guiding heuristics such as
edit-distance.


### Usage

```
usage: prove [-h] [-a AXIOMS [AXIOMS ...]] [-t THEOREM]

Given a set of axioms attempts to prove or disprove a given theorem using
propositional logic and number theory.

optional arguments:
  -h, --help            show this help message and exit
  -a AXIOMS [AXIOMS ...], --axioms AXIOMS [AXIOMS ...]
                        axioms of formal system [default: peano's axioms]
  -t THEOREM, --theorem THEOREM
                        theorem to be proved or disproved [default: ~(Ea((0)=((a)+(1))))]
```
