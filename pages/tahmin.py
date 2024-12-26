import os
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
import warnings
from datetime import datetime

# Uyarıları kapat
warnings.filterwarnings('ignore')

# LSTM Modeli
class LSTMModel(nn.Module):
    def _init_(self, input_size=1, hidden_layer_size=20, output_size=1):
        super(LSTMModel, self)._init_()
        self.lstm = nn.LSTM(input_size, hidden_layer_size, batch_first=True)
        self.fc = nn.Linear(hidden_layer_size, output_size)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        predictions = self.fc(lstm_out[:, -1, :])  # Sadece son zaman adımını alıyoruz
        return predictions

# Veriyi hazırlama
def prepare_data(data, look_back=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data['close'].values.reshape(-1, 1))

    X = []
    y = []

    for i in range(look_back, len(data_scaled) - 1):  # Son adımı çıkarıyoruz
        X.append(data_scaled[i-look_back:i, 0])
        y.append(data_scaled[i, 0])

    X = np.array(X)
    y = np.array(y)

    # PyTorch tensörlerine dönüştürme
    X = torch.tensor(X, dtype=torch.float32).unsqueeze(-1)
    y = torch.tensor(y, dtype=torch.float32).unsqueeze(-1)
    return X, y, scaler

# Modeli eğitme
def train_model(data, coin_name, model_path='./models/', look_back=60, epochs=10, lr=0.001):
    X, y, scaler = prepare_data(data, look_back)
    model = LSTMModel()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
    
    # Modeli kaydetme
    os.makedirs(model_path, exist_ok=True)  # Klasör yoksa oluştur
    model_save_path = os.path.join(model_path, f"{coin_name}_model.pt")
    torch.save(model.state_dict(), model_save_path)

    return model, scaler

# Modeli yükleme
def load_or_train_model(coin_name, data, model_path='./models/', look_back=60, epochs=10, lr=0.001):
    model_save_path = os.path.join(model_path, f"{coin_name}_model.pt")
    if os.path.exists(model_save_path):
        # Modeli yükle
        model = LSTMModel()
        model.load_state_dict(torch.load(model_save_path))
        model.eval()
        _, _, scaler = prepare_data(data, look_back)
    else:
        # Modeli eğit ve kaydet
        model, scaler = train_model(data, coin_name, model_path, look_back, epochs, lr)
    return model, scaler

# Tahmin yapma
def make_prediction(model, X_test, scaler, device):
    last_60_days = X_test[-1].unsqueeze(0)  # Son 60 gün verisi
    model.to(device)
    last_60_days = last_60_days.to(device)
    
    with torch.no_grad():
        prediction = model(last_60_days)
    
    # Tahmini orijinal ölçeğe geri çevirme
    prediction = prediction.cpu().numpy()
    prediction = scaler.inverse_transform(prediction)
    return prediction[0][0]

# Tahminleri hazırlama
def prepare_predictions(coin_data_files, model_path='./models/'):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    predictions = {}

    for coin_name, file_path in coin_data_files.items():
        data = pd.read_csv(file_path)
        model, scaler = load_or_train_model(coin_name, data, model_path)
        X_test, _, _ = prepare_data(data)
        prediction = make_prediction(model, X_test, scaler, device)
        predictions[coin_name] = round(prediction, 2)

    return predictions

# Bugünün tarihi
today_date = datetime.now().strftime('%Y-%m-%d')

# Coin dosyalarının yolu
coin_data_files = {
    'ADA': 'ADA_1y_hourly.csv',
    'BNB': 'BNB_1y_hourly.csv',
    'BTC': 'BTC_1y_hourly.csv',
    'DOGS': 'DOGS_1y_hourly.csv',
    'ETH': 'ETH_1y_hourly.csv',
    'MATIC': 'MATIC_1y_hourly.csv',
    'SHIB': 'SHIB_1y_hourly.csv',
    'SOL': 'SOL_1y_hourly.csv',
    'TON': 'TON_1y_hourly.csv',
    'XRP': 'XRP_1y_hourly.csv',
}

# Tahminleri başlat (Uygulama başlarken yapılır)
st.write("Tahminler hesaplanıyor...")
predictions = prepare_predictions(coin_data_files)
st.write("Tahminler hazır!")

# Streamlit Arayüzü
st.title(f"Coin Tahminleri - {today_date}")
st.markdown("Aşağıdaki seçeneklerden bir coini seçerek yarın için tahmin edilen fiyatı görebilirsiniz.")

selected_coin = st.selectbox("Bir Coin Seçin", list(coin_data_files.keys()))

if selected_coin:
    st.write(f"{selected_coin} için yarınki tahmin edilen fiyat: {predictions[selected_coin]} USD")

# Tüm tahminleri tablo olarak göster
st.markdown("### Tüm Tahminler")
predictions_df = pd.DataFrame(predictions.items(), columns=['Coin', 'Tahmin Edilen Fiyat'])
st.dataframe(predictions_df)
