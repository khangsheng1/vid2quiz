import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from yt_dlp import YoutubeDL

def download_video():
    url = url_entry.get()
    resolution = resolution_var.get()
    audio_only = audio_var.get()
    output_folder = folder_path.get()

    if not url or not output_folder:
        messagebox.showerror("Error", "Please provide a URL and output folder.")
        return

    ydl_opts = {
        'format': f'bestaudio/best' if audio_only else f'bestvideo[height<={resolution}]+bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'noplaylist': True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# GUI setup
app = tk.Tk()
app.title("Video Downloader")
app.geometry("500x300")

tk.Label(app, text="Video URL:").pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

tk.Label(app, text="Resolution (max):").pack(pady=5)
resolution_var = tk.StringVar(value="1080")
ttk.Combobox(app, textvariable=resolution_var, values=["144", "360", "480", "720", "1080"]).pack(pady=5)

audio_var = tk.BooleanVar()
tk.Checkbutton(app, text="Audio Only", variable=audio_var).pack(pady=5)

tk.Label(app, text="Output Folder:").pack(pady=5)
folder_path = tk.StringVar()
tk.Entry(app, textvariable=folder_path, width=40).pack(pady=5)
tk.Button(app, text="Browse", command=select_folder).pack(pady=5)

tk.Button(app, text="Download", command=download_video).pack(pady=20)

app.mainloop()
