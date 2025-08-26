# Skytrax British Airway Analysis
<img width="2560" height="1600" alt="image" src="https://github.com/user-attachments/assets/a3a0d842-0990-4654-837e-bdb603d6e7a0" />

**1. Overview**
- Scope: 3,000 British Airways reviews from 2010 to 2023, sourced from AirlineQuality.com, covering multiple airlines.
- Goal: Identify key drivers of customer satisfaction and convert them into targeted improvement actions.
- Method:
   + SQL (Snowflake) for data extraction, cleaning, and preparation
   + Python (Pandas, Seaborn) for exploratory data analysis and correlation heatmaps
   + Mode Studio for interactive dashboarding and visualization
- Top Insights:
   + Weak overall sentiment: Average rating of 2.6/5 and a 35.13% recommendation rate indicate areas for improvement.
   + In Economy, Food & Beverages and Cabin Staff Service are the strongest satisfaction drivers.
   + In Non Economy, Seat Comfort and Food & Beverages are critical; deficiencies here cause sharp dissatisfaction.
     

     
**2. Data Processing and Analysis Workflow**
   
2.1. Data

- Load 3,000 Skytrax reviews using SQL for data querying.
- Validate schema (data types, null values, data consistency).

2.2. Cleaning

- Normalize the data by ensuring consistency in countries, routes, aircraft names, and seat/traveller categories.
- Resolve missing or out-of-range values to ensure clean and reliable data for further analysis.


2.3. Feature Preparation

- Create flags to differentiate between verified vs unverified reviews, as well as economy vs non-economy cabins (business, first, and premium economy).
- Add features for route direction (origin – destination – transit).

2.4. Modeling/Analysis

- Perform correlation analysis on key satisfaction factors (e.g., seat comfort, staff service, food quality) to identify relationships between them.
- Calculate correlation matrices for Economy and Non-Economy classes separately.

2.5. Validation

- Cross-check data: Verify that the data doesn't contain outliers or errors that could skew results.
- Ensure verified vs unverified review balance to avoid bias in findings.
  
2.6. Visualization

- Use Mode Studio to create interactive dashboards with time-series analysis and class-based comparisons (economy vs premium).
- Visualize correlations using heatmaps (Seaborn) to better understand the relationships between key service factors.
- Add filters for year, class, traveller type, and route to allow dynamic data exploration.


**3. Insights**

3.1. Economy Class

- Food & Beverages and Cabin Staff Service are the strongest drivers of satisfaction.
- Seat Comfort and Ground Service are secondary but important; improving seat comfort, especially on longer flights, can significantly impact satisfaction.
- Relationship Insights: Positive service correlates with higher food quality ratings. Seat comfort and staff service work together to enhance the long-haul experience.

3.2. Non-Economy Classes

- Seat Comfort and Food & Beverages are the most critical factors. Premium passengers expect excellent comfort and dining, and any shortfalls in these areas lead to significant dissatisfaction.
- Comfort Issues: Even small comfort issues, such as inadequate seat space, cause frustration among premium passengers.
- Relationship Insights: Premium cabin passengers who rate food quality poorly also tend to rate the overall experience lower, even when other factors are high.


**4. Recommendations**

4.1. Economy Class

- Enhance Staff Service: Focus on improving staff friendliness and attentiveness through targeted crew training.
- Upgrade Food Offerings: Improve menu variety and quality. Collaborate with renowned chefs or premium food brands to elevate the food experience.
- Improve Seat Comfort: Upgrade seat cushioning, recline features, and legroom to improve overall comfort, especially on longer flights.

4.2. Non-Economy Classes

- Premium Food Quality: Collaborate with high-end chefs to improve food quality. Enhance presentation and offer a diverse range of options to satisfy all dietary preferences.
- Upgrade Seat Comfort: Improve seating design to ensure more comfort, with better padding and additional space for premium passengers.
- Act on Customer Feedback: Implement a more responsive process to address passenger complaints quickly, particularly regarding food and comfort.



**5. Key Learnings**

5.1. Technical Skills

- Writing Snowflake SQL: Developed efficient queries for data extraction, cleaning, and creating reproducible data pipelines.
- Building Mode Studio Reports: Created interactive dashboards with dynamic filters and drill-downs.
- Python (Pandas, Seaborn):
  + Used Pandas for data manipulation and Seaborn for creating correlation heatmaps.
  + Performed exploratory data analysis to visualize relationships between satisfaction factors for Economy and Non-Economy cabins.

5.2. Analytical Skills

- Segment-first approach:
  + By segmenting the data into economy and non-economy (premium) cabins, different satisfaction drivers were identified for each group. For example, economy class passengers prioritize staff service and food quality, while premium cabins focus on seat comfort and food quality.
  + This segmentation revealed that each customer group has different "must-haves" for a positive experience.

- Interpreting correlations carefully:
  + Correlations between service factors (e.g., seat comfort, staff service, food quality) were analyzed with the understanding that correlation does not imply causation. For instance, although staff service correlates with food quality, improving one does not necessarily lead to improvement in the other.
   
5.3. Communication

- Turning metrics into operational levers: Key findings were translated into actionable strategies for improvement, such as enhancing menu variety, improving staff training for better service quality, and focusing on seat comfort for long-haul flights.


**6. Limitations**
   
- Single-airline scope: no competitor benchmark yet.
- Unobserved variables: fare paid, delays, aircraft age/config, load factor.
- Correlation limits: associations only, confounding by route length/season/class mix.
- Verified vs unverified weighting sensitivity not fully explored.


**7. Next Steps**
   
- Benchmarking: Compare British Airways with airlines like Lufthansa, Emirates across routes and classes.
- Text Analysis: Conduct text analysis to identify themes related to key factors.
- Modeling: Use regression or correlation to analyze factors like route, class, and flight length.
- Enrichment: Integrate additional data such as flight delays, cancellations, and aircraft age.
- Prioritization: Create an impact vs effort matrix to focus on the most valuable improvements.
- Monitoring: Set up an automated system for monthly data update


