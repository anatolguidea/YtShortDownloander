import yt_dlp
import tkinter as tk
from tkinter import messagebox
import os

# Create downloads directory if it doesn't exist
if not os.path.exists('downloads'):
    os.makedirs('downloads')

# GUI Setup
root = tk.Tk()
root.title("YouTube Shorts Downloader")

tk.Label(root, text="Paste Shorts URL:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

def download_shorts():
    url = entry.get()
    if not url.strip():
        messagebox.showwarning("Input Error", "Please enter a YouTube Shorts URL")
        return

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join('downloads', '%(title)s.%(ext)s')
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed:\n{e}")

tk.Button(root, text="Download", command=download_shorts).pack(pady=10)

root.mainloop()
