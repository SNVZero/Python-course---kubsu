import xmltodict as xd


def main():
    id = ''
    pharmacyCount = 0
    evdayPhCount = 0
    fin = open('12 -2.osm', 'r', encoding='utf-8')
    dct = xd.parse((fin.read()))

    for node in dct['osm']['node']:
        if 'tag' in node and isinstance(node['tag'], list):
            for tag in node['tag']:
                if tag['@v'] == 'pharmacy':
                    pharmacyCount += 1
        elif 'tag' in node and isinstance(node['tag'], dict):
            if node['tag']['@v'] == 'pharmacy':
                pharmacyCount += 1

    for node in dct['osm']['way']:
        if 'tag' in node and isinstance(node['tag'], list):
            for tag in node['tag']:
                if tag['@v'] == 'pharmacy':
                    pharmacyCount += 1
        elif 'tag' in node and isinstance(node['tag'], dict):
            if node['tag']['@v'] == 'pharmacy':
                pharmacyCount += 1

    for node in dct['osm']['node']:
        if 'tag' in node and isinstance(node['tag'], list):
            for tag in node['tag']:
                if tag['@v'] == 'pharmacy':
                    for ophours in node['tag']:
                        if ophours['@v'] == '24/7':
                            evdayPhCount += 1
        elif 'tag' in node and isinstance(node['tag'], dict):
            if node['tag']['@v'] == 'pharmacy':
                id = node['@id']
            elif node['tag']['@v'] == '24/7' and node['@id'] == id:
                evdayPhCount += 1

    for node in dct['osm']['way']:
        if 'tag' in node and isinstance(node['tag'], list):
            for tag in node['tag']:
                if tag['@v'] == 'pharmacy':
                    for ophours in node['tag']:
                        if ophours['@v'] == '24/7':
                            evdayPhCount += 1
        elif 'tag' in node and isinstance(node['tag'], dict):
            if node['tag']['@v'] == 'pharmacy':
                id = node['@id']
            elif node['tag']['@v'] == '24/7' and node['@id'] == id:
                evdayPhCount += 1

    print("Количество аптек:", pharmacyCount)
    print("Количество круглосуточных аптек:", evdayPhCount)


if __name__ == '__main__':
    main()
