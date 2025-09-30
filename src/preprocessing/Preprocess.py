import string
import re
import emoji
import contractions
import nltk 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

import nltk
# Thư mục bạn muốn lưu dữ liệu
nltk_data_dir = r"../corpora"

# Tải về đúng thư mục này
nltk.download('wordnet', download_dir=nltk_data_dir)
nltk.download('stopwords', download_dir=nltk_data_dir)
nltk.download('omw-1.4', download_dir=nltk_data_dir)
nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download("averaged_perceptron_tagger")

# Thêm đường dẫn để NLTK nhận diện
if nltk_data_dir not in nltk.data.path:
    nltk.data.path.append(nltk_data_dir)

# CLEAN TEXT
remove_character = string.punctuation
def clean_text(text : string):
    # Chuyen ve chu thuong
    text = text.lower() 

    # Xoa cac ki tu dac biet
    for character in remove_character:
        text = text.replace(character, '')

    # Chuyen cac emoji thanh dang text
    text = emoji.demojize(text, delimiters=(' ', ' '))

    # Xoa cac ki tu la so
    text = re.sub(r'\d+', '',text)

    # Xoa cac khoang trang lien tiep
    text = re.sub(r'\s+',' ',text)

    # Chuan hoa cac tu viet tat
    text = contractions.fix(text)

    # Xoa cac khoang trang o dau cau hoac cuoi cau
    text = text.strip()

    return text


# LEMMATIZATION
nltk.data.path.append(r"../corpora")
lemmatizer = WordNetLemmatizer()

# Map POS tag của nltk -> POS tag của WordNet
def get_wordnet_pos(tag):
    
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # mặc định

def lemmatize_with_pos(text):
    tokens = text.split()
    tagged = pos_tag(tokens)  # gán từ loại
    lemmas = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in tagged]
    return " ".join(lemmas)

# REMOVE STOPWORDS
stopwords_english_path = r'../corpora/stopwords/english'

with open(stopwords_english_path, 'r', encoding='utf-8') as f:
    stopwords = list(f.read().splitlines())

def remove_stopwords(text):
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords]
    return " ".join(tokens)

## FULL FUNCTION
def processing_text(text):
    text = clean_text(text)
    text = lemmatize_with_pos(text)
    text = remove_stopwords(text)

    return text 
