import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('customer_transactions.csv')
countries = np.unique(df['Transaction_Origin/Destination'].to_list())
acc_keys = np.unique(df['Account_Key'].to_list())
countries = np.unique(df['Transaction_Origin/Destination'].to_list())
ak_dict2 = {acc_key: {c: [0, 0] for c in countries} for acc_key in acc_keys}

vals = df.values
for val in vals:
    ak = val[1]
    amnt = val[2]
    typ = val[3]
    cou = val[4]
    
    if typ == 'INN':
        ak_dict2[ak][cou][0] += amnt
        
    elif typ == 'OUT':
        ak_dict2[ak][cou][1] += amnt

final_ak_result2 = {ak: {c: None for c in countries} for ak in ak_dict2.keys()}

for ak in ak_dict2.keys():
    for c in countries:
        m = ak_dict2[ak][c]
        
        if (m[0] > 1000) or (m[1] > 800):
            final_ak_result2[ak][c] = 'high_risk'
        elif (600 < m[0] < 1000) or (500 < m[1] < 800) and (final_ak_result2[ak][c] != 'high_risk'):
            final_ak_result2[ak][c] = 'medium_risk'
        elif (m[0] < 600) or (m[1] < 500) and (final_ak_result2[ak][c] != 'high_risk') and (final_ak_result2[ak][c] != 'medium_risk'):
            final_ak_result2[ak][c] = 'low_risk'
            
final_couts = {c: {'high_risk': [], 'medium_risk': [], 'low_risk': []} for c in countries}
for ak in final_ak_result2.keys():
    for c in countries:
        res = final_ak_result2[ak][c]
        if res == 'high_risk':
            final_couts[c]['high_risk'].append(ak)
        elif res == 'medium_risk':
            final_couts[c]['medium_risk'].append(ak)
        elif res == 'low_risk':
            final_couts[c]['low_risk'].append(ak)
            
print(final_couts)