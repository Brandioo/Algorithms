from queue import Queue
import threading
import time


def place_order(orders_queue, orders: list[str]):
    for order in orders:
        time.sleep(0.5)
        orders_queue.put(order)
        print(f'New order placed for: {order}.')


def cook_food(orders_queue, cooked_foods_queue, chef_name: str):
    while True:
        cook_order = orders_queue.get()
        time.sleep(1.5)
        orders_queue.task_done()
        cooked_foods_queue.put(cook_order)
        print(f'{cook_order.title()} is cooked by chef {chef_name.title()}.')


def deliver_food(cooked_foods_queue, delivery_guy_name: str):
    while True:
        food_to_deliver = cooked_foods_queue.get()
        time.sleep(2.5)
        cooked_foods_queue.task_done()
        print(
            f'{delivery_guy_name.title()} got the {food_to_deliver.title()}'
            f' and is delivering it to your home'
        )


orders_q = Queue()
cooked_foods_q = Queue()

for chef in ['Alex', 'Mateo']:
    worker = threading.Thread(target=cook_food, args=(orders_q, cooked_foods_q, chef,), daemon=True)
    worker.start()

for delivery_guy in ['Marco', 'John', 'Saul']:
    worker = threading.Thread(target=deliver_food, args=(cooked_foods_q, delivery_guy,), daemon=True)
    worker.start()

new_orders = ['pizza', 'tacos', 'pasta', 'burger', 'salmon', 'pork meat', 'salad', 'risotto', 'fruits']
for new_order in new_orders:
    orders_q.put(new_order)

orders_q.join()
cooked_foods_q.join()
