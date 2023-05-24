import re
 
text = 'This is some text -- with punctuation.'
 
print(text)
print()
 
patterns = [
    r'^(?P<first_word>\w+)',
    r'(?P<last_word>\w+)\S*$',
    r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
    r'(?P<ends_with_t>\w+t)\b',
]
 
for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}'".format(pattern))
    print('  ', match.groups())
    print('  ', match.groupdict())
    print()

'''
This is some text -- with punctuation.

'^(?P<first_word>\w+)'
   ('This',)
   {'first_word': 'This'}

'(?P<last_word>\w+)\S*$'
   ('punctuation',)
   {'last_word': 'punctuation'}

'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)'
   ('text', 'with')
   {'t_word': 'text', 'other_word': 'with'}

'(?P<ends_with_t>\w+t)\b'
   ('text',)
   {'ends_with_t': 'text'}
'''