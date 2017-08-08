## Automated Theorem Prover

<img src="http://i.imgur.com/BgZ4BYv.png" width="280px">


### Motivation

Many would agree that [Kurt Godel's incompleteness theorems](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems)
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
provide practical efficiency through various guiding heuristics.


### Usage

```
usage: run [-h] [-a AXIOMS [AXIOMS ...]] [-t THEOREM]

Given a set of axioms attempts to prove or disprove a given theorem using
propositional logic and number theory.

optional arguments:
  -h, --help            show this help message and exit
  -a AXIOMS [AXIOMS ...], --axioms AXIOMS [AXIOMS ...]
                        axioms of formal system [default: peano's axioms]
  -t THEOREM, --theorem THEOREM
                        theorem to be proved or disproved [default: ~(Ea((0)=((a)+(1))))]
```

E.g.

```
./run -a "Aa(~(((a)+(1))=(0)))" "Aa(((a)+(0))=(a))" -t "~(Ea((0)=((a)+(1))))"

Aa(~(((a)+(1))=(0)))
->
Aa(~((0)=((a)+(1))))
->
~(Ea((0)=((a)+(1))))
```
```
./run -t "Aa(((0)+(1))=(((a)\*(0))+(1)))"

Aa(((a)*(0))=(0))
->
Aa((((a)*(0))+(1))=((0)+(1)))
->
Aa(((0)+(1))=(((a)*(0))+(1)))
```


### To Do

* More and more tests!

* Add more heuristics, ideally with corresponding theoretical guarantees and performance
  statistics.

* Currently `expression.parse()` is quite rigid and assumes a strictly parenthesized
  expression. Ideally it would work without parenthesization whenever no ambiguity exists,
  or resolves ambiguity by some order of operation.

