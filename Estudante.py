
class Estudante:
    def __init__(self, nome, matricula, turma):
        self.nome = nome
        self.matricula = matricula
        self.turma = turma
        self.nota1 = 0
        self.nota2 = 0
        self.total_aulas = 0
        self.faltas = 0

    def registrar_notas(self, nota1, nota2):
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            raise ValueError("As notas devem estar entre 0 e 10.")

        self.nota1 = nota1
        self.nota2 = nota2

    def registrar_frequencia(self, total_aulas, faltas):
        if total_aulas <= 0:
            raise ValueError("O total de aulas deve ser maior que zero.")

        if faltas < 0 or faltas > total_aulas:
            raise ValueError("A quantidade de faltas é inválida.")

        self.total_aulas = total_aulas
        self.faltas = faltas

