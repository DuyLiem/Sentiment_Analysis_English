# Sentiment_Analysis_English

Dự án phân tích cảm xúc trên dữ liệu văn bản tiếng Anh sử dụng Machine Learning.

## Tính năng chính

- **Xử lý văn bản**: Làm sạch, chuẩn hóa và chuyển đổi văn bản
- **Phân loại cảm xúc**: Dự đoán sentiment (positive/negative/neutral)
- **Training model**: Huấn luyện mô hình machine learning
- **Dự đoán**: Sử dụng mô hình đã train để phân tích văn bản mới

## Cấu trúc thư mục
sentiment_english_analysis/
├── data/ # Thư mục dữ liệu
│ ├── raw/ # Dữ liệu gốc
│ └── processed/ # Dữ liệu đã xử lý
├── models/ # Model đã huấn luyện
├── notebooks/ # Jupyter notebooks
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_model_training.ipynb
│ └── 03_model_inference.ipynb
├── src/ # Mã nguồn
│ ├── preprocessing/ # Xử lý dữ liệu
│ │ ├── init.py
│ │ └── Preprocess.py
│ └── utils/ # Tiện ích
│ └── init.py
├── tests/ # Dữ liệu kiểm thử
├── requirements.txt # Thư viện cần thiết
└── README.md # Tài liệu dự án

## Dữ liệu
Dữ liệu gốc: data/raw/twitter_sentiment_analysis.csv
Link: https://www.kaggle.com/datasets/daniel09817/twitter-sentiment-analysis

Dữ liệu đã xử lý: data/processed/sentiment_processed.csv

## Thư viện chính
pandas - Xử lý dữ liệu

scikit-learn - Machine Learning

nltk - Xử lý ngôn ngữ tự nhiên

joblib - Lưu và tải model

contractions - Xử lý từ viết tắt

emoji - Xử lý biểu tượng cảm xúc

## Quy trình xử lý văn bản
1. Làm sạch dữ liệu:
Chuyển thành chữ thường → text.lower()

Xóa ký tự đặc biệt → string.punctuation + replace()

Xử lý contractions → contractions.fix(text)

Xử lý emoji → emoji.demojize(text)

Xóa số → re.sub(r'\d+', '', text)

Chuẩn hóa khoảng trắng → re.sub(r'\s+', ' ', text)

2. Xử lý ngôn ngữ:
Lemmatization → WordNetLemmatizer() + POS tagging

Loại bỏ stopwords → Filter với stopwords list

3. Trích xuất đặc trưng:
TF-IDF Vectorization → TfidfVectorizer() (trong training)

## Chạy project
Mở các notebooks theo thứ tự:

01_data_preprocessing.ipynb - Tiền xử lý dữ liệu

02_model_training.ipynb - Huấn luyện mô hình

03_model_inference.ipynb - Dự đoán với dữ liệu mới

## Tác giả
1. Nguyễn Duy Liêm [liem.nd239750@sis.hust.edu.vn]
2. Nguyễn Vũ Duy Anh[anh.nvd239755@sis.hust.edu.vn]