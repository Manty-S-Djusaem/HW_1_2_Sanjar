GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del GeekTech['bag']

GeekTech['address'] = 'Свердловский район'

new_contact_information_dict = {'phone': 996507052018, 'inst': 'GeekTech_kg'}
GeekTech.update(new_contact_information_dict)
GeekTech['courses'] = ['Android', 'Backend', 'Frontend', 'UX/UI', 'IOS', 'GeekCamp', 'Full stack']
GeekTech['courses'] = set(GeekTech['courses'])

for k, v in GeekTech.items():
    print(f'{k}: {v}')