
# 🔄 General ETL Pipeline Web App

This project is a **Streamlit-based web application** that allows users to upload a CSV dataset, clean it using a general-purpose ETL (Extract, Transform, Load) pipeline, and download the processed version. It uses popular Python libraries like `pandas` and `scikit-learn` for data cleaning and transformation.

## 🚀 Features

- Upload any CSV dataset
- Automatically identifies numerical and categorical columns
- Handles missing values
  - Mean imputation for numerical columns
  - Most frequent imputation for categorical columns
- Scales numerical values
- One-hot encodes categorical features
- Optionally preserves a target column
- Preview the raw and cleaned datasets
- Download the transformed CSV file

## 🛠️ Tech Stack

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)

## 📦 Installation

1. **Clone the repository:**

   git clone https://github.com/mahithachopra/etl-pipeline-streamlit.git
   cd etl-pipeline-streamlit
Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install the dependencies:
pip install -r requirements.txt


## ▶️ Running the App
Run the following command in your terminal:
streamlit run app.py
Then open the provided URL in your browser (usually http://localhost:8501).

## 📁 File Structure
etl-pipeline-streamlit/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

## 📸 Screenshots
![Screenshot 2025-07-05 123244](https://github.com/user-attachments/assets/e65e4ec0-40f0-4bc3-8ac9-cbec4d46db29)
![Screenshot 2025-07-05 123305](https://github.com/user-attachments/assets/4e4ad610-60e5-4916-bed2-39675541ea1c)
![Screenshot 2025-07-05 123318](https://github.com/user-attachments/assets/05728da9-c572-4bd4-bbe9-ca24f1418ca5)



## 🙌 Acknowledgements
Developed using Streamlit, an open-source app framework.
Thanks to the maintainers of pandas and scikit-learn.

Feel free to contribute or raise issues! 💬








