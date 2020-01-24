# Using syntax: import module_name
import  profile_dictionary

user_profile = profile_dictionary.build_profile('albert', 'einstein',
							location='princeton',
							field='physics',)

print(user_profile)

print('1\n')

# Using syntax: from module_name import function_name
from profile_dictionary import build_profile

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics',)

print(user_profile)

print('2\n')

# Using syntax: from module_name import function_name as fn
from profile_dictionary import build_profile as bp 

user_profile = bp('albert', 'einstein',
							location='princeton',
							field='physics',)

print(user_profile)

print('3\n')

# Using syntax: import module_name as mn
import profile_dictionary as pd 

user_profile = pd.build_profile('albert', 'einstein',
							location='princeton',
							field='physics',)

print(user_profile)

print('4\n')

# Using syntax: from module_name import *
from profile_dictionary import *

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics',)

print(user_profile)