import tkinter as tk
from datetime import datetime, timedelta

# Bayramlar (örnek)
holidays = {
    "01-01": "Yılbaşı",
    "23-04": "Ulusal Egemenlik ve Çocuk Bayramı",
    "19-05": "Atatürk'ü Anma, Gençlik ve Spor Bayramı",
    "30-08": "Zafer Bayramı",
    "29-10": "Cumhuriyet Bayramı"
}

# Şehirler ve UTC farkları
cities = {
    "Mekke": 3,
    "İstanbul": 3,
    "New York": -4,
    "Bakü": 4,
    "Londra": 0,
    "Sidney": 10
}

# Ana pencere
root = tk.Tk()
root.title("Çözüm Kurs - Modern Saat")
root.geometry("1400x700")  # Büyük pencere
root.configure(bg="white")
root.resizable(True, True)  # Büyütülebilir
# root.state('zoomed')  # İstersen tam ekran için açabilirsin

# Canvas ile nokta desenli arka plan
canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)
dot_size = 2
spacing = 25
for x in range(0, 1400, spacing):
    for y in range(0, 700, spacing):
        canvas.create_oval(x, y, x + dot_size, y + dot_size, fill="#e0e0e0", outline="#e0e0e0")

# Üst başlık
title_label = tk.Label(canvas, text="Çözüm Kurs", font=("Helvetica", 36, "bold"),
                       bg="white", fg="#333333")
title_label.place(relx=0.5, rely=0.03, anchor="n")

# Ana saat
main_clock = tk.Label(canvas, text="", font=("Helvetica", 70, "bold"),
                      bg="white", fg="#111111")
main_clock.place(relx=0.5, rely=0.18, anchor="n")

# Şehirler çerçevesi
city_frame = tk.Frame(canvas, bg="white")
city_frame.place(relx=0.5, rely=0.45, anchor="n")

city_labels = {}
date_labels = {}


def on_enter(e):
    e.widget.config(bg="#f0f0f0", fg="#111111")


def on_leave(e):
    e.widget.config(bg="white", fg="#222222")


for city in cities:
    frame = tk.Frame(city_frame, bg="white")
    frame.pack(side="left", padx=12)

    lbl = tk.Label(frame, text="", font=("Helvetica", 20, "bold"),
                   bg="white", fg="#222222", bd=2, relief="raised",
                   padx=20, pady=12)
    lbl.pack()
    lbl.bind("<Enter>", on_enter)
    lbl.bind("<Leave>", on_leave)
    city_labels[city] = lbl

    date_lbl = tk.Label(frame, text="", font=("Helvetica", 14), bg="white", fg="#555555")
    date_lbl.pack(pady=2)
    date_labels[city] = date_lbl

# Reklam alanı
ad_frame = tk.Frame(canvas, bg="#ffcc00", bd=2, relief="ridge")
ad_frame.place(relx=0.5, rely=0.7, anchor="n", width=800, height=60)
ad_label = tk.Label(ad_frame, text="Reklam Alanı - Sponsor Banner", font=("Helvetica", 16, "bold"),
                    bg="#ffcc00", fg="black")
ad_label.pack(expand=True, fill="both")

# Developer etiketi
developer_label = tk.Label(canvas, text="Developer: Mr.Cappy" " (Yusuf Asaf Uçak)",
                           font=("Helvetica", 14), bg="white", fg="#555555")
developer_label.place(relx=0.5, rely=0.93, anchor="n")


# Saat ve tarih güncelleme
def update_time():
    now = datetime.utcnow()
    main_clock.config(text=datetime.now().strftime("%H:%M:%S"))

    today_str = datetime.now().strftime("%d-%m")
    today_holiday = holidays.get(today_str, "Bugün özel gün yok")

    for city, offset in cities.items():
        city_time = now + timedelta(hours=offset)
        city_labels[city].config(text=f"{city}: {city_time.strftime('%H:%M:%S')}")
        date_labels[city].config(text=f"{city} Tarih: {city_time.strftime('%d-%m-%Y')} - {today_holiday}")

    root.after(1000, update_time)


update_time()
root.mainloop()