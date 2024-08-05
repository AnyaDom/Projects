I.	Part I. A research question

A.	A research question

Which factors are the most important for customers who are staying with the company the most?

B.	 Data description

To answer the research question we need to get information about data types and names of columns from CSV file ‘churn_raw_data’. As we see below in the table 1 the file includes the following 50 columns:
Table 1. Description of data
N	Name of column	Numbers of rows		Type of data	Description
1	ï»¿  
	10000	non-null	int64	
2	CaseOrder  	10000	non-null	int64	A placeholder variable to preserve the original order of the raw data file
3	Customer_id	10000	non-null	object	Unique customer ID

4	Interaction	10000	non-null	object	Unique IDs related to customer transactions, technical support, and sign-ups

5	City	10000	non-null	object	Customer address information, splitted  by city,  state, county, zip-code of residence as listed on the billing statement

6	State	10000	non-null	object	
7	County	10000	non-null	object	
8	Zip	10000	non-null	Int64	
9	Lat	10000	non-null	float64	Latitude of residence
10	Lng	10000	non-null	float64	Longitude of residence
11	Population	10000	non-null	int64	Population within a mile radius of the customer
12	Area	10000	non-null	object	Type of area, whether it is rural, urban or suburban 
13	Timezone	10000	non-null	object	Time zone where customer residence is according to the information while signing up the contract
14	Job	10000	non-null	object	Job of the customer according to the information while signing up the contract 
15	Children	7505	non-null	float64	Number of children in the customer’s household according to the information while signing up the contract 
16	Age	7505	non-null	float64	Age of the customer according to the information while signing up the contract 
17	Education	10000	non-null	object	The Customer’s highest degree according to the information while signing up the contract 
18	Employment	10000	non-null	object	Employment status of the customer according to the information while signing up the contract
19	Income	7510	non-null	float64	Customer’s annual income 
20	Marital	10000	non-null	object	Customer’s marital status 
21	Gender	10000	non-null	object	Customer’s gender (male, female, or nonbinary)

22	Churn	10000	non-null	object	If the customer continues or not using the services on the moment of the last month (yes, no)

23	Outage_sec_perweek    	10000	non-null	float64	The average number of seconds per week of system outages in the customer’s neighborhood
24	Email	10000	non-null	int64	Number of emails sent to the customer in the last year 
25	Contacts	10000	non-null	int64	How many times customer contacted technical support
26	Yearly_equip_failure  	10000	non-null	int64	How many times customer’s equipment failed and had to be reset/replaced in the past year
27	Techie	7523	non-null	object	If the customer is  technically inclined (based on customer’s personal assessment) (yes, no)

28	Contract	10000	non-null	object	Duration of the contract (month-to-month, one year, two year)
29	Port_modem	10000	non-null	object	If the customer has a portable modem (yes, no)

30	Tablet	10000	non-null	object	If the customer owns a tablet such as iPad, Surface, etc. (yes, no)
31	InternetService	10000	non-null	object	Customer’s internet service provider (DSL, fiber optic, None)
32	Phone	8974	non-null	object	If the customer has a phone service (yes, no)
33	Multiple	10000	non-null	object	If the customer has multiple lines (yes, no)
34	OnlineSecurity	10000	non-null	object	If the customer has an online security add-on (yes, no)
35	OnlineBackup	10000	non-null	object	If the customer has an online backup add-on (yes, no)
36	DeviceProtection	10000	non-null	object	If the customer has device protection add-on (yes, no)
37	TechSupport	9009	non-null	object	If the customer has a technical support add-on (yes, no)

38	StreamingTV	10000	non-null	object	If the customer has streaming TV (yes, no)

39	StreamingMovies	10000	non-null	object	If the customer has streaming movies (yes, no)

40	PaperlessBilling	10000	non-null	object	If the customer has paperless billing (yes, no)

