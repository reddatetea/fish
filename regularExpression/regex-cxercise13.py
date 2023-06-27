import re

int_string = '1 2 3 4 5'

def int_match_to_float(match_obj):
    return(match_obj.group('num')+'.0')

#注意重命名用的是大写P

pattern = r'(?P<num>[0-9]+)'
regexp = re.compile(pattern)

a = regexp.sub(int_match_to_float,int_string)
#a = regexp.sub(match_obj.group('num'),int_string)
print(a)