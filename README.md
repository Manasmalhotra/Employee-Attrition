#Employee Attrition
------------------

The problem statement for the project was to analyze the reasons for employee attrition and make a predictive model soa s to predict what kind of employees are
likely to leave the company.

##Need of Employee Attrition prediction

**1) Managing workforce**: If the supervisors or HR came to know about some employees that they will be planning to leave the company then they could get in touch 
                       with those employees which can help them to stay back or they can manage the workforce by hiring the new alternative of those employees.
                       
**2) Smooth pipeline**: If all the employees in the current project are working continuously on a project then the pipeline of that project will be smooth but if 
                    suppose one efficient asset of the project(employee) suddenly leave that company then the workflow will be not so smooth.
                    
**3) Hiring Management**: If HR of one particular project came to know about the employee who is willing to leave the company then he/she can manage the number of 
                          hiring and they can get the valuable asset whenever they need so for the efficient flow of work.
                          
 
 ##Approach
 
### Exploratory Data Analysis

1) Loading the data.
2) Check for null values.
3) Checked and Removed duplicate data.
4) Generated descriptive statistics of data.
5) Correlation Heatmap between numerical variables.
6) Countplots of variables with attrition variable(called "left" in data) as hue.

### Data Cleaning

1) Label encoding for ordinal variables.
2) One-hot encoding for nominal variables.
3) Dropped the first column generated through one hot encoding inorder to reduce complexity of the data.

### Predictive Modelling

1) Split the data into x and y variables where x are all independent variables and y is the depenedent variable( "left") which needs to be predicted.
2) Split the data in a ratio of 80:20 for traing and testing purposes respectively.
3) Applied 6 classical machine learning algorithms to identify the best model.
4) Evaluated the performance of the models using stratified cross validation method as there was a class imbalance in the dataset.
5) Random Forest Classifier was identified tobe the best performing model with a F1 score of 0.989.
6) No overfitting was detected as per the cross validation results, but since I had limited data to test on, I performed SMOTE technique to tackle the class imbalance.
7) The model giave a similar level of performance (F1 score : 0.985 Precision:0.995 Recall: 0.975) with the SMOTE technique.

Please Note: Detailed insights and methodology are documented in the juypter notebooks shared.
