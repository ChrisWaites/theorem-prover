# godel-machine

Despite the fact that Mathematician Kurt Godel indirectly proved that computers could not successfully print every true statement of a formal system, I still want to try for non-paradoxical statements. The attempt to take on this challenge includes the creation of classes representing formal propositions, propositional functions, typographic equivalence methods, and a Set&lt;String> of the true conclusions.

For example, given the axioms `p` and `q^r`, the following is produced.
```
  q
  ~~p
  r
  ~~<q^r>
  <<q^r>^<q^r>>
  <p^p>
  <p^<q^r>>
  <<q^r>^p>
  ...
```
