from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from responses.ResponseRAG import AIBot


# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Saudação inicial e introdução ao agendamento presencial
    mensagem = "Olá! 😊 Eu sou a Gabi, sua assistente virtual dedicada a apoiar profissionais da assistência social em Recife. Estou aqui para ajudar com informações sobre o Cadastro Único, Bolsa Família, Benefícios Eventuais, e outras orientações do SUAS. Como posso ajudá-lo(a) hoje? 🤗"
    await update.message.reply_text(mensagem)

async def resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # cria um objeto da classe AIBot
    ai_bot = AIBot()
    # popula a variavel user_message com a mensagem do usuario
    user_message = update.message.text
    # cria uma variavel que recebe a resposta da class AIBot e passa a variavel de mensagem como parametro
    response = ai_bot.invoke(question=user_message)

    await update.message.reply_text(response)


def main():
    app = ApplicationBuilder().token("7668586336:AAEjYVRm3GBPlsPP8fVmT4_HYKZnH0ukJFQ").build()

    app.add_handler(CommandHandler("start", start))  # Handler do comando /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta))

    # Rodando o bot
    app.run_polling()


# Rodar o bot diretamente
if __name__ == "__main__":
    main()