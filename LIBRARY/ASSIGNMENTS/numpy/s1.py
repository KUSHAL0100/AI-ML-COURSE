import numpy as np

# 1. Install NumPy in your Python environment using pip, then create a Python file called insta_likes.py and import numpy as np at the top.
# 2.
# Create a NumPy array called followers using np.array() that stores the follower counts for 5 Instagram influencers: [1200, 15000, 67000, 340000, 1250000]. Print the array, its shape, number of dimensions, and data type.
# 3.
# Use np.arange() to generate an array of order IDs for 10 consecutive Zomato orders starting from 101. Print the array and its size.
# 4.
# Create a 3x3 NumPy array using np.eye() to represent a 'like' identity matrix for a new Spotify playlist feature. Print the matrix and explain what the diagonal values represent in a comment.
# 5.
# Convert a Python list of cricket scores [45, 67, 120, 89, 54] to a NumPy array, then use the .itemsize attribute to print how many bytes each score takes in memory.<br><br><em><strong>Hint:</strong> Use np.array() for conversion and .itemsize for memory size.</em>


influencer=np.array([1200,15000,67000.340000,1250000],dtype="int64")
print(influencer)
print(influencer.shape)
print(influencer.ndim)
print(influencer.dtype)

zomato=np.arange(101,111)
print(zomato, zomato.size)

spotify=np.eye(3)
print(spotify)

cricket_scores=np.array([45,67,120,89,540],dtype="int64")
print(cricket_scores, cricket_scores.itemsize)