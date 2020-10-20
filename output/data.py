from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle  

def rf_data(rf, styleN, styleBH):
    todascategorias = []
    for p in rf:
        lista = []
        titulo = Paragraph(p.title, styleBH)
        lista.append(titulo)
        descripcion = Paragraph(p.description, styleN)
        lista.append(descripcion)
        prioridad = Paragraph(p.priority, styleBH)
        lista.append(prioridad)
        estado = Paragraph(p.state, styleBH)
        lista.append(estado)
        costo = Paragraph(p.cost, styleBH)
        lista.append(costo)
        todascategorias.append(lista)
    return todascategorias

def rnf_data(rf, styleN, styleBH):
    todascategorias = []
    for p in rf:
        lista = []
        titulo = Paragraph(p.title, styleBH)
        lista.append(titulo)
        descripcion = Paragraph(p.description, styleN)
        lista.append(descripcion)
        prioridad = Paragraph(p.priority, styleBH)
        lista.append(prioridad)
        estado = Paragraph(p.state, styleBH)
        lista.append(estado)
        tipo = Paragraph(p.type_r, styleBH)
        lista.append(tipo) 
        costo = Paragraph(p.cost, styleBH)
        lista.append(costo)
        todascategorias.append(lista)
    return todascategorias

def ipo(rf, styleN, styleBH):
    todascategorias = []
    for p in rf:
        lista = []
        entrada = Paragraph(p.input, styleBH)
        lista.append(entrada)
        proceso = Paragraph(p.process, styleN)
        lista.append(proceso)
        salida = Paragraph(p.output, styleBH)
        lista.append(salida)
        todascategorias.append(lista)
    return todascategorias

def team_data(rf, styleN, styleBH):
    todascategorias = []
    for p in rf:
        lista = []
        user = Paragraph(p.user.username, styleBH)
        lista.append(user)
        type_user = Paragraph(p.type_user, styleN)
        lista.append(type_user)
        todascategorias.append(lista)
    return todascategorias