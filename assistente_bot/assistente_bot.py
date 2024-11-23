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
    # Criação do aplicativo com seu token do bot
    app = ApplicationBuilder().token("7668586336:AAEjYVRm3GBPlsPP8fVmT4_HYKZnH0ukJFQ").build()

    # Adicionando handlers
    app.add_handler(CommandHandler("start", start))  # Handler do comando /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_padrao))  # Resposta padrão

    # Rodando o bot
    app.run_polling()

# Rodar o bot diretamente
if __name__ == "__main__":
    main()
