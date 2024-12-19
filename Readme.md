# DOWNLOAD YT SONG CLOUDSHELL WEBSITE
This repository contains a simple, user-friendly web application for downloading songs using yt-dlp, a powerful tool for downloading videos and audio from various platforms. The application is hosted using Serveo to make it accessible over the internet without complex server setup.

# Features:
>video  Downloads: Easily download vidz files from popular platforms
>Audio Downloads: Easily download audio files from popular platforms.
>yt-dlp Integration: Reliable and fast downloads powered by yt-dlp.
>Minimalistic UI: Clean and intuitive interface for a hassle-free user experience.
# Use Cases:
> Download songs for offline listening.
> Streamline access to audio content using a lightweight, web-based solution.
# Requirements:
> Python 3.x
> yt-dlp installed (pip install yt-dlp)
# Setup Instructions:

Clone the repository.
```
$ git clone https://github.com/Dot-ser/SongDL
```
#Build
```
pip install -r requirements.txt
```
# Run
```
python3 app.py
```
# OR

```
gunicorn app:app
```
> May required To add You cookies a cookies.txt
> > 1. Go to browser 
> > 2. Go to youtube.com and login with fake account
> > 3. Via using cookies editor extenion ,Export as Netscope format 
> > 4. Save and cookies.txt and Upload to github respo Root
# For Google CouldShell Depoly




## Setup Instructions:
Generate SSH KEY for Serveo
```
$ ssh-keygen
```
serveo.net  authentication for subdomain
```
$ ssh -R your-domain.com:80:localhost:5000 serveo.net
```

Clone the repository.
```
$ git clone https://github.com/Dot-ser/SongDL
```
> install the required dependencies using 
```
$ bash run.sh
```
> > No cookies required
> install the required dependencies using 
>TIME TO ENJOY ! SpotDL
