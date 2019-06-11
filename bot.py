import discord
import json

# retrieve token (protected)
settings = json.loads(open('settings.json').read())
token = settings['token']
local = False
if "whitelist" in settings:
        local = True
        whitelist = settings['whitelist']

bot_info = json.loads(open('bot_info.json').read())

class MyClient(discord.Client):
        async def on_ready(self):
                print('Logged in as:')
                print(self.user.name)
                print(self.user.id)
                print('------')
        async def on_message(self, message):
                if message.author == self.user:
                        return
                if local:
                        if message.author.id not in whitelist:
                                return
                # print(f'{message.channel}: {message.author}:{message.author.name}: {message.content}')

                if message.content.lower() == 'ping':
                        await message.channel.send('pong')

                if message.content.lower() == '!stop':
                     await client.logout()




client = MyClient()
client.run(token)
