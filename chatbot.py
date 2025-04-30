import nltk
import re
import wikipedia
import wolframalpha

# Replace this with your actual WolframAlpha App ID
app_id = "LY825Y-L8X566YGG4"
client = wolframalpha.Client(app_id)

def is_calculation(query):
    return any(op in query for op in ['+', '-', '*', '/', '**', 'sqrt'])

def calculate_expression(expression):
    try:
        return eval(expression)
    except Exception:
        return "Sorry, I couldn't compute that."

def query_wolframalpha(question):
    try:
        res = client.query(question)
        return next(res.results).text
    except:
        return None

def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many results. Suggestions: {e.options[:3]}"
    except:
        return "No relevant info found."

def chatbot_response(user_input):
    if is_calculation(user_input):
        return f"Result: {calculate_expression(user_input)}"

    result = query_wolframalpha(user_input)
    if result:
        return result

    return search_wikipedia(user_input)

# Main Loop
print("Hi! I'm a chatbot. Ask me anything. Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
