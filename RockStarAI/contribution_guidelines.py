def contributeToProject(user, contribution):
    """
    Function to handle user contributions to the project.
    """
    contributionStatus = "Pending"
    try:
        # Validate the user's contribution
        validateContribution(contribution)

        # Process the user's contribution
        processContribution(user, contribution)

        # Update the contribution status
        contributionStatus = "Acknowledged"
    except Exception as e:
        print(f"Error in contribution: {str(e)}")
        contributionStatus = "Failed"

    return contributionStatus


def validateContribution(contribution):
    """
    Function to validate the user's contribution.
    """
    # Check if the contribution is not empty
    if not contribution:
        raise ValueError("Contribution cannot be empty.")

    # Check if the contribution is of valid type
    if not isinstance(contribution, dict):
        raise TypeError("Contribution must be a dictionary.")

    # Check if the contribution has all the required keys
    required_keys = ["title", "description", "code"]
    if not all(key in contribution for key in required_keys):
        raise ValueError("Contribution must have a title, description, and code.")


def processContribution(user, contribution):
    """
    Function to process the user's contribution.
    """
    # Add the user's contribution to the contributions database
    contributions_db = loadContributionsDB()
    contributions_db.append({
        "user": user,
        "title": contribution["title"],
        "description": contribution["description"],
        "code": contribution["code"],
        "status": "Pending"
    })
    saveContributionsDB(contributions_db)


def loadContributionsDB():
    """
    Function to load the contributions database.
    """
    # Load the contributions database from a file
    with open("contributions_db.json", "r") as file:
        contributions_db = json.load(file)
    return contributions_db


def saveContributionsDB(contributions_db):
    """
    Function to save the contributions database.
    """
    # Save the contributions database to a file
    with open("contributions_db.json", "w") as file:
        json.dump(contributions_db, file)