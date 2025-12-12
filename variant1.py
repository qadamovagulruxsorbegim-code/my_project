def parse_grades(raw_data):
    grades_dict= {}
    for raw_data_item in raw_data:
        student_name, subject, score= raw_data_item.split(",")
        score=int(score)
        if subject not in grades_dict:
            grades_dict[subject]=[]
        grades_dict[subject].append(score)
    return grades_dict

raw_data = [
    "Alice,Math,85",
    "Bob,Physics,70",
    "Charlie,Math,90",
    "David,Chemistry,60",
    "Eve,Physics,88",
    "Frank,Math,75",
    "Grace,Chemistry,82",
    "Heidi,Physics,95"
]

def print_averages(grade_dict):
    new_dict= grade_dict.items()
    for subject, scores in new_dict:
        average= sum(scores)/len(scores)
        formatted_avg= format(average, ".2f")
        print(subject, formatted_avg)


grades=parse_grades(raw_data)
print_averages(grades)