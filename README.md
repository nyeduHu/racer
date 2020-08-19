# TypeRacer.com
Sziasztok! Gondolom YouTube-ról jöttél a kódért.
Minden itt van! :))

## Telepítés

Töltsd le a Python legújabb verzióját! (https://www.python.org/)

Ezek után:

 - pip install selenium

És készen is vagy!

## Futtatás

A mappába ahol van a kód, és a chromedriver.exe, ott nyiss egy cmd-t és írd be az alábbiakat:

 - py main.py
 
## Két karaker közötti idő változtatása
```python
  while not started:
    try:
        for letter in txt:
            driver.find_element_by_class_name('txtInput').send_keys(letter)
            sleep(0.05) # itt tudod változtatni, másodpercben.
        started = True
    except:
         pass
```
