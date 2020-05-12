# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p = (df['fico']>700).value_counts()
print(p)
p_a = float(5357/9578)
total = df['purpose'].value_counts().sum()
print(total)
df1 = df['purpose'].value_counts()
print(df1)
p_b = float(3957 / 9578)
p_a_b = p_a
result = p_a_b != p_a
# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
prob_cs = df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
new_df = df[df['paid.back.loan']=='Yes']
prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
bayes = float(prob_pd_cs*prob_lp / prob_cs)
print(bayes)

# code ends here


# --------------
# code starts here
pur = df['purpose'].value_counts()
pur.plot(kind = 'bar')
df1 = df[df['paid.back.loan']=='No']
df1.plot(kind = 'bar')
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
plt.hist(df.installment, bins=40)
plt.plot([inst_median]*300, range(300), label='median')
plt.plot([inst_mean]*300, range(300), label='mean')

# code ends here


