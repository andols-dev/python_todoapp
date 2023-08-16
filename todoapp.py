class Todo:
    menu_options = ["Add Todo", "Remove Todo", "Exit"]

    @staticmethod
    def menu() -> None:
        print("What would you like to do?")
        for index, option in enumerate(Todo.menu_options, start=1):
            print(f"{index}. {option}")
            print("____________________")


def main():
    Todo.menu()


if __name__ == "__main__":
    main()