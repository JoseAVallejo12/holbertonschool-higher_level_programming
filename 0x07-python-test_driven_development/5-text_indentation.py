#!/usr/bin/python3
# jose vallejo <1545@holbertonschool.com>
"""
    create funtion that print swuare in # 
    @size must be only int
    Return: only print scuare by size*size in #
"""


def text_indentation(text):
    """
        function for split text givend
    """

    chr_match = ['.', '?', ':']
    new_str = ""
    if text:
        if type(text) is str:
            for i in text:
                new_str = new_str + i
                if i in chr_match:
                    print(new_str.strip())
                    print("")
                    new_str = ""
            print(new_str.strip(), end="")
        else:
            raise TypeError("text must be a string")
