import numpy as np


class DataAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def calculate_statistics(self):   #bu fonksyion, verimlilik skorunun istatistiklerini hesaplar ve döndürür

        productivity_array = self.df["productivity_score"].to_numpy()    #pandas numpy dönüşüm

        statistics = {
            "Ortalama Verimlilik": np.mean(productivity_array),
            "Standart Sapma": np.std(productivity_array),
            "Minimum Verimlilik": np.min(productivity_array),
            "Maksimum Verimlilik": np.max(productivity_array)
        }
        productivity_array = self.df[
            "productivity_score"
        ].to_numpy()

        np.mean(productivity_array)

        return statistics

    def correlation_analysis(self):  #bu fonksiyon, sosyal medya kullanım süresi ile verimlilik skoru arasındaki korelasyonu hesaplar

        correlation = np.corrcoef(
            self.df["social_media_hours"],
            self.df["productivity_score"]
        )[0, 1]

        return correlation
    
    def productivity_comment(self):  #bu fonksiyon, verimlilik skorlarının ortalamasına göre genel bir yorum yapar

        average_productivity = np.mean(
            self.df["productivity_score"]
        )

        if average_productivity > 70:
            return "Users generally have high productivity."

        elif average_productivity > 40:
            return "Users generally have medium productivity."

        else:
            return "Users generally have low productivity."
        
    def platform_analysis(self):  #bu fonksiyon, farklı platformlarda verimlilik skorlarını analiz eder, istagarm, face, twitter gibi 

        platform_stats = self.df.groupby(
            "platform"
        )["productivity_score"].mean()

        return platform_stats