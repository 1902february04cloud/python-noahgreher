#!/usr/bin/env python3
import string
def main():
        (reverse("melon"))
        acronym("Portable Network Graphics ")
        whichTriangle(3,4,5)
        whichTriangle(3,3,9)
        whichTriangle(3,3,3)
        scrabble('cabbage')
        armstrong(153)
        primeFactors(15001)
        pangram("The quick brown Fox jumps over the lazy dog")
        sort([2,4,5,1,3,1])
	evenAndOdd()
def reverse(str):
        reverse_string=''
        for letter in str:
                reverse_string=letter+reverse_string
        print(reverse_string)

def acronym(str):
#we split the string to iterate over each word with a for loop.
        TLA=''
        words=str.split()
        for word in words:
                if word[0]==word[0].upper():TLA=TLA+word[0]
        print(TLA)

def whichTriangle(sideOne,sideTwo,sideThree):
        def condition1():
                if sideOne==sideTwo:return(True)
                else:False
        def condition2():
                if sideOne==sideThree:return(True)
                else:False
        def condition3():
                if sideTwo==sideThree: return(True)
                else:False
        conditions=[bool(condition1()),bool(condition2()),bool(condition3())]
        print(conditions)
        if any(conditions):print(sideOne, sideTwo, sideThree,"this is an isoceles, having at least two equal sides")
        if all(conditions):print(sideOne, sideTwo, sideThree, "And it also is an equilateral triangle, having all sides equal")
        if not any(conditions):print(sideOne, sideTwo, sideThree, "Looks like this is a scalene triangle.")

def scrabble(word):
        word=word.upper()
        value_bank={"A":1,"E":1,"I":1,"O":1,"U":1,"L":1,"N":1,"R":1,"S":1,"T":1,"D":2,"G":2,"B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4,"W":4,"Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10}
        word_value=0
        for letter in word:
                word_value+=(value_bank[letter])
        print(word_value)


def armstrong(number):
        def total():
                x=list(str(number))
                y=len(x)
                for digit in x:
                        yield(int(digit)**y)
        summed=(sum(total()))
        if number==summed: print("Armstrong test of number ", number,"The result is: ", True)
        else: print("Armstrong test of number ", number,"The result is: ", False)

def primeFactors(number):

        
        def findDivisors(number):
                for i in range(0,number+1):
                               if i==0:continue
                               if (number/i)==int(number/i):yield(int(i))                     
                                #this findDivisors lists all the divisors of a number.
                                #primeTests tests these divisors, if they are prime.
        def primeCheck(number):
                for i in range(1,number+1):
                        if number/i==1 and number!=1:yield i
                        #The definition of prime encompases only being divisble by one and the number itself
                        if number/i==number and number!=1:yield i
                        #Hence we yield 1 and the number its self on the first 2 lines.
                        #also we do not want 1 included in the result since it can meet the first 2 conditions. So we omit it with number!=1
                        if number/i!=1 and number/i!=number and number/i==int(number/i):yield i
                        #any additional yields automatically disqualify the number from being prime.
                        #so quite simply, we check the len(primeCheck(number) and if len==2, then the number is prime

        for i in findDivisors(number):
                if len(list(primeCheck(i)))==2:print(i)
 
def pangram(sentence):
                sentence=sentence.lower()	
                def char_bank(sentence):
                        for char in sentence:
                                if char.isalpha():yield(char)

                if set(string.ascii_lowercase)==(set(char_bank(sentence))):
                        print("this is a pangram")
                print(bool(set(string.ascii_lowercase)==(set(char_bank(sentence)))))
def evenAndOdd():
	n=0
	while n<11:
                n+=1
                x=(input(("enter a number: ")))
                x=int(x)
                if x%2==0:even.write(str(x))
                if x%2==1:odd.write(str(x))



if __name__ == '__main__':
	main()

