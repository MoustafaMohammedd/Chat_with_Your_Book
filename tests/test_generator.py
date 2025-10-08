import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.generator import ask_your_book

def test_ask_your_book(question):
    answer = ask_your_book(question)
    return answer   

if __name__ == "__main__":
    
    question = "what is the main point of this document?"
    
    answer=test_ask_your_book(question)
    print("Answer:", answer)