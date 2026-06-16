# AI document chatbot

A Flask web application that takes a text document and a question from the user, and returns an AI generated response based on the document content.

- Calls an API to connect the client for the response
- Custom styled HTML web page
- Can break down and summarise document input into clean format
- This app was built using Anthropic as the client, though it can be amended to work with other models such as Gemini, OpenAI, and more

## How to use the program
1. Clone the repo using the below URL
```
git clone https://github.com/DAC2792/ai-document-chatbot.git
```

2. Install a virtual environment onto your terminal using command:
```
python -m venv venv
``` 

3. Install the required library extensions from the requirements.txt file using the following bash command:
```
pip install -r requirements.txt
```

4. Connect your own API key to the program (store this in a .env file for security)
```
ANTHROPIC_API_KEY=your-key-here
```

5. Run the program
```
python app.py
```

6. Access the HTML page using the below URL:
```
http://127.0.0.1:5000
```

## Example output (example data when fed info on the Amazon rainforest and asked to summarise key points):

Amazon Rainforest - Key Facts
Here is a summary of the key facts based on the document:

Size: It is the world's largest tropical rainforest, spanning over 5.5 million square kilometres
Global significance: It accounts for more than half of all remaining rainforests on the planet
Trees: It contains an estimated 390 billion trees across approximately 16,000 species
Biodiversity: It is home to around 10% of all species on Earth, highlighting its enormous ecological importance
