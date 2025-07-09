# logic.py

def valmark(marks):
    return all(0 <= m <= 100 for m in marks)

def calcavg(marks):
    return sum(marks) / len(marks)

def get_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'
