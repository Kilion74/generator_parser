import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
import csv

# pip install lxml

count = 1
while count <= 43:
    url = 'https://www.generatortut.ru/katalog/generatory/?page=2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    data = requests.get(url, headers=headers).text
    block = BeautifulSoup(data, 'lxml')
    heads = block.find('div', id='mse2_results').find_all('div',
                                                          class_='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12 ms2_product')
    print(len(heads))
    for i in heads:
        head = i.find_next('div', class_='p_as_h4')
        print(head.text.strip())
        name = (head.text.strip())
        params = i.find_next('div', class_='atrs').find_all('p')
        print(' '.join(params[0].text.strip().split()))
        param_1 = (' '.join(params[0].text.strip().split()))
        print(' '.join(params[1].text.strip().split()))
        param_2 = (' '.join(params[1].text.strip().split()))
        print(' '.join(params[2].text.strip().split()))
        param_3 = (' '.join(params[2].text.strip().split()))
        print(' '.join(params[3].text.strip().split()))
        param_4 = (' '.join(params[3].text.strip().split()))
        print(' '.join(params[4].text.strip().split()))
        param_5 = (' '.join(params[4].text.strip().split()))
        print(' '.join(params[5].text.strip().split()))
        param_6 = (' '.join(params[5].text.strip().split()))
        try:
            print(' '.join(params[6].text.strip().split()))
            param_7 = (' '.join(params[6].text.strip().split()))
        except:
            print('None')
            param_7 = 'None'
        cena = i.find_next('p', class_='price')
        print(cena.text.strip())
        price = (cena.text.strip())
        pix = i.find_next('div', class_='image').find('img').get('src')
        print('https://www.generatortut.ru' + pix)
        photo = ('https://www.generatortut.ru' + pix)
        print('\n')
        storage = {'name': name, 'price': price, 'param_1': param_1, 'param_2': param_2, 'param_3': param_3,
                   'param_4': param_4, 'param_5': param_5, 'param_6': param_6, 'param_7': param_7, 'photo': photo}
        fields = ['Name', 'Price', 'Param_1', 'Param_2', 'Param_3', 'Param_4', 'Param_5', 'Param_6', 'Param_7', 'Photo']
        with open('example.csv', 'a+', encoding='utf-16') as file:
            pisar = csv.writer(file, delimiter=';', lineterminator='\r')
            # Проверяем, находится ли файл в начале и пуст ли
            file.seek(0)
            if len(file.read()) == 0:
                pisar.writerow(fields)  # Записываем заголовки, только если файл пуст
            pisar.writerow(
                [storage['name'], storage['price'], storage['param_1'], storage['param_2'], storage['param_3'],
                 storage['param_4'], storage['param_5'], storage['param_6'], storage['param_7'], storage['photo']])
    count += 1
    print(count)
