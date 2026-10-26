
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def calcular_frequencia(total_aulas, faltas):
    if total_aulas <= 0:
        return 0

    if faltas < 0 or faltas > total_aulas:
        return 0

    presencas = total_aulas - faltas
    return (presencas / total_aulas) * 100


def verificar_situacao(media, frequencia):
    if frequencia < 75:
        return "Acompanhamento por faltas"

    if media < 5:
        return "Recuperação"

    if media < 7:
        return "Acompanhamento pedagógico"

    return "Bom desempenho"
