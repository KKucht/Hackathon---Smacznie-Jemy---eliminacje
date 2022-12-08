import numpy as np
import pandas as pd
from matplotlib import pyplot as plt




def main():
    name_of_file = "data/2021_CO_1g.csv"
    df = pd.read_csv(name_of_file)
    data_top = df.head()
    print(data_top)



if __name__ == "__main__":
    main()












