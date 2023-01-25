import telebot
import openai


openai.api_key = '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'
bot = telebot.TeleBot("5691866275:AAHVWRzwIseHDCSt7JgF_2KgignaPtkOlsE")


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    responce = openai.Completion.create(
     model="text-davinci-003",
     prompt=message.text,
     temperature=0.5,
     max_tokens=1000,
     top_p=1.0,
     frequency_penalty=0.5,
     presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=responce['choices'][0]['text'])


bot.polling()