41	PaymentMethod	10000	non-null	object	Type of payment (electronic check, mailed check, bank (automatic bank transfer), credit card (automatic))
42	Tenure	9069	not-null	float64	How many months the customer has stayed with the provider
43	MonthlyCharge	10000	non-null	float64	The amount charged to the customer monthly. 
44	Bandwidth_GB_Year	8979	non-null	float64	The average amount of data used, in GB, in a year by the customer
45	Item1	10000	non-null	int64	How important for the customer to get a response from support on time on scale of 1-8
46	Item2	10000	non-null	int64	How important for the customer to fix issue on time on scale of 1-8
47	Item3 	10000	non-null	int64	How important for the customer to get replacements on time on scale of 1-8
48	Item4	10000	non-null	int64	How important for the customer reliability on scale of 1-8
49	Item5	10000	non-null	int64	How important for the customer to have options on scale of 1-8
50	Item6	10000	non-null	int64	How important for the customer to get respectful response on scale of 1-8
51	Item7	10000	non-null	int64	How important for the customer to get courteous exchange on scale of 1-8
52	Item8	10000	non-null	int64	How important for the customer to see evidence of active listening on scale of 1-8

II.	Part II: Data-Cleaning Plan
C. Explain the plan for cleaning the data by doing the following:
1.	Propose a plan that includes the relevant techniques and specific steps needed to assess the quality of the data in the data set.
Step 1: Remove irrelevant data
	From the table 1 above we can see that the first row(column in the data set data) contains irrelevant data to be deleted.
Step 2: Deduplicate your data
	data = data.drop_duplicates().reset_index(drop = True)
Step 3: Fix structural errors
We can see from the table 1 again that all column names started from Capital letters, which usually is not practical and needs to be changed for lower register. The second remark concerns the column names: some of them are difficult to be read and understandable due to writing names without underscores and too short names like item 1…8.

Step 4: Deal with missing data
To define number of missing data the following code will be applied:
data.isnull().sum()
To visualize missing data I will use the library missingno, that provides visualizations to understand the presence and distribution of missing data within a pandas dataframe [9].
The code msno.heatmap() helps to see the correlation between missing data. 
To see if there are any consistent patterns with missing data, helps msno.matrix() 
If there are no patterns and we can make a conclusion that all missing data are completely random we can replace missing data with mean, mode or median values depending on the shape of the distribution. 
To visualize the frequency distribution we can use code:
nans.hist(), where nans – is a dataset with only missing data.
If the distribution will be skewed we should use only median values to replace, for categorical – only mode and for normal distribution – mean values.
An example of the code to replace missing data with median values:
for col in data[[column_names to be replaced]]:
    		data[col].fillna(data[col].median(), inplace=True)
Step 5: Filter out data outliers
Manually we can check if there are any outliers in latitude and longitude, knowing their limits:
data['lat'].max(),data['lat'].min() 
Absolute values of latitude should be less than 180°
data['lng'].max(),data['lng'].min()
Absolute values of longitude should be less than 90°.
To see the rest of the outliers we can make boxplots to visualize them. To build several boxplots with own Y-axis we should use subplots :
fig, axes = plt.subplots(1, len(dataset.columns))
for i, ax in enumerate(axes.flat):
    ax.boxplot(dataset.iloc[:,i])
    ax.set_title(dataset.columns[i])
    ax.tick_params(axis='y', labelsize=14)
plt.tight_layout()
Before deleting outliers we should have a deep look at the boxplot as sometimes we have to increase the threshold to keep data for analysis.
2.	Justify your approach for assessing the quality of the data, including the following:
-	characteristics of the data being assessed
At the beginning of cleaning data, I get basic information such as dimensions, column names, and statistics summary to see at glance inappropriate and incorrect format, abnormalities etc.
While analyzing the quality of the categorical data I check the unique names of outputs in each column to see if it is used the same register in names and correctly formatted data. 
To be sure that all data has the appropriate datatype I applied code data.info() to see types. In case of inappropriate type the commands astype(‘’) with putting needed type are used.

- the approach used to assess the quality of the data

The quality of the data could be checked with applying all methods and codes mentioned above [2, Appendix 2]:
-	checking if there are no duplicates left (data.isnull().sum()=0). If there are duplicates the best practice is just to drop all rows with duplicated information.
-	checking if there are no missing data: in the case when missing data are completely random we can use imputing values to missing data points. Using msno.matrix(data)  make it easier: if there are no missing data there should be no gaps in the columns, all fields should be in solid color; If the gaps have existed we can analyze them and evaluate patterns. Other words, .isnull functions can identify missing data but package MSNO provides a visual depiction of the volume of data missing and if the alignment of missing values exists within related variables [2, Appendix 1]. 
-	generating simple plots like histograms, box plots, and visualizing data, helps to take further decisions about outliers and strategy how to deal with missing data. 
	All the above-mentioned practices and strategies allow us to eliminate all “dirty” data, reduce distortion from the use of incorrect data and get a new cleaned dataset to do exploratory analysis on the next step. 
