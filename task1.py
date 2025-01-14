from queue import Queue
import time

def process_requests():
    service_queue = Queue()
    # Додаємо заявки до черги
    for i in range(1, 6):
        request = f"Заявка #{i}"
        print(f"Додано: {request}")
        service_queue.put(request)  
        time.sleep(0.5) 

    print("\nОбробка заявок:")
    # Обробляємо заявки
    while not service_queue.empty():
        current_request = service_queue.get() 
        print(f"Обробляється: {current_request}")
        time.sleep(1)  

process_requests()
