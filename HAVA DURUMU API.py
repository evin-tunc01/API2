import requests

def hava_durumu_bilgilerini_al(sehir, api_anahtari):
   
    url = f'https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_anahtari}'
    try:
       
        cevap = requests.get(url)
        cevap.raise_for_status() 

        
        veri = cevap.json()

     
        if veri.get("cod") != 200:
            raise ValueError(f"API hatası: {veri.get('message', 'Bilinmeyen hata')}")

       
        sehir_ad = veri.get("name", "Bilinmeyen Şehir")
        sicaklik = veri["main"].get("temp", "Bilgi Yok")
        hava_durumu = veri["weather"][0].get("description", "Bilgi Yok")

        print(f"{sehir_ad} için hava durumu:")
        print(f"Sıcaklık: {sicaklik}K")
        print(f"Hava Durumu: {hava_durumu.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"İstek Hatası: {e}")
    except ValueError as e:
        print(f"Değer Hatası: {e}")
    except KeyError as e:
        print(f"Key Hatası: JSON verisinde {e} anahtarı bulunamadı.")
    except Exception as e:
        print(f"Beklenmeyen Hata: {e}")


api_anahtari = "f1dd5df1f47f58e384cba2fa5e314553"  
sehir = "istanbul"

hava_durumu_bilgilerini_al(sehir, api_anahtari)
