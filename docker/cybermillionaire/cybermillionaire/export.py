import mysql.connector
from mysql.connector import Error
import json
import sys
import cybermillionaire.dynamic_question_generation as generation
import cybermillionaire.database_insert as insert

# Executes all export functionality
def run_sql(cursor, query):
    cursor.execute(query)
    records = cursor.fetchall() #All the records for that query are here.
    #print(records)

    #print("Total rows: ", cursor.rowcount)

    #print("\nPrinting each record")
    
    #Check rows, don't run this if there are thousands of entries.
    #This is how we will read in values though
    """
    for row in records:
        print("Question = ", row[0], "\n")
        print("Ans1 = ", row[1], "\n")
        print("Ans2 = ", row[2], "\n")
        print("Ans3 = ", row[3], "\n")
        print("Ans4 = ", row[4], "\n")
        print("Correct = ", row[5], "\n")
        print("Rank = ", row[6], "\n")
    """
    return records
    
def generate_json(game):
    #data = {}
    #data['games'] = []
    #questions_json = "questions: "
    json_file = {}
    json_file['games'] = []
    questions = []


    
    for question in game:
        #for column in question:
        for i in range(len(question)):
            # Need to include "questions" around the individual question
            if i == 0:
                #print("Question: " + question[i])
                quest_json = question[i]
            #Print "content" here before answers
            # Surround answers with [],
            if i == 1:
                #print("Ans1: " + question[i])
                ans1_json = question[i]
            if i == 2:
                #print("Ans2: " + question[i])    
                ans2_json = question[i]
            if i == 3:
                #print("Ans3: " + question[i])    
                ans3_json = question[i]
            if i == 4:
                #print("Ans4: " + question[i])    
                ans4_json = question[i]
            if i == 5:
                #print("Correct: " + str(question[i]))    
                correct_json = question[i]
                     
            #print("\n")
            
        #create content array
        content = []
        content.append(str(ans1_json))
        content.append(str(ans2_json))
        content.append(str(ans3_json))
        content.append(str(ans4_json))

        # populate questions dictionary
        questions.append({
            "question": str(quest_json),
            "content" : content,
            "correct": int(correct_json)
        })
    json_file['games'].append({"questions" : questions})

    #with open('cybermillionaire/util/millionaire.json','w') as outfile:
    with open('static/js/millionaire.json','w') as outfile:
        json.dump(json_file, outfile)

    # # Clear the dynamic table
    # try:
    #     cursor.execute("DELETE FROM dynamic;")  # Removes all rows from the table
    #     cursor.connection.commit()  # Commit the transaction
    #     print("Dynamic table cleared successfully!")
    # except Exception as e:
    #     print(f"An error occurred while clearing the table: {e}")

""" 
        data['games'].append({
            #Need to include "questions" for all questions

            "question": str(quest_json),
            "content: [ Ans1": str(ans1_json),
            "Ans2": str(ans2_json),
            "Ans3": str(ans3_json),
            "Ans4": str(ans4_json),
            # Don't think we should string this, pretty sure json reads it as int
            "] " + "Correct": int(correct_json)
            
        })
"""
# I think I took care of the two TODO before this comment with the function below? Unless I'm confused
# Making this basic so we have it here, assuming we will have a variable 1-4 for level choice
# This will change a bit when we are getting info from JS not user input (this should solve second TODO)
"""def LevelSelect(selection):

    if selection == '1':
        K_8th()

    elif selection == '2':
        HighSchool()

    elif selection == '3':
        College_NonTech()

    elif selection == '4':
        College_Tech()

    else:
        print("Invalid Level Selection!")
""" 

# This will run when a Static Primary School game is selected. It will gather all questions for the game       
def Static_Primary_School(cursor):
    game = []

    # Gets the 5 easy questions for the Static Primary School game
    sql_Primary_T1 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'easy' AND Level = 1 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Primary_T1)
    for row in result:
        game.append(row)

    #save everything as variables
        
    # Gets the 5 medium questions for the Static Primary School game
    sql_Primary_T2 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'medium' and Level = 1 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Primary_T2)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 5 hard questions for the Static Primary School game
    sql_Primary_T3 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'hard' and Level = 1 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Primary_T3)
    #save everything as variables
    for row in result:
        game.append(row)

    return game


# This will run when a Static Secondary School game is selected. It will gather all questions for the game
def Static_Secondary_School(cursor):

    game = []

    # Gets the 5 easy questions for the Static Secondary School game
    sql_Secondary_T1 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'easy' AND Level = 2 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Secondary_T1)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Gets the 5 medium questions for the Static Secondary School game
    sql_Secondary_T2 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'medium' AND Level = 2 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Secondary_T2)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Gets the 5 hard questions for the Static Secondary School game
    sql_Secondary_T3 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'hard' AND Level = 2 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Secondary_T3)
    #save everything as variables 
    for row in result:
        game.append(row)

    return game


