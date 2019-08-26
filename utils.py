from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Jow',idade=29)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    #pessoa = Pessoas.query.filter_by(nome="Sidney").first()
    #print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jow').first()
    pessoa.nome = 'Camila'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jow').first()
    pessoa.delete()

if __name__ == '__main__':
    insere_pessoas()
    #exclui_pessoa()
    #consulta_pessoas()
    #altera_pessoa()