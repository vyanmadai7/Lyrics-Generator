import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, GRU, Dense

lyrics = """
Once I was seven years old, my mama told me 
"Go make yourself some friends, or you'll be lonely"
Once I was seven years old...
"""

tokenizer = Tokenizer()

tokenizer.fit_on_texts([lyrics])

total_words = len(tokenizer.word_index) + 1

input_sequences = []

for line in lyrics.split("\n"):
    token_list = tokenizer.texts_to_sequences([line])[0]

    for i in range(1, len(token_list)):
        n_gram_seq = token_list[:i+1]
        input_sequences.append(n_gram_seq)

max_len_seq = max([len(x) for x in input_sequences])

input_sequences = np.array(pad_sequences(input_sequences,maxlen=max_len_seq,padding="pre"))

X = input_sequences[:, :-1]
y = input_sequences[:, -1]

y = tf.keras.utils.to_categorical(y, num_classes=total_words)

model = Sequential([
    Embedding(total_words, 64, input_length=max_len_seq-1), 
    LSTM(128, return_sequences=True), 
    GRU(64), 
    Dense(total_words, activation='softmax')
])

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)
model.fit(X, y, epochs=50, verbose=1)

def generate_lyrics(seed_text, next_words=10):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_len_seq-1, padding="pre")
        predicted = model.predict(token_list, verbose=0)
        predicted_index = np.argmax(predicted)

        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                seed_text += " " + word
                break
    return seed_text

print(generate_lyrics("Once I was seven",10))
