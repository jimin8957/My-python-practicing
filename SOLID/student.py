class StudentProfile:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major

class Grade:
    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)

class Report:
    def __init__(self, StudentProfile, Grade):
        self.StudentProfile = StudentProfile
        self.Grade = Grade

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}" \
              .format(self.StudentProfile.name, self.StudentProfile.id, self.StudentProfile.major, self.Grade.get_average_gpa()))

class Student:
    def __init__(self, name, id, class_year):
        self.profile = StudentProfile(name, id, class_year)
        self.grades = []
        self.Grade = Grade(self.grades)
        self.Report = Report(self.profile, self.Grade)


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.profile.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.Grade.add_grade(3.0)
younghoon.Grade.add_grade(3.33)
younghoon.Grade.add_grade(3.67)
younghoon.Grade.add_grade(4.3)

# 학생 성적표
younghoon.Report.print_report_card()