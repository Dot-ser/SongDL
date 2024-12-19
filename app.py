from flask import Flask, render_template, request, send_file, redirect, url_for
import os
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
        resolution = request.form.get("resolution", "best")  # Default to "best" if not specified
        try:
            filename = download_media(query, format_type, resolution)
            return send_file(filename, as_attachment=True)
        except FileNotFoundError:
            return redirect(url_for("error_page", error_message="File not found"))
        except Exception as e:
            return redirect(url_for("error_page", error_message=str(e)))
    return render_template("index.html")

def download_media(query, format_type, resolution):
    cookies_path = "cookies.txt"

    ydl_opts = {
        "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
        "cookiefile": cookies_path,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
    }

    if format_type == "audio":
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    elif format_type == "video":
        if resolution == "360p":
            ydl_opts["format"] = "best[height=360]"
        elif resolution == "1080p":
            ydl_opts["format"] = "best[height=1080]"
        else:
            ydl_opts["format"] = "bestvideo+bestaudio/best"  # Default to best available

    if "http" in query:
        url = query
    else:
        with YoutubeDL({"quiet": True, "noplaylist": True}) as ydl:
            result = ydl.extract_info(f"ytsearch:{query}", download=False)
            url = result["entries"][0]["webpage_url"]

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)

        if format_type == "audio":
            file_path = os.path.splitext(file_path)[0] + ".mp3"

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")
        
        return file_path

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("error_page", error_message="404: Page not found"))

@app.route("/error")
def error_page():
    error_message = request.args.get("error_message", "An unknown error occurred.")
    return render_template("error.html", error_message=error_message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
