from datetime import date



class Disciplina():

    def __init__(self, 
                curso,
                carga_horaria: int, 
                nome: str, 
                ementa: str, 
                referencias: str, 
                data_fim: date, 
                data_inicio = date.today(), 
                sigla = 'N/A',
                ultima_discp = None
            ):

        self.curso = curso
        self.cod = ultima_discp.cod+1 if ultima_discp is not None else 0

        self.nome = nome
        self.ementa = ementa
        self.referencias = referencias
        self.carga_horaria = carga_horaria
        self.data_fim = data_fim
        self.data_inicio = data_inicio
        self.sigla = sigla

        #self.ultima_discp = ultima_discp
        self.proxima_discp = None
        
        if ultima_discp is not None:
            ultima_discp.proxima_discp = self



    def __str__(self):

        attrs = vars(self)
        keys = list(attrs.keys())[0:9]
        keys.remove('curso')
        to_string = ''

        for key in keys:
            to_string += f'{key.replace("_", ' ').title()}: {attrs[key]}\n'

        return to_string + '\n'



    def listar_disciplinas_atuais(d: date, eixo: 'Disciplina'):

        discp_atuais = []

        # passa por todas as disciplinas cadastradas e pega as que sao atuais 
        while eixo is not None:
            if eixo.data_fim > date.today():
                discp_atuais.append(eixo)
        
            eixo = eixo.proxima_discp
        
        return set(discp_atuais)
                
        
        









