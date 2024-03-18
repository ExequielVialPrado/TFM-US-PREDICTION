from fredapi import Fred
from datetime import datetime
import yfinance as yf
import pandas as pd

now = datetime.now()
today = now.strftime('%d/%m/%Y')

fred = Fred(api_key='db75b2725b8810b367291d213affc7dd')

def download_fred(indicator): 

    df = fred.get_series(indicator, observation_start='1993-1-1', ts_frequency = 'm')
    print(df)
    df.to_excel(f'{indicator}.xlsx')
    return df


def download_yf(indicator): 

    df = yf.download(indicator, start='1993-01-01', interval='1mo')
    df.to_excel(f'{indicator}.xlsx')
    return df
    

indicators_fred = ['VIXCLS','UNRATE','CPIAUCNS','FEDFUNDS','T10Y2Y','USREC']
indicators_y = ['^GSPC']

'''
Unrate    -> mensual
SP50      -> diario sin fds
VIX       -> diario
CPIAUCNS  -> CPIAUCNS mensual
FEDFUNDS  -> mensual
T10Y2Y    -> mensual
USREC     -> mensual
'''

dataframes = {}
dataframe_monthly = pd.DataFrame()

for indicator in indicators_fred:
    serie= download_fred(indicator)
    df = pd.DataFrame({'Date':serie.index, 'Valor':serie.values})
    dataframes[indicator] = df
    dataframe_monthly[indicator] = df['Valor']

    print(dataframe_monthly)

for indicator in indicators_y:
    sp500 = download_yf(indicator)
    df_final = pd.DataFrame()
    df_final['Valor'] = sp500['Close']
    df_final.reset_index(inplace=True)
    print(df_final)





