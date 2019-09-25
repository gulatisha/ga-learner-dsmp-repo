# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",",skip_header = 1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data,new_record),axis =0)
#Code starts here
print(census)


# --------------
#Code starts here
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)
print("The maximum age in the dataset is ",max_age)
print("{0} is the minimum age in the dataset".format(min_age))
print("The median of the age is {0} and the standard deviation is {1}".format(age_mean,age_std))


# --------------
#Code starts here
race = census[:,2]
print(race)
race_0 = census[(census[:,2] == 0)]
race_1 = census[(census[:,2] == 1)]
race_2 = census[(census[:,2] == 2)]
race_3 = census[(census[:,2] == 3)]
race_4 = census[(census[:,2] == 4)]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

len_list = [len_0,len_1,len_2,len_3,len_4]
min_len = min(len_list)

minority_race = len_list.index(min_len)
print(minority_race)




# --------------
#Code starts here
senior_citizens = census[(census[:,0] > 60)]
working_hours_sum = np.sum((senior_citizens[:,6]),axis = 0)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print("The average working hours for senior citizens is {0} as per tyhe census data".format(avg_working_hours))


# --------------
#Code starts here
high = census[(census[:,1] > 10)]
low = census[(census[:,1] <= 10)]
avg_pay_high = np.mean((high[:,7]),axis = 0)
avg_pay_low = np.mean((low[:,7]),axis = 0)
print(avg_pay_high)
print(avg_pay_low)
if avg_pay_high > avg_pay_low:
    print("Better education leads to better pay for this dataset")
else:
    print("The dataset does not follow better education leads to better pay")



