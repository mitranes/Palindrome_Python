class Palindrome_String:
    def __init__(self, str):
        self.str = str.casefold()

    def reverse_string(self):
        reverse_str = self.str[::-1]
        return reverse_str

    def is_equal(self):
        return self.reverse_string() == self.str

    def is_string_palindrome(self):
        print("Is " + self.str + " a palindrome? ",self.is_equal())
