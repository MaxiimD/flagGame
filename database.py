import pandas as pd
import os.path
import consts
import soldier


def init():
    if not os.path.isfile('database.csv'):
        with open('database.csv', 'w+') as file:
            df = pd.DataFrame(columns=['Mines', 'Bushes', 'Soldier'],
                              index=list(consts.NUMBER_KEYS_TIME_DICT.keys()))
            df.to_csv(file)


def save(key):
    df = pd.read_csv('database.csv', header=[0], index_col=[0], dtype='object')
    df.loc[key, ['Mines', 'Bushes', 'Soldier']] = [consts.mine_locations, consts.bush_locations, soldier.location]
    with open('database.csv', 'w+') as file:
        df.to_csv(file)


def load(key):
    df = pd.read_csv('database.csv', header=[0], index_col=[0])
    if not df.loc[key].isnull().values.any():
        consts.mine_locations = eval(df.loc[key, 'Mines'])
        consts.bush_locations = eval(df.loc[key, 'Bushes'])
        soldier.location = eval(df.loc[key, 'Soldier'])
