import os
from decouple import config
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

# seta a chave criada no cloud groq para conseguimos ter acessos aos modelos disponiveis
os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        # Inicializa o modelo
        self.__chat = ChatGroq(model='llama-3.1-70b-versatile')
        # Chama o metodo build_retriever() para criar e configurar o recuperador de documentos
        # responsavel por buscar os documentos mais relevantes para responder às perguntas
        self.__retriever = self.__build_retriever()

    def __build_retriever(self):
        # Configura o diretório de persistência e cria o recuperador de documentos
        persist_directory = '../chroma_data'


        #Essa função converte os documentos em representações vetoriais
        embedding = HuggingFaceEmbeddings()
        # Chroma é uma ferramenta de armazenamento de vetores que permite realizar buscas
        # eficientes em grandes volumes de dados
        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding,
        )
        # converte o Chroma em um recuperador de documentos,
        # configurado para retornar os 30 documentos mais relevante
        # k define o numero de documentos a serem retornados
        return vector_store.as_retriever(search_kwargs={'k': 30})

    def invoke(self, question):
        # Template de resposta do assistente
        # define um prompt pré-estabelecido que instrui o modelo
        # context é substituido pela pergunta do usuario
        SYSTEM_TEMPLATE = '''
        Responda as perguntas dos usuários com base no contexto abaixo. 
        Você é um assistente especializado em tirar dúvidas sobre o CRAS e seus serviços e atendimentos. 
        Tire dúvidas dos usuarios que entrarem em contato. 
        Responda de forma natural, agradável e respeitosa. Seja objetivo nas respostas, com informações claras e diretas. Foque em ser natural e humanizado, como um diálogo comum entre duas pessoas. 
        Responda sempre em português brasileiro. 
        <context>
        {context}
        </context>
        '''

        # Recupera o contexto relevante (documentos) com base na pergunta
        docs = self.__retriever.invoke(question)

        # ChatPromptTemplate.from_messages - cria um template de prompt que será usado
        # para formular a interação entre o modelo e a pergunta.
        question_answering_prompt = ChatPromptTemplate.from_messages(
            [
                ('system', SYSTEM_TEMPLATE), # passa o template setado anteriormente
                ('user', '{question}')  # passa a pergunta atual como variavel
            ]
        )

        # create_stuff_documents_chain - cria uma cadeia que combina o modelo de linguagem
        # e o template de prompt para gerar a resposta
        document_chain = create_stuff_documents_chain(self.__chat, question_answering_prompt)

        # docs - Recupera o contexto relevante nod documentos
        # question - pergunta do usuario
        response = document_chain.invoke(
            {
                'context': docs,
                'question': question,
            }
        )

        return response
