"""
1.
Create two NumPy arrays representing the daily step counts of two friends over a week and use element-wise addition, subtraction, multiplication, and division to compare their activity levels.
2.
Simulate a Spotify-like 'Recommended Songs' feature: Given two 3x3 matrices representing user-song interaction scores (user preferences and song popularity), use dot() and matmul() to compute the final recommendation matrix and explain the difference between the two results.
3.
Given a 4x4 NumPy matrix representing the pixel brightness of a small Instagram image, use transpose (T) to rotate the image and then calculate the mean, median, standard deviation, and variance of the pixel values.
4.
Take a 3x3 NumPy matrix representing a Zomato restaurant rating correlation grid and use np.linalg.inv(), np.linalg.det(), and np.linalg.eig() to compute its inverse, determinant, and eigenvalues/eigenvectors.<br><br><em><strong>Hint:</strong> If the matrix is not invertible, modify one value and try again.</em>
5.
Create a NumPy array of shape (2, 6) representing the number of orders placed on Swiggy in two cities over 6 days. Reshape it to (3, 4), flatten it, split it into two equal parts, and then stack both parts vertically.
"""

import numpy as np

"""
first_friend=np.array([5000,6000,5000,5500,6400,7800,9000],dtype="int64")
second_friend=np.array([5600,4500,7800,9800,4500,6000,10000],dtype="int64")

print(first_friend+second_friend)
print(first_friend-second_friend)
print(first_friend*second_friend)
print(first_friend/second_friend)


# User preferences matrix (3 users × 3 song features)
user_preferences = np.array([
    [5, 3, 1],
    [4, 2, 3],
    [1, 5, 4]
])

# Song popularity matrix (3 song features × 3 songs)
song_popularity = np.array([
    [2, 4, 1],
    [3, 1, 5],
    [4, 2, 3]
])

recommendation_dot = np.dot(user_preferences, song_popularity)

recommendation_matmul = np.matmul(user_preferences, song_popularity)

print("Recommendation Matrix using dot():")
print(recommendation_dot)

print("\nRecommendation Matrix using matmul():")
print(recommendation_matmul)

image = np.array([
    [120, 150, 180, 200],
    [100, 130, 170, 210],
    [90,  140, 160, 220],
    [80,  110, 190, 230]
])
rotated_image=image.T
print(rotated_image)
mean=np.mean(image)
median=np.median(image)
std_dev=np.std(image)
variance=np.var(image)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
"""

orders = np.array([
    [120, 135, 150, 145, 160, 170],  # City 1
    [100, 110, 125, 130, 140, 155]   # City 2
])
print("Original Array (2x6):")
print(orders)

#Reshape(3,4)
reshaped=orders.reshape(3,4)
print(reshaped)


flatten=orders.flatten()
print(flatten)

part1,part2=np.split(flatten,2)
print(part1,part2)



#Vertical Stack
stacked=np.vstack((part1,part2))
print(stacked)


# import pandas as pd
# from scipy.stats import zscore
# df = pd.DataFrame({
#     'days' :[1,2,3,4,5,6,7,8,9,10,11], 
#     "sales" :[100,200,250,350,170,300,400,500,600,-10000,20000]
# })

# # print(df)
# df['z_score'] = zscore(df['sales'])
# print(df)
# outlier = df[df['z_score'].abs() > 1]
# print(outlier)