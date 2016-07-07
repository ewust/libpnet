#!/usr/bin/python

import csv

with open('tls-parameters-4.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in r:
        try:
            a, b = [int(x.replace('0x', ''),16) for x in row[0].split(',')]
            num = (a << 8) + b;

            print '    pub const %s: u16be = 0x%04x;' % (row[1], num)
        except ValueError:
            continue
