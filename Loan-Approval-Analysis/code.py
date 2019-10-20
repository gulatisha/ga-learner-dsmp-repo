# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path,sep = ',')
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)


# code ends here


# --------------
# code starts here

banks = bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
banks = banks.fillna(bank_mode)
for col in banks.columns:
    banks[col]=banks[col].fillna(bank_mode[col][0])
print(banks.isnull().sum())


# --------------
# Code starts here




avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)
# code ends here



# --------------
# code starts here




bank_approved_self_emp = banks[(banks['Self_Employed']== 'Yes') & (banks['Loan_Status']=='Y')]
loan_approved_se = len(bank_approved_self_emp)
bank_approved_not_self_emp = banks[(banks['Self_Employed']== 'No') & (banks['Loan_Status']=='Y')]
loan_approved_nse = len(bank_approved_not_self_emp)
percentage_se = (loan_approved_se/614)*100
percentage_nse = (loan_approved_nse/614)*100
print(percentage_se)
print(percentage_nse)



# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term = len(banks[loan_term >= 25])

print(big_loan_term)



# code ends here


# --------------
# code starts here
loan_groupby = pd.groupby(banks,by='Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)


# code ends here


