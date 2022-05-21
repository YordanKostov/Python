todo_notes = input()
notes = []

while todo_notes != 'End':
    data = todo_notes.split('-')
    notes.insert(int(data[0]), data[1])
    todo_notes = input()
    
