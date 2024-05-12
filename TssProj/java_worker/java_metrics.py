import sys
import re
import math
import javalang
import pandas as pd

####### Code made with the help of ChatGPT #######
def extract_functions_and_code(file_path):
    with open(file_path, 'r') as file:
        code = file.readlines()

    functions = {}
    current_method_name = None
    current_method_code = []
    indentation_level = 0

    for line in code:
        line = line.strip()
        if (line.startswith("public") or line.startswith("private") or line.startswith("protected") or line.startswith("default")) and "(" in line and ")" in line:
            if current_method_name:
                functions[current_method_name] = current_method_code
            current_method_name = line.split("(")[0].split()[-1]
            current_method_code = []
            indentation_level = 1
        elif current_method_name:
            # Collect method code
            if line.endswith("{"):
                current_method_code.append("    " * indentation_level + line)
                indentation_level += 1
            elif line.endswith("}"):
                indentation_level -= 1
                current_method_code.append("    " * indentation_level + line)
            else:
                current_method_code.append("    " * indentation_level + line)

    # Save the last method code
    if current_method_name:
        functions[current_method_name] = current_method_code

    return functions

if len(sys.argv) != 2:
    print("Format: python java_metrics.py <file_path>")
    sys.exit(1)

else:
    file_path = sys.argv[1]

functions = extract_functions_and_code(file_path)


def count_comments(code):
    comments = re.findall(r'/\*.*?\*/|//.*?$', code,  re.MULTILINE | re.DOTALL)
    return len(comments)

def count_indents(code):
    lines = code.split('\n')
    num_indents = 0
    for line in lines:
        num_indents += line.count('    ')
    return num_indents

def count_keywords(code, keywords):
    count = 0
    in_comment = False
    in_string = False

    for i in range(len(code)):
        if code[i:i+2] == '/*' and not in_string:
            in_comment = True
        elif code[i:i+2] == '*/' and not in_string:
            in_comment = False
            continue
        elif code[i:i+2] == '//':
            in_comment = True
        if in_comment:
            continue
        if code[i] == '"':
            in_string = not in_string

        if not in_string:
            for keyword in keywords:
                if code[i:i+len(keyword)] == keyword:
                    if (i + len(keyword) == len(code) or
                       not code[i + len(keyword)].isalnum()) and \
                       (i == 0 or not code[i - 1].isalnum()):
                        count += 1
    return count


loop_keywords = ['for', 'while', 'if']
identifier_chars = [':', '=', '<', '>', ',']

def cyclomatic_complexity(code):
    decision_points = ['if', 'while', 'for', 'switch']
    complexity = count_keywords(code, decision_points) + 1
    return complexity

num_of_lines = []
code_length = []
comments = []
c_complexity = []
indents = []
loop_count = []
identifiers = []
readability = []
name = []

# Print the extracted methods and their code
for method_name, method_code in functions.items():
    print("Method:", method_name)
    #print("Code:")
    method_code = '\n'.join(method_code)
    print(method_code)
    num_of_lines.append(method_code.count('\n') + 1)
    code_length.append(len(method_code))
    comments.append(count_comments(method_code))
    indents.append(count_indents(method_code))
    loop_count.append(count_keywords(method_code, loop_keywords))
    identifiers.append(count_keywords(method_code, identifier_chars))
    c_complexity.append(cyclomatic_complexity(method_code))
    name.append(method_name)
    print(count_comments(method_code))
    print("----")


data = {
    'num_of_lines': num_of_lines,
    'code_length': code_length,
    'comments': comments,
    'cyclomatic_complexity': c_complexity,
    'indents': indents,
    'loop_count': loop_count,
    'identifiers': identifiers,
    'readability': [0 for text in functions],
    'name' : name
}

df = pd.DataFrame(data)
from joblib import load


model = load('random_forest_model.joblib')
X = df[['num_of_lines', 'code_length', 'comments', 'cyclomatic_complexity', 'indents', 'loop_count', 'identifiers']]
df['readability'] = model.predict(X)

buffer_file = []

file_name = file_path.split('\\')[-1].split('.')[0]

for name, readability, c_complexity in zip(df['name'], df['readability'], df['cyclomatic_complexity']):
    buffer = ''
    name_snip = name
    buffer += name_snip
    buffer += '\ncyclomatic_complexity: '
    buffer += str(c_complexity)
    buffer += '\nreadability: '
    buffer += str(readability)
    buffer += '\n----------\n'
    buffer_file.append(buffer)

with open(f'result_{file_name}.txt', 'w') as file:
    file.writelines(buffer_file)

print(df['readability'].describe())