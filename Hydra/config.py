import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "26691248"))
API_HASH = getenv("API_HASH", "7cc5f91b8389eaea67407887a7c1a6a3")
BOT_TOKEN = getenv("BOT_TOKEN", "6604047506:AAGJuRbXzX0n1EVswQQq6qWZaSZ76GtCQe0")
STRING_SESSION = getenv("STRING_SESSION", "BQADMVMANF8AJlw8WSBY5jwEq1ezToG5r4Vx_XhFTNLgppx-jMu_-PCVly2AJdrFKFaOcQ9R72dqUCpuxOYICX4YjCweXwZ7L2kP5D8C8qRCjeR0yCUPzC4PJF95PfhFQBt64Cv8je8v3hO5wWPPscNNjFCCLGGtifc6FuLWLYVz8bvacSfp4JUcjQPMjOYGqTRHAk6XSF-xJGLSw3sIPXu6-kx2MF0MTGMWcI1NWS39na7qp1jv28Hb5iw26dx8YmkqKvAg50uRAz0M94xMMfmoECMt97dlfcWm48IVYXJa-UItH_HfWAdNwrtP6BA-uHyL1ckEDl5nmlfWK-fF78QkYaDqZAAAAAF41aRLAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://udoh:udoh@cluster0.sdmodpx.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6322234443").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001976372339"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6322234443").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/opet321/lol")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
                       
