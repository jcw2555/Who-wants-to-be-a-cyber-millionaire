# Description

Welcome to our project, Who Wants to Be a Cyber Millionaire. The goal of our project is to provide cybersecurity education
 while presenting it in a fun platform, accessible to all audiences. The game play just like the popular game show Who Wants to Be a Millionaire; You will answer increasing more challenging questions until you either lose or win it all! Our game provides 4 different difficulty levels depending on educational background: K-8th Grade, High School, College+, and College+ Technical Background. We hope you enjoy our game!
 
Special thank you to aaronech, whose project was refactored to fit our needs. His project can be found here: https://github.com/aaronnech/Who-Wants-to-Be-a-Millionaire
# Usage

This game uses mysql to house the question bank, python's flask library to host the web server, and HTML and Javascript for the web application itself.

Before running the game, you must make sure you set up the proper mysql database and that it can communicate with export.py. export.py is the script which will query the database and generate a JSON file depending on which level the user chooses. Our team plans on developing a bash script to install all dependencies and set up the mysql database properly at later stages of the project.

To run the game, simply execute the command: python ajax_test.py and then navigate to http:127.0.0.1:5000 on your browser. From here, select the difficulty you wish to play on and then press start!

# Question format

The question bank is simply an array of "games". You can have as many "games" as you like. You select them at the beginning of loading index.html.

	{
		"games" : [
			{
				"questions" : [ ... ]
			},
			{
				"questions" : [ ... ]
			}, ...
		]
	}

Each array of questions is in the following format.

1.	"content" is the key for the possible answer texts. "content" must have a length of 4 (4 multiple choices).
2.	The question prompt text is located in the key "question"
3.	The zero-based index of the value in "content" that is the correct answer is located in the key "correct"



	    {
	        "question" : "What is Aurora Borealis commonly known as?",
	        "content" : [
	            "Fairy Dust",
	            "Northern Lights",
	            "Book of ages",
	            "a Game of Thrones main character"
	        ],
	        "correct" : 1
	    }


# Who Wants to Be a Millionaire Materials

The sounds and images used from Who Wants to Be a Millionaire, and the questions used from India-Bix and other sources are not mine, nor do I claim any involvement in their creation. The materials are used under Fair Use for academic and educational purpose, and should not be redistributed otherwise without permission from their creators.


