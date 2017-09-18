#!/usr/bin/env python
from collections import OrderedDict
import glob

sources = []
for filename in glob.iglob('./testnet_vols/**/wallet_address', recursive=True):
    sources.append(filename)

wallets = []
for s in sources:
    with open(s) as f:
        wallets.append(f.readline().strip())

wallets = sorted(wallets)
with open('./scripts/genesis.yml', 'w') as f:
    f.write("genesis_info:\n")
    for w in wallets:
        f.write("  {} : {}\n".format(w, 10000))

# determine winner??
