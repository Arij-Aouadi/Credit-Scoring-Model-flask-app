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

 send a list via Postman of 17 attributes according to the attributes listed on #Attributes

 example : []
 
![Demo](demo.gif)

## Features

- Predicts creditworthiness based on user inputs.
- Provides explanations for model predictions.
- Cost-sensitive classification to minimize misclassification costs.

## Dataset Information

The dataset used for training the machine learning model is the German Credit dataset. It contains 20 attributes, including numerical and categorical features, and is originally provided in two formats: one with categorical attributes and one with all attributes converted to numerical form. The dataset includes information about checking accounts, credit history, purpose of the loan, and other relevant features.

### Attributes:

- Status of existing checking account
- Duration in months
- Credit history
- Purpose
- Credit amount
- Savings account/bonds
- Present employment since
- Installment rate in percentage of disposable income
- Personal status and sex
- Other debtors/guarantors
- Present residence since
- Property
- Age in years
- Other installment plans
- Housing
- Number of existing credits at this bank
- Job
- Number of people being liable to provide maintenance for
- Telephone
- Foreign worker

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

