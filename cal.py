def convert_letter_to_grade4(grade):
    if grade == 'A+':
        return 4.0
    elif grade == 'A':
        return 3.7
    elif grade == 'B+':
        return 3.5
    elif grade == 'B':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D':
        return 1.0
    else:
        return 0.0


def convert_grade10_to_letter(grade):
    if 9 <= grade <= 10:
        return 'A+'
    elif grade >= 8.5:
        return 'A'
    elif grade >= 8.0:
        return 'B+'
    elif grade >= 7:
        return 'B'
    elif grade >= 6.5:
        return 'C+'
    elif grade >= 5.5:
        return 'C'
    elif grade >= 5:
        return 'D+'
    elif grade >= 4:
        return 'D'
    else:
        return 'F'


def calculate_gpa(subjects):
    total_credit = 0
    total_points = 0

    for subject in subjects:
        name = subject[0]
        credits = subject[1]
        grade = subject[2]

        credit_points = convert_letter_to_grade4(convert_grade10_to_letter(grade)) * credits
        total_credit += credits
        total_points += credit_points

    gpa = total_points / total_credit
    return gpa


def main():
    subjects = []
    total_credit = 0

    with open('monhoc.text', 'r') as rf:
        content = rf.readline()
        while content:
            x = content.split(" - ")
            print(x)
            name = x[0]
            grade = float(x[1])
            credits = int(x[2])
            total_credit += credits
            subjects.append((name, credits, grade))
            content = rf.readline()

    gpa = calculate_gpa(subjects)
    print("Điểm chung bình tích luỹ hệ 4:", "%.3f" % gpa)
    print("Tổng tín chỉ:", total_credit)
    print("Nhập phím bấm kì để thoát...")
    input()


if __name__ == "__main__":
    main()
