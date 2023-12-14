def display_task(task):
    details = f"Name: {task['name']}, Priority: {task['priority']}, "
    details += f"Status: {task['status']}"
    print(details)
    
    # Splitting the description into parts and printing each part on a new line
    print("Description:")
    description = task['description']
    description_parts = [description[i:i+50] for i in range(0, len(description), 50)]
    for part in description_parts:
        print(part)

# Example task dictionary
task = {
    'name': 'Complete assignment',
    'priority': 'High',
    'description': 'Finish the project by Friday. It needs to be submitted before the end of the day. Make sure to cover all the required points.',
    'status': 'In Progress'
}

# Calling the function to display the task details
display_task(task)