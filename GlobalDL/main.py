import linkretriever
import htmlparser
import listdownloader
import ytdlpfork
import time
import sys

def main(inputlocal,inputurlchoice,ytdl_sites_list):
    print('')
    if inputurlchoice != False:
        inputurl = str(inputurlchoice)
    elif inputurlchoice == False:
        inputurl = input('Enter the site you want to scrape: ')
    inputurl = str(inputurl)

    url = linkretriever.urlformattask(inputurl)
    errorcheck = linkretriever.errorchecktask(linkretriever.urlchecktask(url)[0],linkretriever.urlchecktask(url)[1])

    if errorcheck[0] == 'Success':
        print(f'Success accesing site: {str(url)} status code: {str(errorcheck[1])}')
    elif errorcheck[0] != 'Success':
        print(f'Error accesing for site: {str(url)} status code: {str(errorcheck[1])}')
        return

    htmlcontent = errorcheck[2]
    soupobj = htmlparser.soupobj(htmlcontent,inputlocal,inputurl)

    #Get Title Tag
    page_title = htmlparser.parsehtml(soupobj)[0]

    #Check For Accepted YT-DLP Video Sites and DL From Them
    truefalseytlistval = ytdlpfork.ytsitelistcheck(inputurl,ytdl_sites_list)
    if truefalseytlistval == True:

        print('')
        ytdlchoice = input('Would you like Audio[a], Video[v], or Both[b]? ')
        ytdlchoice = str(ytdlchoice).lower()
        print('')

        ytdllocation = ytdlpfork.yttitlecleaner(page_title, inputlocal)[0]
        print(ytdllocation)

        if ytdlchoice == 'b':
            ytofficialdlaudio = ytdlpfork.ytdlaudio(str(inputurl), ytdllocation)
            if ytofficialdlaudio == 1:
                print(f'Saved audio to: {ytdllocation} For: {inputurl}')
            elif ytofficialdlaudio != 1:
                print(f'Failed to save audio for: {str(inputurl)}')
            ytofficialdlvideo = ytdlpfork.ytdlvideo(str(inputurl), ytdllocation)
            if ytofficialdlvideo == 1:
                print(f'Saved video to: {ytdllocation} For: {inputurl}')
            elif ytofficialdlvideo != 1:
                print(f'Failed to save video for: {str(inputurl)}')
        
        elif ytdlchoice == 'v':
            ytofficialdlvideo = ytdlpfork.ytdlvideo(str(inputurl), ytdllocation)
            if ytofficialdlvideo == 1:
                print(f'Saved video to: {ytdllocation} For: {inputurl}')
            elif ytofficialdlvideo != 1:
                print(f'Failed to save video for: {str(inputurl)}')

        elif ytdlchoice == 'a':
            ytofficialdlaudio = ytdlpfork.ytdlaudio(str(inputurl), ytdllocation)
            if ytofficialdlaudio == 1:
                print(f'Saved audio to: {ytdllocation} For: {inputurl}')
            elif ytofficialdlaudio != 1:
                print(f'Failed to save audio for: {str(inputurl)}')

        print('Done!')
        return

    #Get Page Tags
    p_tag = htmlparser.parsehtml(soupobj)[1]
    a_tag = htmlparser.parsehtml(soupobj)[2]
    img_tag = htmlparser.parsehtml(soupobj)[3]
    video_tag = htmlparser.parsehtml(soupobj)[4]
    audio_tag = htmlparser.parsehtml(soupobj)[5]
    article_tag = htmlparser.parsehtml(soupobj)[6]
    block_quote_tag = htmlparser.parsehtml(soupobj)[7] #NOT USED

    #Get Page Lists
    paragraph_list = htmlparser.listrefiner(p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag)[0]
    hyperlink_list = htmlparser.listrefiner(p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag)[1]
    image_list = htmlparser.listrefiner(p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag)[2]
    video_source_list = htmlparser.listrefiner(p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag)[3]
    audio_source_list = htmlparser.listrefiner(p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag)[4]
    article_list = htmlparser.listrefiner(p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag)[5]
    #block_quote_list = htmlparser.listrefiner(p_tag,a_tag,img_tag,video_tag,audio_tag,article_tag,block_quote_tag)[6]

    #Clean Page Lists
    cleaned_paragraph_list = listdownloader.url_cleaner(paragraph_list,inputurl)
    cleaned_hyperlink_list = listdownloader.url_cleaner(hyperlink_list,inputurl)
    cleaned_image_list = listdownloader.url_cleaner(image_list,inputurl)
    cleaned_video_source_list = listdownloader.url_cleaner(video_source_list,inputurl)
    cleaned_audio_source_list = listdownloader.url_cleaner(audio_source_list,inputurl)
    cleaned_article_list = listdownloader.url_cleaner(article_list,inputurl)
    #cleaned_block_quote_list = listdownloader.url_cleaner(block_quote_list,inputurl)

    #Clean Page Title
    cleaned_page_title = listdownloader.page_title(page_title,inputurl)

    #Page DL Choices
    print('')
    print('Download Options...')
    print('Paragraphs : 1')
    print('Hyperlinks : 2')
    print('Images : 3')
    print('Videos : 4')
    print('Audio : 5')
    print('Articles : 6')
    print('All : 7')
    listdownloaderchoice = input('Enter Corresponding Number For Desired Output: ')
    listdownloaderchoice = int(listdownloaderchoice)

    #Download Page Links Choice:
    if listdownloaderchoice == 1:
        listdownloader.downloader(cleaned_paragraph_list, inputlocal, cleaned_page_title, 'Paragraph')
    elif listdownloaderchoice == 2:
        listdownloader.downloader(cleaned_hyperlink_list, inputlocal, cleaned_page_title, 'Hyperlink')
    elif listdownloaderchoice == 3:
        listdownloader.downloader(cleaned_image_list, inputlocal, cleaned_page_title, 'Image')
    elif listdownloaderchoice == 4:
        listdownloader.downloader(cleaned_video_source_list, inputlocal, cleaned_page_title, 'Video')
    elif listdownloaderchoice == 5:
        listdownloader.downloader(cleaned_audio_source_list, inputlocal, cleaned_page_title, 'Audio')
    elif listdownloaderchoice == 6:
        listdownloader.downloader(cleaned_article_list, inputlocal, cleaned_page_title, 'Article')
    else:
        listdownloader.downloader(cleaned_paragraph_list, inputlocal, cleaned_page_title, 'Paragraph')
        listdownloader.downloader(cleaned_hyperlink_list, inputlocal, cleaned_page_title, 'Hyperlink')
        listdownloader.downloader(cleaned_image_list, inputlocal, cleaned_page_title, 'Image')
        listdownloader.downloader(cleaned_video_source_list, inputlocal, cleaned_page_title, 'Video')
        listdownloader.downloader(cleaned_audio_source_list, inputlocal, cleaned_page_title, 'Audio')
        listdownloader.downloader(cleaned_article_list, inputlocal, cleaned_page_title, 'Article')
        #listdownloader.downloader(cleaned_block_quote_list, inputlocal, cleaned_page_title, 'Block Quote')
    print('''
Done!
    ''')

