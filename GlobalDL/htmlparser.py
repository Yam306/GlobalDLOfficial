import bs4
import os
import listdownloader

#Parses html input from linkretriever

def soupobj(htmlcontent,inputlocal,inputurl):
    soupobj = bs4.BeautifulSoup(htmlcontent, "html.parser") #gets soup object from HTML content that is input from linkretriever

    title_tag = soupobj.find("title").text

    page_title = listdownloader.page_title(title_tag,inputurl)

    htmlsavelocal = str(inputlocal+'\\'+str(page_title)+'\\'+str(page_title)+'.html')

    dllocation = str(inputlocal+'\\'+str(page_title))
    if os.path.isdir(str(dllocation)) == False:
        os.mkdir(dllocation)
        print(f'Made DL Location At: {str(dllocation)}')

    with open(htmlsavelocal, "w", encoding='utf-8') as file:
        file.write(str(soupobj))
        print(f'Wrote HTML File For Site To -> {htmlsavelocal}')

    return soupobj

def parsehtml(soupobj):
    #each of the following should return lists of the content they are designated to find

    #hyperlink tag:a list
    a_tag = soupobj.find_all("a")

    #paragraph tag:text
    p_tag = soupobj.find_all("p")

    #block text tag:blockquote
    block_quote_tag = soupobj.find_all("blockquote")

    #img tag:img list
    img_tag = soupobj.find_all("img")

    #video tag:video list MUST USE SOURCE TAG TO GET ACTUAL FILE
    video_tag = soupobj.find_all("video")

    #audio tag:audio list MUST USE SOURCE TAG TO GET ACTUAL FILE
    audio_tag = soupobj.find_all("audio")

    #article tag:article list
    article_tag = soupobj.find_all("article")

    #title tag:title list MUST USE SOURCE TAG TO GET ACTUAL FILE
    title_tag = soupobj.find("title").text

    return(title_tag,p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag)

def listrefiner(p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag):

    paragraph_list = []
    for paragraph in p_tag:
        try:
            paragraph_list.append(paragraph)
        except:
            continue

    block_quote_list = []    #Not Working
    for block_quote in block_quote_list:
        try:
            block_quote_list.append(block_quote)
        except:
            continue

    audio_source_list = []
    for audio in audio_tag:
        try:
            audio_source_list.append(audio['src'])
        except:
            continue

    video_source_list = []
    for video in video_tag:
        try:
            video_source_list.append(video['src'])
        except:
            continue

    hyperlink_list = []
    for link in a_tag:
        try:
            hyperlink_list.append(link['href'])
        except:
            continue

    image_list = []
    for img in img_tag:
        try:
            image_list.append(img['src'])
        except:
            continue

    article_list = []
    for article in article_tag:
        try:
            article_list.append(article['data-large-file-url'])
        except:
            continue
    
    return(paragraph_list,hyperlink_list,image_list,video_source_list,audio_source_list,article_list,block_quote_list)
