import customtkinter as ctk
from speedtest import Speedtest
def select_speedtest(root_window):
    speedtest_wind = ctk.CTkToplevel(root_window)
    speedtest_wind.title("Speedtest")
    speedtest_wind.geometry('300x400')
    speedtest_wind.resizable(False, False)

    # Labels for displaying download and upload speeds
    download_label = ctk.CTkLabel(speedtest_wind, text="Download speed\n-", font=("Arial", 20))
    download_label.pack(pady=(50, 0))

    upload_label = ctk.CTkLabel(speedtest_wind, text="Upload speed\n-", font=("Arial", 20))
    upload_label.pack(pady=(10, 0))

    # Function to perform speed test
    def test():
        try:
            # Perform the test and get results
            s = Speedtest()
            s.download()
            s.upload()
            download_speed = round(s.results.download / (10 ** 6), 2)
            upload_speed = round(s.results.upload / (10 ** 6), 2)

            # Update labels with results
            download_label.configure(text=f"Download speed\n{download_speed} Mbps")
            upload_label.configure(text=f"Upload speed\n{upload_speed} Mbps")
            message_user_wait.configure(text='')
        except Exception as e:
            message_user_wait.configure(text=f'Error: {e}', text_color='red')

    # User message label
    message_user_wait = ctk.CTkLabel(speedtest_wind, text="Тест триває близько 10 секунд")
    message_user_wait.pack(pady=20)

    # Button to start the test
    button_start_test = ctk.CTkButton(speedtest_wind, text="Start test", command=test)
    button_start_test.pack(side=ctk.BOTTOM, pady=20)

    speedtest_wind.mainloop()
