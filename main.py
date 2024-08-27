from Palindrome_String import Palindrome_String
class Palindrome:
    def __init__(self,x):
        self.x = x

    def reverse(self):
        reverseList = []
        num = self.x
        while num > 0:
            digit = num % 10
            reverseList.append(digit)
            num //= 10
        print("Reverse List is ", reverseList)
        return reverseList

    def getNumToList(self):
        numList = [int(i) for i in str(self.x)]
        print("The list from number is " + str(numList))
        return numList

    def isEqual(self,x,y):
        for i in range(len(x)):
            if x[i] != y[i]:
                return False
        return True

    def isPalindrome(self):
        if self.x < 0:
            print("This is not a palindrome.")
            return False
        numList = self.getNumToList()
        reverseList = self.reverse()
        print("Is this a palindrome? ", self.isEqual(numList,reverseList))


    #when file is run as a script, __name__ = __main__ and therefore it runs whatever is below.
    #When file is imported, then this is not automatically executed as it is when its a script from command line.
if __name__ == "__main__":
    p = Palindrome(122112210)
    p.isPalindrome()

    s = Palindrome_String("Ava")
    s.is_string_palindrome()




