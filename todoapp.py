class Todo:
    todos: list = []

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add_todo(self) -> None:
        """
        Adds a new todo item to the Todo.todos list.

        This function appends the current Todo object to the Todo.todos list, which serves as a collection of all todo items. It also prints a message indicating that a todo item has been added, along with the name and description of the item.

        Parameters:
            self: The current instance of the Todo class.

        Returns:
            None
        """
        Todo.todos.append(self)
        print(f"Todo added: Name: {self.name}, Description: {self.description}")

    def remove_todo(self):
        """
        Removes the current todo object from the Todo.todos list.
        """
        Todo.todos.remove(self)

    def remove_todo_by_name(self, name):
        """
        Removes the todo with the specified name from the Todo.todos list.
        """
        todos_to_remove = [todo for todo in Todo.todos if todo.name == name]
        if todos_to_remove:
            for todo in todos_to_remove:
                todo.remove_todo()
                print(f"Todo removed: Name: {todo.name}, Description: {todo.description}")
        else:
            print("Todo not found")

    @staticmethod
    def show_todos() -> None:
        """
        Displays all the todos in the Todo.todos list.
        """
        if len(Todo.todos) == 0:
            print("No todos to show")
        for todo in Todo.todos:
            print(f"Name: {todo.name}, Description: {todo.description}")

    @staticmethod
    def menu() -> None:
        """
        Print a menu of options for the user to choose from.

        Parameters:
            None

        Returns:
            None
        """
        print("Choose an option")
        menu_options = ["Add todo", "remove todo", "Show todos", "Exit"]
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")
            print("________________")

    @staticmethod
    def handle_choice():
        """
        Handles the user's choice by prompting for an option and executing the corresponding action.

        Parameters:
            None

        Returns:
            None
        """
        choose = int(input("Choose an option: "))
        if choose == 1:
            print("Add todo")
            name = input("Name: ")
            description = input("Description: ")
            new_todo = Todo(name, description)
            new_todo.add_todo()
        if choose == 2:
            print("Remove todo")
            name = input("Name: ")
            new_todo = Todo(name, "")
            new_todo.remove_todo_by_name(name)
        if choose == 3:
            print("Show todos")
            Todo.show_todos()


def main():
    """
    Executes the main logic of the program.

    This function calls the `menu` method of the `Todo` class to display the menu options to the user.
    It then enters an infinite loop where it repeatedly calls the `handle_choice` method of the `Todo` class to handle the user's choice.

    Parameters:
        None

    Returns:
        None
    """
    Todo.menu()
    while True:
        Todo.handle_choice()


if __name__ == "__main__":
    main()
