# Seattle Affordable Housing Initiative

![king county image, from https://www.racialequityalliance.org/jurisdictions/king-county-washington/](https://www.racialequityalliance.org/wp-content/uploads/2016/10/assessors_social-1.jpg)

## Business Problem

The Low Income Housing Institute (LIHI) has received a $60 million grant from Amazon to purchase and lease affordable homes to working class families.
Our goal was to find an efficient model that can help choose which homes to buy, to maximize the number of homes LIHI can purchase.

## Dataset Characteristics

The dataset describes around 22,000 homes sold between 2014-2015, with over 20 different characteristics listed, including price, number of bedrooms and bathrooms, square feet of living space, and more.

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
Via a multiple linear regression model using the below features, we were able to predict housing prices with ~62% greater accuracy than with a baseline model. Given this increased accuracy, we were able to predict housing prices within $100,000 of the true price. Given the wide range of hoursing prices and how expensive many homes are within the Seattle region, an error of $100,000 was deemed accceptable. (Our baseline model assessed median price using the medians of each feature below.)
Of note, we created roughly 20 models using varying cominations of features, and the above model was found to be optimal.
- latitude
- living space square footage
- grade 
- closest 15 neighbors living space square footage

## Conclusion:  

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

## Credit

## Dataset Glossary:
- https://info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r#b
