# İstanbul İntihar İstatistikleri Analizi (2009-2025)

Ödev: TÜİK verileriyle İstanbul'daki intihar vakalarının analizi (Python, pandas, numpy, matplotlib).

**Hipotez:** "Anadolu Durgun, Metropol İnsanı Yorgun": İstanbul'un kaba intihar hızı Türkiye'den belirgin şekilde yüksektir.
**Sonuç:** Veri hipotezi desteklemiyor. İstanbul'un hızı 17 yılın 17'sinde Türkiye'nin altında.

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `115_analiz.ipynb` | Ana analiz defteri (açıklamalar + kod + grafikler) |
| `veri_olustur.py` | 4 Excel dosyasından CSV üretir |
| `istanbul_intihar_2009_2025.csv` | Analizde kullanılan birleşik veri (17 satır, 32 sütun) |
| `il_ve_cinsiyete_gore_intiharlar.xlsx` | TÜİK ham tablo: cinsiyet |
| `illere_gore_kaba_intihar_hizi.xlsx` | TÜİK ham tablo: kaba hız |
| `il_ve_yas_grubuna_gore_intiharlar.xlsx` | TÜİK ham tablo: yaş grubu |
| `il_ve_sekle_gore_intiharlar.xlsx` | TÜİK ham tablo: intihar şekli |

## Çalıştırma

```
pip install pandas numpy matplotlib openpyxl jupyter
python veri_olustur.py      # CSV'yi yeniden üretir (isteğe bağlı)
jupyter notebook            # 115_analiz.ipynb dosyasını açıp Run All
```

## Kaynak ve not

Kaynak: TÜİK İntihar İstatistikleri (https://veriportali.tuik.gov.tr/tr/press/58233), olay yerine göre tablolar.
Kaba hız yaş ve cinsiyete göre standartlaştırılmamıştır. Yaş ve şekil sonuçları vaka payıdır, risk oranı değildir.
Yardım için: 112 Acil Çağrı Merkezi.
