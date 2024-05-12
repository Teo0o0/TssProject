import ast
import pandas as pd
import sys

####### Code made with the help of ChatGPT #######
def extract_functions_and_code_outside(file_path):
    # Read the content of the Python file
    with open(file_path, 'r') as file:
        code = file.read()

    # Parse the code into an Abstract Syntax Tree (AST)
    tree = ast.parse(code)

    functions = []
    code_outside_functions = []

    # Flag to indicate if any functions or classes were found
    functions_or_classes_found = False

    # Visit each node in the AST
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):  # Check if the node is a function or class definition
            # Extract the functions or methods inside the class
            if isinstance(node, ast.ClassDef):
                for class_node in node.body:
                    if isinstance(class_node, ast.FunctionDef):
                        function_code = ast.unparse(class_node).strip()
                        functions.append(function_code)
            else:
                function_code = ast.unparse(node).strip()
                functions.append(function_code)
            functions_or_classes_found = True
        else:
            # Extract the code outside of functions and classes
            if hasattr(node, 'lineno') and hasattr(node, 'end_lineno'):
                start_lineno = node.lineno
                end_lineno = node.end_lineno
                code_outside_functions.extend(code.split('\n')[start_lineno - 1:end_lineno])

    # If no functions or classes were found, all code is outside functions
    if not functions_or_classes_found:
        code_outside_functions = code.split('\n')

    return functions, code_outside_functions


if len(sys.argv) != 2:
    print("Format: python main.py <file_path>")
    sys.exit(1)

else:
    file_path = sys.argv[1]

functions, code_outside_functions = extract_functions_and_code_outside(file_path)

outside = '\n'.join(code_outside_functions)

functions.append(outside)

print("Functions or methods inside classes:")
for func_code in functions:
    print(func_code)
    print('----')


import re

def count_comments(code):
    comments = re.findall(r'#.*|(\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\`)|```[\s\S]*?```', code)
    return len(comments)


def cyclomatic_complexity(code):
    decision_points = len(re.findall(r"(if|elif|while|for)\s+.*:", code, re.IGNORECASE))
    exits = len(re.findall(r"(return|break|continue)\b", code, re.IGNORECASE))
    complexity = decision_points + 1 - exits
    return complexity


import math
def count_indents(code):
    lines = code.split('\n')
    num_indents = 0
    for line in lines:
        num_indents += line.count('    ')
    return num_indents


def count_loops(code):
    loop_keywords = ['for', 'while', 'if']
    count = sum(code.lower().count(keyword) for keyword in loop_keywords)
    return count

def count_identifiers(code):
    identifiers = [':', '=', '==', '<', '>', ',']
    count = sum(code.lower().count(keyword) for keyword in identifiers)
    return count

data = {
    'num_of_lines': [text.count('\n') + 1 for text in functions],
    'code_length': [len(text) for text in functions],
    'comments': [count_comments(text) for text in functions],
    'cyclomatic_complexity': [cyclomatic_complexity(text) for text in functions],
    'indents': [count_indents(text) for text in functions],
    'loop_count': [count_loops(text) for text in functions],
    'identifiers': [count_identifiers(text) for text in functions],
    'readability': [0 for text in functions],
    'difficulty': [0 for text in functions],
    'python_solutions': functions
}

df = pd.DataFrame(data)
from joblib import load


model = load('random_forest_model.joblib')
X = df[['num_of_lines', 'code_length', 'comments', 'cyclomatic_complexity', 'indents', 'loop_count', 'identifiers']]
df['readability'] = model.predict(X)

buffer_file = []

file_name = file_path.split('\\')[-1].split('.')[0]

for i in range(len(functions)):
    snippet = functions[i]
    buffer = ''
    name_snip = 'outside'
    if snippet[:3] == 'def':
        name_snip = snippet.split(' ')[1].split('(')[0]
    buffer += name_snip
    buffer += '\ncyclomatic_complexity: '
    buffer += str(cyclomatic_complexity(snippet))
    buffer += '\nreadability: '
    buffer += str(df['readability'][i])
    buffer += '\n----------\n'
    buffer_file.append(buffer)

with open(f'result_{file_name}.txt', 'w') as file:
    file.writelines(buffer_file)



# import tensorflow as tf
# from transformers import TFAutoModel, AutoTokenizer
# import numpy as np
#
# loaded_model = tf.keras.models.load_model("codebert_model")
#
# tokenizer = AutoTokenizer.from_pretrained('codebert_tokenizer')
#
# def preprocess_text(text):
#     encoded = tokenizer(text, padding='max_length', truncation=True, max_length=128, return_tensors='tf')
#     input_ids = encoded['input_ids']
#     attention_mask = encoded['attention_mask']
#     return input_ids, attention_mask
#
# def predict(text):
#     input_ids, attention_mask = preprocess_text(text)
#     prediction = loaded_model.predict([input_ids, attention_mask])
#     return prediction[0]
# #
#
# # input_text = "def add(a, b):\n    return a + b"
# # predicted_value = predict(input_text)
# # print("Predicted value:", predicted_value)
# #
#
# # df['difficulty'] = [predict(text) for text in functions]
# #
# # print(df['difficulty'])
#
