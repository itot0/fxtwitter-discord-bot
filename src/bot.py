import yaml
import discord

# Load secrets
with open('./secrets.yml', 'r') as file:
    secrets = yaml.safe_load(file)
token = secrets['credentials']['API_TOKEN']

# Set up Discord client with intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await process_message(message)

async def process_message(message):
    """Process a message: replace URL and send a new message."""
    original_domain = 'https://x.com'
    replacement_domain = 'https://fxtwitter.com'
    if original_domain in message.content:
        new_message = f"{message.author.mention}, here's your updated link: {message.content.replace(original_domain, replacement_domain)}"
        try:
            await message.delete()
            print("Original message deleted.")
        except discord.errors.DiscordException as e:
            print(f"Error deleting message: {e}")
        try:
            await message.channel.send(new_message)
            print(f"New message sent: {new_message}")
        except discord.errors.DiscordException as e:
            print(f"Error sending new message: {e}")    

# Run Bot
client.run(token)