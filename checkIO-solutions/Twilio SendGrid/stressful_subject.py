#!/usr/bin/env checkio --domain=py run stressful-subject

# 
# END_DESC

def is_stressful(subj):
    """
        recognize stressful subject
    """
    return False

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')