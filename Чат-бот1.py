class ChatBot:
    state = "main_menu"
    tasks = {}
    subordinates = {}
    current_task = None
    current_subordinate = None

    @classmethod
    def display_main_menu(cls):
        print("Main Menu:")
        print("1. Создать задачу")
        print("2. Просмотреть все задачи")
        print("3. Выйти")


    @classmethod
    def process_input(cls):

        if cls.state == "main_menu":
            user_input = input("Enter your choice: ")
            if user_input == "1":
                cls.create_task()
            elif user_input == "2":
                cls.display_subordinates()
            elif user_input == "3":
                exit()
            else:
                print("Invalid input. Try again.")


        elif cls.state == "task_confirm":
            print("Task_confirm Menu:")
            print("1. Подтвердить задачу")
            print("2. Редактировать задачу")
            print("3. Выйти в меню")
            user_input2 = input("Enter your choice: ")
            if user_input2 == "1":
                cls.confirm_task()
                cls.state = "assign_choose"
            elif user_input2 == "2":
                cls.edit_task()
            elif user_input2 == "3":
                cls.state = "main_menu"
            else:
                print("Invalid input. Try again.")


        elif cls.state == "assign_choose":
            print("Выберите сотрудника:")
            print("1. Bim")
            print("2. Dim")
            print("3. Gim")
            user_input2 = input("Enter your choice: ")
            if user_input2 == "1":
                cls.current_subordinate = 1

                cls.state = "assign_confirm"
            elif user_input2 == "2":
                cls.current_subordinate = 2
                cls.state = "assign_confirm"
            elif user_input2 == "3":
                cls.current_subordinate = 3
                cls.state = "assign_confirm"
            else:
                print("Invalid input. Try again.")


        elif cls.state == "assign_confirm":
            print("Assign_confirm Menu:")
            print("1. Подтвердить сотрудника")
            print("2. Выбрать другого")
            print("3. Выйти в меню")
            user_input2 = input("Enter your choice: ")
            if user_input2 == "1":
                cls.assign_task()
                cls.confirm_assignment()
                cls.state = "main_menu"
            elif user_input2 == "2":
                cls.edit_assignment()
            elif user_input2 == "3":
                cls.state = "main_menu"
            else:
                print("Invalid input. Try again.")

    @classmethod
    def create_task(cls):
        task_name = input("Имя задачи: ")
        task_description = input("Enter task description: ")
        cls.tasks[task_name] = task_name
        print(f"Task '{task_name}' created successfully.")
        cls.state = "task_confirm"
        cls.current_task = task_name

    @classmethod
    def assign_task(cls):
        subordinate_id = cls.current_subordinate
        task_id = cls.current_task
        if subordinate_id not in cls.subordinates:
            cls.subordinates[subordinate_id] = [task_id]
        else:
            cls.subordinates[subordinate_id].append(task_id)
        print(f"Task '{task_id}' assigned to subordinate '{subordinate_id}'.")
        cls.state = "assign_confirm"

    """@classmethod
    def view_tasks(cls):
        cls.display_subordinates()
        subordinate_id = input("Enter subordinate ID: ")
        tasks_for_subordinate = cls.subordinates.get(subordinate_id, [])
        if tasks_for_subordinate:
            print(f"Tasks for subordinate '{subordinate_id}':")
            for task_id in tasks_for_subordinate:
                task_description = cls.tasks.get(task_id, "Task not found")
                print(f"  - {task_id}: {task_description}")
        else:
            print(f"No tasks assigned to subordinate '{subordinate_id}'.")"""

    @classmethod
    def confirm_task(cls):
        print("Task confirmed successfully.")
        cls.state = "assign_choose"

    @classmethod
    def edit_task(cls):
        new_task_name = input("Enter new name: ")
        new_description = input("Enter new task description: ")
        cls.tasks[new_task_name] = new_description
        # Удаляем старую задачу (если она существует)
        cls.tasks.pop(cls.current_task, None)
        print("Task edited successfully.")
        cls.current_task = new_task_name

    @classmethod
    def confirm_assignment(cls):
        print("Assignment confirmed successfully.")

    @classmethod
    def edit_assignment(cls):
        new_task_id = input("Enter new subord ID: ")
        cls.current_subordinate = new_task_id
        print("Assignment edited successfully.")

    @classmethod
    def display_subordinates(cls):
        print("Subordinates:")
        for subordinate_id, subordinate_name in cls.subordinates.items():
            print(f"{subordinate_id}. {subordinate_name}")

    @classmethod
    def run(cls):
        while True:
            if cls.state == "main_menu":
                cls.display_main_menu()


            cls.process_input()


if __name__ == "__main__":
    ChatBot.run()
