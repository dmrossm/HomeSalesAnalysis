# Seattle Affordable Housing Initiative

![king county image, from https://www.racialequityalliance.org/jurisdictions/king-county-washington/](https://www.racialequityalliance.org/wp-content/uploads/2016/10/assessors_social-1.jpg)

## Business Problem

The Low Income Housing Institute (LIHI) has received a $60 million grant from Amazon to purchase and lease affordable homes to working class families.
Our goal was to find an efficient model that can help choose which homes to buy, to maximize the number of homes LIHI can purchase.

## Dataset Characteristics

The dataset describes 21,597 homes in Kings County sold between 2014-2015, with 21 different characteristics listed, including price, number of bedrooms and bathrooms, square feet of living space, and more.
While most of the data is listed for each house, some features have several null values. Waterfront is missing around 2000 values and view is missing around 200. Year renovated is missing 5000 values. As the three of these features didn’t have a high pearson correlation coefficient to the variable of interest, price, we decided to drop the rows.
Another important characteristic included was the qualitative grade and condition of the dataset. Each house was scored on a 1-13 scale of quality, from poor to luxury. The condition meanwhile assesses the wear and tear on the household, from Poor to Very Good.

## Key Takaways
These features were used to develop the most effective model: 
1) Living space square footage (LSSF): Square footage of living space in the home
2) Closest 15 neighbors living space square footage: The square footage of interior housing living space for the nearest 15 neighbors
3) Latitude: Latitude coordinate
4) Grade: Overall grade of the house. Related to the construction and design of the house.

## Exploratory Data Analysis

## Data Cleaning Process
1) Narrowed data to single family homes (2-5 bedrooms).
2) Removed extraneous variables based on missing values and outliers (view, year renovated, date, waterfront)
3) Eliminated other outliers (excessive basement space, bathrooms, floors, etc.)
4) Matched locational data to city names. 

## Modeling: 
Via a multiple linear regression model using the below features, we were able to predict housing prices with ~62% greater accuracy than with a baseline model. Given this increased accuracy, we were able to predict housing prices within ~$100,000 of the true price. Given the wide range of housing prices and how expensive many homes are within the Seattle region, an error of $100,000 was deemed accceptable. (Our baseline model assessed median price using the medians of each feature below.)
Of note, we created roughly 20 models using varying cominations of features, and the above model was found to be optimal.
- latitude
- living space square footage
- grade 
- closest 15 neighbors living space square footage

## Conclusion: 
- Using a multiple linear regression model with the features latitude, living space square footage, grade, and closest 15 neighbors living space square footage, we can predict housing prices within this region within ~$100,000 of true price and with ~62% greater accuracy than our baseline model.
- Actionable Insights:
LIHI can now use this model to predict housing prices of both listed (for sale) and unlisted (not for sale) properties. 
1) Finding Bargains: By comparing the model's predicted price to the listed price, LIHI can now find under-priced homes and prioritize their purchases. (Underpriced homes are expected to arise due to various factors, including financial difficulties being experienced by the owner and a need for immediate income, as well as lenghty stretches of time that a home may remain on the market and the owner's subsequent willingness to lower the price in order to find a buyer.)
2) Creating lists of eligible homes (sitting within LIHI's desired price range) that include both the listed price and our estimated price. As houses are rarely bought at the listed price, this will allow LIHI to enter the "bargaining arena" with additional knowledge on each property and the confidence needed to submit lower bids for homes that are listed at prices that do not align with our estimates. As this work, of assessing a home's "true" value would normally involve indivual work done by an employee, on each property, this model will save LIHI both time and money during this process. Additionally, by having valuable knowledge with which to "bid down" a seller, LIHI will be able to spend less money on each property, thereby allowing them to purchase more homes and house more individuals in need.


## Important libraries:
- pandas
- numpy
- matplotlib
- seaborn
- datetime
- sklearn
- statsmodels
- random
- mpl_toolkits
- scipy
- warnings
- utils (self-made library compilation)

## Files:
- Main notebook: 

- Functions: 

## Contributors:
- Jade Adams
- Jennifer Cobb
- Danielle Rossman

## Credit:
- Image by [Local and Regional Government Alliance on Race and Equity](https://www.racialequityalliance.org/)

## Dataset Glossary:
- https://info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r#b
