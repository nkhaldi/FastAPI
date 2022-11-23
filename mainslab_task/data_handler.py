#!/usr/bin/env python

import csv
import json
import codecs
import datetime


def parse_csv(file):
    data = dict()
    csvReader = csv.DictReader(codecs.iterdecode(file, 'utf-8'))

    data = dict()
    for row in csvReader:
        if not is_valid(row):
            print(row)
            continue
        id = row['№']
        data[id] = row

    return data


def is_valid(row):
# 1. Значение sum является числом
# В датасете были как числа с разделителем ',' так и с разделителем '.'. Я сделал валидными оба
    try:
        row['sum'] = row['sum'].replace(',', '.')
        float(row['sum'])
    except:
        print("cp-1")
        return False
# 2. В service не пусто ( пусто так же считается, если вместо текста знак “-”)
    if not row['service'] or row['service'] == '-':
        print("cp-2")
        return False
# 3. Корректная дата (дата считается корректной, если есть день, месяц и год).
    try:
        datetime.datetime.strptime(row['date'], "%d.%m.%Y")
    except ValueError:
        print("cp-3")
        return False
# 4. №(номер счета) тип int
    try:
        int(row['№'])
    except:
        print("cp-4")
        return False
# 5. Указаны client_name и client_org
    if not row['client_name'] or not row['client_org']:
        print("cp-5")
        return False
    return True
