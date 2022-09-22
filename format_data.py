def format_data_for_display(people):
    return [f"{person['given_name']} {person['family_name']}: {person['title']}" for person in people]


def format_data_for_excel(people):
    result = "given, family, title\n"
    for person in people:
        result += f"{person['given_name']},{person['family_name']},{person['title']}\n"
    return result
