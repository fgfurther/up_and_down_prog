import threading
import time
import random
from queue import Queue, Empty


class Commander:
    def __init__(self, command_queue):
        self.target_discovered = False
        self.command_queue = command_queue

    def discover_target(self):
        # Имитация обнаружения цели командиром
        time.sleep(2)
        print("Цель обнаружена!")

        # Отправка команды "ATTACK" в очередь три раза с интервалами
        for _ in range(3):
            self.command_queue.put("ATTACK")
            time.sleep(2)


class Soldier:
    def __init__(self, name, command_queue, lock):
        self.name = name
        self.command_queue = command_queue
        self.lock = lock

    def receive_command(self):
        while True:
            # Захват блокировки для безопасного доступа к общим данным
            self.lock.acquire()
            try:
                # Попытка получить команду из очереди
                command = self.command_queue.get_nowait()
                if command == "ATTACK":
                    # Вывод сообщения о получении команды атаковать
                    print(f"{self.name}: Получил команду атаковать!")
                    break
            except Empty:
                pass
            finally:
                # Освобождение блокировки
                self.lock.release()

    def choose_vehicle(self):
        # Имитация выбора машины
        time.sleep(random.randint(1, 3))

        # Захват блокировки
        self.lock.acquire()
        try:
            print(f"{self.name}: Выбрал машину")
        finally:
            # Освобождение блокировки
            self.lock.release()


def main():
    # Создание очереди и блокировки для обеспечения безопасности работы с данными
    command_queue = Queue()
    lock = threading.Lock()

    # Создание объекта командира и солдатов
    commander = Commander(command_queue)
    soldiers = [Soldier(f"Солдат {i}", command_queue, lock) for i in range(3)]

    # Создание потока для discover_target
    discovery_thread = threading.Thread(target=commander.discover_target)
    discovery_thread.start()

    # Создание потоков для receive_command и choose_vehicle
    soldier_threads = [threading.Thread(target=s.receive_command) for s in soldiers]
    vehicle_threads = [threading.Thread(target=s.choose_vehicle) for s in soldiers]

    # Запуск всех потоков
    for t in soldier_threads + vehicle_threads:
        t.start()

    # Ожидание завершения receive_command солдат
    for t in soldier_threads:
        t.join()

    # Ожидание завершения choose_vehicle солдат
    for t in vehicle_threads:
        t.join()


if __name__ == "__main__":
    main()
