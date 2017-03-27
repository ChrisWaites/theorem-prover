# Automated Theorem Prover

Despite the fact that Mathematician Kurt Godel in his incompleteness theorems proved that one could not systematically deduce every true statement within a formal system, I thought it would still be interesting to see the limits of what an automated system could practically deduce. The attempt to take on this challenge includes classes and functions able to replicate propositional logic, Peano's axioms of number theory, as well as rules of  logical equivalnce.

Given a set of axioms, the system uses A\* graph search to determine whether a given proposition or its negation is true within the system you specify, where a system is defined as a set of axioms and a set of logical equivalency functions. The goal is to potentially design a heuristic which could guarantee a certain level of performance in determining theorems relating to number theory.
