import pandas as pd # write your code here
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)
general = pd.read_csv(r"C:\Users\Sviatlana Kash\Downloads\diles\general.csv")
prenatal = pd.read_csv(r"C:\Users\Sviatlana Kash\Downloads\diles\prenatal.csv")
sports = pd.read_csv(r"C:\Users\Sviatlana Kash\Downloads\diles\sports.csv")
# print(general.head(20))
# print(prenatal.head(20))
# print(sports.head(20))
prenatal.columns = ['Unnamed: 0', 'hospital', 'gender', 'age', 'height', 'weight', 'bmi',
       'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray',
       'children', 'months']
sports.columns = ['Unnamed: 0', 'hospital', 'gender', 'age', 'height', 'weight', 'bmi',
       'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray',
       'children', 'months']
hospital = pd.concat([general, prenatal, sports], ignore_index=True)
hospital.drop(columns=['Unnamed: 0'], inplace=True)
# print(hospital.sample(n=20, random_state=30))
hospital.dropna(axis=0, thresh=1, inplace=True)
hospital.replace(to_replace= 'female', value = 'f', inplace=True )
hospital.replace(to_replace= 'woman', value = 'f', inplace=True )
hospital.replace(to_replace= 'male', value = 'm', inplace=True )
hospital.replace(to_replace= 'man', value = 'm', inplace=True )
hospital['gender'].fillna('f', inplace=True)
df2 = pd.DataFrame(np.zeros((4, 4)), columns=list("ABCE"))
hospital['bmi'].fillna(0, inplace = True)
hospital['diagnosis'].fillna(0, inplace = True)
hospital['blood_test'].fillna(0, inplace = True)
hospital['ecg'].fillna(0, inplace = True)
hospital['ultrasound'].fillna(0, inplace = True)
hospital['mri'].fillna(0, inplace = True)
hospital['xray'].fillna(0, inplace = True)
hospital['children'].fillna(0, inplace = True)
hospital['months'].fillna(0, inplace = True)
# print('Data shape:', hospital.shape)
# print(hospital.sample(n=20, random_state=30))
# print(hospital.hospital.value_counts())
# print(hospital.groupby(['hospital']).diagnosis.value_counts())
# print(hospital.groupby(['hospital']). aggregate({'age': 'median'}))
# print(hospital.pivot_table(index = 'hospital',columns = 'blood_test', aggfunc = {'blood_test': 'count'}))
#
# print('The answer to the 1st question is general')
# print('The answer to the 2st question is 0.325')
# print('The answer to the 3st question is 0.285')
# print('The answer to the 4st question is 19')
# print('The answer to the 5st question is prenatal, 325 blood tests')
bins  = [0, 15, 35, 55, 70, 80]
plt.hist(hospital['age'], bins = bins)
plt.show()
hospital.diagnosis.value_counts().plot.pie()
plt.show()
data2 = hospital.loc[ hospital.hospital == 'prenatal', 'height']
data1 = hospital.loc[ hospital.hospital == 'general', 'height']
data3 = hospital.loc[ hospital.hospital == 'sports', 'height']
data_list = [data1, data2, data3]
fig, axes = plt.subplots()
axes.set_xticks((1, 2, 3))
axes.set_xticklabels(("general","prenatal","sports"))
plt.violinplot(data_list)
plt.show()




print('The answer to the 1st question: 15-35')
print('The answer to the 2nd question: pregnancy')
print("The answer to the 3rd question: It's because different unit of measurement of height")
