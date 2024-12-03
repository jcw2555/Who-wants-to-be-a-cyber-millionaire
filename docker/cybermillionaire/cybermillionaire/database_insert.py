import mysql.connector
import re

# Function to parse the returned text and remove the A, B, C, D labels
def parse_question_and_answers(text):
    # Regular expression to extract the question and answers
    question_match = re.search(r"Question: (.*?)\n", text)
    answers_match = re.findall(r"([A-D])\.\s([^\n]+)", text)  # Matches A. Answer text, B. Answer text, etc.
    correct_answer_match = re.search(r"Correct Answer: (\w+)\.\s([^\n]+)", text)

    if not question_match or not answers_match or not correct_answer_match:
        raise ValueError("Unable to parse the text correctly")

    question = question_match.group(1)
    answers = [a[1] for a in answers_match]  # Remove A, B, C, D labels and keep the answer text
    correct_answer = answers_match.index((correct_answer_match.group(1), correct_answer_match.group(2))) + 1  # Get the correct answer index (1-based)

    return question, answers, correct_answer

# Function to insert the parsed data into the database
def insert_question_into_db(question, answers, correct_answer):
    # Connect to MySQL
    try:
    
        f = open("cybermillionaire/util/mysqlPassword.txt")
        conn = mysql.connector.connect(host='db',
                                         database='Millionaire',
                                         user='root',
                                         password= f.read().strip())
        cursor = conn.cursor()
    
    except Error as e:
        print("Error reading data from MySQL table", e)
    

    # Insert query
    insert_query = '''
    INSERT INTO dynamic (Question, Ans1, Ans2, Ans3, Ans4, Correct)
    VALUES (%s, %s, %s, %s, %s, %s)
    '''

    # Data to insert
    data = (
        question,
        answers[0],  # Ans1
        answers[1],  # Ans2
        answers[2],  # Ans3
        answers[3],  # Ans4
        correct_answer  # Correct answer is an integer (1-4)
    )

    # Execute the query
    cursor.execute(insert_query, data)

    # Commit the transaction
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

# Sample text returned from the API
text = """
Question: Which of the following is a strong password?

A. Password123
B. 123456
C. SunnyDay!
D. ABCDEFG

Correct Answer: A. Password123
"""

# Parse the text and insert it into the database
try:
    question, answers, correct_answer = parse_question_and_answers(text)
    insert_question_into_db(question, answers, correct_answer)
    print("Question inserted successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
