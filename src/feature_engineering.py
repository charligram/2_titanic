def extract_title(name):
    first_part_of_name = ''
    for character in name:
        if character == '.':
            break
        else:
            first_part_of_name = first_part_of_name + character

    first_part_of_name = first_part_of_name.split()[-1]
    
    return first_part_of_name

def rename_titles(title):
    common_titles = ['Mr', 'Miss', 'Mrs', 'Master']

    if title not in common_titles:
        title = 'Other'

    return title