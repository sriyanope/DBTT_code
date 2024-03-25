# DBTT_overall

# Algorithms used

- K nearest neighbours algorithm (KNN)
    KNN algo mianly relies on a distance metric (Euclidian distance in this case) to measure the similarity between isntances in the feature space
    the K in KNN refer to the K nearest neighbours to the chosen seed in the algo
    based on the attributes of the K neighbours, the relevant proerties will be assinged to the seed (Majority Voting)
        - in the scenario of regression, the alogirthms will predicts the average or the median value of the target vairable among the K nearest neighbours 

- Characteristics of KNN 
    - no training necessary (great for small datasets like the DBTT one)
    - very useful for user based collaborative filtering
    - issue might arise at scalability, esp when the network gets rlly big, but not much of an issue with small datasets

# CV model for flower 
sequence of actions 
1. Loading up the flowers dataset 
2. Preprocessing 
    - converting the pictures into number arrays 
    - data augmentation (filling in data with whatever dataset we have)
3. Sequential CNN model (Keras)
    - training 
    - test 
    - validation dataset 
    - going to create a web app for it

youtube tutorial link: https://www.youtube.com/watch?v=h6TJiGrYINk
