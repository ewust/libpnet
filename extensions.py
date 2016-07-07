#!/usr/bin/python

import csv

with open('tls-extensiontype-values-1.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in r:
        try:
            num = int(row[0])

            print '    pub const %s: u16be = 0x%04x;' % (row[1], num)
        except ValueError:
            continue
