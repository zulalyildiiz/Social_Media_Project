from visualizer import Visualizer
from model_trainer import ModelTrainer
from analyzer import DataAnalyzer
from report_generator import ReportGenerator

import pandas as pd


try:

    df = pd.read_csv(
        "../data/social_media_sleep_stress_productivity_11000.csv"
    )

    df["age"] = df["age"].astype(int) #yaş sütununu tam sayıya dönüştürülür

    print("\n=== DATASET YÜKLENDİ ===\n")

    print("İlk 5 Satır:")
    print(df.head())

    print("\nVeri Seti Bilgileri:")
    print(df.info())

    print("\nEksik Veriler:")
    print(df.isnull().sum())

    print("\nDescribe Analizi:")
    print(df.describe())

    analyzer = DataAnalyzer(df)  #DataAnalyzer sınıfından bir nesne oluşturulur ve veri seti analiz edilir

    stats = analyzer.calculate_statistics() #verimlilik skorunun istatistiklerini hesaplar ve döndürür

    print("\n=== İSTATİSTİKLER ===") 

    for key, value in stats.items():
        print(f"{key}: {value:.2f}") #istatistikler yazdırılır


    correlation = analyzer.correlation_analysis()  #sosyal medya kullanım süresi ile verimlilik skoru arasındaki korelasyonu hesaplar ve döndürür

    print("\n=== KORELASYON ===")

    print(
        f"Sosyal Medya ve Verimlilik Korelasyonu: "
        f"{correlation:.2f}"
    )

    comment = analyzer.productivity_comment() #verimliliğe göre genel bir yorum yapar

    print("\n=== AI YORUMU ===")
    print(comment)

    ai_comment = comment 

    
    platform_stats = analyzer.platform_analysis()  #farklı platformlarda verimlilik skorlarını analiz eder, istagarm, face, twitter gibi

    print("\n=== PLATFORM ANALİZİ ===")
    print(platform_stats)

    
    visualizer = Visualizer(df) #veri görselleştirme işlemleri yapılır

    visualizer.productivity_histogram()

    visualizer.social_media_vs_productivity()

    visualizer.correlation_heatmap()


    trainer = ModelTrainer(df) #model eğitimi yapılır

    mse, rmse = trainer.train_model()

    print("\n=== MODEL SONUÇLARI ===")

    print(f"MSE: {mse:.2f}")  
    print(f"RMSE: {rmse:.2f}")


    report = ReportGenerator(  #rapor oluşturulur
        stats,
        correlation,
        mse,
        rmse,
        ai_comment
    )

    report.generate_report()

    
except FileNotFoundError:
    print("CSV dosyası bulunamadı!")