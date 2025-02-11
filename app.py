from fuzzywuzzy import fuzz
from data import administrator_skills, users, queries, match_results


def is_admin(username):
    """Check if the user is an admin."""
    for user in users:
        if user["username"] == username and user["role"] == "admin":
            return True
    return False


def add_skill(username, skill):
    """Add a new skill (admin only)."""
    if is_admin(username):
        if skill not in administrator_skills:
            administrator_skills.append(skill)
            print(f"New skill added: {skill}")
        else:
            print(f"Skill '{skill}' already exists.")
    else:
        print("Access Denied. Admin privileges required.")


def update_skill(username, old_skill, new_skill):
    """Update a skill (admin only)."""
    if is_admin(username):
        if old_skill in administrator_skills:
            index = administrator_skills.index(old_skill)
            administrator_skills[index] = new_skill
            print(f"Skill updated: {old_skill} -> {new_skill}")
        else:
            print(f"Skill '{old_skill}' not found.")
    else:
        print("Access Denied. Admin privileges required.")


def delete_skill(username, skill):
    """Delete a skill (admin only)."""
    if is_admin(username):
        if skill in administrator_skills:
            administrator_skills.remove(skill)
            print(f"Skill '{skill}' deleted.")
        else:
            print(f"Skill '{skill}' not found.")
    else:
        print("Access Denied. Admin privileges required.")


def match_skill(input_skill):
    """Match input skill with the administrator's skills."""
    matched_skills = []
    for skill in administrator_skills:
        ratio = fuzz.partial_ratio(input_skill.lower(), skill.lower()) / 100  # Fuzzy match score
        if ratio >= 0.5: 
            matched_skills.append((skill, ratio))
    
    return matched_skills


def submit_query(user, input_skill):
    """Submit a query for matching skills."""
    query = {"user": user, "input_skill": input_skill}
    queries.append(query)

    matched_skills = match_skill(input_skill)
    for matched_skill, score in matched_skills:
        match_results.append({
            "user": user,
            "input_skill": input_skill,
            "matched_skill": matched_skill,
            "method": "partial" if score < 1.0 else "exact",
            "score": score
        })
    return matched_skills


def show_results():
    """Display all match results."""
    print("\nMatch Results:")
    for result in match_results:
        print(result)

def main():
    print("Welcome to Teamo AI Skill Matching System!\n")
    
    while True:
        print("\nChoose an option:")
        print("1. Add Skill (Admin Only)")
        print("2. Update Skill (Admin Only)")
        print("3. Delete Skill (Admin Only)")
        print("4. Submit Skill Query")
        print("5. Show Match Results")
        print("6. Exit")
        
        choice = input("\nEnter choice: ")

        if choice == '1':
            username = input("Enter admin username: ")
            skill = input("Enter skill to add: ")
            add_skill(username, skill)

        elif choice == '2':
            username = input("Enter admin username: ")
            old_skill = input("Enter skill to update: ")
            new_skill = input("Enter new skill: ")
            update_skill(username, old_skill, new_skill)

        elif choice == '3':
            username = input("Enter admin username: ")
            skill = input("Enter skill to delete: ")
            delete_skill(username, skill)

        elif choice == '4':
            user = input("Enter your username: ")
            input_skill = input("Enter skill for matching: ")
            matched_skills = submit_query(user, input_skill)
            print(f"\nMatched skills for '{input_skill}': {matched_skills}")

        elif choice == '5':
            show_results()

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
