1. Install python 3.10.7 (or any version of python from 3.8.x to 3.10.x), be sure to add python to PATH while installing it 

https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe

https://datatofish.com/add-python-to-windows-path/

2. Install Visual C++ Redistributable Packages for Visual Studio 2013

https://www.microsoft.com/en-eg/download/details.aspx?id=40784

3. Run install.requirements.bat

4. Install this Chrome extension

https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid

**and go to primevideo.com and download the cookies, rename the file to pv.txt and put it in the folder cookies**

4b. For Firefox use this addon

https://addons.mozilla.org/en-US/firefox/addon/cookies-txt-one-click/

5. To download the video you will need to get the asin for the video, use this userscript for getting it

https://greasyfork.org/en/scripts/381997-amazon-video-asin-display

6. In the script's folder three batches

**A. download.video.bat**

For downloading the video from primevideo.com use

`amazon.py -r pv -p pv -a amzn1.dv.gti.9ab600aa-6625-b547-cfc0-190e3ad8a27d --alang en --noAD --slang en -q 1080`

The downloads will be saved in the folder output.

For adding more options use the instructions in amazon.py, open the file with Notepad++.

**B. download.subtitles.bat**

For downloading only the subtitles from primevideo.com use

`amazon.py --subs --slang en -r pv -p pv -a amzn1.dv.gti.9ab600aa-6625-b547-cfc0-190e3ad8a27d`

change en to the language you need to download the subtitles in.

To download the subtitles in multiple languages from primevideo.com use

`amazon.py --subs --slang en,fr,it  -r pv -p pv -a amzn1.dv.gti.9ab600aa-6625-b547-cfc0-190e3ad8a27d`

**C. download.audio.bat**

For downloading only the audio from primevideo.com

`amazon.py -r pv -p pv -a amzn1.dv.gti.9ab600aa-6625-b547-cfc0-190e3ad8a27d --nosubs --novideo --keep --alang en --noAD`

change en to the language you need to download the audio in.

To download only the original audio from primevideo.com use

`amazon.py -r pv -p pv -a amzn1.dv.gti.9ab600aa-6625-b547-cfc0-190e3ad8a27d --nosubs --novideo --keep --original`

To download the audio in a specific bitrate use (choose from 128, 192, 224, 256, 384, 448, 640)

`amazon.py -r pv -p pv -a amzn1.dv.gti.9ab600aa-6625-b547-cfc0-190e3ad8a27d --nosubs --novideo --noAD --keep -qa 384`
