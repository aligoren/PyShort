# PyShort

## Python Url Shortener with BottlePy Framework

Python ve Bottle Framework Kullanılarak Basit URL Shortener

Projede hashids ve bottle kullanıldı. Veritabanı seçimi SQLite üzerinde gerçekleştirildi. Ancak Mongo ve MySQL ile de çalışabiliyor. Veritabanı ayarlarınızı ona göre yaparsınız.

MongoDB için PyPI Linki: [https://pypi.python.org/pypi/bottle-mongo/](https://pypi.python.org/pypi/bottle-mongo/)

Front-end kısmında ise Bootstrap ve JQuery Kullanıldı. Örnek olması açısından.

# Gereksinimler

```
hashids
bottle
```

# Nasıl Çalışır?

Çalışma işlemi için komut satırına `python PyShortUrl.py` yazmanız yeterli olacaktır.
Çalışma anında girilen URL hatalı ise dahili 404 döndürür.

# Ekran Görüntüleri

### URL Oluşturma Ekranı

![ss1.png](ss1.png)

### Hatalı ID Girilince

![ss2.png](ss2.png)
