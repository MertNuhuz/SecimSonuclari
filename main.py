#Kütüphaneleri tanıyoruz.
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv') #okuyacağımız dataları import ediyoruz. Veriler: "veridefteri.com" dan alınmıştır.
istenilenSehir = float(input("Seçim Sonuçlarını görmek istediğiniz ilin plakasını giriniz: ")) #sonucu gösterilecek şehrin plakasını talep ediyoruz.
TotalSehir = data[(data['il_id']==istenilenSehir)] #verilerimizi istenilen şehir için filtreliyoruz.
SehirAdi=TotalSehir['il'].values.tolist() #pasta gösteriminin üzerinde yazması için listeye alıyoruz.
TotalSehirHayir = TotalSehir['hayir'].sum() #verideki toplam hayir sayisini alıyoruz
TotalSehirEvet = TotalSehir['evet'].sum() #verideki toplam evet sayisini alıyoruz


labels = 'Evet', 'Hayir' #pastadaki başlıkları tanımlıyoruz.
sizes = [TotalSehirEvet, TotalSehirHayir] #pastada gözükecek verileri tanımlıyoruz.

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("16 nisan 2018 " + SehirAdi[0]+ " Seçim Sonuçları") #dinamik olması için seçilen şehrin adını listeden basıyoruz.
plt.show() #oluşturduğumuz pastayı çıktı alıyoruz.