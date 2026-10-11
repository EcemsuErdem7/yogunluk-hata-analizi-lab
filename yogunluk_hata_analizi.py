"""
Proje Adı: Fizik Laboratuvarı - Yoğunluk ve Hata Yayılımı Analizi
Açıklama: Kumpas (uzunluk) ve Hassas Terazi (kütle) ölçümleri kullanılarak 
          dikdörtgen prizma ve silindir cisimler için yoğunluk hesaplanır; 
          cihaz hassasiyetleri göz önüne alınarak hata yayılımı (mutlak ve bağıl hata) 
          uygulanır.
"""

import math

def prizma_hata_analizi(a, b, c, m, delta_kumpas=0.01, delta_terazi=0.01):
    """
    Dikdörtgen Prizma İçin Yoğunluk ve Belirsizlik Hesaplaması
    ---------------------------------------------------------
    Formüller:
    - Hacim (V) = a * b * c
    - Yoğunluk (d) = m / V
    - Hacim Belirsizliği (ΔV) = √[ (b*c*Δa)² + (a*c*Δb)² + (a*b*Δc)² ]
    - Yoğunluk Belirsizliği (Δd) = √[ ( (1/V)*Δm )² + ( (-m/V²)*ΔV )² ]
    """
    V = a * b * c
    d = m / V
    
    delta_V = math.sqrt(
        ((b * c * delta_kumpas) ** 2) + 
        ((a * c * delta_kumpas) ** 2) + 
        ((a * b * delta_kumpas) ** 2)
    )
    
    kist_m = 1.0 / V
    kist_V = -m / (V ** 2)
    delta_d = math.sqrt(
        ((kist_m * delta_terazi) ** 2) + 
        ((kist_V * delta_V) ** 2)
    )
    
    bagil_hata = delta_d / d
    yuzde_hata = bagil_hata * 100
    
    return {
        "geometrik_sekil": "Dikdörtgen Prizma",
        "hacim": V,
        "yogunluk": d,
        "mutlak_hata": delta_d,
        "bagil_hata": bagil_hata,
        "yuzde_hata": yuzde_hata
    }


def silindir_hata_analizi(r, h, m, delta_kumpas=0.01, delta_terazi=0.01):
    """
    Silindir İçin Yoğunluk ve Belirsizlik Hesaplaması
    -----------------------------------------------
    Formüller:
    - Hacim (V) = π * r^2 * h
    - Yoğunluk (d) = m / V
    - Hacim Belirsizliği (ΔV) = √[ (2*π*r*h * Δr)² + (π*r² * Δh)² ]
    """
    V = math.pi * (r ** 2) * h
    d = m / V
    
    kist_r = 2 * math.pi * r * h
    kist_h = math.pi * (r ** 2)
    
    delta_V = math.sqrt(
        ((kist_r * delta_kumpas) ** 2) + 
        ((kist_h * delta_kumpas) ** 2)
    )
    
    kist_m = 1.0 / V
    kist_V = -m / (V ** 2)
    delta_d = math.sqrt(
        ((kist_m * delta_terazi) ** 2) + 
        ((kist_V * delta_V) ** 2)
    )
    
    bagil_hata = delta_d / d
    yuzde_hata = bagil_hata * 100
    
    return {
        "geometrik_sekil": "Silindir",
        "hacim": V,
        "yogunluk": d,
        "mutlak_hata": delta_d,
        "bagil_hata": bagil_hata,
        "yuzde_hata": yuzde_hata
    }


def sonuclari_yazdir(sonuc):
    """Hesaplanan sonuçları düzenli bir formatta konsola yazdırır."""
    print(f"==========================================")
    print(f" CİSİM: {sonuc['geometrik_sekil']}")
    print(f"==========================================")
    print(f" Hesaplanan Hacim (V)      : {sonuc['hacim']:.4f} cm³")
    print(f" Hesaplanan Yoğunluk (d)   : {sonuc['yogunluk']:.4f} g/cm³")
    print(f" Mutlak Hata (Δd)          : {sonuc['mutlak_hata']:.6f}")
    print(f" Bağıl Hata                : {sonuc['bagil_hata']:.6f}")
    print(f" Yüzde Hata (%)            : %{sonuc['yuzde_hata']:.4f}")
    print(f" Raporlanacak Sonuç        : ({sonuc['yogunluk']:.3f} ± {sonuc['mutlak_hata']:.3f}) g/cm³\n")


if __name__ == "__main__":
    print("\n--- FİZİK LABORATUVARI HATA ANALİZİ PROGRAMI ---\n")
    
    DELTA_KUMPAS = 0.01  # cm
    DELTA_TERAZI = 0.01  # g
    
    # Dikdörtgen Prizma Ölçüm Değerleri
    prizma_sonuc = prizma_hata_analizi(5.20, 3.10, 2.05, 42.50, DELTA_KUMPAS, DELTA_TERAZI)
    sonuclari_yazdir(prizma_sonuc)
    
    # Silindir Ölçüm Değerleri
    silindir_sonuc = silindir_hata_analizi(1.25, 6.00, 30.15, DELTA_KUMPAS, DELTA_TERAZI)
    sonuclari_yazdir(silindir_sonuc)
