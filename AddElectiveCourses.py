
def read_course_info():
    course_info = []  # 保存課程信息的列表

    try:
        with open("Course.txt", "r") as file:
            for line in file:
                # 解析每一行，以逗號分隔
                course_id, course_name, course_credit, course_remainder = map(str.strip, line.split(','))

                # 將課程信息組成一個字典，加入列表中
                course = {
                    "course_id": course_id,
                    "course_name": course_name,
                    "course_credit": course_credit,
                    "course_remainder": course_remainder
                }
                course_info.append(course)

        return course_info
    except FileNotFoundError:
        print("ERROR: 找不到Course.txt檔案。")
        return None

# 測試讀取課程信息功能
courses = read_course_info()