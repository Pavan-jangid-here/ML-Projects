Kaggle: [Link to the Kaggle](https://www.kaggle.com/datasets/floser/french-motor-claims-datasets-fremtpl2freq/data)


About Dataset
Context
In the dataset freMTPL2freq risk features and claim numbers were collected for 677,991 motor third-part liability policies (observed on a year).

Content
freMTPL2freq contains 11 columns (+IDpol): • IDpol The policy ID (used to link with the claims dataset). • ClaimNb Number of claims during the exposure period. • Exposure The exposure period. • Area The area code. • VehPower The power of the car (ordered categorical). • VehAge The vehicle age, in years. • DrivAge The driver age, in years (in France, people can drive a car at 18). • BonusMalus Bonus/malus, between 50 and 350: <100 means bonus, >100 means malus in France. • VehBrand The car brand (unknown categories). • VehGas The car gas, Diesel or regular. • Density The density of inhabitants (number of inhabitants per km2) in the city the driver of the car lives in. • Region The policy regions in France (based on a standard French classification)

Acknowledgements
Source:
R-Package CASDatasets, Version 1.0-6 (2016) by Christophe Dutang [aut, cre], Arthur Charpentier [ctb]

Inspiration
The Swiss Actuarial Society's data science tutorials ( https://www.actuarialdatascience.org/ADS-Tutorials/ ) are build on the original dataset (see above) . This copy enables the use of notebooks (kernels) to further study this interesting topic.


Claim Frequency Dataset – Detailed Explanation

Objective:
The main goal is to predict how many insurance claims a customer will make in a certain time. This helps insurance companies estimate risk and set fair prices.

Label (Target Variable):

ClaimNb:
This is the number of claims made by a customer. It is the answer we want our model to predict. For example, if a person had two accidents in one year, their ClaimNb is 2.

Columns of dataset:

IDpol: The unique identifier or policy number for each insurance contract. It helps to distinguish different policies.

Exposure: The measure of risk exposure typically expressed as the amount of time or proportion of a year the policy is active. It reflects how long the insurer is exposed to risk for that policy.

Area: The geographic area or zone where the insured vehicle or risk is located. Location affects risk and premiums.

VehPower: The power or performance measure of the vehicle, often engine horsepower or power rating. Greater power often implies higher risk.

VehAge: The age of the vehicle, which can influence depreciation and likelihood of claims.

DrivAge: The age of the primary driver insured under the policy. Younger or older drivers may have different risk profiles.

BonusMalus: A bonus-malus system factor that adjusts premiums based on the claim history of the policyholder. Bonus for claim-free years lowers premiums; malus for claims increases them.

VehBrand: The manufacturer or brand of the vehicle. Some brands have higher repair costs or theft risks influencing premiums.

VehGas: The type of fuel the vehicle uses (e.g., petrol, diesel, CNG). Fuel type can affect maintenance costs and risks.

Density: Possibly the population or vehicle density in the area, which impacts risk of accidents or theft.

Region: A broader regional classification of the insured location, used to account for regional risk variations.

fold: Dataset-specific column, likely indicating cross-validation fold number used in model training and testing.

frequency: The claim frequency, calculated as the number of claims divided by exposure, indicating claims per unit of time.

Usage:
This data is used by data scientists to build models, like logistic regression, decision trees, or neural networks. The models learn from past data and help insurance companies predict future claims and design fair policies.