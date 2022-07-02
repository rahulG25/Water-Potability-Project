# water-potability
CONTEXT:
Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection. This is important as a health and development issue at a national, regional and local level. In some regions, it has been shown that investments in water supply and sanitation can yield a net economic benefit, since the reductions in adverse health effects and health care costs outweigh the costs of undertaking the interventions.

content: 
The water_potability.csv file contains water quality metrics for 3276 different water bodies. The inputs used in the projects are ph_value, hardness, solid, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity. The output in this project is potability.If potability is zero then the water is non drinkable else the water is drinkable.

In this project I got good accuracy in Light GBM model,so i'm used that model in my project.Deployment done in streamlit method.
Let’s start :-
Import all the required libraries which are used to train the model or visualise the data. Then load the data set using a Pandas’s function read_csv() and display the top five rows of the data set.
Introduction
In this tutorial, we are going to implement a water quality prediction using machine learning techniques. In this technique, our model predicts that the water is safe to drink or not using some parameters like Ph value, conductivity, hardness, etc. 

Let’s start :-
Import all the required libraries which are used to train the model or visualise the data. Then load the data set using a Pandas’s function read_csv() and display the top five rows of the data set.Then perform Exploratory Data Analysis. In EDA,Firstly check the shape of the data set. Then  check that there are Null values or not and you can see in the below image that ph, Sulfate, Trihalomethanes contain NULL values. Then check the information of the data set.

                                  Now describe the dataset which shows the minimum value, maximum value, mean value, count, standard deviation, etc. Then finally we handle the missing values. We filled the missing values in our feachers using a mean value of each feature which means we filled the mean value to handle missing data. Then again check that there are null values present or not.Check the value counts of our target feature Potability. Then visualize the portability using a countplot function of seaborn.Now visualize the pH value using a distplot function to check that it contains a normal distribution or not. So, you can see that it is a normal distribution.Now it’s time to prepare the data set. Divide the data into the independent and dependent features. All are independent features except Potability because Potability is our dependent feature.Split the data set into the training and testing using the train_test_split function which returns four data sets.
Then test the model using the test data set (X_test).Now it’s time to evaluate the model using the accuracy score, confusion matrix and classification report. Evaluation techniques take two parameters; one is the actual data and the other one is a predicted data. And You can see that overall accuracy is 78%.And deployed in streamlit using jupyter notebook.



![Screenshot (117)](https://user-images.githubusercontent.com/99119200/172815483-feca2c29-ab52-468c-b96d-c6f0f4fe4d92.png)
