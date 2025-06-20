import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# Load dataset
df = pd.read_csv("twitter_training.csv", header=None)
df.columns = ['Tweet_ID', 'Entity', 'Sentiment', 'Text']

# Basic Cleaning Function
# Update this function to handle NaN values safely
def clean_text(text):
    if isinstance(text, str):  # Check if it's a string
        text = re.sub(r"http\S+|@\w+|#\w+|[^A-Za-z\s]", '', text)
        text = text.lower()
        return text.strip()
    else:
        return ""  # Replace NaN or non-strings with an empty string

# Apply it safely
df['Cleaned_Text'] = df['Text'].apply(clean_text)


# ---------------------- ANALYSIS ----------------------

# 1. Sentiment Distribution Overall
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Sentiment', palette='Set2')
plt.title("Overall Sentiment Distribution")
plt.savefig("overall_sentiment_distribution.png")
plt.close()

# 2. Top 10 Entities by Tweet Volume
plt.figure(figsize=(10, 5))
top_entities = df['Entity'].value_counts().head(10)
sns.barplot(x=top_entities.index, y=top_entities.values, palette='coolwarm')
plt.title("Top 10 Entities Mentioned in Tweets")
plt.xticks(rotation=45)
plt.ylabel("Number of Tweets")
plt.savefig("top_entities.png")
plt.close()

# 3. Sentiment by Top Entities
plt.figure(figsize=(12, 6))
top10_df = df[df['Entity'].isin(top_entities.index)]
sns.countplot(data=top10_df, x='Entity', hue='Sentiment', palette='pastel')
plt.title("Sentiment by Top 10 Entities")
plt.xticks(rotation=45)
plt.savefig("sentiment_by_entity.png")
plt.close()

# 4. WordCloud for Positive Tweets
positive_text = ' '.join(df[df['Sentiment'] == 'Positive']['Cleaned_Text'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud - Positive Tweets")
plt.savefig("positive_wordcloud.png")
plt.close()
