# Palindromy - Moduł 4.2
def palindrome(string):      #commit1 Definicja funkcji 
    if string == string[::-1]:   #commit2 Odwrócone litery
        return True
    else:
        return False
string = "level"        #commit3 sprawdz palindrom
wynik = palindrome(string)
if wynik ==1:
  print(True)
else:
  print(False)
