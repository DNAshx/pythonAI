from datetime import datetime
from flask import Flask, render_template
from ImageApp import app
from fastai import *
from fastai.vision import *
from fastai.widgets import *
import torch
from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse

from pathlib import Path
from io import BytesIO
import sys
import uvicorn
import aiohttp
import asyncio

@app.route('/')
@app.route('/index')
@app.route('/detect')
def index():    
     return render_template(
        "index.html",
        title='Detect',
        year=datetime.now().year,
    )
@app.route('/hello')
def hello():    
    # Render the page
    return "Hello Python!"