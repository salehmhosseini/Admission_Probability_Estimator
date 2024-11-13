# Admission_Probability_Estimator
This is a python flask application to calculate and estimate the admission probabilty in universities

# University Admission Probability Predictor

A web application developed using Flask that helps Iranian university entrance exam candidates assess their chances of admission to various universities and majors based on their academic data. This project was built for Sahel Barati's Academy to assist students and counselors in making more informed and optimized major selection decisions.

[Live Demo](https://sahelbaratii.com/probability-of-acceptance/)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This application is designed to provide a comprehensive view for university candidates on their chances of admission. The tool uses a dataset scraped from the 2021 admissions data and applies machine learning algorithms to enhance predictions and fill any missing data points.

The application displays a list of potential universities and majors for the candidate along with both quantitative and qualitative admission probabilities, making it easier for candidates to make data-driven decisions during the application process.

## Features

- **Data Entry**: Candidates enter details such as their region, major, regional and national rank, GPA score, and desired majors.
- **University List**: Displays a list of universities and programs with calculated probabilities for admission based on input.
- **Qualitative and Quantitative Probability**: Shows both percentage-based and qualitative acceptance chances.
- **Machine Learning Enhanced Predictions**: Completes and improves dataset predictions for higher accuracy.
- **Scraped Data Integration**: Utilizes real data from 2021 to provide realistic predictions.

## Screenshots

### Main Interface
![Main Interface](https://github.com/salehmhosseini/Admission_Probability_Estimator/blob/main/screenshots/main.png)
Candidates can input their details such as major group, regional and national rank, and desired majors to calculate admission probabilities.

### Results Page
![Results Page](https://github.com/salehmhosseini/Admission_Probability_Estimator/blob/main/screenshots/result1.png)
Displays a list of possible admissions with each university’s program, acceptance probability, and type (full-time or part-time).

## Installation

To run this project on your local machine, follow these steps:

1. **Install Python** (if not already installed).
2. **Install Flask**: 
   ```bash
   pip install flask
3. **Clone the repository**:
   ```
   git clone https://github.com/salehmhosseini/Admission_Probability_Estimator.git
4. **Navigate to the project directory**:
   ```
   cd UniversityAdmissionPredictor
5. **Run the application**
   ```
   python api_not_null_complete.py
6. **Access the application:**  Open a browser and navigate to http://localhost:5000.

## Usage
1. **Input Details:** Enter your exam-related data in the input fields provided on the main page.
2. **Get Predictions:** Click on "نمایش رشته ها احتمال قبولی" (Show Admission Probabilities) to see a list of universities with your calculated chances of admission.
3. **Interpret Results:** Use the admission probabilities provided to understand your admission likelihood across different programs and universities.

## Future Enhancements
1. **UI Improvement:** Refine the user interface for a more polished and intuitive experience.
2. **Dataset Expansion:** Gather additional datasets to improve prediction accuracy.
3. **Model Accuracy:** Enhance the prediction model for even higher accuracy.
4. **Data Validation:** Implement stricter data validation mechanisms.
5. **Process Validation:** Ensure consistency and reliability in the admission prediction process.

## Contributing
We welcome contributions! If you’d like to improve the project, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License.
