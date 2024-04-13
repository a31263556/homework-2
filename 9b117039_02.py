import os
import json


def load_students_data(file_path: str) -> list:
    """讀取學生資料"""
    if not os.path.isfile(file_path):
        print("錯誤: 找不到指定的檔案路徑。")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)



def get_student_info(student_id: str, students_data: list) -> dict:
    """根據學號返回該學生的個人資料字典"""
    for student in students_data:
        if student["student_id"] == student_id:
            return student
    raise ValueError(f"學號 {student_id} 找不到.")


def add_course(
    student_id: str,
    course_name: str,
    course_score: float,
    students_data: list
):
    """為指定學生添加一門課程及其分數"""
    if not course_name.strip() or not course_score:
        raise ValueError("課程名稱或分數不可空白.")

    for student in students_data:
        if student["student_id"] == student_id:
            student["courses"].append({
                "name": course_name,
                "score": course_score
            })
            print("課程已成功新增。")
            return
    raise ValueError(f"學號 {student_id} 找不到.")


def calculate_average_score(student_data: dict) -> float:
    """計算並返回該學生所有課程的平均分數"""
    courses = student_data.get("courses", [])
    if not courses:
        return 0.0

    total_score = sum(course["score"] for course in courses)
    return total_score / len(courses)


def main():
    file_path = "students.json"
    students_data = load_students_data(file_path)

    while True:
        print("***************選單***************")
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")
        print("**********************************")
        choice = input("請選擇操作項目：")
        if choice == "1":
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(student_id, students_data)
                print("=>學生資料:", json.dumps(student_info, ensure_ascii=False, indent=2))
            except ValueError as e:
                print("=>發生錯誤:", e)

        elif choice == "2":
            student_id = input("請輸入學號: ")
            course_name = input("請輸入要新增課程的名稱: ")
            course_score = input("請輸入要新增課程的分數: ")
            try:
                add_course(student_id, course_name, float(course_score), students_data)
            except ValueError as e:
                print("=>其它例外:", e)

        elif choice == "3":
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(student_id, students_data)
                average_score = calculate_average_score(student_info)
                print("=>各科平均分數:", average_score)
            except ValueError as e:
                print("=>發生錯誤:", e)

        elif choice == "4":
            print("=>程式結束。")
            break

        else:
            print("=>請輸入有效的選項。")

if __name__ == "__main__":

    main()
