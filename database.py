import pandas
import pandas as pd
import os.path

import consts
import soldier


def init():
    if not os.path.isfile('database.csv'):
        with open('database.csv', 'w+') as file:
            data = {'mines': [], 'bushes': [], 'player': []}
            df = pandas.DataFrame(data)
            df.to_csv(file)



# database = open('database.csv', 'w+')
# database.close()
# df = pd.read_csv('database.csv')
# data = {'mines': consts.mine_locations, 'bushes': consts.bush_locations, 'player': soldier.location}
