# Teamo AI Skill Matching System

## Overview
Teamo AI is a skill matching system that compares user-submitted skills with an administrator's curated list of skills. The system uses various fuzzy matching algorithms to calculate the similarity score and returns the best matching skills to the user.

This project includes:
- A Python implementation of the Teamo AI system
- An ER diagram illustrating the database structure
- Features such as adding, updating, and deleting skills (admin only)
- User-submitted skill matching with fuzzy matching logic

## Features
- **Skill Management (Admin only)**: Add, update, or delete skills in the administrator list.
- **Skill Matching**: Match user-submitted skills to the administrator list using fuzzy matching techniques.
- **User Queries**: Users can submit a skill for matching and receive a list of matching skills with scores.
- **Match Result Storage**: The system stores match results, including matching method and score, for later review.


### Prerequisites
Ensure that you have Python 3.x installed on your system. You will also need to install the following Python package:
- "fuzzywuzzy" for fuzzy string matching.

## How to Run

1. Clone the repository to your local machine using Git:
   -bash
   git clone https://github.com/stolee2/Teamo_ai.git
   
2.Navigate to the project directory:
  -cd teamo-ai
  
3.Install the required dependencies:
-bash
pip install fuzzywuzzy

4.Run the Python script to start the Teamo AI Skill Matching System:
-bash
python app.py

