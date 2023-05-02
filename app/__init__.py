from api import app

import nltk

nltk.download('stopwords')

if __name__ == '__main__':
    app.run(debug=True, port=3333)