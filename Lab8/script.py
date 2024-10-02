from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "<YOUR_API_KEY>"
endpoint = "<YOUR_ENDPOINT>"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = ["Azure Cognitive Services est super pour l'analyse de texte."]
response = client.analyze_sentiment(documents=documents)
for document in response:
    print(f"Sentiment: {document.sentiment}, Scores: {document.confidence_scores}")
