# palindromy - Moduł 4.2
#
#    '''
#    * Definiujemy funkcję sprawdzającą czy dany wyraz/zdanie jest palindromem (Palindrom czytany od lewej do prawej i od prawej do lewej brzmi tak samo).
#    * Tworzymy zmienną, dla której chcemy sprawdzić czy nasz wyraz/zdanie jest palindromem.
#    * Odwracamy wszystkie litery zmiennej i porównujemy z wersją nieodwróconą. Jeśli są sobie równe, dany wyraz/zdanie jest palindromem.
#    * Funkcja jako wynik zwraca wartośc True lub False.
#    * Korzystamy z metody str.replace(), str.lower(), str.isalpha().
#    '''

#No 1
def palindrome(sentence):                                    #1 Definicja funkcji
  new = sentence.lower().replace(" ","").replace(",","")     #2 Małe litery, pomienięcie spacji i przecinków
  if new == new[::-1]:                                       #3 Odwrócone litery
    return True
  else:
    return False
print(palindrome("Kobyła ma mały bok,,,"))                   #4 Sprawdź palindrom
print(palindrome("Ala ma kota"))

#No 2
def palindrome2(sentence2):                                 
    new2 = [litera for litera in sentence2.lower() if litera.isalpha()]        #5 Wersja No2 z metodą isalpha()
    print(new2)
    return new2 == new2[::-1]
    if new2 == new2[::-1]:
        return True
    else:
        return False
print(palindrome2("Rats live on no evil star"))
print(palindrome2("Madam, I'm Adam"))
print(palindrome2("Ada jodu dojada!!!"))
