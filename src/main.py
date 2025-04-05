import yt_dlp
import pygame
import json
import math
import pygame
from pygame.locals import *
import pyperclip
import subprocess
from subprocess import Popen
import time

disclaimerText = """I am not responsible for your usage of this program. A TV Licence is required."""

bgColour = (40,40,40)
icon = pygame.image.load("dl-logo.PNG")
w = 600
h = 400

downloadYTBtn = pygame.image.load("downloadBTN.png")
dlRect = downloadYTBtn.get_rect()
dlRect.center = w//2 - 150, h//2 + 100

downloadBBCBtn = pygame.image.load("downloadBBC.png")
BBCRect = downloadBBCBtn.get_rect()
BBCRect.center = w//2 + 150, h//2 + 100

pasteBtn = pygame.image.load("paste.png")
pasteRect = pasteBtn.get_rect()
pasteRect.center = w//2, h//2 - 15

logoDisplay = pygame.image.load("dl-logo - hd.png")
logoRect = logoDisplay.get_rect()
logoRect.center = w//2, h//2 - 115

gradientBG = pygame.image.load("grad.png")
gradientRect = gradientBG.get_rect()
gradientRect.center = w//2- 380, h//2 - 80

gradient2 = pygame.image.load("grad2.png")
gradientRect2 = gradient2.get_rect()
gradientRect2.center = w//2 + 380, h//2 + 60

url = ""
chosenFormat = "mp4/best"

# ydl_opts = {
#     'format': chosenFormat,
# }

# URLS = [url]
# with yt_dlp.YoutubeDL() as ydl:
#     ydl.download(URLS)

def getInfo():     
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(json.dumps(ydl.sanitize_info(info)))

def getVideo():
     ydl_opts = {
         'format': chosenFormat
     }
     URLS = [url]
     with yt_dlp.YoutubeDL() as ydl:
         ydl.download(URLS)
        
def getBBCVideo():
    global url
    bbcPrepCommand = """"C:\Program Files\get_iplayer\get_iplayer.cmd" --refresh"""
    bbcCommand = """"C:\Program Files\get_iplayer\get_iplayer.cmd" """ + url + """ --tvquality fhd --force"""
    print(bbcCommand)
    print(url)
    # Popen(str(bbcPrepCommand) + """ && """ + str(bbcCommand), creationflags=subprocess.CREATE_NEW_CONSOLE)
    Popen(bbcCommand, creationflags=subprocess.CREATE_NEW_CONSOLE)
    

def pasteURL():
    global url
    url = pyperclip.paste()
    print(url)
     
pygame.init()
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((600,400))

font = pygame.font.SysFont("Segoe UI", 18)
disfont = pygame.font.SysFont("Segoe UI", 6)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if dlRect.collidepoint(mouse_pos):
                getVideo()
            if BBCRect.collidepoint(mouse_pos):
                getBBCVideo()
            if pasteRect.collidepoint(mouse_pos):
                pasteURL()
    
    gradientBG.convert()
    screen.blit(gradientBG, gradientRect)
    pygame.draw.rect(screen, bgColour, gradientRect, 1)
    
    gradient2.convert()
    screen.blit(gradient2, gradientRect2)
    pygame.draw.rect(screen, bgColour, gradientRect2, 1)

    downloadYTBtn.convert()
    screen.blit(downloadYTBtn, dlRect)
    pygame.draw.rect(screen, bgColour, dlRect, 1)

    downloadBBCBtn.convert()
    screen.blit(downloadBBCBtn, BBCRect)
    pygame.draw.rect(screen, bgColour, BBCRect, 1)

    pasteBtn.convert()
    screen.blit(pasteBtn, pasteRect)
    pygame.draw.rect(screen, bgColour, pasteRect, 1)

    logoDisplay.convert()
    screen.blit(logoDisplay, logoRect)
    pygame.draw.rect(screen, bgColour, logoRect, 1)

    url_text = font.render(url, True, (255, 255, 255))
    screen.blit(url_text, (10, 375))

    disclaimer_text = font.render(disclaimerText, True, (127, 127, 127))
    screen.blit(disclaimer_text, (10, 0))

    pygame.display.update()

    screen.fill(bgColour)
    

    windowCaption = "iDownload - Download BBC iPlayer and YouTube!"
    pygame.display.set_caption(windowCaption)

pygame.quit()