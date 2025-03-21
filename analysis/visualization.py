import matplotlib.pyplot as plt

def visualization(df,column1,column):
    plt.bar(df[column1],df[column],color="Black")
    plt.xlabel(column1)
    plt.ylabel(column)
    plt.title("retail_data")
    plt.show()