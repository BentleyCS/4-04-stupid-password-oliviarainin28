"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""

def stupidPassword(n: int, l: int):
    passwords = []
    letters = ("a","b","c","d","e","f","g","h","i")

    for num1 in range(1,n+1):
        for num2 in range(1, n+1):
            for i in range(0,l):
                letter1 = letters[i]
                for j in range(0,l):
                    letter2 = letters[j]
                    for num3 in range(1,n+1):
                        if num3 > num1 and num3 > num2:
                            newPassword = f"{num1}{num2}{letter1}{letter2}{num3}"

                            passwords.append(newPassword)
    return passwords

