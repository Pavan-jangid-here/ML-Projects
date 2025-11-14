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