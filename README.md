# GlobalDL
A Global Media Downloader Supporting All Sites Supported Explicitly by YT-DL and More!

# Uses of GlobalDL
- GlobalDL is a very versatile media downloader
- GlobalDL can be used to effectivley download video/audio from ANY site supported by YT-DL officially [https://ytdl-org.github.io/youtube-dl/supportedsites.html]
- However GlobalDL can also download media from any site on the internet that has HTML, including downloading IMAGES [which yt-dl by itself cannot do]
- GlobalDL uses the HTML to download realtive filetypes and HTML headers from the target site
- Although GlobalDL can be used to download from almost any site ONLY USE IT ON SITES THAT PERMIT YOU TO DOWNLOAD FROM THEM
- This software [GlobalDL] is NOT to be used for malicious or illegal intent
- This software [GlobalDL] is NOT to be used for downloading illegal content
- This software [GlobalDL] is to ONLY be used under U.S. and international law

# Required Pre-requisites:
- FFMPEG: https://ffmpeg.org/
- YT-DLP: https://github.com/yt-dlp/yt-dlp | pip install -U yt-dlp
- Python Requests: https://docs.python-requests.org/en/latest/ | pip install requests
- BeautifulSoup4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | pip install beautifulsoup4

# For FFMPEG Installation:
Check: https://ffmpeg.org/ for specifics or problems installing
1. Download latest full package from these: https://www.gyan.dev/ffmpeg/builds/ OR https://github.com/BtbN/FFmpeg-Builds/releases
2. Extract folder to downloads
3. Place "bin" folder into root C: Directory
4. Rename "bin" folder -> "ffmpeg"
5. Search "edit the system enviornment variables" in windows search bar
6. Click Advanced -> Enviornment Variables
7. Navigate to System variables
8. Locate PATH variable and click it
9. Click "New" and add ffmpeg to system enviornment variables -> "C:\ffmpeg\bin"
10. Check ffmpeg has been added to system enviornment variables by typing ffmpeg in command prompt

# Usage of Global DL
- Locate where the main "Global DL" file was saved
- Create a text file here called sites.txt [insert any YT-DL accepted sites here]
- Open a CMD prompt at the location (type cmd in filepath at the top of file explorer)
- Type "python main.py [Output File Save Location] [YT-DL accepted site list txt file location]"
- For YT-DL Accepted Site List go to: https://ytdl-org.github.io/youtube-dl/supportedsites.html and enter any you want to be able to download from in sites.txt
- Follow prompts in program
