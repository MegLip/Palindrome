# palindromy - Moduł 4.2

#No 1
def palindrome(sentence):                                      #1 Definicja funkcji
    new = sentence.lower().replace(" ","").replace(",","")     #2 Małe litery, pomienięcie spacji i przecinków
    if new == new[::-1]:                                       #3 Odwrócone litery
        return True
    else:
        return False
print(palindrome("Kobyła ma mały bok,,,"))                     #4 Sprawdź palindrom
print(palindrome("Ala ma kota"))

#No 2
def palindrome2(sentence2):
    new2 = [litera for litera in sentence2.lower() if litera.isalpha()]        #5 Wersja No2 z metodą isalpha()
    print(new2)
    if new2 == new2[::-1]:
        return True
    else:
        return False
print(palindrome2("Rats live on no evil star"))
print(palindrome2("Madam, I'm Adam"))
print(palindrome2("Ada jodu dojada!!!"))
