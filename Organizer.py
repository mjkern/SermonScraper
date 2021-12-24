import pandas as pd

def main():
    # get the csv of scraped data into memory
    data = pd.read_csv('./output/outfile.csv')
    print(data)


if __name__ == '__main__':
    main()