if __name__ == "__main__":

    cmd_argument_length = int(len(sys.argv))

    if cmd_argument_length < 3:
        print('Must Enter In Form: main.py [Out File Path] [Site List Path]')
        exit()

    cmd_argument_0 = sys.argv[0] #This is just the filename
    cmd_argument_1 = sys.argv[1] #Input Save Location
    cmd_argument_2 = sys.argv[2] #YT-DL Site List File Location
    #cmd_argument_3 = sys.argv[3]
    #cmd_argument_4 = sys.argv[4]
    #cmd_argument_5 = sys.argv[5]

    print('''
GlobalDL: A global site media downloader
Created By: Yam306''')
    #inputlocal = input('Enter download folder for content: ')
    inputlocal = cmd_argument_1   #CMD ARG INPUT 1
    inputlocal = str(inputlocal)

    ytdl_sites_list = []
    #ytdl_sites_file = input('Enter the directory of sites accepted by yt-dl: ')
    ytdl_sites_file = cmd_argument_2    #CMD ARG INPUT 2
    with open(str(ytdl_sites_file),'r',encoding='utf-8') as file:
        lines = file.readlines()

    for site in lines:
        site.strip('\n')
        ytdl_sites_list.append(str(site))

    main(inputlocal,False,ytdl_sites_list)

    restartchoice = 'y'
    while restartchoice != 'n':
        print('')
        newurl = input('Enter new URL or leave blank to exit: ')
        newurl = str(newurl)
        if str(newurl).lower().find('http') != -1:
            main(inputlocal,newurl,ytdl_sites_list)
            restartchoice = 'y'
        else:
            print('Error: No Valid URL Entered')
            restartchoice = 'n'
    print('Exiting in 5 seconds...')
    time.sleep(5)
    exit()