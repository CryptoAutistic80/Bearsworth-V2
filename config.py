import os

# Retrieve Discord bot token from environment variables
TOKEN = os.environ['DISCORD_TOKEN']

# Retrieve OpenAI API key from environment variables
OPENAI_KEY = os.environ['KEY_OPENAI']

PINECONE_KEY = os.environ['PINECONE_KEY']

# Set the maximum number of retries for failed OpenAI API requests
MAX_RETRIES = 10

# Set personlity temperature 0 = deterministic 1 = random and more creative
PERSONALITY_TEMP = 0.5

# Set number of tokens the bot can use for the chat completion
BOT_TOKENS = 600

# Set the number of chat messages in the chat history
CHAT_HISTORY = 10

# Set time in secs of inactivity before coversation auto-closes, example (5 minute = 60*5)
CONVO_TIMEOUT = 60*10

# Set the maximum word limit for user messages
MESSAGE_WORD_LIMIT = 80

# Set the number of top similar documents to retrieve from Pinecone
TOP_K_SIMILAR_DOCS = 10