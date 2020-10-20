def count_state(rf, rnf):
    lista = []
    contador = []
    x = set()

    for requeriment in rf:
        lista.append(requeriment.state)
    for requeriment in rnf:
        lista.append(requeriment.state)
    for item in lista:
        x.add(item)
    for item in x:
        contador.append(lista.count(item))
    dic = dict(zip(x,contador))

    return dic

def count_cost(rf, rnf):
    lista = []
    contador = []
    x = set()

    for requeriment in rf:
        lista.append(requeriment.cost)
    for requeriment in rnf:
        lista.append(requeriment.cost)
    for item in lista:
        x.add(item)
    for item in x:
        contador.append(lista.count(item))
    dic = dict(zip(x,contador))

    return dic

def count_priority(rf, rnf):
    lista = []
    contador = []
    x = set()

    for requeriment in rf:
        lista.append(requeriment.priority)
    for requeriment in rnf:
        lista.append(requeriment.priority)
    for item in lista:
        x.add(item)
    for item in x:
        contador.append(lista.count(item))
    dic = dict(zip(x,contador))

    return dic

def count_rstate(rf):
    lista = []
    contador = []
    x = set()

    for requeriment in rf:
        lista.append(requeriment.state)
    for item in lista:
        x.add(item)
    for item in x:
        contador.append(lista.count(item))
    dic = dict(zip(x,contador))

    return dic

def count_rcost(rf):
    lista = []
    contador = []
    x = set()

    for requeriment in rf:
        lista.append(requeriment.cost)
    for item in lista:
        x.add(item)
    for item in x:
        contador.append(lista.count(item))
    dic = dict(zip(x,contador))

    return dic

def count_rpriority(rf):
    lista = []
    contador = []
    x = set()

    for requeriment in rf:
        lista.append(requeriment.priority)
    for item in lista:
        x.add(item)
    for item in x:
        contador.append(lista.count(item))
    dic = dict(zip(x,contador))

    return dic