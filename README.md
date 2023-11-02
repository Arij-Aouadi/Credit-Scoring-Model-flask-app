# Credit Scoring App with Machine Learning

A Flask web application for credit scoring using a machine learning model trained on the German Credit dataset.

## Table of Contents
- [Description](#description)
- [Demo](#demo)
- [Features](#features)
- [Dataset Information](#dataset-information)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Description

This web application allows users to input their financial information, and it uses a machine learning model to predict their creditworthiness. The model has been trained on the German Credit dataset provided by Professor Dr. Hans Hofmann from the University of Hamburg. It uses a cost-sensitive approach to make more accurate predictions, taking into account the cost of misclassifications.

## Demo

 the flask app is hosted here : arij123.pythonanywhere.com

 send a list via Postman of 17 attributes according to the attributes listed on [Attributes](#Attributes)

 example : []
 
![Demo](demo.gif)

## Features

- Predicts creditworthiness based on user inputs.
- Provides explanations for model predictions.
- Cost-sensitive classification to minimize misclassification costs.

## Dataset Information

The dataset used for training the machine learning model is the German Credit dataset. It contains 20 attributes, including numerical and categorical features, and is originally provided in two formats: one with categorical attributes and one with all attributes converted to numerical form. The dataset includes information about checking accounts, credit history, purpose of the loan, and other relevant features.

### Attributes:

- Attribute 1:  Status of Existing Checking Account
          1 :      ... <    0 Dt
          2 : 0 <= ... <  200 Dt
     	  3 :      ... >= 200 Dt /salary assignments for at least 1 year
          4 : no checking account 

- Attribute 2: Duration in months

- Attribute 3: Credit history
	 0 : no credits taken/all credits paid back duly
         1 : all credits at this bank paid back duly
	 2 : existing credits paid back duly till now
         3 : delay in paying off in the past
	 4 : critical account/other credits existing (not at this bank) 

- Attribute 4: Purpose
	     0 : car (new)
	     1 : car (used)
	     2 : furniture/equipment
	     3 : radio/television
	     4 : domestic appliances
	     5 : repairs
	     6 : education
	     7 : vacation
	     8 : retraining
	     9 : business
	     10 : others 

- Attribute 5: Credit amount

- Attribute 6: Savings account/bonds
	     1 :          ... <  100 Dt
	     2 :   100 <= ... <  500 Dt
	     3 :   500 <= ... < 1000 Dt
	     4 :          .. >= 1000 Dt
             5 :   unknown/ no savings account 


- Attribute 7: Present employment since
	     1 : unemployed
	     2 :       ... < 1 year
	     3 : 1  <= ... < 4 years
	     4 : 4  <= ... < 7 years
	     5 :       .. >= 7 years 

- Attribute 8: Installment rate in percentage of disposable income

- Attribute 9: Personal status and sex
         1 : male   : divorced/separated
	 2 : female : divorced/separated/married
         3 : male   : single
	 4 : male   : married/widowed
	 5 : female : single 

- Attribute 10: Other debtors/ guarantors
	     1 : none
	     2 : co-applicant
	     3 : guarantor 

- Attribute 11: Present residence since*/

- Attribute 12:  Property
	     1 : real estate
	     2 : if not 1 : building society savings agreement/life insurance
             3 : if not 2 : car or other, not in attribute 6
	     4 : unknown / no property 

- Attribute 13: Age in years 


- Attribute 14: Other installment plans
	     1 : bank
	     2 : stores
	     3 : none  

- Attribute 15: Housing
	     1 : rent
	     2 : own
	     3 : for free 


- Attribute 16: Number of existing credits at this bank 


- Attribute 17: Job
	     1 : unemployed/ unskilled  - non-resident
	     2 : unskilled - resident
	     3 : skilled employee / official
	     4 : management/ self-employed/ highly qualified employee/ officer

  For a detailed description of each attribute, refer to the [original dataset](german.data).

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Flask
- Scikit-Learn
- Pandas
- Numpy

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Arij-Aouadi/credit-scoring-app.git
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Access the app in your web browser at `http://localhost:5000`.

3. Enter your financial information to get a credit scoring prediction.

## Model Training

If you wish to retrain the model using the German Credit dataset, follow these steps:

1. Download the dataset from [the source](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data).

2. Use the Jupyter Notebook provided in the `model-training` folder to preprocess and train the model.

3. Save the trained model and place it in the `models` directory.

4. Update the model loading code in `app.py` to load your new model.

## Technologies Used

- Python
- Flask
- Scikit-Learn
- Pandas
- Numpy
- pickle

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy using the Credit Scoring App! If you have any questions or suggestions, feel free to contact us.

