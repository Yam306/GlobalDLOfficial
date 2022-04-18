import requests
import os

def url_cleaner(url_list,inputurl,specification):
    cleaned_list = []
    if specification == 'block_quote':
        return url_list

    for url in url_list:
        url = str(url)
        ##################Enter Site Specifics Here##########################
        if str(inputurl).find('wiki') != -1: #for wikipedia and wiki sites
            if str(url).find('https:') == -1:
                url = str('https:'+url)
                cleaned_list.append(url)

        else:
            cleaned_list.append(url)

        #####################################################################

    return cleaned_list

def page_title(page_title):
    page_title = str(page_title).strip()
    page_title = page_title.encode('ascii', 'ignore')
    page_title = page_title.decode('ascii')
    #not allowed in windows:
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
    page_title = page_title.replace("'",'')
    page_title = page_title.replace(' ','')
    page_title = page_title.replace(' - ','.')
    page_title = page_title.replace('=','.')
    page_title = page_title.strip('\"')
    page_title = page_title.strip('\'')

    return page_title

def downloader(cleaned_url_list,inputlocation,page_title,specification):
    dllocation = str(inputlocation+'\\'+str(page_title))
    if os.path.isdir(str(dllocation)) != True:
        os.mkdir(dllocation)

    i = 0
    for url in cleaned_url_list:
        i+=1

        filename = str(page_title+'.'+str(url.split('/')[-1]))
        filename = filename.replace('<','')
        filename = filename.replace('>','')
        filename = filename.replace(':','')
        filename = filename.replace('“','')
        filename = filename.replace('/','')
        filename = filename.replace('|','')
        filename = filename.replace(r'\\','')
        filename = filename.replace(r'\n','')
        filename = filename.replace('?','')
        filename = filename.replace('*','')
        filename = filename.replace('=','')
        filename = filename.strip('\"')
        filename = filename.strip('\'')

        fulldllocal = str(dllocation+'\\'+filename)

        if specification == 'block_quote':
            continue

        try:
            print('')
            print(f'{str(i)}/{str(len(cleaned_url_list))} | Attempting DL for: {str(url)} at location: {fulldllocal}')

            response = requests.get(url)
            if response.ok == True:
                open(fulldllocal, "wb").write(response.content)
            else:
                print(f'{str(i)}/{str(len(cleaned_url_list))} | Failed DL for: {str(url)} at location: {fulldllocal} [Most Likely 404]')
                continue

            print(f'{str(i)}/{str(len(cleaned_url_list))} | Succeeded DL for: {str(url)} at location: {fulldllocal}')
        except:
            print(f'{str(i)}/{str(len(cleaned_url_list))} | Failed DL for: {str(url)} at location: {fulldllocal}')
            continue

    with open(str(inputlocation+'\\'+str(page_title)+'\\'+str(specification)+'-'+str(page_title)+'.txt'), 'w', encoding='utf-8') as f:
        f.write(f'{str(specification)} Links For: {str(page_title)} \n')

    for url in cleaned_url_list:
        with open(str(inputlocation+'\\'+str(page_title)+'\\'+str(specification)+'-'+str(page_title)+'.txt'), 'a', encoding='utf-8') as f:
            f.write('| '+str(url)+'\n')
    f.close
            