3.	Justify your selected programming language and any libraries and packages that will support the data-cleaning process.
For this project, I have chosen Python programming language and there is no clear justification from my side why I did so, for this type of task: cleaning data, both languages work great. This is just my personal preference. I can not be objective concerning this question as I have never learned R. But researching this question I can make a conclusion that Python language is suitable for a wide range of tasks beyond statistical analysis and data manipulation, which usually are great for R programming language to be used.
One of the second advantage of Python vs R for me as Python has easy-to-read syntax, which intuitively more understandable for beginning programmers. The complexity of advanced functionality in R makes it more difficult to develop expertise [10, Appendix 1].
With R, novices can be running data analysis tasks within minutes. But 
To cover questions I had to import several packages in python:
-	pandas (as pd) to create a Dataframe;
-	numpy (as np) to use high-level mathematical functions for arrays, not with list, which saves memory and decrease time for execution.  In the project were used np.dot, np. cumsum for cumulative variances, np.mean and others. 
-	matplotlib.pyplot (as plt) to visualize graphs
-	missingno (as msno) to visualize missing data
-	 sklearn.decomposition (as PCA) to make PCA
-	matplotlib.patches (as mpatches) to create a custom matplotlib legend
-	matplotlib.cbook (boxplot_stats) to deal with outliers. Build-in functions of Boxplot_stats module gets out outliers from data in just 2 lines with no additional calculation of Q1, Q3 and IQR. It saves time and memory.
To sum up, all Python libraries, imported additionally, help reduce coding errors, and decrease the number of code lines, which makes code more readable and efficient. 
4.	Provide the annotated code you will use to assess the quality of the data in an executable script file.
To check the quality we need to be sure that there is no duplicated data, no missing data and no outliers.
for col in data.columns:
    if data[col].isnull().sum()>0:
        print(data[col])
If there is no missing data left there will no be output

#Deleting duplicates 
data = data.drop_duplicates().reset_index(drop = True)

To deal with outliers it was used this code:

outliers_mc = boxplot_stats(data["column_name"]).pop(0)['fliers']
res = data[~data["column_name"].isin(outliers_mc)]
III.	Part III: Data cleaning
D.  Summarize the data-cleaning process by doing the following:
1.	Describe the findings for the data quality issues found from the implementation of the data-cleaning plan from part C.
The first step towards quality data was renaming columns by using only lowercase and underscore. While uploading the CSV file I noticed that the first column is irrelevant as it contains the same values as case-order and name of the columns contains only symbols. I decided to drop this column.
I checked if there are duplicated data but didn’t find it. 
I renamed some columns using underscore and columns [item 1..8] to ones reflecting their meaning : 'caseorder' renamed 'case_order', 'internetservice' renamed to 'internet_service', 'onlinesecurity' renamed to 'online_security', 'onlinebackup' renamed to 'online_backup', 'deviceprotection' renamed to 'device_protection', 'techsupport' renamed to 'tech_support', 'streamingtv' renamed to 'streaming_tv', 'streamingmovies' renamed to 'streaming_movies', 'paperlessbilling' renamed to 'paperless_billing', 'item1' renamed to 'timely_response', 'item2' renamed to 'timely_fixes', 'item3' renamed to 'timely_replace', 'item4' renamed to 'reliability', 'item5' renamed to 'options', 'item6' renamed to 'respect_response', 'item7' renamed to 'courteous_exchange', 'item8' renamed to 'active_listen', 'monthlycharge' renamed to 'monthly_charge', 'paymentmethod' renamed to 'payment_method'.
The next step was dealing with missing data. I found that some of the columns have more than a quarter of missing data (columns ‘children’, ‘age’, ). A little bit less (<10%) of missing data were found in columns ‘phone’, ‘tech_support’, ‘tenure’, ‘bandwidth_gb_year’.
To be sure in quality data I checked unique names in columns. Also I apply max and min function to see if there are any outliers for latitude and longitude. 
To visualize outliers I used boxplots. And found out that data in columns ‘children’, ‘income’, ‘monthly_charge’ and ‘population’ have outliers. However, I noticed that the boxplot limit ‘population’ to around 300000 people and income of around 75000$. But by cutting down outliers with 75% threshold we will lose a lot of data. That’s why I have chosen a 99.9% threshold for these 2 columns. 
To improve datasets all columns with ordinal data – yes or no were ordinary encoded to 1(yes) and 0 (no).
2.	Justify your methods for mitigating the data quality issues in the data set.

