import smtplib
import threading
from threading import Thread
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import tkinter as tk
from tkinter import ttk, messagebox
import re
import logging

logging.basicConfig(level=logging.INFO)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

class EmailSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Günlük E-posta Raporu Gönderici")
        self.dark_theme = tk.BooleanVar(value=False)

        self.init_gui()
        self.apply_theme()

    def init_gui(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0)

        labels = ["Gönderen E-posta:", "Şifre:", "Alıcı E-posta:", "Konu:", "İçerik:", "Gönderim Zamanı:"]
        self.entries = []

        for i, text in enumerate(labels):
            label = ttk.Label(self.main_frame, text=text)
            label.grid(row=i, column=0, sticky="w")
            if text == "İçerik:":
                entry = tk.Text(self.main_frame, height=8, width=40)
                entry.grid(row=i, column=1, padx=5, pady=5)
            elif text == "Gönderim Zamanı:":
                entry = self.create_time_picker(self.main_frame)
                entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            else:
                entry = ttk.Entry(self.main_frame)
                if text == "Şifre:":
                    entry.configure(show="*")
                entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        self.start_button = ttk.Button(self.main_frame, text="Başlat", command=self.start_schedule)
        self.start_button.grid(row=6, column=1, pady=10)
        
        self.dark_theme_checkbox = ttk.Checkbutton(self.main_frame, text="Dark Theme", variable=self.dark_theme, command=self.toggle_theme)
        self.dark_theme_checkbox.grid(row=7, column=0, columnspan=2, pady=10)

    def create_time_picker(self, parent):
        frame = ttk.Frame(parent)
        hours = [f"{i:02d}" for i in range(24)]
        minutes = [f"{i:02d}" for i in range(60)]

        self.hour_var = tk.StringVar(value=hours[0])
        self.minute_var = tk.StringVar(value=minutes[0])

        hour_combobox = ttk.Combobox(frame, textvariable=self.hour_var, values=hours, width=3)
        minute_combobox = ttk.Combobox(frame, textvariable=self.minute_var, values=minutes, width=3)

        hour_combobox.grid(row=0, column=0)
        ttk.Label(frame, text=":").grid(row=0, column=1)
        minute_combobox.grid(row=0, column=2)

        return frame

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def send_email(self):
        sender_email = self.entries[0].get()
        receiver_email = self.entries[2].get()
        password = self.entries[1].get()

        if not (self.validate_email(sender_email) and self.validate_email(receiver_email)):
            self.show_error("Geçersiz e-posta adresi.")
            return

        subject = self.entries[3].get()
        body = self.entries[4].get("1.0", tk.END)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            logging.info("E-posta başarıyla gönderildi!")
            self.show_info("Başarılı", "E-posta başarıyla gönderildi!")
        except smtplib.SMTPAuthenticationError:
            self.show_error("Kimlik doğrulama hatası. Lütfen e-posta ve şifrenizi kontrol edin.")
        except Exception as e:
            logging.error(f"E-posta gönderilemedi. Hata: {e}")
            self.show_error(f"E-posta gönderilemedi. Hata: {e}")
        finally:
            server.quit()

    def job(self):
        self.send_email()

    def start_schedule(self):
        send_time = f"{self.hour_var.get()}:{self.minute_var.get()}"

        try:
            schedule.every().day.at(send_time).do(self.job)
            self.show_info("Başlatıldı", f"E-posta her gün saat {send_time}'de gönderilecek.")
            self.run_scheduler()
        except Exception as e:
            logging.error(f"Geçersiz zaman formatı: {e}")
            self.show_error(f"Geçersiz zaman formatı: {e}")

    def run_scheduler(self):
        def run():
            while True:
                schedule.run_pending()
                time.sleep(1)

        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    def apply_theme(self):
        theme_color = "black" if self.dark_theme.get() else "white"
        text_color = "white" if self.dark_theme.get() else "black"
        
        self.root.tk_setPalette(background=theme_color, foreground=text_color)
        self.main_frame.configure(style="TFrame")

        for entry in self.entries:
            if isinstance(entry, tk.Text):
                entry.configure(bg=theme_color, fg=text_color)
            else:
                entry.configure(style="TEntry")

        for widget in self.main_frame.winfo_children():
            if isinstance(widget, ttk.Label) or isinstance(widget, ttk.Button) or isinstance(widget, ttk.Checkbutton):
                widget.configure(style="TButton" if isinstance(widget, ttk.Button) else "TLabel")
        
        style = ttk.Style()
        style.configure("TFrame", background=theme_color)
        style.configure("TLabel", background=theme_color, foreground=text_color)
        style.configure("TEntry", fieldbackground=theme_color, foreground=text_color)
        style.configure("TButton", background=theme_color, foreground=text_color)
        style.configure("TCheckbutton", background=theme_color, foreground=text_color)

    def toggle_theme(self):
        self.apply_theme()

    def show_info(self, title, message):
        self.root.after(0, lambda: messagebox.showinfo(title, message))

    def show_error(self, message):
        self.root.after(0, lambda: messagebox.showerror("Hata", message))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSchedulerApp(root)
    root.mainloop()
