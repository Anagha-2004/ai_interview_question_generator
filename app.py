import random

# Predefined sample prompts and questions
QUESTIONS_DB = {
    "data analyst": [
        "How would you handle missing or inconsistent data in a dataset?",
        "Explain the difference between supervised and unsupervised learning.",
        "How do you decide which visualization to use for your data?",
        "Describe a time you improved a business decision with data analysis.",
        "What is your experience with SQL and querying large datasets?"
    ],
    "software developer": [
        "Explain the principles of object-oriented programming.",
        "How do you ensure code quality in large projects?",
        "What is the difference between REST and SOAP APIs?",
        "Describe a challenging bug you resolved and how.",
        "How do you stay updated with new technologies?"
    ],
    "ui ux designer": [
        "How do you conduct user research before starting a design?",
        "Explain the importance of accessibility in design.",
        "Describe a project where you improved user experience.",
        "What tools do you prefer for prototyping and why?",
        "How do you handle feedback from clients or stakeholders?"
    ]
}

def generate_questions(role):
    role_key = role.lower()
    questions = QUESTIONS_DB.get(role_key)
    if not questions:
        print(f"Sorry, I don't have questions for '{role}'.")
        return []
    return random.sample(questions, k=5)

def main():
    print("=== AI Interview Question Generator ===")
    print("Available roles:")
    for r in QUESTIONS_DB.keys():
        print(f"- {r.title()}")

    role = input("\nEnter a job role from the list: ").strip()
    questions = generate_questions(role)

    if questions:
        print("\nGenerated Interview Questions:\n")
        for i, q in enumerate(questions, start=1):
            print(f"{i}. {q}")

        save = input("\nDo you want to save these questions to a file? (y/n): ").strip().lower()
        if save == "y":
            filename = f"output_{role.replace(' ', '_')}.txt"
            with open(filename, "w") as f:
                for i, q in enumerate(questions, start=1):
                    f.write(f"{i}. {q}\n")
            print(f"Questions saved to '{filename}'.")

if __name__ == "__main__":
    main()
