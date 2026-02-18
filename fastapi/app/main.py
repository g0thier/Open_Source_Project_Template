#¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ #
#           Library            #
#_____ _____ _____ _____ _____ #

# General Libraries
import ssl
import json
import art

# FastAPI requierements
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse

# Debug
ssl._create_default_https_context = ssl._create_unverified_context

# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#           Metadata            #
# ______________________________#

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#           Homepage            #
# ______________________________#

with open("index.html", "r") as html_file:
    # Lire le contenu du fichier HTML dans une variable texte
    html = html_file.read()


# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#       FastAPI describe        #
# ______________________________#

app = FastAPI(
    timeout=config["timeout"],
    title=config["title"],
    summary=config["summary"],
    description=config["description"],
    version=config["version"],
    contact=config["contact"],
    terms_of_service=config["terms_of_service"],
    openapi_tags=config["openapi_tags"]
)


# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#        FastAPI run app        #
# ______________________________#

@app.get("/", tags=["Home"])
async def get():
    return HTMLResponse(html)

@app.post("/ascii/", tags=["ascii"])
async def question(input_text: str = "Hello World"):
    return art.text2art(input_text)