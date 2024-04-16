import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

files = {'air_pol': 'API_EN.ATM.PM25.MC.ZS_DS2_en_excel_v2_3588.xls',
         'water': 'API_ER.GDP.FWTL.M3.KD_DS2_en_excel_v2_3500.xls',
         'industry': 'API_NV.IND.TOTL.KD.ZG_DS2_en_excel_v2_2566.xls',
         'gdp': 'API_NY.GDP.MKTP.KD.ZG_DS2_en_excel_v2_67.xls',
         'cancer': 'API_SH.DYN.NCOM.ZS_DS2_en_excel_v2_3058.xls',
         'tobacco': 'API_SH.PRV.SMOK_DS2_en_excel_v2_3887.xls',
         'mortality': 'API_SH.STA.AIRP.MA.P5_DS2_en_excel_v2_3403.xls'}

data = {}
for name, file in files.items():
    df = pd.read_excel('xmls/' + file, sheet_name='Data', skiprows=3)
    df = df.drop(df.columns[[0, 2, 3]], axis=1)
    df = df.transpose()
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df = df.reset_index().rename(columns={'index': 'year'})
    df.columns.name = None

    data[name] = df

# country code
cc = 'USA'
# country data
cd = pd.DataFrame()

cd['year'] = pd.to_datetime(data['gdp']['year'])
for name, df in data.items():
    cd[name] = df[cc]

cd = cd.set_index('year')
cd.index = cd.index.year
for col in cd:
    cd[col] = pd.to_numeric(cd[col], errors='coerce')

cd_copy = cd.dropna(how='all')

excelWriter = pd.ExcelWriter(cc + '.xlsx')
cd_copy.to_excel(excelWriter, sheet_name='Sheet1', index=True)

plt.title('Heatmap of missing values')
sns.heatmap(cd.isnull(), cbar=False, cmap='RdYlGn_r')
plt.show()

missing = cd.isnull().sum() / cd.shape[0] * 100
missing = missing.round(0).astype(int)
print('Missing values percentage')
for key, value in missing.items():
    print(f'{key} - {value}%')
print()

threshold = len(cd.columns) * 0.35
cd_filt = cd.dropna(thresh=int(threshold))

threshold = cd.shape[0] * 0.35
cd_filt = cd_filt.dropna(axis='columns', thresh=int(threshold))

plt.title('Heatmap of missing values')
sns.heatmap(cd_filt.isnull(), cbar=False, cmap='RdYlGn_r')
plt.show()

missing = cd_filt.isnull().sum() / cd_filt.shape[0] * 100
missing = missing.round(0).astype(int)
print('Missing values percentage')
for key, value in missing.items():
    print(f'{key} - {value}%')
print()

cd_filt.to_excel(excelWriter, sheet_name='Sheet2', index=True)

sns.lineplot(data=cd_filt, markers=True)
plt.grid()
plt.show()

for col in cd_filt:
    if cd_filt[col].isnull().sum() > 0:
        y = cd_filt[col].dropna().values

        model = ARIMA(y, order=(3, 0, 1))
        model = model.fit()

        pred = model.predict(start=0, end=len(cd_filt[col]) - 1)
        cd_filt[col] = cd_filt[col].fillna(pd.Series(pred, index=cd_filt[col].index))

sns.lineplot(data=cd_filt, markers=True)
plt.grid()
plt.show()

cd_filt.to_excel(excelWriter, sheet_name='Sheet3', index=True)
excelWriter.close()