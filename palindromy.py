# palindromy - Moduł 4.2
def palindrome(string):      #commit1 Definicja funkcji 
    if string == string[::-1]:   #commit2 Odwrócone litery
        return True
    else:
        return False
print(palindrome("level"))        #commit3 sprawdz palindrom
