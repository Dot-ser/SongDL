# DOWNLOAD YT SONG CLOUDSHELL WEBSITE
This repository contains a simple, user-friendly web application for downloading songs using yt-dlp, a powerful tool for downloading videos and audio from various platforms. The application is hosted using Serveo to make it accessible over the internet without complex server setup.

# Features:
>video  Downloads: Easily download vidz files from popular platforms
>Audio Downloads: Easily download audio files from popular platforms.
>yt-dlp Integration: Reliable and fast downloads powered by yt-dlp.
>Serveo Hosting: Seamlessly access the application via a public URL without additional hosting costs.
>Minimalistic UI: Clean and intuitive interface for a hassle-free user experience.
# Use Cases:
> Download songs for offline listening.
> Streamline access to audio content using a lightweight, web-based solution.
# Requirements:
> Python 3.x
> yt-dlp installed (pip install yt-dlp)
> SSH client for Serveo hosting
# Setup Instructions:
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
>TIME TO ENJOY ! SpotDL
