# Discord bot using the spaCy and wikipedia libraries in Python

import discord
import spacy
import wikipedia

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the Discord bot client
client = discord.Client()

@client.event
async def on_message(message):
    # Check if the message is a question
    if message.content.endswith("?"):
        # Process the question using spaCy
        doc = nlp(message.content)

        # Use the wikipedia library to search for an article on the topic
        try:
            article = wikipedia.summary(doc.text, sentences=3)

            # Reply with the article summary
            await message.channel.send(article)
        except wikipedia.exceptions.DisambiguationError:
            await message.channel.send("I'm sorry, I couldn't find a specific article on that topic.")
        except wikipedia.exceptions.PageError:
            await message.channel.send("I'm sorry, I couldn't find any information on that topic.")

# Connect to Discord
client.run("<discord_bot_token>")

# This code uses the Discord.py library to create a Discord bot 
# that listens for messages ending with a question mark (?) and 
# uses the spaCy library to process the questions. 

# The wikipedia library is used to search for articles on the topic, and 
# the bot replies with a summary of the article if one is found. 

# The bot connects to Discord using the provided bot token. 
# Replace <discord_bot_token> with your own Discord bot token.
