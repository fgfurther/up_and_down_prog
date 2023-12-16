class ChatBot:
    def __init__(self):
        self.state = "main_menu"
        self.tasks = {}
        self.subordinates = {}
        self.current_task = None
        self.current_subordinate = None

        self.states = {
            "main_menu": {
                "display_menu": self.display_main_menu,
                "process_input": self.process_main_menu_input
            },
            "task_confirm": {
                "display_menu": self.display_task_confirm_menu,
                "process_input": self.process_task_confirm_input
            },
            "assign_choose": {
                "display_menu": self.display_assign_choose_menu,
                "process_input": self.process_assign_choose_input
            },
            "assign_confirm": {
                "display_menu": self.display_assign_confirm_menu,
                "process_input": self.process_assign_confirm_input
            }
        }

    def set_state(self, new_state):
        self.state = new_state

    def display_main_menu(self):
        print("Main Menu:")
        print("1. Создать задачу")
        print("2. Просмотреть все задачи")
        print("3. Выйти")

    def process_main_menu_input(self):
        user_input = input("Enter your choice: ")
        if user_input == "1":
            self.create_task()
            self.set_state("task_confirm")
        elif user_input == "2":
            self.display_subordinates()
        elif user_input == "3":
            exit()
        else:
            print("Invalid input. Try again.")

    def display_task_confirm_menu(self):
        print("Task_confirm Menu:")
        print("1. Подтвердить задачу")
        print("2. Редактировать задачу")
        print("3. Выйти в меню")

    def process_task_confirm_input(self):
        user_input = input("Enter your choice: ")
        if user_input == "1":
            self.confirm_task()
            self.set_state("assign_choose")
        elif user_input == "2":
            self.edit_task()
        elif user_input == "3":
            self.set_state("main_menu")
        else:
            print("Invalid input. Try again.")

    def display_assign_choose_menu(self):
        print("Выберите сотрудника:")
        print("1. Bim")
        print("2. Dim")
        print("3. Gim")

    def process_assign_choose_input(self):
        user_input = input("Enter your choice: ")
        if user_input in ["1", "2", "3"]:
            self.current_subordinate = int(user_input)
            self.set_state("assign_confirm")
        else:
            print("Invalid input. Try again.")

    def display_assign_confirm_menu(self):
        print("Assign_confirm Menu:")
        print("1. Подтвердить сотрудника")
        print("2. Выбрать другого")
        print("3. Выйти в меню")

    def process_assign_confirm_input(self):
        user_input = input("Enter your choice: ")
        if user_input == "1":
            self.assign_task()
            self.confirm_assignment()
            self.set_state("main_menu")
        elif user_input == "2":
            self.set_state("assign_choose")
        elif user_input == "3":
            self.set_state("main_menu")
        else:
            print("Invalid input. Try again.")

    def create_task(self):
        task_name = input("Имя задачи: ")
        task_description = input("Enter task description: ")
        self.tasks[task_name] = task_description
        print(f"Task '{task_name}' created successfully.")
        self.current_task = task_name

    def assign_task(self):
        subordinate_id = self.current_subordinate
        task_id = self.current_task
        if subordinate_id not in self.subordinates:
            self.subordinates[subordinate_id] = [task_id]
        else:
            self.subordinates[subordinate_id].append(task_id)
        print(f"Task '{task_id}' assigned to subordinate '{subordinate_id}'.")

    def confirm_task(self):
        print("Task confirmed successfully.")

    def edit_task(self):
        new_task_name = input("Enter new name: ")
        new_description = input("Enter new task description: ")
        self.tasks[new_task_name] = new_description
        self.tasks.pop(self.current_task, None)
        print("Task edited successfully.")
        self.current_task = new_task_name

    def confirm_assignment(self):
        print("Assignment confirmed successfully.")

    def edit_assignment(self):
        new_task_id = input("Enter new subord ID: ")
        self.current_subordinate = new_task_id
        print("Assignment edited successfully.")

    def display_subordinates(self):
        print("Subordinates:")
        for subordinate_id, subordinate_name in self.subordinates.items():
            print(f"{subordinate_id}. {subordinate_name}")

    def run(self):
        while True:
            state_functions = self.states[self.state]
            state_functions["display_menu"]()
            state_functions["process_input"]()




if __name__ == "__main__":
    chat_bot = ChatBot()
    chat_bot.run()
