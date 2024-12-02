import os
from decouple import config
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings

# seta a chave criada no cloud groq para conseguimos ter acessos aos modelos disponiveis
os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
# seta a chave criada no huggingface para conseguimos ter acessos aos embeddings
os.environ['HUGGINGFACE_API_KEY'] = config('HUGGINGFACE_API_KEY')

if __name__ == '__main__':
    # Caminho do arquivo PDF a ser carregado
    file_path = '../Rag/data/Cadastro_Unico.pdf'

    # Carrega o documento PDF usando o PyPDFLoader
    loader = PyPDFLoader(file_path)
    docs = loader.load()


    # RecursiveCharacterTextSplitter: Esta classe é usada para dividir o conteúdo do
    # documento em pedaços menores de texto(chunks)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Tamanho máximo de cada pedaço de texto
        chunk_overlap=200,  # Sobreposição entre os pedaços de texto
    )

    # split_documents: Este metodo divide o conteúdo do documento em pedaços menores de texto, conforme configurado acima
    chunks = text_splitter.split_documents(documents=docs)

    # Define o diretorio onde os dados vetoriais serão armazenados
    persist_directory = '../chroma'
    if not os.path.exists(persist_directory):
      os.makedirs(persist_directory)
      print(f"Diretório criado: {persist_directory}")
    else:
       print(f"Diretório já existe: {persist_directory}")

    # cria uma instancia de HuggingFaceEmbeddings, que é usada para converter o texto em vetores numéricos
    #Esses embeddings representam semanticamente o conteúdo de cada pedaço de texto e permitem a comparação e busca eficiente
    embedding = HuggingFaceEmbeddings()

    # Inicializa o Chroma, configurado para usar a função de embeddings
    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=persist_directory,
    )

    # adiciona os documentos divididos em chunks ao Chroma
    vector_store.add_documents(documents=chunks)


