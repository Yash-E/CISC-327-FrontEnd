class TaskManager:
    def __init__(self):
        #Import these fields from backend in backend portion
        self.users = {}  
        self.projects = {} 
        self.tasks = {} 


    def register_user(self, username, password):
        """
        Registers a user with the provided username and password.

        Parameters:
            username (str): The desired username for the new user.
            password (str): The password for the new user.

        Returns:
            bool: Returns True if the user is registered successfully. 
                Returns False if the username is already taken.

        """
        # Will be done for backend prototype
        print("Registered user " + username + " successfully")

        return True


    def login_user(self, username, password):
        """
        Logs in a user with the provided username and password.

        Parameters:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: Returns True if the user is logged in successfully. 
                Returns False if the login fails the login data does not match that of the database.

        """
        #Will be done for backend prototype
        print("Logged in user "+ username + " successfully")

        return True
    
    def view_tasks(self):
        """
        View tasks grouped by projects.
        """
        for project, tasks in self.projects.items():
            print(f"{project}:")
            for task_id in tasks:
                task_details = self.tasks.get(task_id)
                print(f"  - Task ID: {task_id}: {task_details['name']}")


    def create_task(self, priority, name, description, assignees, project, deadline):
        """
        Create a new task and add it to the task manager.

        Parameters:
            priority (int): The priority level of the task (1 to 10).
            name (str): The name of the task.
            description (str): The description of the task.
            assignees (list): A list of users assigned to the task.
            project (str): The name of the project to which the task belongs.
            deadline (str): The deadline for completing the task (formatted YYYY-MM-DD).

        Returns:
            int: The unique ID of the newly created task.
        """
        task_id = len(self.tasks) + 1
        task_details = {
            "priority": priority,
            "name": name,
            "description": description,
            "assignees": assignees,
            "project": project,
            "deadline": deadline
        }
        self.tasks[task_id] = task_details
        return task_id
        

    def create_project(self, project_name, project_description):
        """
        Create a new project.

        Args:
            project_name (str): The name of the project.
            project_description (str): The description of the project.

        Returns:
            None
        """
        if project_name in self.projects:
            print(f"Project '{project_name}' already exists.")
            return
        self.projects[project_name] = project_description
        print(f"Project '{project_name}' created successfully.")


    def edit_task(self):
        """
        Edit an existing task.

        Prompts the user for the ID of the task they want to edit and new details for the task.
        Updates the task with the specified ID with the new details.

        Parameters:
            None

        Returns:
            None
        """
        task_id = int(input("Enter the ID of the task you want to edit: "))
        if task_id not in self.tasks:
            print(f"Task with ID {task_id} does not exist.")
            return

        print("Enter new details for the task:")

        priority = int(input("Priority (1 to 10): "))
        name = input("Task Name: ")
        description = input("Task Description: ")
        assignees = input("Assignees (comma-separated list): ").split(',')
        project = input("Project Name: ")
        deadline = input("Task Deadline (YYYY-MM-DD): ")

        task_details = {
            "priority": priority,
            "name": name,
            "description": description,
            "assignees": assignees,
            "project": project,
            "deadline": deadline
        }

        self.tasks[task_id] = task_details
        print(f"Task with ID {task_id} edited successfully.")

    def delete_task(task_list, task_id):
        """
        Deletes a task with the specified task ID from the task list.

        Parameters:
            task_list (list): The list containing the tasks.
            task_id (int): The ID of the task to be deleted.

        Returns:
            bool: Returns True if the task is successfully deleted, 
                False if the task ID is not found.

        """
        for task in task_list:
            if task['id'] == task_id:
                task_list.remove(task)
                return True
        return False

    def edit_project(self):
        """
        Edit an existing project's description.

        Prompts the user for the name of the project they want to edit and the new description.
        Updates the project with the specified name with the new description.

        Parameters:
            None

        Returns:
            None
        """
        project_name = input("Enter the name of the project you want to edit: ")

        if project_name not in self.projects:
            print(f"Project '{project_name}' does not exist.")
            return

        new_description = input("Enter the new description: ")
        self.projects[project_name] = new_description
        print(f"Project '{project_name}' edited successfully.")

    def delete_project(self):
        """
        Delete an existing project.

        Prompts the user for the name of the project they want to delete.
        Asks for confirmation before deleting the project.
        Removes the project from the list of projects if confirmed.

        Parameters:
            None

        Returns:
            None
        """
        project_name = input("Enter the name of the project you want to delete: ")

        if project_name not in self.projects:
            print(f"Project '{project_name}' does not exist.")
            return

        confirmation = input(f"Are you sure you want to delete project '{project_name}'? (yes/no): ")

        if confirmation.lower() == 'yes':
            del self.projects[project_name]
            print(f"Project '{project_name}' deleted successfully.")
        else:
            print(f"Deletion of project '{project_name}' cancelled.")



