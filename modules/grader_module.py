import customtkinter as ctk
def select_grader(root_window):
    grade_wind = ctk.CTkToplevel(root_window)
    grade_wind.title('Оцінювач оцінки.')
    grade_wind.geometry('300x100')
    grade_wind.resizable(False, False)

    # Create CustomTkinter variable
    var = ctk.DoubleVar()

    # Create CTkSlider widget
    slider = ctk.CTkSlider(grade_wind, from_=1, to=12, orientation='horizontal', variable=var, number_of_steps=11)
    slider.pack(pady=10)

    number_label = ctk.CTkLabel(grade_wind, text='Введіть свою оцінку.')
    number_label.pack(pady=1)

    # Create label to display grade
    grade_label = ctk.CTkLabel(grade_wind, text='')
    grade_label.pack(pady=10)

    def get_value():
        value = var.get()
        if value == 1:
            grade_label.configure(text='Ну... В розробника нема ідей що тут написати')
            number_label.configure(text=value)
        elif 2 <= value <= 4:
            grade_label.configure(text='Ну як мінімум краще ніж 1.')
            number_label.configure(text=value)
        elif 5 <= value <= 7:
            grade_label.configure(text='Можна краще.')
            number_label.configure(text=value)
        elif 8 <= value <= 10:
            grade_label.configure(text='Молодець.')
            number_label.configure(text=value)
        elif 11 <= value <= 12:
            grade_label.configure(text='Молодчинка!!!')
            number_label.configure(text=value)

    slider.bind('<ButtonRelease-1>', lambda event: get_value())
    grade_wind.mainloop()