X_text = ["The pizza tastes terrible.","The book was a perfect balance between wrtiting style and plot.","I am bad","You are very good","It is Awesome Product","This is very bad","That movie was very bad","you are bad person"]
from textblob import TextBlob
for i in X_text:
    print(i,"\t\t",TextBlob(i).sentiment.polarity)