def main():
    task_manager = TaskManager()

    task_manager.projects = {
        "Project 1": [1, 2],
        "Project 2": [3]
    }

    task_manager.tasks = {
        1: {
            "priority": 5,
            "name": "Clean the car",
            "description": "have to wash the car",
            "assignees": ["User1", "User2"],
            "project": "Project 1",
            "deadline": "2023-10-31"
        },
        2: {
            "priority": 8,
            "name": "Wash the dishes",
            "description": "was the dishes",
            "assignees": ["User3"],
            "project": "Project 1",
            "deadline": "2023-11-15"
        },
        3: {
            "priority": 3,
            "name": "Fix the roof",
            "description": "fix the leak in the roof",
            "assignees": ["User1"],
            "project": "Project 2",
            "deadline": "2023-11-20"
        }
    }


    while True:
        print("Welcome! Please choose an option:")
        print("1. Register an account")
        print("2. Login")
        print("3. Exit")  

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            if (task_manager.register_user(username, password)):
                print(f"User {username} registered successfully")
            else:
                print("Username is taken")

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if task_manager.login_user(username, password):
                print(f"Welcome, {username}!")
                while True:
                    print("Options:")
                    print("1. View tasks")
                    print("2. Create task")
                    print("3. Edit task")
                    print("4. Delete task")
                    print("5. Create project")
                    print("6. Edit project")
                    print("7. Delete project")
                    print("8. Logout")

                    command = input("Enter your command: ")

                    if command == "1":
                        task_manager.view_tasks()

                    elif command == "2":
                        priority = int(input("Enter priority (1 to 10): "))
                        name = input("Enter task name: ")
                        description = input("Enter task description: ")
                        assignees = input("Enter assignees (comma-separated list): ").split(',')
                        project = input("Enter project name: ")
                        deadline = input("Enter deadline (YYYY-MM-DD): ")
                        task_manager.create_task(priority, name, description, assignees, project, deadline)

                    elif command == "3":
                        priority = int(input("Enter priority (1 to 10): "))
                        name = input("Enter task name: ")
                        description = input("Enter task description: ")
                        assignees = input("Enter assignees (comma-separated list): ").split(',')
                        project = input("Enter project name: ")
                        deadline = input("Enter deadline (YYYY-MM-DD): ")
                        task_manager.edit_task(priority, name, description, assignees, project, deadline)

                    elif command == "4":
                        task_id = int(input("Enter the ID of the task you want to delete: "))
                        if task_manager.delete_task(task_id):
                            print(f"Task with ID {task_id} deleted successfully.")
                        else:
                            print(f"No task found with ID {task_id}.")

                    elif command == "5":
                        project_name = input("Enter project name: ")
                        project_description = input("Enter project description: ")
                        task_manager.create_project(project_name, project_description)

                    elif command == "6":
                        task_manager.edit_project()

                    elif command == '7':
                        task_manager.delete_project()
                        
                    elif command == "8":
                        break
            else:
                print("Invalid username or password.")
        elif choice == "3":
            break  

if __name__ == "__main__":
    main()
