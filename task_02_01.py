#!/usr/bin/python3.5

def is_palindrome(s):
    s = s.lower().replace(' ', '').replace(',', '').replace('.','').replace('!','').replace('?','')
    rev_s = ''.join(reversed(s))
#   if s == rev_s:
#        print('Yes')
#    else:
#        print('No')
    return s == rev_s
