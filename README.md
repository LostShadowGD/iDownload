# iDownload
<img src="dl-logo.PNG" width="200" height="200"><br><br><br>

Python wrapper that downloads iPlayer and YouTube, using yt_dlp and get_iplayer!<br><br>

## Credits

get-iplayer from [get-iplayer/get-iplayer](https://github.com/get-iplayer/get_iplayer)
yt-dlp from [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp))

## Building

```
pyinstaller --noconfirm --onedir --windowed --icon "<path to file>/icon.ico" --name "iDownload" --add-data "<path>/dl-logo - hd.png;." --add-data "<path>/dl-logo.PNG;." --add-data "<path>/downloadBBC.png;." --add-data "<path>/downloadBTN.png;." --add-data "<path>/grad.png;." --add-data "<path>/grad2.png;." --add-data "<path>/icon.ico;." --add-data "<path>/paste.png;."  "<path to file>"
```