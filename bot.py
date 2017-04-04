#!/usr/bin/python

import os
import argparse
from mastodon import Mastodon

parser = argparse.ArgumentParser()
parser.add_argument('file', help = 'Path to the list of phrases to toot. Will toot in line order. Required.')
parser.add_argument('--user', default = './usercred.txt', help = 'Path to the file containing your client ID and client secret. (default: %(default))')
parser.add_argument('--client', default = './clientcred.txt', help = 'Path to the file containing your access token. (default: %(default))')
parser.add_argument('--toot', help = 'Toot a single phrase.')
parser.add_argument('--debug', action = 'store_true', required = False, help = 'Outputs debug info to stdout. Optional')

args = parser.parse_args()

filename = os.path.abspath(args.file)
usercred = os.path.abspath(args.user)
clientcred = os.path.abspath(args.client)

if args.debug:
    print('Files:')
    print('\t' + filename)
    print('\t' + usercred)
    print('\t' + clientcred)

bot = Mastodon(
    client_id = clientcred,
    access_token = usercred)

if args.toot:
    print('Toot:')
    print('\t' + args.toot)
    bot.toot(args.toot)
else:
    lines = ''

    with open(filename, 'r')  as f:
        lines = f.readlines()

    print('Toot:')
    print('\t' + args.toot)
    bot.toot(lines[0])

    lines += [lines.pop(0)]

    with open(filename, 'w') as f:
        f.writelines(lines)
