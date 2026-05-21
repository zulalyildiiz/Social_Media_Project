from sklearn.model_selection import train_test_split #Modeli eğitmek için veriyi eğitim ve test setlerine böler
from sklearn.ensemble import RandomForestRegressor  #Random Forest Regressor modeli içim
from sklearn.metrics import mean_squared_error  #Model performansını değerlendirmek için gerekli metrikler
import numpy as np #numpy kütüphanesi, özellikle korelasyon analizi ve model değerlendirmesi için kullanılır


class ModelTrainer:

    def __init__(self, dataframe):  #ModelTrainer sınıfının yapıcı metodu, veriyialır ve sınıfın bir özelliği olarak saklar
        self.df = dataframe

    def train_model(self): 

        X = self.df[[  #Modeli eğitmek için kullanılacak özellikler
                "social_media_hours",
                "sleep_hours",
                "exercise_minutes",
                "study_work_hours",
                "age"
            ]
        ]

        y = self.df["productivity_score"]

        X_train, X_test, y_train, y_test = train_test_split( #veriyi eğitim ve test setlerine böler
            X,
            y,
            test_size=0.2,  #verinin %20'si test seti olarak ayrılır
            random_state=1  #veri bölme işleminin tekrarlanabilir olmasını sağlar
        )

     
        model = RandomForestRegressor( #Random Forest Regressor modeli oluşturulur
            n_estimators=100,  #100 tane karar ağacı oluşturulur
            random_state=1
        )

   
        model.fit(X_train, y_train) #Modelin eğitildiği satır

    
        predictions = model.predict(X_test) #Modelin test seti üzerinde tahminler yapması
        mse = mean_squared_error(y_test, predictions) #hata hesaplama

        rmse = np.sqrt(mse)  #MSE, modelin tahmin hatalarının kareli ortalamasını ölçerken 
                             #RMSE bu hatayı karekök alarak daha anlaşılır (veriyle aynı birimde) şekilde gösterir.

        return mse, rmse
    
    def predict_productivity(
        self,
        age,
        screen_time,
        social_media,
        sleep,
        exercise,
        study
    ):

        X = self.df[
            [
                "daily_screen_time_hours",
                "social_media_hours",
                "sleep_hours",
                "exercise_minutes",
                "study_work_hours",
                "age"
            ]
        ]

        y = self.df["productivity_score"]

        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        model.fit(X, y) #modelinin verilerden öğrenmesini sağla

        user_data = [[
            screen_time,
            social_media,
            sleep,
            exercise,
            study,
            age
        ]]

        prediction = model.predict(user_data)

        return prediction[0]