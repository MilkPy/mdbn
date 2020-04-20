import discord

client = discord.Client()#Переменная для кпрощения использования клиента

@client.event
async def on_ready():#Создание асинхронной переменной для проверки бота
	print('We have logged in as {0.user}'.format(client))#Тут смотрим работает бот иди нет

@client.event
async def on_message(message):
	if message.author == client.user:#это мы делаем что бы не возникало ошибок с пользывателем
		return

	if message.content.startswith('$Help'):#Тут мы вводим команду
		await message.channel.send('''Что я могу? Я пока что ничего, потому что я в разработке (это не так и уж легко)
Но вы можете предложить что нибудь в текстовой канал #идеи! Может быть мдея воплотится в реальность!!!''')
	if message.content.startswith('$Porn'):
		await message.channel.send('ой ляяя, извращенец',file=discord.File(fp='kirill.jpg', spoiler=True))


client.run('NzAxNzg2MTM3MzY2MzY0MTkx.Xp2jWA.qmQeatNkHhsOYEteLkWoEgxU1Gs')#Тут мы запускаем бота
