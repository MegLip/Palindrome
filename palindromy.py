# palindromy - Moduł 4.2
#
#    '''
#    * Definiujemy funkcję sprawdzającą czy dany wyraz/zdanie jest palindromem (Palindrom czytany od lewej do prawej i od prawej do lewej brzmi tak samo).
#    * Tworzymy zmienną, dla której chcemy sprawdzić czy nasz wyraz/zdanie jest palindromem.
#    * Odwracamy wszystkie litery zmiennej i porównujemy z wersją nieodwróconą. Jeśli są sobie równe, dany wyraz/zdanie jest palindromem.
#    * Funkcja jako wynik zwraca wartośc True lub False.
#    '''

def palindrome(word):                                        #1 Definicja funkcji 
    if word == word[::-1]:                                   #2 Odwrócone litery
        return True
    else:
        return False
print(palindrome("level"))                                   #3 Sprawdź palindrom
print(palindrome("ananas"))


def palindrome_s(sentence):                                  #4 Definicja funkcji
  new = sentence.lower().replace(" ","").replace(",","")     #5 Małe litery, pomienięcie spacji i przecinków
  if new[::1] == new[::-1]:                                  #6 Odwrócone litery
    return True
  else:
    return False
print(palindrome_s("Kobyła ma mały bok,,,"))                 #7 Sprawdź palindrom
print(palindrome_s("Ala ma kota"))
