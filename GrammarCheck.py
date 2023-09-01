import tkinter as tk
from tkinter import scrolledtext
from spellchecker import SpellChecker
import language_tool_python

# Initialize the spell checker
spell_checker = SpellChecker()

# Initialize the language tool for grammar checking
grammar_tool = language_tool_python.LanguageTool('en-US')

# Function to correct the text, highlight spelling and grammar mistakes, and count words
def check_text():
    input_text = text_widget.get("1.0", "end-1c")  # Get text from the widget
    
    # Clear previous tags
    text_widget.tag_remove("error", "1.0", tk.END)
    
    # Correct spelling and highlight spelling mistakes in red
    corrected_text = ""
    current_index = "1.0"
    
    for word in input_text.split():
        # Check if the word is spelled correctly
        if not spell_checker.correction(word):
            # If not, suggest corrections and highlight in red
            suggestions = spell_checker.candidates(word)
            if suggestions:
                corrected_word = suggestions[0]
            else:
                corrected_word = word
            
            text_widget.tag_add("error", current_index, f"{current_index} + {len(word)} chars")
            text_widget.tag_config("error", foreground="red")
            
            corrected_text += corrected_word + " "
        else:
            corrected_text += word + " "
        
        current_index = text_widget.index(f"{current_index} + {len(word)} chars +1 char")
    
    # Correct grammar
    corrected_grammar_text = grammar_tool.correct(corrected_text)
    
    # Count words
    word_count = len(corrected_grammar_text.split())
    
    # Display corrected text and word count
    result_widget.delete(1.0, tk.END)  # Clear previous result
    result_widget.insert(tk.END, corrected_grammar_text)  # Display corrected text
    word_count_label.config(text=f"Word Count: {word_count}")

# Create the main window
window = tk.Tk()
window.title("Grammar and Spell Checker")

# Create a text input field
text_widget = scrolledtext.ScrolledText(window, width=40, height=10, wrap=tk.WORD)
text_widget.pack()

# Create a button to check and correct the text
check_button = tk.Button(window, text="Check Grammar and Spelling", command=check_text)
check_button.pack()

# Create a result display field
result_widget = scrolledtext.ScrolledText(window, width=40, height=10, wrap=tk.WORD)
result_widget.pack()

# Create a label to display word count
word_count_label = tk.Label(window, text="Word Count: 0")
word_count_label.pack()

# Create a label indicating the creator and year
creator_label = tk.Label(window, text="Created by DinethH using Python - 2023")
creator_label.pack()

# Start the GUI event loop
window.mainloop()
