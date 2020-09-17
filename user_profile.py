
# the list will be named as **user_info inside the function and to return from the function
def build_profile(first,last,**user_info):
    """when the function is being called,the dictionary will fill first & then others(first/last)"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('aminur','rahman',location = 'dhaka',field = 'CS')

print(user_profile)


# simplifying ..
def build_profile(**user_info):
    return user_info

user_profile = build_profile(location = 'dhaka',field = 'CS')

print(user_profile)