To deal with missing data I used library missingno. 
The module msno (matrix and heatmap) helped me to see if there is any relation between missing data as I saw that 3 columns didn’t have exactly 25% of data. But looking at the matrix (drawing 1) and heatmap I found that all missing data could be considered as missing completely at random (MCAR). 

 
Drawing 1. Matrix with missing data (for sampling 100 rows)
Heatmap (drawing 2) did not show any correlation between parameters. 

 
Drawing 2. Heatmap
After taking this result into consideration I decided to replace missing data with mean/mode/median values. To take this decision I visualize frequency distributions (see drawing 3 below) and for skewed histograms I used median values, for categorical data I used mode and medan was used only for 1 parameter for  ‘age’ as the data are spread more or less evenly.
 
Drawing 3. Histograms for missing data
	To deal with outliers I used boxplot to visualize and see which columns have outliers. Boxplot_stats were used to clean data from outliers.
3.	Summarize the outcome from the implementation of each data-cleaning step

3.1 There were deleted one column with irrelevant data
3.2 There were renamed 19 columns
3.3 The “int” type for columns [Item1…8] was changed to type “category”
3.4 All missing data were replaced with corresponding values (median, mode or mean)
3.5 Almost 4.6% were eliminated from the dataset as outliers.
3.6  The data in 12 columns were encoded as 0 and 1.

4.	Provide the annotated code you will use to mitigate the data quality issues—including anomalies—in the data set in an executable script file.
The code was attached in python notebook
5.	Provide a copy of the cleaned data set as a CSV file.
The copy of the cleaned data set was attached as a CSV file.
6.	Summarize the limitations of the data-cleaning process.

The limitations of the cleaning process are related to the amount of missing data. You can not just drop 25% of data. You have to analyze it and take a decision on what technique you have to use for it. The same problem happened while finding out outliers. If we choose only the classical approach with a threshold 75% the dataset could be dramatically decreased. 
7.	Discuss how the limitations summarized in part D6 could affect the analysis of the question or decision from part A.
Not taking into account limitations pointed in part 6 could lead to losing a big part of data and as a result - incorrect data analysis. 
E.  Apply principal component analysis (PCA) to identify the significant features of the data set by doing the following:
1.  Identify the total number of principal components and provide the output of the principal components loading matrix.

According to the general rule, PCA is applicable for numerical data. For PCA I have chosen the following columns from the dataset:
pca_data=clean_data[['children', 'age', 'income', 'tenure', 'monthly_charge', 'bandwidth_gb_year']]
The loading matrix you can see below:
	PC1	PC2	PC3	PC4	PC5	PC6
children	-0.011044	-0.475047	0.533661	0.505152	-0.483628	0.018430
age	-0.007308	-0.568209	0.320476	-0.746034	0.131912	-0.020333
income	0.013531	0.317892	0.692900	0.166014	0.625371	-0.001399
tenure	0.705530	0.027764	0.021573	-0.045040	-0.039747	0.705254
monthly_charge	0.044749	-0.591228	-0.363216	0.397976	0.596465	0.048650
bandwidth_gb_year	0.707013	-0.009663	-0.000151	0.016758	-0.016249	-0.706750

PC1: The most significant feature positively associated with PC1 is 'tenure' with a covariance of 0.705530. It suggests that 'tenure' has a strong influence on PC1. 'bandwidth_gb_year' also has a relatively high positive covariance of 0.707013 with PC1.
PC2: The most influential features negatively associated with PC2 are 'age' with a covariance of -0.568209 and 'monthly_charge' with a covariance of -0.591228. These features contribute significantly to PC2.
PC3: The most prominent feature positively related to PC3 is 'income' with a covariance of 0.692900 and ‘children’ with covariance 0.533661. It indicates that 'income' has a strong impact on PC3. 
PC4: The primary feature negatively associated with PC4 is 'age' with a covariance of -0.746034. It suggests that 'age' has a strong negative influence on PC4. Strong positive correlation PC4 has with ‘children’ with covariance 0.505152.
PC5: The most significant feature positively associated with PC5 is 'income with a covariance of 0.625371 and ‘monthly_charge’ with a covariance of 0.596465. 
PC6: The most prominent feature positively associated with PC6 is 'tenure' with a covariance of 0.705254. It suggests that 'tenure' contributes strongly to PC6. And negative contributions to PC6 give ‘bandwidth_gb_year” with covariance value -0.706750.

