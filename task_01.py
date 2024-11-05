def type_of_string(string_before):
    string_before = ''


def is_palindrome(string):
    for letter in range(len(string)//2):
        if string[letter] != string[-letter]:
            print(0)
            break
        else:
            print(1)


word = input('Введите строку')
is_palindrome(word)
