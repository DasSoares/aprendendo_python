# Programação orientada a objetos

class Estudante:
    def __init__(self, nome, idade, grade):
        self.nome = nome
        self.idade = idade
        self.grade = grade # 0 - 100

    def pega_grade(self):
            return self.grade


class Curso:
    def __init__(self, nome, max_estudantes):
        self.nome = nome
        self.max_estudantes = max_estudantes
        self.estudantes = []

    def adiciona_estudante(self, estudante):
        if len(self.estudante) < self.max_estudantes:
            self.estudantes.append(estudante)
            return True
        return False

    def obter_media_grade(self):
        valor = 0
        for s in self.estudantes:
            valor += Estudante.pega_grade()

        return valor / len(self.estudantes)


s1 = Estudante("Danilo", 26, 72)
s2 = Estudante("Julia", 20, 69)
s3 = Estudante("Joao", 29, 98)

curso = Curso("Administracao", 3)
curso.adiciona_estudante(s1)
curso.adiciona_estudante(s2)
#curso.adiciona_estudante(s3)
print(curso.obter_media_grade())
