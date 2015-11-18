
import json
from collections import OrderedDict

f = file('amzntinker.json')
data = json.load(f)
f.close()

ticks = OrderedDict()

for tick in data['ticks']:
    ticks[tick['date']] = tick['price']

output = {}
output['ticker'] = 'AMZN'
output['ticks'] = []

for tick in sorted(ticks):
    output['ticks'].append({'date':tick,'price':ticks[tick]})
