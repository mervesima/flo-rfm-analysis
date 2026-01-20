# flo-rfm-analysis
Python ve Pandas ile 20.000 müşterilik veri setinde RFM metrikleri üzerinden müşteri segmentasyonu ve veri analizi.
# 📊 FLO Müşteri Segmentasyonu ve RFM Analizi

Bu proje, 20.000 müşteriden oluşan bir veri seti üzerinde, müşteri sadakatini ve satın alma davranışlarını ölçümlemek amacıyla **RFM (Recency, Frequency, Monetary)** analizi metodolojisi kullanılarak geliştirilmiştir.

## 🚀 Proje Kapsamı
- **Veri Mühendisliği:** Online ve offline kanallardan gelen veriler birleştirilerek her müşteri için toplam harcama ve sipariş sayıları türetilmiştir.
- **RFM Skorlaması:** Müşterilerin son alışveriş tarihleri, alışveriş sıklıkları ve bıraktıkları toplam değere göre 1-5 arası puanlama yapılmıştır.
- **Müşteri Segmentasyonu:** Regex (Düzenli İfadeler) kullanılarak müşteriler; *Champions, At Risk, Hibernating* gibi 10 farklı stratejik segmente ayrılmıştır.

## 🛠️ Kullanılan Teknolojiler
- **Python:** Veri işleme ve algoritma kurgusu.
- **Pandas & Numpy:** Veri manipülasyonu.
- **Matplotlib:** Segment dağılımlarının görselleştirilmesi.

## 📂 Dosya Yapısı
- `final.py`: Analiz sürecinin tüm fonksiyonlarını içeren ana Python scripti.
- `flo_data_20k.csv`: 20.000 satırlık ham veri seti.
- `Odev_Fonksiyonel_Terminalli_Gorselli.ipynb`: Analizin adım adım raporlandığı ve görselleştirildiği Jupyter Notebook dosyası.

## 📊 Örnek Çıktı
Analiz sonucunda müşterilerin segment dağılımları grafiksel olarak raporlanmış ve pazarlama stratejilerine hazır hale getirilmiştir.
