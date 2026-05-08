from statistics import variance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sympy import Indexed

np.random.seed(42)
num_students=300

student_ids=np.arange(1,num_students+1) #1,2,3,4,5
gender=np.random.choice(['male','female'],num_students) #random gender assign krya
department=np.random.choice(['CS','IT','EC','Mechanical'],num_students)
study_hours=np.random.normal(loc=5,scale=2,size=num_students)
attendance=np.random.normal(loc=80,scale=10,size=num_students)
marks=(
    study_hours *8 +
    attendance *0.4 +
    np.random.normal(0,5,num_students)
)
# Marks depend on:
# study hours
# attendance
# random noise



#Limit all value
study_hours=np.clip(study_hours,1,12) #kayo array,min,max
attendance = np.clip(attendance, 40, 100)
marks = np.clip(marks, 0, 100)

#convert it in clean values
study_hours=np.round(study_hours,1) #10.5,11.0,6.2
attendance = attendance.astype(int) #55,78,22
marks = marks.astype(int) #50,20,66,65


#outlier create kriye for tests
marks[5] = 10
marks[25] = 100
marks[100] = 5
marks[150] = 99

#dataframe
student_data= pd.DataFrame({

    'Student_ID':student_ids,
    'Gender':gender,
    'Department':department,
    'Study_Hours':study_hours,
    'Attendance':attendance,
    'Marks':marks
})
# student_data.to_csv('student_data.csv',index=False)


#printing data
# print(student_data.head())
# print(student_data.shape)
# student_data.info()
# print(student_data.describe())

#Question 1
mean_marks=np.mean(student_data['Marks'])
variance_marks=np.var(student_data['Marks'])
std_marks=np.std(student_data['Marks'])

# print(f"Mean: {mean_marks}")
# print(f"Variance: {variance_marks}")
# print(f"Standard Daviation: {std_marks}")



#Question 2:
#randome samplee of 30 students
sample_data=student_data['Marks'].sample(30)

sample_mean=np.mean(sample_data)
sample_variance = np.var(sample_data)
sample_std = np.std(sample_data)


# print("Sample Mean:", sample_mean)
# print("Sample Variance:", sample_variance)
# print("Sample Standard Deviation:", sample_std)

#CLT
sample_means=[]
for i in range(1000):
    sample=student_data["Marks"].sample(30,replace=True)
    mean = np.mean(sample)
    sample_means.append(mean) #darek mean ne ama append kryu

# plt.hist(sample_means,bins=20)
# plt.title("Central Limit Theoram")
# plt.xlabel("Sample Means")
# plt.ylabel("Frequency")
# plt.show()


#Estimated Mean Q3
estimated_mean = np.mean(student_data['Marks'])

# print("Estimated Mean:", estimated_mean) #Etle ej ke bhai real vadu mean em


#Question 4
t_statatic,p_value=stats.ttest_1samp(student_data['Marks'],75)


# print(f"T Test: {t_statatic}")
# print("P-Value:", p_value)


# if p_value < 0.05:
#     print("Reject Null Hypothesis")

# else:
#     print("Fail to Reject Null Hypothesis")


#Question 5
#One way ANOVA
cs_marks=student_data[
    student_data['Department']=='CS'
]['Marks']
it_marks = student_data[
    student_data['Department'] == 'IT'
]['Marks']


ec_marks = student_data[
    student_data['Department'] == 'EC'
]['Marks']


mechanical_marks = student_data[
    student_data['Department'] == 'Mechanical'
]['Marks']

f_stat, p_value = stats.f_oneway(
    cs_marks,
    it_marks,
    ec_marks,
    mechanical_marks
)

# print(f"F Test: {f_stat}")
# print(f"P value: {p_value}")


#Two way ANOVA
pivot_table=pd.pivot_table(
    student_data, #Data frame
    values='Marks',
    index='Department',
    columns='Gender'
)

# print(pivot_table)

#Question 6
#T Test

male_marks=student_data[
    student_data['Gender'] == 'male'
]['Marks']
female_marks=student_data[
    student_data['Gender'] == 'female'
]['Marks']

#ind means independent,two sample
t_statistic, p_value = stats.ttest_ind(
    male_marks,
    female_marks
)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

# Hypothesis decision

if p_value < 0.05:
    print("Reject Null Hypothesis")

else:
    print("Fail to Reject Null Hypothesis")