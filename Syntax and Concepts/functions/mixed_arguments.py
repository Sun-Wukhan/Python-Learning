def user_profile(name, **details):
    print(f'profile: {name}')
    for key, value in details.items():
        print(f'{key}: {value}')
        

user_profile("navid", city="toronto", country="canada", age="30")