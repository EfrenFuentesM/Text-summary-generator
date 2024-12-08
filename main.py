import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

# Descargar datos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    # Tokenización en oraciones y palabras
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    
    # Eliminar puntuación y palabras irrelevantes (stopwords)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and word not in string.punctuation]
    
    # Calcular la frecuencia de las palabras
    word_frequencies = Counter(words)
    
    # Puntuación de las oraciones según palabras clave
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = 0
                sentence_scores[sentence] += word_frequencies[word]
    
    # Seleccionar las oraciones más relevantes
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(summarized_sentences)

# Leer texto desde un archivo
with open('input.txt', 'r') as file:
    text = file.read()

# Generar resumen
summary = summarize_text(text)
print("Resumen del texto:")
print(summary)
