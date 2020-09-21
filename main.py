import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

constituents_df = pd.read_csv('constituents_CSV.csv', parse_dates = True, index_col= 0)

sector_names = set(constituents_df['Sector'].tolist())
companies = constituents_df['Name'].to_dict()

# start = dt.datetime(2020, 7, 1)
# end =  dt.datetime(2020, 8, 1)

# for key in companies:
#     df = web.DataReader(key, 'yahoo', start, end)
#     title = '{}.csv'.format(key)
#     df.to_csv(title)


# Lines below will plot the Adj Close of the AAP data frame
#plt.plot(dfs['AAP_DF'].index,dfs['AAP_DF']['Adj Close'], label = 'AAP')
#plt.show()

# prints all of the Adj Close of every data frame BUT on a SEPARATE chart
#for key in dfs:
#    plt.plot(dfs[key].index, dfs[key]['Adj Close'], label=key)
#    plt.show()


class StockAnalysis:
    def __init__(self, one_large_df = pd.DataFrame()):
        self.one_large_df = one_large_df

    def create_df(self):
        for key in companies:
            file = '{}.csv'.format(key)
            stock_df = pd.read_csv(file, index_col=0, parse_dates=True)
            # stock_df.insert(len(stock_df.columns),'Ticker', [key], True)
            self.one_large_df.append(stock_df)

    @staticmethod
    def pick_sector():

        for values in sector_names:
            print(values, sep='\n')

        sector_choice = input('Please enter which sector you would like to analyze: ')
        sector_choice = sector_choice.lower()
        sector_companies = []

        for index, row in constituents_df.iterrows():
            if row['Sector'] == sector_choice:
                in_the_sector = row['Symbol']
                sector_companies.append(in_the_sector)

    # def plot_sector(self):
    #     temp_df = pd.DataFrame()
    #     for index, row in one_large_df.iterrows():
    #         if row['Ticker'] in sector_companies:
    #             plt.plot(one_large_df['Adj Close'], label = )
    #             plt.show()

    @staticmethod
    def daily_best(one_large_df):
        one_large_df['Daily Return'] = one_large_df['Adj Close'].pct_change()
        column = one_large_df['Daily Return']
        max_value = column.max()
        return max_value

# -------- L O G I C --------

analysis = StockAnalysis()

analysis.create_df()

print(one_large_df)

analysis.pick_sector()
# if __name__ == '__main__':