import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog
from pytube import YouTube

LANGUAGES = {
    "eng": {
        "insert_link": "Insert Youtube Link",
        "download_complete": "Download completed successfully!",
        "error": "Error",
        "select_quality": "Select Quality",
        "download_audio": "Download audio only",
        "select_folder": "Select Destination Folder",
        "downloading": "Downloading...",
        "enter_url": "Enter URL",
        "choose_lang": "Choose Language",
        "start_download": "Start Download",
        "pause": "Pause",
        "resume": "Resume"
    },
    "ua": {
        "insert_link": "Вставте посилання на Youtube",
        "download_complete": "Завантаження завершено успішно!",
        "error": "Помилка",
        "select_quality": "Виберіть Якість",
        "download_audio": "Завантажити лише аудіо",
        "select_folder": "Вибрати Папку Призначення",
        "downloading": "Завантаження...",
        "enter_url": "Введіть URL",
        "choose_lang": "Виберіть Мову",
        "start_download": "Почати Завантаження",
        "pause": "Пауза",
        "resume": "Продовжити"
    }
}

selected_language = "ua"  # Змінити на потрібну мову
lang = LANGUAGES[selected_language]

# Основна функція для завантаження відео
def select_yt_saver(root_window):
    def download_video():
        ytlink = link.get()
        try:
            ytObject = YouTube(ytlink, on_progress_callback=on_progress)
            if quality_choice.get() == "audio":
                stream = ytObject.streams.filter(only_audio=True).first()
            else:
                stream = ytObject.streams.filter(res=quality_choice.get(), mime_type="video/mp4").first()
            if stream:
                stream.download(output_path=destination_directory)
                title_insert_link_and_video_name.configure(text_color='white', text=ytObject.title)
                finishLabel.configure(text=lang["download_complete"])
            else:
                finishLabel.configure(text=f"{lang['error']}: {lang['select_quality']} {quality_choice.get()}", text_color='red')
        except Exception as e:
            finishLabel.configure(text=f"{lang['error']}: {str(e)}", text_color='red')

    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_progressbar = bytes_downloaded / total_size * 100
        per = str(int(percentage_progressbar))
        pPersentage.configure(text=per + '%')
        pPersentage.update()
        progressbar.set(float(percentage_progressbar) / 100)

    def select_destination_directory():
        global destination_directory
        destination_directory = filedialog.askdirectory(title=lang["select_folder"], initialdir="C:/")

    ctk.set_appearance_mode('System')
    ctk.set_default_color_theme('dark-blue')


    yt_saver_wind = ctk.CTkToplevel(root_window)
    yt_saver_wind.title('YouTube Downloader')
    yt_saver_wind.geometry('450x400')
    yt_saver_wind.minsize(450, 220)

    title_insert_link_and_video_name = ctk.CTkLabel(yt_saver_wind, text=lang['insert_link'])
    title_insert_link_and_video_name.pack()

    url_var = tk.StringVar()
    link = ctk.CTkEntry(yt_saver_wind, textvariable=url_var, width=400)
    link.pack(pady=3)

    quality_choice = tk.StringVar(value="1080p")
    quality_label = ctk.CTkLabel(yt_saver_wind, text=lang["select_quality"])
    quality_label.pack(pady=3)
    quality_menu = ctk.CTkOptionMenu(yt_saver_wind, variable=quality_choice, values=["1080p", "720p", "480p", "audio"])
    quality_menu.pack(pady=3)

    download_button = ctk.CTkButton(yt_saver_wind, text=lang['start_download'], command=download_video)
    download_button.pack(pady=3)
    select_destination_folder_button = ctk.CTkButton(yt_saver_wind, text=lang['select_folder'], command=select_destination_directory)
    select_destination_folder_button.pack(pady=3)

    finishLabel = ctk.CTkLabel(yt_saver_wind, text='')
    finishLabel.pack()

    pPersentage = ctk.CTkLabel(yt_saver_wind, text='0%')
    pPersentage.pack()
    progressbar = ctk.CTkProgressBar(yt_saver_wind, width=400)
    progressbar.set(0)
    progressbar.pack()

    yt_saver_wind.mainloop()