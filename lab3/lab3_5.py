import pandas as pd

# water (GDP.FWTL)
# air_pol (ATM)
# cancer (DYN)
# gdp (GPD.MKTP)
# industry (IND)
# mortality (STA)
# tobacco (PRV)

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

    data[name] = df

