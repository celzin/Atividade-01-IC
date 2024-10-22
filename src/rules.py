def fuzzy_rule_and(mf1, mf2):
    """
    Regra fuzzy que utiliza a operação "E" (t-norma mínima) feita manualmente.
    SE (X1 é A) E (X2 é B) ENTÃO Y.
    mf1: grau de pertinência da variável X1.
    mf2: grau de pertinência da variável X2.
    """
    if mf1 < mf2:
        return mf1
    else:
        return mf2


def fuzzy_rule_or(mf1, mf2):
    """
    Regra fuzzy que utiliza a operação "OU" (s-norma máxima) feita manualmente.
    SE (X1 é A) OU (X2 é B) ENTÃO Y.
    mf1: grau de pertinência da variável X1.
    mf2: grau de pertinência da variável X2.
    """
    if mf1 > mf2:
        return mf1
    else:
        return mf2
