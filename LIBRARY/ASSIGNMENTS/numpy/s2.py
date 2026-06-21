"""
1.
Create a 2D NumPy array representing the ratings (out of 5) given by 4 users to 5 different food items on Zomato. Use slicing to extract the ratings given by the second and third users only.
2.
Given a NumPy array of daily steps tracked for 10 days, use boolean indexing to select only the days where the steps were greater than 8000.<br><br><em><strong>Hint:</strong> Use an array like steps = np.array([7500, 8200, 9000, ...]) and apply a boolean condition.</em>
3.
Create a NumPy array of IPL team scores for 8 matches. Use fancy indexing to select the scores from matches 2, 5, and 7, and print them.
4.
Suppose you have a NumPy array of product prices from Flipkart. Use broadcasting to apply a 10% discount to all prices and print the new array.<br><br><em><strong>Constraint:</strong> Do not use any loops.</em>
5.
Given a NumPy array of user ratings (can be negative, zero, or positive) for songs on Spotify, use boolean masking to set all negative ratings to zero, keeping other ratings unchanged.
"""
import numpy as np
ratings = np.array([
    [5, 4, 3, 4, 5],   # User 1
    [3, 2, 4, 3, 4],   # User 2
    [4, 5, 5, 4, 5],   # User 3
    [2, 3, 3, 2, 3]    # User 4
])
print(ratings[1:3])

steps = np.array([7500, 8200, 9000, 6700, 10000, 7800, 8500, 9200, 7000, 8800])
print(steps>8000)

ipl_score=np.array([100,150,51,200,190,145,138,185,153,100])
print(ipl_score[[2,5,7]])

flipcart_price=np.array([100,5200,150,5820,415,451,4812,452])
discount_price=flipcart_price * 0.9
print(discount_price)

spotify_ratings=np.array([-2,-1,-3,0,0,5,3,4,2])
spotify_ratings[spotify_ratings<0]=0
print(spotify_ratings)