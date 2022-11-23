#!/usr/bin/env python

import csv
import json
import codecs
from datetime import datetime


def get_data(csvFile):
    data = list()
    params = list()
    csvReader = csv.reader(codecs.iterdecode(csvFile, 'utf-8'))

    for row in csvReader:
        if not params:
            params = row
            print('skip')
            continue

        tmp = dict()
        for j in range(len(row)):
            tmp[params[j]] = row[j]

        if is_valid(tmp):
            data.append(row)

    return data


def save_data(data):
    dbFileName = 'db/bills.csv'
    with open(dbFileName, 'r') as fdr:
        dbData = fdr.readlines()

    newLines = list()
    for row in data:
        if row not in dbData:
            newLines.append(row)

    with open(dbFileName, 'a') as fda:
        for line in newLines:
            fda.write(','.join(line) + "\n")

    return newLines


def is_valid(row):
# 1. Значение sum является числом
# В датасете были как числа с разделителем ',' так и с разделителем '.'. Я сделал валидными оба
    try:
        #row['sum'] = row['sum'].replace(',', '.')
        float(row['sum'])
    except:
        print(f"DBG: invalid row: {row} #1 - sum is not a number")
        return False
# 2. В service не пусто ( пусто так же считается, если вместо текста знак “-”)
    if not row['service'] or row['service'] == '-':
        print(f"DBG: invalid row: {row} #2 - Bad empty service")
        return False
# 3. Корректная дата (дата считается корректной, если есть день, месяц и год).
    try:
        datetime.strptime(row['date'], "%d.%m.%Y")
    except ValueError:
        print(f"DBG: invalid row: {row} #3 - Invalid date")
        return False
# 4. №(номер счета) тип int
    try:
        int(row['№'])
    except:
        print(f"DBG: invalid row: {row} #4 - '№' is not int")
        return False
# 5. Указаны client_name и client_org
    if not row['client_name'] or not row['client_org']:
        print(f"DBG: invalid row: {row} #5 - Bad empty service")
        return False

    return True
