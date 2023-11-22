
#讀入所有課程
def read_course_info():
    course_info = []  # 保存課程信息的列表

    try:
        with open("Course.txt", "r") as file:
            for line in file:
                # 解析每一行，以逗號分隔
                course_id, course_name, course_credit, course_time, course_remainder = map(str.strip, line.split(','))

                # 將課程信息組成一個字典，加入列表中
                course = {
                    "course_id": course_id,
                    "course_name": course_name,
                    "course_credit": course_credit,
                    "course_time": course_time,
                    "course_remainder": course_remainder
                }
                course_info.append(course)

        return course_info
    except FileNotFoundError:
        print("ERROR: 找不到Course.txt檔案。")
        return None

# 讀入學生課表資料
def get_curriculum(student_id):
    filename = student_id + ".txt"
    curriculum_info = []

    try:
        with open(filename, "r") as file:
            for line in file:
                course_id, course_credit,course_time = map(str.strip, line.split(','))
                curriculum = {
                    "course_id": course_id,
                    "course_credit": course_credit,
                    "course_time": course_time
                }
                curriculum_info.append(curriculum)
        return curriculum_info
    
    except FileNotFoundError:
        print("ERROR: 找不到" + student_id + "檔案")

def write_curriculum(student_id, course_id, course_credit, course_time):
    filename = student_id + ".txt"

    try:
        with open(filename, "a") as file:
            line = [course_id, course_credit, course_time]
            file.writelines(line)
            file.close()
        return True
    except FileNotFoundError:
        print("ERROR: " + student_id +"檔案不存在")
        return False

def verify(student_id, course_time):
    curriculum = get_curriculum(student_id)
    
