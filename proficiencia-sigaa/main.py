from curso import Curso
from disciplina import Disciplina
from datetime import date



def main():

    # primeiros registros necessarios para funcionamento
    curso_eixo = Curso(600, 'eixo', 'graduacao', 'eix')
    disciplina_eixo = Disciplina(curso_eixo, 20, 'eixo', 'a'*30, 'b'*50, date(1900,1,2), data_inicio = date(1900,1,1))

    ads = Curso(2300, 'Analise e Desenvolvimento de Sistemas', 'Graduacao', 'ADS', 'Melhor curso da tinga', ultimo_curso=curso_eixo)
    a = Disciplina(ads, 
        80, 
        'Programacao 1', 
        'Fundamentos e iniciacao em programacao', 
        'Alan Turing, Albert Einstein (todas as obras)',
        date(2025,12,31), 
        sigla = 'PRG01',
        ultima_discp=disciplina_eixo
    )
    b = Disciplina(ads, 
        110, 
        'Programacao 2', 
        'Orientacao a objeto e afins', 
        'Alan Turing, Albert Einstein (todas as obras)',
        date(2025,12,31), 
        sigla = 'PRG02',
        ultima_discp = a
    )
    c = Disciplina(ads, 
        60, 
        'Alguma optativa', 
        'Serve pra poder ter opçao', 
        'Alan Turing, Albert Einstein (todas as obras)',
        date(2024,12,31), 
        data_inicio = date(2024,7,1),
        sigla = 'OPT01',
        ultima_discp = b
    )

    print(ads)
    exemplo1 = Curso.listar_disciplinas_curso(ads, disciplina_eixo)
    exemplo2 = Disciplina.listar_disciplinas_atuais(date.today(), disciplina_eixo)

    _= [print(i) for i in exemplo1]
    _= [print(i) for i in exemplo2]

    


if __name__ == "__main__":
    main()