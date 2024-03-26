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
    - going to create a web app for it (did not create in this scenario as we will be integrating this code with our arduino uno, not on a web app)

for the CV code, we referenced this youtube tutorial link (hopefully this is ok for attribution) : https://www.youtube.com/watch?v=h6TJiGrYINk

# More info about the Sequential CNN model 
we are using a sequential CNN model, the layer are organized in a sequential manner, and the layers that are usually found in a neural network at layered on on top of one another. each layer mainly performs specific operations. 

the convolutional layers mainly apply filters ot the input data to detect feauters like the sepal length, color of the petals etc. 

there are also some thigns involved such as activation function, pooling layers etc 

the fully connected layers at the end perform the classification of the photos into various classes, and thats why we are using Keras for that. the algorithm we are using is the stochastic gradient descent algorithm or Adam in short

to penalise the algo for overfitting, we are using L2 regularisation