2.  Justify the reduced number of the principal components and include a screenshot of a scree plot.

From the plot below we see that the line is refracted and keep the same value for components 1-5.
 
Drawing 1.
It will be logical to leave only the first 2 components. But let’s have a look at the cumulative variance from each component:
Based on Kaiser’s rule, we can keep all the components with eigenvalues greater or equal to 1. From this perspective, we can leave 1-5 components.
But let’s look at the cumulative variance graph (drawing 2 below).
 
Drawing 2.
While performing PCA the question arises of how many components to choose? We can see from the drawing 2 that number of components to choose from could be defined by the desired cumulative variance. Do we need to choose 2 components as the explain around 50 % of the total variability or 3 with over 65%? It is obvious that we can not retain all six components even though they explain 100% of the variability. Just because it does not help us to reduce the dimensionality. 
Taking into account everything I mentioned above I suggest considering only PC1. PC2, PC3, PC4 with cumulative variance 0.8.
3.  Describe how the organization would benefit from the use of PCA.

PCA helps to reduce the dimension of dataset, choosing among many components just a few principal components. Large datasets have a lot of predictors which as a result of multicollinearity leads to unstable regression models [1]. 
Reducing dimensionality, the volume of the predictor space is gone down by exponential law, that is, much less than the number of predictors itself [1].
All correlations of features are done automatically which helps us to save time and money because of the PCA module in the library sklearn. 
When implementing the PCA in our data set, we get principal components that are independent of one another.
Part IV: Supporting documents

C.	Providing a Panopto video recording 
https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7b32b16b-3d8c-43ea-9668-b00f0111cd3e

D.	List of web resources 
A list of web resources is provided in Appendix 1.   

H.  List of sources
A list of sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized is provided in Appendix 2.

I.	Demonstration of professional communication in the content and presentation of submission.

To support a professional communication style there have been used formal language, citations and professional terminology.




Appendix 1. 
List of web sources 

1	Datacamp D206 – Data cleaning
2	WGU. D206. Webinars by Dr. Keoina Middleton
3	Rukshan Pramoditha. How to Select the Best Number of Principal Components for the Dataset https://towardsdatascience.com/how-to-select-the-best-number-of-principal-components-for-the-dataset-287e64b14c6d
4	Sunny Solanki. Visualize Missing Values (NaNs/Null Values) Distribution in Datasets https://coderzcolumn.com/tutorials/data-science/missingno-visualize-missing-data-in-python
5	Brenda Loznik. Pump it up — How to deal with missing data? https://medium.com/@brendaloznik_48450/pump-it-up-how-to-deal-with-missing-data-ac60178f1ae5 
6	Carolina Bento. Create and customize boxplots with Python’s Matplotlib to get lots of insights from your data https://towardsdatascience.com/create-and-customize-boxplots-with-pythons-matplotlib-to-get-lots-of-insights-from-your-data-d561c9883643
7	https://ru.stackoverflow.com/questions/1517587/%D0%9D%D0%B5-%D1%83%D0%B4%D0%B0%D0%BB%D1%8F%D1%8E%D1%82%D1%81%D1%8F-%D0%B2%D1%8B%D0%B1%D1%80%D0%BE%D1%81%D1%8B-%D0%B2-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B5-pandas

8	BIGABID. What is Principal Component Analysis?
https://www.bigabid.com/what-is-pca-and-how-can-i-use-it/

9	Andy McDonald. Using the missingno Python library to Identify and Visualise Missing Data Prior to Machine Learning

10	Python vs. R: What’s the Difference? By: IBM Cloud Team, IBM Cloud. https://www.ibm.com/cloud/blog/python-vs-r
IV.	ython vs. R: What’s the Difference?
V.	hoat’s the Difference?































Appendix 2 
List of resources

1 Daniel T. Larose, Chantal D. Larose. Data science using Python and R 
2 Vo. T. H, Phuong. Python: Data Analytics and Visualization



