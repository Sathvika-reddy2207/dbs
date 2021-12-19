import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('customer_transactions.csv')
countries = np.unique(df['Transaction_Origin/Destination'].to_list())
acc_keys = np.unique(df['Account_Key'].to_list())
# inn, out, num_tranc
countries = np.unique(df['Transaction_Origin/Destination'].to_list())
ak_dict1 = {acc_key: [[0, 0] for _ in range(3)] for acc_key in acc_keys}

vals = df.values
for val in vals:
    ak = val[1]
    amnt = val[2]
    typ = val[3]
    month = int(val[5].split('/')[1]) - 1
    
    if typ == 'INN':
        ak_dict1[ak][month][0] += amnt
        ak_dict1[ak][month][0] += amnt
        
    elif typ == 'OUT':
        ak_dict1[ak][month][1] += amnt
        ak_dict1[ak][month][1] += amnt

final_ak_result1 = {ak: [None for _ in range(3)] for ak in ak_dict1.keys()}

for ak in ak_dict1.keys():
    for i in range(3):
        m = ak_dict1[ak][i]
        if (m[0] > 1000) or (m[1] > 800):
            final_ak_result1[ak][i] = 'high_risk'
        elif (600 < m[0] < 1000) or (500 < m[1] < 800):
            final_ak_result1[ak][i] = 'medium_risk'
        elif (m[0] < 600) or (m[1] < 500):
            final_ak_result1[ak][i] = 'low_risk'

x, y, colors = [], [], []
color_dict = {'high_risk': 'red', 'medium_risk': 'yellow', 'low_risk': 'green'}
for ak in final_ak_result1.keys():
    if 'high_risk' in final_ak_result1[ak]:
        color = color_dict['high_risk']
        res = 2
    elif 'medium_risk' in final_ak_result1[ak] and 'high_risk' not in final_ak_result1[ak]:
        color = color_dict['medium_risk']
        res = 1
    elif 'low_risk' in final_ak_result1[ak] and 'high_risk' not in final_ak_result1[ak] and 'medium_risk' not in final_ak_result1[ak]:
        color = color_dict['low_risk']
        res = 0
    x.append(ak)
    y.append(res)
    colors.append(color)
    
plt.scatter(x, y, color=colors)
plt.xticks(rotation='vertical')
plt.show()