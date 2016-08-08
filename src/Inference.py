def infer(theorems, rules):
    a = []
    for i in range(len(theorems)):
        for j in range(i, len(theorems)):
            for rule in rules:
                a.append(rule(theorems[i], theorems[j]))
    return a
