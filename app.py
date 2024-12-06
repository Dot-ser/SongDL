from flask import Flask, render_template, request, redirect, send_file, url_for
import os
import subprocess
from yt_dlp import YoutubeDL

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        format_type = request.form["format"]
        try:
            filename = download_media(query, format_type)
            return send_file(filename, as_attachment=True)
        except FileNotFoundError:
            return "Error: File not found. Please try again.", 404
    return render_template("index.html")

def download_media(query, format_type):
    ydl_opts = {
        "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
    }
    if format_type == "audio":
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    elif format_type == "video":
        ydl_opts["format"] = "bestvideo+bestaudio/best"

    # Check if input is a URL or a search query
    if "http" in query:
        url = query
    else:
        with YoutubeDL({"quiet": True, "noplaylist": True}) as ydl:
            result = ydl.extract_info(f"ytsearch:{query}", download=False)
            url = result["entries"][0]["webpage_url"]

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)

        # Handle cases where extensions differ (e.g., .webm to .mp3)
        if format_type == "audio":
            file_path = os.path.splitext(file_path)[0] + ".mp3"

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")
        
        return file_path

@app.route("/kill", methods=["POST"])
def kill_server():
    subprocess.call(["pkill", "-f", "app.py"])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
