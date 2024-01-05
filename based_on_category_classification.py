#Here we are defining modules
from sklearn.neighbors import NearestNeighbors
import pandas as pandaModule

#Read the date from csv file
dataframe_list_of_values=pandaModule.read_csv('category.csv')
#Here we are considering attributes like price rating count and rating
attributes_considered=['price','rating_count','rating']

X=dataframe_list_of_values[attributes_considered]#Here we are defining dataframe

minimum_rating=float(input("Enter the minimum rating value out of 5\t\t"))#Here user will enter the rating value out of 5
minimum_rating_count=int(input("Enter the minimum of total ratings like total is 100 ratings or total is 1000 ratings and so on\t\t"))#Here user will enter the rating count

minimum_price=float(input("Enter the minimum price\t\t"))
maximum_price=float(input("Enter the maximum price\t\t"))

filtered_data=dataframe_list_of_values[
    (dataframe_list_of_values['rating']>=minimum_rating) & 
    (dataframe_list_of_values['rating_count']>=minimum_rating_count) & 
    (dataframe_list_of_values['price']>=minimum_price) & 
    (dataframe_list_of_values['price']<=maximum_price)
    ]
#here we are defining the rules for attributes if the rating is greater than minimum rating,
#Rating count is greater than minimum rating count and price is greater than minimum price and
#Price is lesser than mzximum price

if not((filtered_data['price']>=minimum_price) & (filtered_data['price']<=maximum_price)).any():#Here I am defining criteria like if the price does no lie in the range of input values then predict the error
    print("Hey the price ranges are a mismatch please reenter the range")
    exit()

if not (filtered_data['rating_count']>=minimum_rating_count).any():#Here I am mentioning if the rating count is greater than minimum rating count then print the error message
    print("Rating count is a mismatch")
    exit()

if not(filtered_data['rating']).any():
    print("Hey no products for the given rating please try again")
    
if filtered_data.empty:
    print("Hey no products match the given criteria as the criteria is empty")
    exit()



X_filtered=filtered_data[attributes_considered]#Here we are filtering the attributes


k_neighbors=min(5,len(X_filtered))#Here we are making use of K Neighbors algorithm with default neighbors as 5 for filtered attributes
if k_neighbors<1:
    print("Hey sorry  you have reached the minimum limit")
    exit()
knn=NearestNeighbors(n_neighbors=k_neighbors,metric='euclidean')
knn.fit(X_filtered)

user_input = [[0, minimum_rating_count, minimum_rating]]  # The first feature (price) is set to 0 for user input
distances,indices=knn.kneighbors(user_input)#here we are caluclating the nearest neighbors for user input

recommended_products=filtered_data.iloc[indices[0]]
recommended_products = recommended_products[['Category', 'brand_name', 'product_title', 'price', 'rating', 'rating_count']]#here we are defining what data needs to be printed
print(recommended_products)