# This will run when a Static College game is selected. It will gather all questions for the game.
def Static_College(cursor):
    game = []

    # Gets the 5 easy questions for the Static College game
    sql_College_T1 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'easy' AND Level = 3 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_College_T1)
    #save everything as variables 
    for row in result:
        game.append(row)


    # Gets the 5 medium questions for the Static College game
    sql_College_T2 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'medium' AND Level = 3 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_College_T2)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 5 hard questions for the Static College game
    sql_College_T3 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'hard' AND Level = 3 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_College_T3)
    #save everything as variables
    for row in result:
        game.append(row)

    return game


# This will run when a Static Expert game is selected. It will gather all questions for the game
def Static_Expert(cursor):
    game = []

    # Gets the 5 easy questions for the Static Expert game
    sql_Expert_T1 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'easy' AND Level = 4 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Expert_T1)
    #save everything as variables
    for row in result:
        game.append(row)


    # Gets the 5 medium questions for the Static Expert game
    sql_Expert_T2 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'medium' AND Level = 4 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Expert_T2)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 5 hard questions for the Static Expert game
    sql_Expert_T3 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Difficulty, Level FROM millionaire WHERE Difficulty = 'hard' AND Level = 4 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Expert_T3)
    #save everything as variables
    for row in result:
        game.append(row)
    
    return game


# DYNAMIC
# This will run when a dynamic primary school game is selected. It will gather all questions for the game and then empty the dynamic table.
def Dynamic_Primary_School(cursor):
    game = []
    
    for i in range(0, 15):
        question_text = generation.generate_question("easy")

        try:
            question, answers, correct_answer = insert.parse_question_and_answers(question_text)
            insert.insert_question_into_db(question, answers, correct_answer)
            print("Question inserted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    # add questions from database to game
    sql_dynamic_primary = "SELECT * FROM dynamic LIMIT 15;"
    result = run_sql(cursor, sql_dynamic_primary)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Clear the dynamic table
    cursor.execute("TRUNCATE TABLE dynamic;")

    return game

# This will run when a dynamic secondary school game is selected. It will gather all questions for the game.
def Dynamic_Secondary_School(cursor):
    game = []
    
    for i in range(0, 15):
        question_text = generation.generate_question("medium")

        try:
            question, answers, correct_answer = insert.parse_question_and_answers(question_text)
            insert.insert_question_into_db(question, answers, correct_answer)
            print("Question inserted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    # add questions from database to game
    sql_dynamic_secondary = "SELECT * FROM dynamic LIMIT 15;"
    result = run_sql(cursor, sql_dynamic_secondary)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Clear the dynamic table
    cursor.execute("TRUNCATE TABLE dynamic;")

    return game

# This will run when a dynamic college game is selected. It will gather all questions for the game.
def Dynamic_College(cursor):
    game = []
    
    for i in range(0, 15):
        question_text = generation.generate_question("hard")

        try:
            question, answers, correct_answer = insert.parse_question_and_answers(question_text)
            insert.insert_question_into_db(question, answers, correct_answer)
            print("Question inserted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    # add questions from database to game
    sql_dynamic_college = "SELECT * FROM dynamic LIMIT 15;"
    result = run_sql(cursor, sql_dynamic_college)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Clear the dynamic table
    cursor.execute("TRUNCATE TABLE dynamic;")

    return game

# This will run when a dynamic expert game is selected. It will gather all questions for the game.
def Dynamic_Expert(cursor):
    game = []
    
    for i in range(0, 15):
        question_text = generation.generate_question("expert")

        try:
            question, answers, correct_answer = insert.parse_question_and_answers(question_text)
            insert.insert_question_into_db(question, answers, correct_answer)
            print("Question inserted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    # add questions from database to game
    sql_dynamic_expert = "SELECT * FROM dynamic LIMIT 15;"
    result = run_sql(cursor, sql_dynamic_expert)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Clear the dynamic table
    cursor.execute("TRUNCATE TABLE dynamic;")

    return game

#def main():
def export_questions(selection):
    # export questions from mysql based on a given level
    game = []
    try:
    
        f = open("cybermillionaire/util/mysqlPassword.txt")
        connection = mysql.connector.connect(host='db',
                                         database='Millionaire',
                                         user='root',
                                         password= f.read().strip())
        cursor = connection.cursor()
    
    except Error as e:
        print("Error reading data from MySQL table", e)
    
    if selection == '1':
        game = Static_Primary_School(cursor)

    elif selection == '2':
        game = Static_Secondary_School(cursor)

    elif selection == '3':
        game = Static_College(cursor)

    elif selection == '4':
        game = Static_Expert(cursor)

    elif selection == 'dynamic-1':
        game = Dynamic_Primary_School(cursor)

    elif selection == 'dynamic-2':
        game = Dynamic_Secondary_School(cursor)

    elif selection == 'dynamic-3':
        game = Dynamic_College(cursor)

    elif selection == 'dynamic-4':
        game = Dynamic_Expert(cursor)

    else:
        print("Invalid Level Selection!")
    
    generate_json(game)

    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")