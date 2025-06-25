def insert_task(p_queue, task):
    p_queue.append(task)
    


def extract_task(p_queue):
    if len(p_queue) == 0:
        return None

    min_p_index = 0
    min_p = p_queue[0]['priority']

    for ind, ele in enumerate(p_queue):
        if ele['priority'] < min_p:
            min_p_index = ind
            min_p = ele['priority']

    return p_queue.pop(min_p_index) 


def peek_task(p_queue):
    if len(p_queue) == 0:
        return None

    min_p_index = 0
    min_p = p_queue[0]['priority']

    for ind, ele in enumerate(p_queue):
        if ele['priority'] < min_p:
            min_p_index = ind
            min_p = ele['priority']

    return p_queue[min_p_index]


def is_empty(p_queue):
    return len(p_queue) == 0

completed_tasks = []
def complete_next_task(p_queue):
    task = extract_task(p_queue)
    if task:
        completed_tasks.append(task)
        print("Completed Task:")
        print("Title:", task['title'])
        print("Duration:", task['duration'], "mins")
        print("Priority:", task['priority'])
    else:
        print("No tasks to complete.")

def sort_by_title(task_list):
    for i in range(1, len(task_list)):
        key = task_list[i]
        j = i - 1
        while j >= 0 and task_list[j]['title'] > key['title']:
            task_list[j + 1] = task_list[j]
            j -= 1
        task_list[j + 1] = key

def search_for_task(tasks, target_title):
    low = 0
    high = len(tasks) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_title = tasks[mid]['title']

        if mid_title == target_title:
            return tasks[mid]
        elif mid_title < target_title:
            low = mid + 1
        else:
            high = mid - 1

    return None

def sort_tasks(p_queue):
    for i in range(1, len(p_queue)):
        key = p_queue[i]
        j = i - 1

        while j >= 0 and p_queue[j]['duration'] > key['duration']:
            p_queue[j + 1] = p_queue[j]
            j -= 1

        p_queue[j + 1] = key
    return p_queue

task_p_queue = []
number = 0
while number <= 0:
    num_input = input("How many tasks do you want to enter? ")
    if num_input.isdigit():
        number = int(num_input)
        if number <= 0:
            print("Please enter a number greater than 0.")
    else:
        print("Please enter a valid number.")

for i in range(number):
    print("\nTask", i + 1)
    title = ""
    while title.strip() == "":
        title = input("Enter title: ").strip()
        if title == "":
            print("Title cannot be empty.")

    duration = 0
    while duration <= 0:
        dur_input = input("Enter duration (in minutes): ")
        if dur_input.isdigit():
            duration = int(dur_input)
            if duration <= 0:
                print("Duration must be greater than 0.")
        else:
            print("Please enter a valid number.")
            
    priority = -1
    while priority < 0:
        prio_input = input("Enter priority (lower = higher priority): ")
        if prio_input.isdigit():
            priority = int(prio_input)
        else:
            print("Please enter a valid number (0 or more).")

    task = {'title': title, 'duration': duration, 'priority': priority}
    insert_task(task_p_queue, task)
    
print("\nAll Tasks in Queue: ")
for t in task_p_queue:
    print(t)

print("\nComplete Next Task: ")
complete_next_task(task_p_queue)

  
all_tasks = task_p_queue + completed_tasks
sort_by_title(all_tasks)
print("\nSearch for a Task: ")
search_title = input("Enter task title to search: ")
result = search_for_task(all_tasks, search_title)
if result:
        print("Task Found:", result)
else:
        print("Task Not Found.")

print("\nTasks Sorted by Duration: ")
sorted_list = sort_tasks(all_tasks)
for t in sorted_list:
    print(t)