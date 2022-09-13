from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
from pytube import YouTube
from datetime import datetime
import os
from pydantic import BaseModel
from pathlib import Path

templates = Jinja2Templates(directory="app/templates")
root = APIRouter()


class Data(BaseModel):
    link: str


@root.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@root.get('/download')
async def back_home(request: Request):
    response = "Add link to download"
    return templates.TemplateResponse("home.html", {"request": request, "data": response})


@root.post('/download')
async def download(request: Request, link: str = Form(...)):
    try:
        if len(link) > 0:
            print(link)
            YT_LINK = link
            video = YouTube(YT_LINK)
            # Showing details
            print("\n\nTitle: ", video.title)
            print("Number of views: ", video.views)
            MIN = int(video.length / 60)
            SEC = video.length % 60
            print(f"Length of video: {MIN}min:{SEC}sec")
            print(f"Rating of video: {video.rating}\n\n")

            # getting the highest resolution
            data = video.streams.get_highest_resolution()

            # save video
            destination_folder = str(Path.home() / "Downloads")
            path = destination_folder
            print(">>>>>>>>>>>>>>>>path is "+path)
            if os.path.exists(destination_folder):
                print("Downloading...")
                now = datetime.now()
            else:
                os.mkdir(destination_folder)
                print("Downloading...")
                now = datetime.now()
            data.download(destination_folder, timeout=60, max_retries=1)
            end = datetime.now()
            print("Download completed!!")
            print(f'Elapsed time: {end - now}')
            response = "Successfully downloaded video"
            return templates.TemplateResponse("home.html", {"request": request, "data": response, "path": path})
    except Exception as e:
        print(e)
        response = "Failed to download video"
        return templates.TemplateResponse("home.html", {"request": request, "data": response})
