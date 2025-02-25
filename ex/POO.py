class Aluno():
    def __init__(self,nome):
        self.nome = nome
        self.nota = 0
    def notas(self,nota):
        self.nota = nota
    def passou(self,media):
        if self.nota >= media:
            print(self.nome, 'foi APROVADO!')
        else:
            print(self.nome, 'foi REPROVADO!')


aluno1 = Aluno('Renzo')
aluno1.nome()
aluno1.notas(10)
aluno1.passou(4)
aluno2 = Aluno('Sofia')
aluno2.notas(5)
aluno2.passou(7)
