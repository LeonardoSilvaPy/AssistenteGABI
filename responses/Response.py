import os
from decouple import config #carregar configurações de um arquivo .env

#é utilizado para processar e formatar as respostas geradas pelo modelo de linguagem
from langchain_core.output_parsers import StrOutputParser

# é usada para criar e gerenciar templates de prompts, ou seja, textos com espaços reservados (variáveis)
from langchain_core.prompts import PromptTemplate

#é uma implementação de um modelo de linguagem
from langchain_groq import ChatGroq

# recebe o valor da api key do arquivo .env
os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

# Define uma classe que poderá ser chamada em varias partes do codigo
class AIBot:
    # essa função é chamada automaticamente quando um objeto dessa classe é criado
    # metodo construtor da classe AIBot
    def __init__(self):
        # seta o um dos modelos disponibilizados pela groq para gerar as respostas
        self.__chat = ChatGroq(model='llama-3.1-70b-versatile')

    # essa função recebe as perguntas e processa usando o modelo setado anteriormente
    def invoke(self, question):
        # define o template para o prompt que será enviado ao modelo de linguagem
        prompt = PromptTemplate(
            input_variables=['texto'],
            template='''
            você é o assistente virtual do cras, que vai auxiliar os usuarios com encaminhamentos e apoiando no que for necessario.
            <texto>
            {texto}
            </texto>
            ''')
        # (prompt) é aplicado primeiro, fornecendo o template com o espaço reservado para o texto da pergunta
        # (self.__chat) gera a resposta com base no prompt
        # StrOutputParser() - processa a saída do modelo, e formata como uma string simples
        chain = prompt | self.__chat | StrOutputParser()

        #  Aqui o encadeamento é executado. O invoke no chain aplica o template, gera a resposta do modelo e a formata
        response = chain.invoke({
            'texto': question,
        })

        # a classe retorna uma resposta de acordo com a pergunta do usuario
        return response