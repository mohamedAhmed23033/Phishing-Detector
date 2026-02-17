import tkinter as tk
from tkinter import messagebox
import tldextract  

def is_suspicious(url):
    suspicious_tlds = ['tk', 'ml', 'ga', 'cf', 'gq']
    suspicious_words = ['login', 'bank', 'verify', 'account', 'update', 'secure']
    extract = tldextract.extract(url)
    tld = extract.suffix
    for word in suspicious_words:
        if word in url.lower():
            return True, f'كلمة مشبوهة: "{word}"'
    if tld in suspicious_tlds:
        return True, 'نطاق مشبوه'
    if any(short in url.lower() for short in ['bit.ly', 'tinyurl.com', 'goo.gl']):
        return True, 'رابط مختصر مشبوه'
    return False, 'الرابط يبدو آمناً'

def check_url():
    url = url_entry.get()
    suspicious, reason = is_suspicious(url)
    if suspicious:
        messagebox.showwarning("تحذير", f"الرابط مشبوه: {reason}")
        result_label.config(text=f"❗ الرابط مشبوه: {reason}", fg="#B71C1C", bg="#FFEBEE")
        result_frame.config(bg="#FFEBEE")
    else:
        messagebox.showinfo("معلومات", "الرابط يبدو آمناً")
        result_label.config(text="✔ الرابط يبدو آمناً", fg="#1B5E20", bg="#E8F5E9")
        result_frame.config(bg="#E8F5E9")

app = tk.Tk()
app.title("كشف روابط التصيد الاحتيالي")
app.geometry("600x350")
app.config(bg="#ECEFF1")

title_label = tk.Label(app, text="🔒 كشف روابط التصيد الاحتيالي", font=("Arial", 18, "bold"), bg="#ECEFF1")
title_label.pack(pady=15)

main_frame = tk.Frame(app, bg="#ECEFF1")
main_frame.pack(pady=10)

tk.Label(main_frame, text="أدخل الرابط:", font=("Arial", 14), bg="#ECEFF1").grid(row=0, column=0, sticky="w", padx=5)
url_entry = tk.Entry(main_frame, width=45, font=("Arial", 12))
url_entry.grid(row=1, column=0, padx=10, pady=8)

check_button = tk.Button(main_frame, text="تحقق من الرابط", command=check_url, font=("Arial", 13), bg="#0277BD", fg="#fff", height=2, width=20)
check_button.grid(row=2, column=0, pady=15)

result_frame = tk.Frame(app, bg="#ECEFF1", bd=2, relief="groove")
result_frame.pack(pady=10, fill="x", padx=25)

result_label = tk.Label(result_frame, text="", font=("Arial", 14), bg="#ECEFF1")
result_label.pack(pady=10, fill="x")

footer_label = tk.Label(app, text="تأكد دائماً من الروابط قبل إدخال بياناتك", font=("Arial", 11), bg="#ECEFF1", fg="#000000")
footer_label.pack(side="bottom", pady=9)

app.mainloop()