def car_profile(owner, **details):
    print(f'{owner}')
    for key, value in details.items():
        print(f'{key}: {value}')

car_profile("navid", make="Lexus", model="RC350", year="2021", whp=305)