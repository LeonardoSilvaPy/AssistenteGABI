import os
from decouple import config
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings

# Configuração das chaves de API usando o arquivo .env
os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
os.environ['HUGGINGFACE_API_KEY'] = config('HUGGINGFACE_API_KEY')

if __name__ == '__main__':
    # Caminho do arquivo PDF a ser carregado
    file_path = '../Rag/data/Cadastro_Unico.pdf'

    # Carrega o documento PDF usando o PyPDFLoader
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    # Inicializa o divisor de texto para dividir os documentos em partes menores
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Tamanho máximo de cada pedaço de texto
        chunk_overlap=200,  # Sobreposição entre os pedaços de texto
    )

    # Divide o documento em pedaços de texto menores
    chunks = text_splitter.split_documents(documents=docs)

    # Diretório onde os dados vetoriais serão persistidos
    persist_directory = '/app/chroma_data'

    # Inicializa o modelo de embeddings da Hugging Face
    embedding = HuggingFaceEmbeddings()

    # Cria o banco de dados vetorial (Chroma) para armazenar os embeddings
    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=persist_directory,
    )

    # Adiciona os documentos vetorizados ao banco de dados
    vector_store.add_documents(documents=chunks)
