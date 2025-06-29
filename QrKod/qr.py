import tkinter as tk
from tkinter import filedialog
import pyqrcode 
from pyqrcode import QRCode

#Temel kodlar
def qr_kodu_olustur():
    url = url_entry.get()

    if url:
        qr_url = pyqrcode.create(url)
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG files", "*.svg")])  #*.svg anlamı sadece kullanıcı SVG dosyası olarak kaydedebilir.
        if dosya_yolu:
            qr_url.svg(dosya_yolu, scale=8) # scale parametresi QR kodunun boyutunu ayarlar.
            durum_etiketi.config(text="QR kod başarıyla oluşturuldu ve kaydedildi.", fg="green")

#tasarım ayarları
pencere = tk.Tk()
pencere.title("QR Kod Oluşturucu")

etiket = tk.Label(pencere, text="Lütfen URL giriniz:")
url_entry = tk.Entry(pencere, width=50)
olustur_buton = tk.Button(pencere, text="QR Kodu Oluştur", command=qr_kodu_olustur) # QR kodunu oluşturmak için buton, command parametresi ile qr_kodu_olustur fonksiyonunu çağırır.
durum_etiketi = tk.Label(pencere, text="", fg="red") # Durum etiketini başlangıçta boş olarak ayarlıyoruz. Text boş bırakma nedeni başarılı kaydedildiğinde yukarıdaki durum_etiketi texti çalışacak.

#Bunlar pek kullanılmaz gridi kullanacağız.
# etiket.pack() # Etiket widget'ını pencereye ekliyoruz.
# url_entry.pack() # URL giriş alanını pencereye ekliyoruz.
# olustur_buton.pack() # QR kodunu oluşturmak için butonu pencereye ekliyoruz.
# durum_etiketi.pack() # Durum etiketini pencereye ekliyoruz. 

# Grid kullanarak pencereyi düzenliyoruz.
etiket.grid(row=0, column=0, padx=10, pady=10)
url_entry.grid(row=0, column=1, padx=10, pady=10) 
olustur_buton.grid(row=1, column=0, columnspan=2, pady=10) # Butonun grid düzeni (columnspan), iki sütun boyunca yayılacak şekilde ayarlanıyor.
durum_etiketi.grid(row=2, column=0, columnspan=2, pady=10)

pencere.mainloop() # Pencereyi sürekli açık tutmak için mainloop fonksiyonunu çağırıyoruz.


