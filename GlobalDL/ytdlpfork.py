from yt_dlp import YoutubeDL
import os

def yttitlecleaner(page_title, inputlocal):
    page_title = str(page_title).strip()
    page_title = page_title.encode('ascii', 'ignore')
    page_title = page_title.decode('ascii')
    page_title = page_title.replace('<','')
    page_title = page_title.replace('>','')
    page_title = page_title.replace(':','')
    page_title = page_title.replace('"','')
    page_title = page_title.replace('(','')
    page_title = page_title.replace(')','')
    page_title = page_title.replace('/','')
    page_title = page_title.replace('|','')
    page_title = page_title.replace(r'\\','')
    page_title = page_title.replace('?','')
    page_title = page_title.replace('*','')
    page_title = page_title.replace(' ','')
    page_title = page_title.replace('!','')
    page_title = page_title.replace('-','')
    page_title = page_title.replace(r"'",'')
    page_title = page_title.strip('\"')
    page_title = page_title.strip('\'')
    page_title = page_title.replace(' ','')
    page_title = page_title.replace(' - ','.')
    page_title = page_title.replace('=','.')

    dllocation = str(inputlocal+'\\'+str(page_title))
    if os.path.isdir(str(dllocation)) != True:
        os.mkdir(dllocation)

    return (dllocation,page_title)

def ytsitelistcheck(inputurl,ytdl_sites_list):
    list1 = []
    for site in ytdl_sites_list:
        site = site.strip('\n')
        if str(inputurl).lower().find(str(site)) != -1:
            list1.append(site)
        elif str(inputurl).lower().find(str(site)) == -1:
            continue
    if len(list1) != 0:
        print('Done with yt-list check (Found)')
        return True
    elif len(list1) == 0:
        print('Done with yt-list check (Not Found)')
        return False

def ytdlvideo(url,inputlocal):

    try:
        print(f'Downloading video for {url}...')
        ydl_opts = {  #video
            'outtmpl': str(str(inputlocal) + '\\' + 'video-%(title)s-%(id)s.%(ext)s'),
            'restrictfilenames': True,
            'forcetitle': True,
            'continuedl': True,
            'retries': 5,       #THE AMOUNT OF RETRIES CAN BE CHANGED
            'continuedl': True,
            'ignoreerrors': True
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(url)])

        return 1
    
    except:
        print(f'Failure for some in: {url}')
        return 0

def ytdlaudio(url,inputlocal):
    try:
        print(f'Downloading audio for {url}...')
        ydl_opts = {  #audio
        'outtmpl': str(str(inputlocal) + '\\' + 'audio-%(title)s-%(id)s.%(ext)s'),
        'restrictfilenames': True,
        'forcetitle': True,
        'format': 'bestaudio/best',
        'retries': 5,      #THE AMOUNT OF RETRIES CAN BE CHANGED
        'continuedl': True,
        'ignoreerrors': True,
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
        }]}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(url)])

        return 1

    except:
        print(f'Failure for some in: {url}')
        return 0