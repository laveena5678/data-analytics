from loading import data_load
from cleaning import cleaning
from visualization import visualization

def main():
    df=data_load("retail_store (1).csv")

    df=cleaning(df,"Price")

    visualization(df,"Product","Price")

    return df

if __name__=="__main__":
    main()