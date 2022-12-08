import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, patches

start_x = 496 # 18E
start_y = 261 # 54N
x_edge = 110
y_edge = 170



def get_coordinates(x,y):
    new_x = (x - 18)*x_edge + start_x
    new_y = (y - 54) * y_edge + start_y
    return new_x, new_y

def render():
    pass

# init naszej stacji
def init_stations():
    stations_file = "data/stacje.csv"
    df = pd.read_csv(stations_file)
    stations = df.set_index('Kod stacji').T.to_dict('list')
    return stations

# get stacji
def get_stations(name: str, stations):
    return stations[name]


def main():
    #name_of_file = "data/2021_CO_1g.csv"
    stations = init_stations()
    coordinates = get_stations('DsJelGorOgin',stations)
    print(coordinates)
    x , y = get_coordinates(coordinates[1],coordinates[0])
    print(x,y)
    #data_top = df.head()
    fig, ax = plt.subplots()
    im = plt.imread("data/mapa.jpg")
    implot = plt.imshow(im)

    circle1 = patches.Circle((200, 200), radius=100, color='green')

    ax.add_patch(circle1)
    plt.show()



if __name__ == "__main__":
    main()












