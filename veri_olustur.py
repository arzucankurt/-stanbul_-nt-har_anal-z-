# Bu dosya veri setini olusturur.
# 4 adet TÜİK Excel dosyasi -> 1 adet CSV (sadece İstanbul, 2009-2025).
# Calistirmak icin: python veri_olustur.py
# (Excel dosyalari bu dosyayla ayni klasorde olmali.)

import pandas as pd

ILK_YIL = 2009
SON_YIL = 2025


# --- Yardimci fonksiyonlar -------------------------------------------------

def yil_duzelt(deger):
    # TÜİK bazi yillari "2024(r)" seklinde yazmis. Ilk 4 karakteri alip sayiya ceviriyoruz.
    return int(str(deger)[:4])


def sayiya_cevir(tablo):
    # Excel'de "-" yazan hucreler "bilgi yok" demek. Bunlar sayiya cevrilemez,
    # errors="coerce" onlari bos (NaN) yapar.
    for sutun in tablo.columns:
        if sutun != "yil":
            tablo[sutun] = pd.to_numeric(tablo[sutun], errors="coerce")
    return tablo


def istanbul_oku(dosya, sutun_adlari, onek):
    # Yas ve sekil tablolari ayni düzende:
    # 1. sutun = yil, 2. sutun = il, 3. sutun = toplam, sonraki sutunlar = kategoriler.
    tablo = pd.read_excel(dosya, header=None)
    tablo[0] = tablo[0].ffill()                 # yil sadece ilk satirda yazili, asagi dogru doldur
    istanbul = tablo[tablo[1] == "İstanbul"].copy()
    istanbul = istanbul.iloc[:, [0] + list(range(3, 3 + len(sutun_adlari)))]
    istanbul.columns = ["yil"] + [onek + ad for ad in sutun_adlari]
    istanbul["yil"] = istanbul["yil"].apply(yil_duzelt)
    istanbul = istanbul[(istanbul["yil"] >= ILK_YIL) & (istanbul["yil"] <= SON_YIL)]
    return sayiya_cevir(istanbul)


# --- 1) Cinsiyet tablosu ---------------------------------------------------
# İl adinin yazdigi satir "Toplam", altindaki iki satir "Erkek" ve "Kadin".
cinsiyet_tablo = pd.read_excel("il_ve_cinsiyete_gore_intiharlar.xlsx", header=None)
yillar = [yil_duzelt(x) for x in cinsiyet_tablo.iloc[3, 2:]]   # 4. satirda yillar yaziyor

ist_satir = cinsiyet_tablo[cinsiyet_tablo[0] == "İstanbul"].index[0]
tr_satir = cinsiyet_tablo[cinsiyet_tablo[0] == "Türkiye"].index[0]

cinsiyet = pd.DataFrame({
    "yil": yillar,
    "istanbul_toplam": cinsiyet_tablo.iloc[ist_satir, 2:].values,
    "istanbul_erkek": cinsiyet_tablo.iloc[ist_satir + 1, 2:].values,
    "istanbul_kadin": cinsiyet_tablo.iloc[ist_satir + 2, 2:].values,
    "turkiye_toplam": cinsiyet_tablo.iloc[tr_satir, 2:].values,
})
cinsiyet = sayiya_cevir(cinsiyet)

# --- 2) Kaba hiz tablosu (100 bin kisiye dusen intihar) --------------------
hiz_tablo = pd.read_excel("illere_gore_kaba_intihar_hizi.xlsx", header=None)
hiz = pd.DataFrame({
    "yil": [yil_duzelt(x) for x in hiz_tablo.iloc[4, 1:]],
    "istanbul_hiz": hiz_tablo[hiz_tablo[0] == "İstanbul"].iloc[0, 1:].values,
    "turkiye_hiz": hiz_tablo[hiz_tablo[0] == "Türkiye"].iloc[0, 1:].values,
})
hiz = sayiya_cevir(hiz)

# --- 3) Yas ve sekil tablolari ---------------------------------------------
yas = istanbul_oku(
    "il_ve_yas_grubuna_gore_intiharlar.xlsx",
    ["0_14", "15_19", "20_24", "25_29", "30_34", "35_39", "40_44", "45_49",
     "50_54", "55_59", "60_64", "65_69", "70_74", "75_ustu", "bilinmeyen"],
    "yas_",
)
sekil = istanbul_oku(
    "il_ve_sekle_gore_intiharlar.xlsx",
    ["asarak", "kimyevi_madde", "yuksekten_atlayarak", "suya_atlayarak", "atesli_silah",
     "yakarak", "kesici_alet", "dogalgaz_tupgaz", "arac_altina_atlayarak", "diger"],
    "sekil_",
)

# --- 4) Hepsini "yil" sutununa gore birlestir ------------------------------
veri = cinsiyet.merge(hiz, on="yil")
for parca in [yas, sekil]:
    veri = veri.merge(parca, on="yil")

veri = veri[(veri["yil"] >= ILK_YIL) & (veri["yil"] <= SON_YIL)]
veri = veri.sort_values("yil").reset_index(drop=True)

veri.to_csv("istanbul_intihar_2009_2025.csv", index=False)
print("Tablo boyutu (satir, sutun):", veri.shape)
print(veri[["yil", "istanbul_toplam", "istanbul_hiz", "turkiye_hiz"]].head())
