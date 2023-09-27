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
STRING_SESSION = getenv("STRING_SESSION", "BQCPfH8gtvv3rQCbVBdkaYYmY21Nn-uCK-EKesdqmvmMNR9K3uNzrkXPhmjmxmrqBoRretHmmop6ldGk3viQfHsXIYSr9iFL6sx1roThw44wSrAh87t-VnHJSUiDvBzexF4Vf-Rk5WjM3HaKBcLpD2FQzb6ye2dHj9QnAHhQXfRLRMy9SxanC0VXVVDalq2bEdhdASxDjlOnsaC09Bs1NCGw2omuDpDrEsX5gGJP-sP39f7kSD-U8pGUDLL_NFWtY2npw-uDz958qd_KwrwTIQZSXZwcPHTn9GH4jXmIJZGgsu3vSQ8HbMOWPJl0fNLCW7_eaqXiI6eRC4CAmosXrPhRAAAAAXjVpEsA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://udoh:udoh@cluster0.sdmodpx.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6322234443").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001976372339"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6322234443").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/opet321/lol")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
                       
