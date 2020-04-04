import mysql.connector
from mysql.connector import Error
import json

# Executes all export functionality
#class Export:
#    def run_sql(self, query):
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

    with open('test.json','w') as outfile:
        json.dump(json_file, outfile)

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

# This will run when a K-8th game is selected. It will gather all questions for the game       
def K_8th(cursor):
    game = []

    # Gets the 5 Tier 1 questions for the K-8th game
    sql_K_8th_T1 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 1 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_K_8th_T1)
    for row in result:
        game.append(row)

    #save everything as variables
        
    # Gets the 5 Tier 2 questions for the K-8th game
    sql_K_8th_T2 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 2 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_K_8th_T2)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 3 Tier 3 questions for the K-8th game
    sql_K_8th_T3 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 3 ORDER BY rand() LIMIT 3;"
    result = run_sql(cursor, sql_K_8th_T3)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 1 Tier 4 question for the K-8th game
    sql_K_8th_T4 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 4 ORDER BY rand() LIMIT 1;"
    result = run_sql(cursor, sql_K_8th_T4)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 1 Tier 5 question for the K-8th game
    sql_K_8th_T5 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 5 ORDER BY rand() LIMIT 1;"
    result = run_sql(cursor, sql_K_8th_T5)
    #save everything as variables
    for row in result:
        game.append(row)

    #remove this print later, just using for test2ing now
    #print("K-8th Selected!")
    #print(game)

    return game
    #TODO: Run method for JSON creation/formatting here
    #Jump to error processing shit


# This will run when a High School game is selected. It will gather all questions for the game
def HighSchool(cursor):

    game = []

    # Gets the 5 Tier 1 questions for the High School game
    sql_HS_T1 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 6 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_HS_T1)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Gets the 5 Tier 2 questions for the High School game
    sql_HS_T2 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 7 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_HS_T2)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Gets the 3 Tier 3 questions for the High School game
    sql_HS_T3 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 8 ORDER BY rand() LIMIT 3;"
    result = run_sql(cursor, sql_HS_T3)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Gets the 1 Tier 4 question for the High School game
    sql_HS_T4 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 9 ORDER BY rand() LIMIT 1;"
    result = run_sql(cursor, sql_HS_T4)
    #save everything as variables 
    for row in result:
        game.append(row)

    # Gets the 1 Tier 5 question for the High School game
    sql_HS_T5 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 10 ORDER BY rand() LIMIT 1;"
    result = run_sql(cursor, sql_HS_T5)
    #save everything as variables 
    for row in result:
        game.append(row)

    #remove this print later, just using for testing now
    #print("High School Selected!")
    #print(game)

    return game

    #TODO: Run method for JSON creation/formatting here
    #Jump to error processing shit


# This will run when a Non-Technical College game is selected. It will gather all questions for the game.
def College_NonTech(cursor):
    game = []

    # Gets the 5 Tier 1 questions for the Non-Technical College game
    sql_nonTech_T1 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 11 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_nonTech_T1)
    #save everything as variables 
    for row in result:
        game.append(row)


    # Gets the 5 Tier 2 questions for the Non-Technical College game
    sql_nonTech_T2 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 12 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_nonTech_T2)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 3 Tier 3 questions for the Non-Technical College game
    sql_nonTech_T3 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 13 ORDER BY rand() LIMIT 3;"
    result = run_sql(cursor, sql_nonTech_T3)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 1 Tier 4 question for the Non-Technical College game
    sql_nonTech_T4 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 14 ORDER BY rand() LIMIT 1;"
    result = run_sql(cursor, sql_nonTech_T4)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 1 Tier 5 question for the Non-Technical College game
    sql_nonTech_T5 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 15 ORDER BY rand() LIMIT 1;"
    result = run_sql(cursor, sql_nonTech_T5)
    #save everything as variables
    for row in result:
        game.append(row)

    #remove this print later, just using for test2ing now
    #print("College Non-Tech Selected!")
    #print(game)

    return game
    #TODO: Run method for JSON creation/formatting here
    #Jump to error processing shit


# This will run when a Technical College game is selected. It will gather all questions for the game
def College_Tech(cursor):
    game = []

    # Gets the 5 Tier 1 questions for the Technical College game
    sql_Tech_T1 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 16 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Tech_T1)
    #save everything as variables
    for row in result:
        game.append(row)


    # Gets the 5 Tier 2 questions for the Technical College game
    sql_Tech_T2 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 17 ORDER BY rand() LIMIT 5;"
    result = run_sql(cursor, sql_Tech_T2)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 3 Tier 3 questions for the Technical College game
    sql_Tech_T3 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 18 ORDER BY rand() LIMIT 3;"
    result = run_sql(cursor, sql_Tech_T3)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 1 Tier 4 question for the Technical College game
    sql_Tech_T4 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 19 ORDER BY rand() LIMIT 1;"
    result = run_sql(cursor, sql_Tech_T4)
    #save everything as variables
    for row in result:
        game.append(row)

    # Gets the 1 Tier 5 question for the Technical College game
    sql_Tech_T5 = "select Question, Ans1, Ans2, Ans3, Ans4, Correct, Rank FROM test2 WHERE Rank = 20 ORDER BY rand() LIMIT 1;"
    result = run_sql(cursor, sql_Tech_T5)
    #save everything as variables
    for row in result:
        game.append(row)

    #remove this print later, just using for test2ing now
    #print("College Tech Selected!")
    #print(game)
    return game

    #TODO: Run method for JSON creation/formatting here
    #Jump to error processing shit


#def main():
def export_questions(selection):
    # export questions from mysql based on a given level
    game = []
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='Millionaire',
                                         user='root',
                                         password='password')

        cursor = connection.cursor()
    
    except Error as e:
        print("Error reading data from MySQL table", e)
    
    #temporary way of controlling which level we want to select
    #selection = input("Which level would you like to play (1-4)? ")
    
    if selection == '1':
        game = K_8th(cursor)

    elif selection == '2':
        game = HighSchool(cursor)

    elif selection == '3':
        game = College_NonTech(cursor)

    elif selection == '4':
        game = College_Tech(cursor)

    else:
        print("Invalid Level Selection!")
    
    generate_json(game)

    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

#main()
