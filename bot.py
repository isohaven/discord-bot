import discord


class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged in as:')
		print(self.user.name)
		print(self.user.id)
		print('------')
	async def on_message(self, message):
		if message.author == self.user:
			return
		# print(f'{message.channel}: {message.author}:{message.author.name}: {message.content}')
		if message.content.lower() == 'ping':
			await message.channel.send('pong')


client = MyClient()
client.run('NTM3MTMxODI4NTcwNzUwOTc2.DygzMQ.a8enKXYvfwry6uxt7TR_ULypv70')