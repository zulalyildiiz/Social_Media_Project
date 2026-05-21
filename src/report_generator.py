class ReportGenerator:

    def __init__(
        self,
        statistics,
        correlation,
        mse,
        rmse,
        ai_comment
    ):

        self.statistics = statistics
        self.correlation = correlation
        self.mse = mse
        self.rmse = rmse
        self.ai_comment = ai_comment

    def generate_report(self):

        report_text = f"""
SOCIAL MEDIA ANALYSIS REPORT
============================

1. DATASET INFORMATION
----------------------------
This dataset contains social media,
sleep, stress and productivity data
from 11,000 users.


2. STATISTICAL ANALYSIS
----------------------------

Average Productivity:
{self.statistics['Ortalama Verimlilik']:.2f}

Standard Deviation:
{self.statistics['Standart Sapma']:.2f}

Minimum Productivity:
{self.statistics['Minimum Verimlilik']:.2f}

Maximum Productivity:
{self.statistics['Maksimum Verimlilik']:.2f}


3. CORRELATION ANALYSIS
----------------------------

Social Media vs Productivity:
{self.correlation:.2f}


4. MACHINE LEARNING RESULTS
----------------------------

MSE:
{self.mse:.2f}

RMSE:
{self.rmse:.2f}

Random Forest Regressor model
was used for productivity prediction.

5. AI COMMENT
----------------------------

{self.ai_comment}


6. GENERAL EVALUATION
----------------------------

The dataset was analyzed using:

- Pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn

Graphs and machine learning
predictions were successfully created.
"""

        with open(
            "../outputs/reports/report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report_text)

        print("\n Rapor başarıyla oluşturuldu!")