# Real Estate Price Prediction and Recommendation System

## Overview
This project focuses on predicting real estate prices and providing recommendations to assist potential property buyers in making informed decisions. The system aggregates data through web scraping, followed by rigorous data preprocessing, exploratory data analysis (EDA), and the development of a machine learning model for price prediction.

## Project Highlights
- **Data Aggregation and Preprocessing:**
  - Web scraping using Python to collect real estate data.
  - Implemented comprehensive data cleaning, outlier detection, and missing value imputation techniques using Pandas and NumPy to ensure high-quality input data for analysis.

- **Exploratory Data Analysis (EDA):**
  - Conducted thorough EDA using Seaborn and Matplotlib to uncover significant data patterns.
  - Refined strategies based on EDA insights to enhance model performance.

- **Model Development:**
  - Developed a Random Forest model using Scikit-learn, achieving an impressive R² score of 90%.
  - Reduced mean absolute error by 44%, resulting in a 30% improvement in model prediction capabilities.

- **Recommendation System:**
  - Utilized an analysis module to visualize graphs, providing a better understanding of factors affecting real estate prices.
  - Provided actionable recommendations, enabling faster and more accurate decision-making for property buyers.

## Technologies Used
- Python
- Scikit-learn
- Pandas, NumPy
- Seaborn, Matplotlib
- BeautifulSoup (for web scraping)

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/RealEstate-PricePrediction.git
    ```

2. Navigate to the project directory:
    ```bash
    cd RealEstate-PricePrediction
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the price prediction and recommendation system:

1. **Run Data Preprocessing:**
    ```bash
    python preprocess_data.py
    ```

2. **Train the Model:**
    ```bash
    python train_model.py
    ```

3. **Make Predictions:**
    ```bash
    python predict.py --features "list of features"
    ```

4. **Generate Recommendations:**
    ```bash
    python recommend.py --parameters "list of parameters"
    ```

## Results
- Achieved an R² score of 90%, significantly improving the accuracy of price predictions.
- Reduced mean absolute error by 44%, ensuring more reliable predictions.
- The recommendation module offers actionable insights, helping property buyers make faster, informed decisions.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries, reach out via  email at yadavakhi1508@gmail.com.

