import datetime

def login(name_user):
    print(f'Hi, {name_user}')

def what_mission():
    print('What would you like to do? write the number')
    print('1.New task\n2.View previous tasks\n3.Delete Task\n4.Watch Deleted Tasks\n5.Exit')
    number_mission = int(input("Enter your number: "))
    match number_mission:
        case 1:
            match_case_mission='New task'
            print(f'You choose: {match_case_mission}')
            New_task()

        case 2:
            match_case_mission='View previous tasks'
            print(f'You choose: {match_case_mission}')
            view_previous_tasks()

        case 3:
            match_case_mission='Delete Task'
            print(f'You choose: {match_case_mission}')
            Delete_Task()

        case 4:
            match_case_mission='Watch Deleted Tasks'
            print(f'You choose: {match_case_mission}')
            Watch_Deleted_Task()

        case 5:
            match_case_mission='Exit'
            print(f'You choose: {match_case_mission}')
            Exit()

        case _:
            match_case_mission='Invalid number'
            print(f'You choose: {match_case_mission}')
            Invalid_number()


def New_task():
    global number_task
    name_task= str(input('what would you like to add? '))
    new_task_map[number_task] = name_task
    number_task += 1
    print(f'would you like to continue? Y/N')
    if input() == 'Y':
        what_mission()
    else:
        Exit()

def view_previous_tasks():
    print(f'Here is the list: {new_task_map}')
    print(f'would you like to continue? Y/N')
    if input() == 'Y':
        what_mission()
    else:
        Exit()


def Delete_Task():
    global delete_task_number
    delete_task = int(input('what task would you like to delete? : '))
    print(f'Are you surre?')
    if input().upper() == 'Y':
        new_task_map.pop(delete_task)
        delete_task_map[delete_task_number] = delete_task
        time_map[delete_task_number] = str(datetime.datetime.now())
        delete_task_number += 1
    print(f'would you like to continue? Y/N')
    if input() == 'Y':
        what_mission()
    else:
        Exit()

def Watch_Deleted_Task():
    global delete_task_number
    print(f'Here is the list: {delete_task_map[delete_task_number-1]} ')
    print(f'At time: {time_map}')
    print(f'would you like to continue? Y/N')
    if input().upper() == 'Y':
        what_mission()
    else:
        Exit()

def Exit():
    exit

def Invalid_number():
    print('Invalid number - please try again and press between the numbers 1 to 5')
    what_mission()


if __name__ == '__main__':
    name_user = input("Enter your name: ")
    login(name_user)
    new_task_map = {}
    delete_task_map = {}
    time_map = {}
    number_task = 1
    delete_task_number = 1
    what_mission()



