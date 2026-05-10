AI Lyrics Generator 🎵
This is a simple AI project that can generate song lyrics.
It uses TensorFlow and NumPy to train a small neural network on lyrics text and then create new words based on a starting sentence.
What This Project Does


Reads lyrics text


Learns word patterns


Predicts the next word


Generates new lyrics automatically


Tools Used


Python


NumPy


TensorFlow / Keras


Installation
Clone the project:
git clone https://github.com/yourusername/ai-lyrics-generator.gitcd ai-lyrics-generator
Install the required libraries:
pip install numpy tensorflow
How The Program Works


The program reads the lyrics text.


It converts words into numbers using a tokenizer.


It creates training sequences from the lyrics.


The AI model learns patterns between words.


After training, the model can generate new lyrics from a starting sentence.


Model Structure
Embedding LayerLSTM LayerGRU LayerDense Output Layer
Run The Program
python main.py
Example
Input:Once I was sevenOutput:Once I was seven years old my mama told me
Future Ideas


Train with bigger lyrics datasets


Generate longer songs


Add different music styles


Build a website version


Save trained models


Project Files
├── main.py├── README.md└── requirements.txt
Requirements
numpytensorflow

Author
Made by Vyan 🚀
