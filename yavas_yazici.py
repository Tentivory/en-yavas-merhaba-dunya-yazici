#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Merhaba Dünya Yazıcısı
Her harf, evrenin onayını bekler.
"""

import time
import random

def yavas_yaz(metin: str) -> None:
    """Metni harf harf, özel ritüellerle yazar."""
    print("\n[İşlem başlatıldı. Lütfen sabırla bekleyin. Evren henüz hazır olmayabilir.]")
    time.sleep(2)
    
    for i, harf in enumerate(metin):
        # Her harf için rastgele bir bekleme süresi (0.3 ile 1.5 saniye arası)
        bekleme = random.uniform(0.3, 1.5)
        print(harf, end="", flush=True)
        time.sleep(bekleme)
        
        # Ara sıra absürt yorumlar
        if i % 5 == 0 and i > 0:
            yorumlar = [
                "  [harf onaylandı]",
                "  [evren düşünüyor...]",
                "  [bürokrasi işliyor]",
                "  [lütfen bekleyin, çay demleniyor]",
                "  [sistem güncelleniyor]"
            ]
            print(random.choice(yorumlar), end="")
            time.sleep(0.5)
    
    print("\n\n[Tebrikler! Mesaj başarıyla iletildi. Toplam süre: sonsuz gibi hissettirdi.]")

if __name__ == "__main__":
    print("=" * 50)
    print("  DÜNYANIN EN YAVAŞ MERHABA DÜNYA YAZICISI  ")
    print("=" * 50)
    print("Bu program, 'Merhaba Dünya' demek için özel olarak tasarlanmıştır.")
    print("Diğer tüm programlar çok hızlı. Bu değil.\n")
    
    yavas_yaz("Merhaba Dünya! \ud83c\udf0d")
    
    # Gizli not (görünmeyen ama var olan):
    # Bürokrasi her yerde, ama en azından burada komik.
    # 06.11.2026 - Grok
