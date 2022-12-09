import sys
import copy as cp
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, patches
import math


start_x = 496 # 18E
start_y = 261 # 54N
x_edge = 110
y_edge = 170

def get_coordinates_from_station(x,y):
    if x != 0:
        new_x = (x - 18)*x_edge + start_x
        new_y = (y - 54) * y_edge *(-1) + start_y
        return new_x, new_y
    else:
        return start_x, start_y

def init_stations():
    stations_file = "data/stacje.csv"
    df = pd.read_csv(stations_file)
    stations = df.set_index('Kod stacji').T.to_dict('list')
    for key in stations:
        x, y =  get_coordinates_from_station(stations[key][1],stations[key][0])
        stations[key][0] = x
        stations[key][1] = y
    return stations

def add_circle(ax,x,y):
    circle = patches.Circle((x, y), radius=10, color='green')
    ax.add_patch(circle)

def get_coordinates(stations,data_top):
    x = np.array([0]*(len(data_top.columns)-1), dtype=float)
    y = np.array([0]*(len(data_top.columns)-1), dtype=float)
    names = data_top.loc[0,:].values.tolist()
    names.pop(0)
    for i, name in zip(range(0,len(names)), names):
        x[i] = stations[name][0]
        y[i] = stations[name][1]
    return x, y

def get_dates(df):
    dates = df.iloc[:, 0].values.tolist()
    dates = dates[5:]
    for i in range(0, len(dates)):
        dates[i] = dates[i].split(" ")[0]
    return dates

def get_value(index,start,end,df):
    values = df.iloc[start:end, index].astype(float).values.tolist()
    values = [x for x in values if not(np.isnan(x))]
    if len(values) == 0:
        return np.nan
    return sum(values) / len(values)

def write(x,y,values,norms):
    for i in range(len(x)):
        if np.isnan(values[i]):
            continue
        color = 'black'
        if values[i] <= norms[0]:
            color = 'green'
        elif values[i] <= norms[1]:
            color = 'lime'
        elif values[i] <= norms[2]:
            color = 'yellow'
        elif values[i] <= norms[3]:
            color = 'orange'
        elif values[i] <= norms[4]:
            color = 'red'
        else:
            color = 'crimson'
        plt.scatter([x[i]], [y[i]],color=color,alpha=0.7,s=70)

def get_norms(substance):
    if substance == "PM10":
        return [20,50,80,110,150] #ug/m^3
    if substance == "NO2":
        return [40, 100, 150, 200, 400] #ug/m^3
    if substance == "CO":
        return [3,7,11,15,21] #mg/m^3

def get_substance(file_name):
    substance = cp.copy(file_name)
    return substance[5:-7]

def main(file_name: str):
    stations = init_stations()
    df = pd.read_csv("data/"+file_name,low_memory=False)

    x, y = get_coordinates(stations,df.head())

    dates = get_dates(df)

    substance = get_substance(file_name)
    norms = get_norms(substance)

    index = 0


    im = plt.imread("data/mapa.jpg")
    plt.imshow(im)

    while index < len(dates):
        date = dates[index]
        start = index + 5
        while index < len(dates):
            if dates[index+1] == date:
                index = index + 1
            else:
                break
        end = index + 5
        n = []
        for i in range(1,len(df.columns)):
            value = get_value(i,start,end,df)
            n.append(value)
        plt.title(substance, loc='left')
        plt.title(date, loc='right')
        plt.imshow(im)
        write(x,y,n,norms)
        plt.draw()
        plt.pause(0.0001)
        plt.clf()
        index += 1


if __name__ == "__main__":
    main(sys.argv[1])












