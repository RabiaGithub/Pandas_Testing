import pandas as pd
from decimal import Decimal

# data = {"A": ["A1","A2","A3","A4"],"B": ["B1","B2","B3","B4"],"C": ["C1","C2","C3","C4"],"D": ["D1","D2","D3","D4"],
#         "E": ["E1","E2","E3","E4"],"F": ["F1","F2","F3","F4"]}

#
# df = pd.DataFrame(data)
# print(df)
# result = (df.groupby(['A', 'B', 'C'],
#                      as_index=False).apply(lambda x: x[[col for col in df.columns
#                                                         if col not in ['A', 'B', 'C']]].to_dict('r'))
#           .reset_index().rename(columns={0: 'D'}))
#
# print(result)


data_items = [{'TechSpecCode': 'G3321-00.FS0', 'TechSpecName': 'Ink / OPP', 'MPG': '0010000240_02', 'MaterialCode': '2',
               'MaterialName': '2', 'ProductType': 'Rollstock', 'ProductSubType': 'Rollstock', 'CustomerItemNumber': '2',
               'MarketCode': 'BNA', 'CustomerCode': '0010004260', 'ParentCustomerCode': '0001550',
               'CustomerName': '3-I PHILIPPINES (0010004260)', 'ParentCustomerName': '3M CORP (0001550)',
               'MarketDescription': 'Bemis North America', 'UPCProductConfigurationId': 68463,
               'BatchDate': '2022-08-19:15:06:31', 'BatchID': '2022-08-19:15:06:31.PDLC.Elastic.dat',
               'RmrPrice': Decimal('0.044991'), 'UpcProductConfigurationId': 68463, 'UpcIdSoldTo': '68463_0010004260'},
              {'TechSpecCode': 'G3321-00.FS0', 'TechSpecName': 'Ink / OPP', 'MPG': '0010000240_02',
               'MaterialCode': '66', 'MaterialName': '2', 'ProductType': 'Rollstock', 'ProductSubType': 'Rollstock',
               'CustomerItemNumber': '95', 'MarketCode': 'BNA', 'CustomerCode': '0010004260',
               'ParentCustomerCode': '0001550', 'CustomerName': '3-I PHILIPPINES (0010004260)',
               'ParentCustomerName': '3M CORP (0001550)', 'MarketDescription': 'Bemis North America',
               'UPCProductConfigurationId': 68181, 'BatchDate': '2022-08-19:15:06:31',
               'BatchID': '2022-08-19:15:06:31.PDLC.Elastic.dat', 'RmrPrice': Decimal('0.044991'),
               'UpcProductConfigurationId': 68181, 'UpcIdSoldTo': '68181_0010004260'}]

# data_items = [{'TechSpecCode': 'G3321-00.FS0', 'TechSpecName': 'Ink / OPP', 'MPG': '0010000240_02', 'MaterialCode': '2',
#                'MaterialName': '2', 'ProductType': 'Rollstock', 'ProductSubType': 'Rollstock', 'CustomerItemNumber': '2',
#                'MarketCode': 'BNA', 'CustomerCode': '0010004260', 'ParentCustomerCode': '0001550',
#                'CustomerName': '3-I PHILIPPINES (0010004260)', 'ParentCustomerName': '3M CORP (0001550)',
#                'MarketDescription': 'Bemis North America', 'UPCProductConfigurationId': 68463,
#                'BatchDate': '2022-08-19:15:06:31', 'BatchID': '2022-08-19:15:06:31.PDLC.Elastic.dat',
#                'RmrPrice': 0.044991, 'UpcProductConfigurationId': 68463, 'UpcIdSoldTo': '68463_0010004260'},
#               {'TechSpecCode': 'G3321-00.FS0', 'TechSpecName': 'Ink / OPP', 'MPG': '0010000240_02',
#                'MaterialCode': '66', 'MaterialName': '2', 'ProductType': 'Rollstock', 'ProductSubType': 'Rollstock',
#                'CustomerItemNumber': '95', 'MarketCode': 'BNA', 'CustomerCode': '0010004260',
#                'ParentCustomerCode': '0001550', 'CustomerName': '3-I PHILIPPINES (0010004260)',
#                'ParentCustomerName': '3M CORP (0001550)', 'MarketDescription': 'Bemis North America',
#                'UPCProductConfigurationId': 68181, 'BatchDate': '2022-08-19:15:06:31',
#                'BatchID': '2022-08-19:15:06:31.PDLC.Elastic.dat', 'RmrPrice': 0.044991,
#                'UpcProductConfigurationId': 68181, 'UpcIdSoldTo': '68181_0010004260'}]

data = pd.DataFrame(data_items)
data = data.where(data.notnull(), None)
if not data.empty:
    data = (data.groupby(['TechSpecCode', 'TechSpecName', 'MPG'],
                         as_index=False).apply(lambda x: x[[col for col in data.columns
                                                            if col not in ['TechSpecCode', 'TechSpecName',
                                                                           'MPG']]].to_dict('r'))
            .reset_index().rename(columns={0: 'Materials'}))
    data = data.to_dict(orient='records')[0]
print(data)
