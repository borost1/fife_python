

def convert_trading(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

    if kwargs['ice']:
        print('ICE feldolgozas')


convert_trading(ice=True, mcq=True, akarmilyen_nevet_adok_itt="tenyleg barmit megeszik")