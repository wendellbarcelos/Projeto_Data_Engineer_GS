import numpy as np
import pandas as pd

data = pd.read_csv('datasets/base_de_respostas_10k_amostra.csv')

print(data.head())
print('\n\n')

print(data.shape)


print('\n\n')
print(data[['Salary', 'SalaryType', 'ConvertedSalary']])


data['Salary'].fillna(0, inplace=True)
data['ConvertedSalary'].fillna(0, inplace=True)
print('\n')
print(data[['Salary', 'SalaryType', 'ConvertedSalary']])


data['ConvertedSalary'] = data['ConvertedSalary'] * 5.60
print('\n\nValores convertidos em R$')
print(data['ConvertedSalary'])


data['Salary'] = data['ConvertedSalary']/12
print('\n\nValores mensais convertidos em R$')
print(data['Salary'])


data['Respondent'] = [f'Respondente_{x}' for x in range(1,len(data)+1)]
print('\n\n')
print(data['Respondent'])


print('\n\n')
print(data['LanguageWorkedWith'])


data['LanguageWorkedWith'] = [str(x).split(';')[0] for x in data.LanguageWorkedWith]
print('\n\n')
print(data['LanguageWorkedWith'])


print('\n\n')
print(data['CommunicationTools'])


print('\n\n')
data['CommunicationTools'] = [str(x).replace("(", ";") for x in data.CommunicationTools]


data['CommunicationTools'] = [str(x).split(';')[0] for x in data.CommunicationTools]
print(data['CommunicationTools'])


# Exportando arquivo para uso no PostgreSQL

df = data[['Respondent', 'OpenSource', 'Hobby', 'ConvertedSalary', 'CommunicationTools', 'LanguageWorkedWith', 'OperatingSystem', 'CompanySize', 'Country']]

df.to_csv('carga_db.csv', sep=',', index=False)
