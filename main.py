import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

start_x = 496 # 18E
start_y = 261 # 54N
x_edge = 110
y_edge = 170

station = dict()

def render():
    pass

# init naszej stacji

# get stacji
def get_stations():
    pass

def main():
    #name_of_file = "data/2021_CO_1g.csv"
    station_file = "data/stacje.csv"
    df = pd.read_csv(station_file)



    df.set_index('ID').T.to_dict('list')

    data_top = df.head()

    im = plt.imread("data/mapa.jpg")
    implot = plt.imshow(im)
    plt.show()



if __name__ == "__main__":
    main()












