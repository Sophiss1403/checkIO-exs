#!/usr/bin/env checkio --domain=py run between-markers

'''
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:
The initial and final markers are always different. ok
If there is no initial marker, then the first character should be considered the beginning of a string.ok
If there is no final marker, then the last character should be considered the ending of a string.ok
If the initial and final markers are missing then simply return the whole string.ok
If the final marker comes before the initial marker, then return an empty string. ok
Input:Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output:A string.
Precondition:can't be more than one final marker and can't be more than one initial. Marker can't be an empty string
'''

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    if begin != '':
        start = text.find(begin) + len(begin)
    if end != '':
        finish = text.find(end)
    if begin not in text:
        start = 0
        finish = 2
    if end not in text:
        finish = text.index(text[-1]) + 1

    return text[start:finish]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
