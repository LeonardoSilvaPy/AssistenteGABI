import os
from decouple import config
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        # Inicializa o modelo de chat (Groq)
        self.__chat = ChatGroq(model='llama-3.1-70b-versatile')
        # Inicializa o recuperador de contexto (Chroma)
        self.__retriever = self.__build_retriever()

    def __build_retriever(self):
        # Configura o diretório de persistência e cria o recuperador de documentos
        persist_directory = '/app/chroma_data'
        embedding = HuggingFaceEmbeddings()
        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding,
        )
        # Retorna o recuperador configurado para buscar os 30 documentos mais relevantes
        return vector_store.as_retriever(search_kwargs={'k': 30})

    def invoke(self, question):
        # Template de resposta do assistente (definido no sistema)
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

        # Cria o template de prompt para o modelo de chat
        question_answering_prompt = ChatPromptTemplate.from_messages(
            [
                ('system', SYSTEM_TEMPLATE),
                ('user', '{question}')  # Passa a pergunta atual como variável
            ]
        )

        # Cria a cadeia de documentos para processar o contexto e gerar a resposta
        document_chain = create_stuff_documents_chain(self.__chat, question_answering_prompt)

        # Gera a resposta usando o contexto recuperado e a pergunta atual
        response = document_chain.invoke(
            {
                'context': docs,
                'question': question,
            }
        )

        return response
