import pandas as pd
import json

#讀入所有課程
def read_course_info():
    filename = 'Course.json'
    dict_course = {}  # 保存課程信息的列表

    try:
        with open(filename, 'r') as f:
            dict_course = json.load(f)
        f.close()
        return dict_course
    except FileNotFoundError:
        print("ERROR: 找不到 " + filename + " 檔案。")
        return None

# 讀入學生課表資料
def get_curriculum(student_id):
    filename = student_id + ".json"
    curriculum_info = {}

    try:
        with open(filename, 'r') as f:
            curriculum_info = json.load(f)
        f.close()
        return curriculum_info
    except FileNotFoundError:
        print("ERROR: 找不到 " + filename + " 檔案。")
        return None

def search_course(course_id):
    course_info = read_course_info()
    return course_info[course_id]

def write_curriculum(student_id, course_id):
    filename = student_id + ".json"

    try:
        course_info = search_course(course_id)
        if (verify(student_id, course_info['time'])):
            with open(filename, "w") as f:
                json.dump(course_info, f, indent = 2)
            return True
    except FileNotFoundError:
        print("ERROR: " + student_id +"檔案不存在")
        return False

def verify(student_id, course_time):
    curriculum = get_curriculum(student_id)
    for key, data in curriculum:
        if data['time'] == course_time:
            return False
    return True

