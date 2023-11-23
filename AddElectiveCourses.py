import pandas as pd
import json

#讀入Json檔案
def read_json_file(filename):
    data = {}
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        f.close()
        return data
    except FileNotFoundError:
        print("ERROR: 找不到 " + filename + " 檔案。")
        return None

def write_json_file(filename, new_data):
    try:
        with open(filename, 'w') as f:
            json.dump(new_data, f, indent = 2)
        return True
    except FileNotFoundError:
        print("ERROR: 找不到 " + filename + " 檔案。")
        return FileNotFoundError
    except FileExistsError:
        print("ERROR: " + filename + " 檔案存在錯誤。")
        return FileExistsError

def search_course(course_id):
    course_info = read_json_file("Course.json")
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

# 核實是否衝堂
def verify(student_id, course_id):
    filename = student_id + ".json"
    curriculum = read_json_file(filename)
    course_info = read_json_file("Course.json")
    course_time = course_info[course_id]["Time"]

    time1 = []
    for key, data in curriculum.items():
        time1.append(data["Time"]["Week"])
        time1.append(data["Time"]["Class"])
        time1.append(data["Time"]["Duration"])

    time2 = []
    for key, data in course_time.items():
        time2.append(data["Week"])
        time2.append(data["Class"])
        time2.append(data["Duration"])

    if time1[0] == time2[0]:
        if is_duplicate(time1, time2) == True:
            return False
        else:
            return True

# 是否重複
def is_duplicate(time1, time2):
    times = 0
    arr1 = generate_value(time1)
    arr2 = generate_value(time2)
    
    for v1 in arr1:
        if v1 in arr2:
            times += 1
    if times == 0:
        return False
    else:
        return True

# 生成計算值
def generate_value(arr):
    value = []
    min_ = arr[1]
    max_ = min_ + arr[2]
    for i in range(min_, max_):
        value.append(i)
    return value
