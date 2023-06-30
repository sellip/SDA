# Create a class for string operation. The class Constructor accepts a string
#
# Methods
#
# Get length of string
# Reverse the string
# if length > 5: get the first three characters
# if length > 6: get the last 4 characters
# returns character in a position. This method accepts int. if the inputted int is less than the length of the string, return the character in position [int], else return error
# Test
#
# Write test for all your methods

class Strings():

    def __init__(self, text):
        self.text = text

    def length(self):
        return len(self.text)

    def reverse(self):
        return self.text[::-1]

    def three_char(self):
        if len(self.text) > 5:
            return self.text[0:3:1]

    def four_char(self):
        if len(self.text) > 6:
            return self.text[-4:-1]


text = Strings("HaveANiceDay")
print(text.length())
print(text.reverse())
print(text.three_char())
print(text.four_char())
