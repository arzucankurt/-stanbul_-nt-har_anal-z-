# Metropol İnsanı Gerçekten Yorgun mu? İstanbul'un 17 Yıllık İntihar Verisi (2009-2025)

TÜİK verileriyle İstanbul'daki intihar vakalarının analizi. Python, pandas, numpy ve matplotlib ile hazırlandı; her adımı açıklayan, yeni başlayanlara göre yazılmış bir Jupyter defteridir.

**Hipotez:** "Anadolu durgun, metropol insanı yorgun": İstanbul'un kaba intihar hızı Türkiye'den belirgin şekilde yüksektir.

## Bulgular

- **Hipotez çürütüldü.** İstanbul'un hızı 17 yılın 17'sinde Türkiye'nin altında (ortalama 3,42 ve 4,39).
- **Cinsiyet:** Vakaların yaklaşık %78'i erkek; erkek/kadın oranı 2,7 ile 4,5 arasında dalgalanıyor.
- **Yaş:** Vakalar en çok 25-29 yaşta yoğunlaşıyor (vaka payıdır, risk oranı değildir).
- **Yöntem:** En sık şekil asarak (yaklaşık %48).
- **Neden:** TÜİK'in kayda geçirdiği nedenler arasında hastalık, 17 yılın 17'sinde ilk sırada (nedeni belli vakaların yaklaşık %58'i). Vakaların yaklaşık %56'sı "diğer" ya da "bilinmeyen" olarak kayıtlı, bu yüzden nedenle ilgili yorumlar temkinlidir.

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `115_analiz.ipynb` | Ana analiz defteri (açıklamalar + kod + grafikler) |
| `veri_olustur.py` | 5 Excel dosyasından CSV üretir |
| `istanbul_intihar_2009_2025.csv` | Analizde kullanılan birleşik veri (17 satır, 40 sütun) |
| `il_ve_cinsiyete_gore_intiharlar.xlsx` | TÜİK ham tablo: cinsiyet |
| `illere_gore_kaba_intihar_hizi.xlsx` | TÜİK ham tablo: kaba hız |
| `il_ve_yas_grubuna_gore_intiharlar.xlsx` | TÜİK ham tablo: yaş grubu |
| `il_ve_nedene_gore_intiharlar.xlsx` | TÜİK ham tablo: neden |
| `il_ve_sekle_gore_intiharlar.xlsx` | TÜİK ham tablo: intihar şekli |

## Çalıştırma

```
pip install pandas numpy matplotlib openpyxl jupyter
python veri_olustur.py      # CSV'yi yeniden üretir (isteğe bağlı)
jupyter notebook            # 115_analiz.ipynb dosyasını açıp Run All
```

## Kaynak ve notlar

Kaynak: TÜİK İntihar İstatistikleri (https://veriportali.tuik.gov.tr/tr/press/58233), olay yerine göre tablolar.
Kaba hız yaş ve cinsiyete göre standartlaştırılmamıştır. Yaş, şekil ve neden sonuçları vaka payıdır, risk oranı değildir.
Bu çalışma tanımlayıcıdır; nedensellik iddia etmez.

Kendiniz ya da çevrenizde biri için destek arıyorsanız 112 Acil Çağrı Merkezi'ni arayabilirsiniz.
