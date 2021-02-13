computers = {
    'comp1': {
        'Processor':'i5-10400F',
        'GPU':'GTX 1650',
        'Storage':'240GB SSD',
        'Price':799.99
    },

    'comp2': {
        'Processor':'i7-10700F',
        'GPU':'GTX 1660Ti',
        'Storage':'480GB SSD + 1TB HDD',
        'Price':1149.99
    },

    'comp3': {
        'Processor':'i5-10600KF',
        'GPU':'GTX 1660 SUPER',
        'Storage':'240GB SSD + 1TB HDD',
        'Price':949.99
    },

    'comp4': {
        'Processor':'i7-9700K',
        'GPU':'GTX 2080 SUPER',
        'Storage':'512GB SSD + 2TB HDD',
        'Price':1499.99
    }
}

for comp, info in computers.items():
    print(f"\nCPU: {info['Processor']}")
    gpu = info['GPU']
    storage = info['Storage']
    price = info['Price']

    print(f"\tGPU: {gpu}")
    print(f"\tStorage: {storage}")
    print(f"\tPrice: {price}")