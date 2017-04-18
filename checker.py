

dir_name="F:\Dropbox\Giang vien work\DHCN 2016-2017\AI - thay Son\Assignments\Assignment1\\1617II_INT3401_1-Assignment 1 (Q1-3)-2594\\0done"
check_files=["search.py", "searchagents.py"]
check_function=["B"]
#check_codes[check_file][name_student][check_function] = text
#check_paths={}
#check_codes={}


def searchCheckFile(parrent_dir):
    import glob
    import os
    check_paths={}
    for check_file in check_files:
        student_map = {}
        for student_dir in os.listdir(parrent_dir):
            #find root
            full_student_dir = os.path.join(parrent_dir, student_dir)
            name_files = glob.glob(full_student_dir+"\\"+check_file)
            if (name_files.__len__()>0):
                #print (name_files.)
                student_map.update({student_dir:name_files[0]})
            level_dir = "*\\"
            level_depth = 1
            while (student_dir not in student_map.keys()) and (level_depth <5):
                #find level
                level_depth += 1
                name_files_level = glob.glob(full_student_dir + "\\"+level_dir + check_file)
                if (name_files_level.__len__()>0):
                    student_map.update({student_dir:name_files_level[0]})
                else:
                    level_dir+"*\\"

        # update
        check_paths.update({check_file: student_map})

    print (len(check_paths["search.py"]))
    return check_paths

def getTextFromFunctionCode(path_name):
    #get text from function name + path
    return "abc"

if __name__ == '__main__':
    import util
    check_paths = searchCheckFile(dir_name)
    student_dirs = check_paths["search.py"]
    print (student_dirs)
    for (student_dir, student_path) in student_dirs.items():
        print(student_dir, student_path)
        text1 = getTextFromFunctionCode(student_path)
        for (student_dir2, student_path2) in student_dirs.items():
            text2 = getTextFromFunctionCode(student_path2)
            print(util.cosine_sim(text1, text2))
    #checkPairCodes(codes)
