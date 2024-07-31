import customtkinter as ctk
from Solyanka.speedtest_module import select_speedtest
from Solyanka.yt_saver_module import select_yt_saver
from Solyanka.grader_module import select_grader

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')

root_window = ctk.CTk()
root_window.geometry('500x500')
root_window.minsize(500, 150)
root_window.title("Головне вікно")

select_program_label = ctk.CTkLabel(root_window, text='Виберіть потрібну вам програму.').pack()
button_select_speedtest = ctk.CTkButton(root_window, text='Speedtest', command=lambda: select_speedtest(root_window)).pack()
button_select_grade_wind = ctk.CTkButton(root_window, text='Оцінювач оцінки.', command=lambda: select_grader(root_window)).pack(pady=10)
button_select_yt_saver = ctk.CTkButton(root_window, text='Зберігач відео з Ютуб', command=lambda: select_yt_saver(root_window)).pack()

root_window.mainloop()