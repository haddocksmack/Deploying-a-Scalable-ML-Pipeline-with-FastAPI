# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- **Name**: Census Income Prediction
- **Type**: AdaBoostClassifier
- **Version**: 1.0
- **Developed by**: Corey Reed
- **Date**: 3/18/2024

## Intended Use
This model predicts if an individual's income exceeds $50,000 based on demographic info found
in census data. It could be used in targeted advertising, determination of eligibility for
government aide, loan pre-approval, or any other instance where it is important to determine
the financial viability of an individual.

## Training Data
**Dataset**: [Census Income](https://archive.ics.uci.edu/dataset/20/census+income)

This dataset features data extracted from the 1994 United States Census. The data includes 
demographic information on individuals and the target variable: their income level,
above or below $50k.

The data was preprocessed with one hot encoding on the categorical features and binary encoding
on the target variable.

## Evaluation Data
The evaluation was performed on a subset of the original dataset (20%). The remaining 80%
made up the training set.

Similar preprocessing was performed on the test set as the training data above.

## Metrics
 - **Precision**: 0.7637
 - **Recall**: 0.6276
 - **F1**: 0.6890

## Ethical Considerations
- **Data Privacy**: The dataset is publicly available and has been anonymized. The current
data maintains excellent data privacy. Any future data used in the model needs to be similarly
anonymized.
- **Bias**: Resultant model should be thoroughly assessed for any potential bias, particularly along
any protected class (race, sex, religion, etc.)

## Caveats and Recommendations
The data used in this model is outdated as it is 30 years old. It would be beneficial to test
the model on updated data to see if the results are still accurate. To make the model effective
in a current ML pipeline, updated data would need regularly fed in and the model re-fitted to the 
new data.
