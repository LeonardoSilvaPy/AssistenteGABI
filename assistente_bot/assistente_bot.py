import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Saudação inicial e introdução ao agendamento presencial
    mensagem = "Como posso lhe ajudar?"
    await update.message.reply_text(mensagem)

# Função para responder a qualquer outra mensagem após o início
async def resposta_padrao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Resposta fixa para qualquer pergunta após a inicial
    mensagem = "Estou em fase de desenvolvimento, favor comparecer à unidade mais próxima."
    await update.message.reply_text(mensagem)

# Função principal para configurar e rodar o bot
def main():
    # Carrega as variáveis do arquivo .env
    load_dotenv()

    # Acessa o token da variável de ambiente
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

    # Criação do aplicativo com o token do bot carregado
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Adicionando handlers
    app.add_handler(CommandHandler("start", start))  # Handler do comando /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_padrao))  # Resposta padrão

    # Rodando o bot
    app.run_polling()

# Rodar o bot diretamente
if __name__ == "__main__":
    main()
