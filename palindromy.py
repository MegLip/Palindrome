# palindromy - Moduł 4.2

def palindrome(string):        #commit1 Definicja funkcji 
    '''
    * Definiujemy funkcję sprawdzającą czy dany wyraz jest palindromem (Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo).
    * Tworzymy zmienną string, dla której podajemy wyraz, który chcemy sprawdzić.
    * Odwracamy wszystkie litery wyrazu (string[::-1]) i porównujemy oryginalny wyraz z odwróconym. Jeśli są sobie równe, wyraz jest palindromem.
    * Funkcja zwraca wartość True dla wyrazów, które są palindromem (bądź False, dla wyrazów, które palindromem nie są).
    '''
    if string == string[::-1]:    #commit2 Odwrócone litery
        return True
    else:
        return False
print(palindrome("level"))           #commit3 sprawdz palindrom
print(palindrome("kobylamamalybok"))
print(palindrome("nowytarggóryzakopanenapokazyróggratywon"))
