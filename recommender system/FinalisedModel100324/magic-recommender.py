import pandas as pd
from sklearn.neighbors import NearestNeighbors
from datetime import datetime


'''
STEP 1: Loading and preprocess the dummy data
- Source of proportions from dummy data: https://www.similarweb.com/website/xpressflower.com/#geography
- Using one-hot encoding to convert categorical variables such as Gender, Location, Referal Source, Item Bought etc etc into binary values - essential for the future steps
'''
data = pd.read_csv('DBTT_personal/datasets/DBTT xpressflower dummy data.csv')
data_encoded = pd.get_dummies(data, columns=['Gender', 'Location', 'Referral Source', 'Item bought', 'Purpose'])




'''
STEP 2: Initialising and Fitting the K-Nearest-Neighbours Model through scikit's NearestNeighbours Model. 
    - thought KNN usually doesnt need training, we trained the model here just to give it a feel of our data and how it is formatted
'''
k = 5
metric = 'euclidean'
knn_model = NearestNeighbors(n_neighbors=k, metric=metric)
knn_model.fit(data_encoded.drop(columns=['Customer ID']))  # Exclude Customer ID from features

'''
STEP 3: Taking User input for the "Magic Recommendation System"
- Made it interactive and more personal for the user 
- Added + 1 to the customer ID so that the code does not give me an error (really dont know why it throws me an error if i dont give it CID)
'''
customer_id = data_encoded['Customer ID'].max() + 1  # Increment the maximum customer ID by 1
print("Thank you for visiting XpressFlower's Magic Recommendation! You are customer No. ", customer_id)
age = (input("Enter your age: "))
location = input("Enter your location (Singapore, US, Russia, Mexico, Philippines): ").title()  # Convert input to title case
gender = input("Enter your gender (Male/Female): ").title()  # Convert input to title case
occasion = input("Enter the occasion (Graduation, Anniversary, Funeral, Birth, Opening Ceremony, Birthday, No reason): ").title()  # Convert input to title case
search_engine = input("How did you find us? (Google/Instagram/Facebook etc): ")
'''
ADDITIONAL PART: mapping seasons to months through dictionary for easy lookup, along with the function to determine the current season 
    - allows for better recommendations based on the user's location
    - getting current seasons through DateTime()
'''
seasons = {
    'Spring': (3, 4, 5),
    'Summer': (6, 7, 8),
    'Fall': (9, 10, 11),
    'Winter': (12, 1, 2)
}

def get_season(month):
    for season, months in seasons.items():
        if month in months:
            return season
        
current_month = datetime.now().month
current_season = get_season(current_month)

'''
STEP 4: Creating a dataframe for the user_input and matching it up with our current DF through one hot encoding etc 
'''
user_input = pd.DataFrame([[customer_id] + [age] + [1 if loc == location else 0 for loc in ['Singapore', 'US', 'Russia', 'Mexico', 'Philippines']] +
                           [1 if gen == gender else 0 for gen in ['Male', 'Female']] +
                           [1 if occ == occasion else 0 for occ in ['Graduation', 'Anniversary', 'Funeral', 'Birth', 'Opening Ceremony', 'Birthday', 'No reason']] +
                           [1 if sea == current_season else 0 for sea in ['Spring', 'Summer', 'Fall', 'Winter']]],
                          columns=['Customer ID', 'Age'] + ['Location_' + loc for loc in ['Singapore', 'US', 'Russia', 'Mexico', 'Philippines']] +
                                   ['Gender_' + gen for gen in ['Male', 'Female']] +
                                   ['Purpose_' + occ for occ in ['Graduation', 'Anniversary', 'Funeral', 'Birth', 'Opening Ceremony', 'Birthday', 'No reason']] +
                                   ['Season_' + sea for sea in ['Spring', 'Summer', 'Fall', 'Winter']])

user_input = user_input.reindex(columns=data_encoded.columns, fill_value=0)

'''
STEP 5: Using our fitted KNN model to find the recommendation for the users -> finding the most similar user based on thier demographic info
'''
distances, indices = knn_model.kneighbors(user_input.drop(columns=['Customer ID']))  # Exclude Customer ID from input features
neighbor_items = data_encoded.iloc[indices[0]].drop(columns=['Customer ID'])

'''
STEP 6: Totalling up the recommended items to check for majority attribute within the group 
'''
recommended_items = neighbor_items.sum().sort_values(ascending=False)

'''
STEP 7: Extracting and printing out the top 3 recommended items based on the user's info
'''
recommended_item_names = [item for item in recommended_items.index.tolist() if item.startswith("Item bought")]
print("Top 3 recommended items based on demographic information and current season:")
for item in range(len(recommended_item_names[:3])):
    print(f"{item + 1}. {recommended_item_names[item].replace('Item bought_', '')}")

'''
STEP 8: Ask the user to choose a product from the top 3 recommendations
'''
chosen_product_index = int(input("Enter the number corresponding to the product you want to purchase: "))
chosen_product = recommended_item_names[chosen_product_index - 1].replace("Item bought_", "")

'''
STEP 9: Collect additional information from the user based on the chosen product
'''
def collect_additional_info(chosen_product):
    additional_info = {}
    additional_info["Item bought"] = chosen_product
    additional_info["Referral Source"] = occasion
    additional_info["Purpose"] = search_engine
    
    return additional_info

additional_info = collect_additional_info(chosen_product)

'''
STEP 10: Append the user's information (including the chosen product) to the existing CSV file
'''
user_data = pd.DataFrame([{
    'Customer ID': customer_id,
    'Gender': gender,
    'Age': age,
    'Location': location,
    **additional_info
}])

data = pd.read_csv('DBTT_personal/datasets/DBTT xpressflower dummy data.csv')
data = pd.concat([data, user_data], ignore_index=True)
data.to_csv('DBTT_personal/datasets/DBTT xpressflower dummy data.csv', index=False)

print("Thank you for your purchase! Your information has been added to our database.")