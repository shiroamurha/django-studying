from disciplina import Disciplina



class Curso():

    def __init__(self, 
                carga_horaria_total: int, 
                nome: str, 
                grau: str, 
                sigla: str, 
                descricao = '', 
                ultimo_curso = None
            ):
        
        self.cod = ultimo_curso.cod+1 if ultimo_curso is not None else 0

        self.carga_horaria_total = carga_horaria_total
        self.nome = nome
        self.grau = grau 
        self.sigla = sigla
        self.descricao = descricao

        if ultimo_curso is not None:
            ultimo_curso.proximo_curso = self 



    def __str__(self):
        
        # gera uma string com todos os atributos do objeto e seus valores

        attrs = vars(self)
        keys = list(attrs.keys())
        to_string = ''

        for key in keys:
            to_string += f'{key.replace("_", ' ').title()}: {attrs[key]}\n'

        return to_string + '\n'



    def listar_disciplinas_curso(c: 'Curso',  disciplina_eixo: Disciplina):

        #pega todas disciplinas cadastradas (sem filtrar data)
        todas_disciplinas = [disciplina_eixo]

        while disciplina_eixo.proxima_discp is not None:
            todas_disciplinas.append(disciplina_eixo.proxima_discp)
            disciplina_eixo = disciplina_eixo.proxima_discp

        # agrupa as disciplinas que sao de dado curso
        disciplinas_curso = []

        for discp in todas_disciplinas:
            if discp.curso == c:
                disciplinas_curso.append(discp)

        return disciplinas_curso

        

if __name__ == '__main__':
    c = Curso(900, 'abcde', 'aaa', 'abc')
    print(c)
