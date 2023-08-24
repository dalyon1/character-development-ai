import os

def gather_character_information():
    questions = {
        "Basic Information": {
            "Character name": "",
            "Age": "",
            "Nationality": "",
            "Home town": "",
            "Current residence": "",
            "Occupation": "",
            "Income and salary": "",
            "Talents and skills": "",
        },
        "Background as a Child": {
            "Birth order": "",
            "Brothers and sisters (describe relationship)": "",
            "Husband or wife (describe relationship)": "",
            "Children (describe relationship)": "",
            "Grandparents (describe relationship)": "",
            "Grandchildren (describe relationship)": "",
            "Significant others (describe relationship)": "",
            "Relationship skills": "",
        },
        "Physical Characteristics": {
            "Height": "",
            "Weight": "",
            "Race": "",
            "Hair colour": "",
            "Eye colour": "",
            "Glasses or contact lenses?": "",
            "Skin colour": "",
            "Shape of face": "",
            "Distinguishing features": "",
            "Disabilities": "",
            "Dress style": "",
            "Physical habits (drinking, smoking etc.)": "",
            "Mannerisms": "",
            "Health": "",
            "Hobbies": "",
        },
        "Speech and Personality": {
            "Speech patterns": "",
            "Favourite sayings": "",
            "Style": "",
            "Greatest flaw": "",
            "Best quality": "",
            "Introvert or extrovert?": "",
            "Educational background": "",
            "Learning experiences": "",
            "Intelligence level": "",
            "Mental health": "",
            "Short-term goals": "",
            "Long-term goals": "",
            "How does your character see themselves?": "",
            "How does your character believe they are perceived by others?": "",
            "How confident is your character?": "",
            "How emotional is your character?": "",
            "How logical is your character?": "",
            "What would most embarrass your character?": "",
        },
        "Emotional Characteristics": {
            "Strengths": "",
            "Weaknesses": "",
            "How does the character deal with conflict?": "",
            "How does the character deal with sadness?": "",
            "How does the character deal with change?": "",
            "How does the character deal with loss?": "",
            "What does the character want out of life?": "",
            "What would the character like to change in his or her life?": "",
            "What motivates this character?": "",
            "What frightens this character?": "",
            "What makes this character happy?": "",
            "Is the character judgmental of others?": "",
            "Is the character generous or stingy?": "",
            "Is the character generally polite or rude?": "",
        },
        "Spiritual Characteristics": {
            "Does the character believe in a god?": "",
            "What are the character’s spiritual beliefs?": "",
            "Is religion or spirituality a part of this character’s life?": "",
            "How does this character’s spirituality manifest itself in daily life?": "",
        },
    }
    
    for category, category_questions in questions.items():
        print(f"\n{category}:")
        for question in category_questions:
            response = input(question + ": ")
            category_questions[question] = response
    
    return questions

def main():
    character_profile = gather_character_information()
    
    # Get the character name
    character_name = character_profile["Basic Information"]["Character name"]

    # Create a folder named "character profile" if it doesn't exist
    folder_name = "character profile"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # Create or overwrite a file with the character profile
    file_path = os.path.join(folder_name, character_name + ".txt")
    with open(file_path, "w") as file:
        for category, category_questions in character_profile.items():
            file.write(f"{category}:\n")
            for question, answer in category_questions.items():
                file.write(f"{question}: {answer}\n")
            file.write("\n")

    print("Character profile saved to:", file_path)

if __name__ == "__main__":
    main()
