from pandas import read_csv
if __name__ == '__main__':
    url = "https://pkgstore.datahub.io/core/exchange-rates/daily_csv/data/03e15e28c7eea87026fee299a8859e97/daily_csv.csv"
    dataset = read_csv(url,header=0)
    #print(dataset.head(10))
    dataset = dataset.set_index("Country")
    dataset1 = dataset.loc["Thailand":"Thailand",:]
    #print(dataset1.min())
    #print(dataset1.max())
    print(dataset1)
    #print(dataset1)