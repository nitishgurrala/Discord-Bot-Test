from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'RGAPI-4cee2f90-t9cbd-490d-a169-63f1c2fec9bf'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'BlueDressCapital')
print(me)