

dir_name="F:\Dropbox\Giang vien work\DHCN 2016-2017\AI - thay Son\Assignments\Assignment1\\1617II_INT3401_1-Assignment 1 (Q1-3)-2594\\0done"
check_files=["search.py", "searchagents.py"]
check_functions=["depthFirstSearch", "breadthFirstSearch", "uniformCostSearch"]
#check_codes[check_file][name_student][check_function] = text
#check_paths={}
#check_codes={}
SCORE_THRESHOLD = 0.75

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

    #print(len(check_paths["search.py"]))
    return check_paths

def getTextByFunct(str, function_name):
    function_start = ("def "+function_name+"(").lower()
    function_end = "def"
    str = str.lower()
    #print (str.find(function_start))
    str = str[str.find(function_start):]
    #print(str)
    str = str[0:str.find(function_end, 5, len(str))]
    #print (str)
    return str

def readText(pathname):
    #print(pathname)
    function_texts={}
    with open(pathname) as file:
        data = file.read()
    for function_name in check_functions:
        text = getTextByFunct(data, function_name)
        if (len(text)>0):
            function_texts.update({function_name:text})

    return function_texts


def getTextFromFunctionCode(pathname):
    #get text from function name + path
    return readText(pathname)

#calculate consine similarity between 2 texts for each function
def cosineSim2FunctionTexts(function_text1, function_text2):
    #print(function_text1)
    #print(function_text2)
    #consineSim_functions = {}
    sum=0.0
    count=0
    for key in function_text1.keys():
        text1 = function_text1.get(key)
        text2 = function_text2.get(key)
        sum+=util.cosine_sim(text1, text2)
        count+=1
    if (count>0):
        return sum*1.0/count #percent
    else:
        return 0.0

if __name__ == '__main__':
    import util
    check_paths = searchCheckFile(dir_name)
    student_dirs = check_paths["search.py"]
    #print(student_dirs)
    import operator
    score_codes={}
    for (student_dir1, student_path) in student_dirs.items():
        cosineScores={}
        #print(student_dir1, student_path)
        function_text1 = getTextFromFunctionCode(student_path)
        for (student_dir2, student_path2) in student_dirs.items():
            function_text2 = getTextFromFunctionCode(student_path2)
            cosineScores.update({student_dir2:cosineSim2FunctionTexts(function_text1, function_text2)})

        #cosineScores = sorted(cosineScores.items(), key=operator.itemgetter(1), reverse=True)
        #print(sortX.reverse())
        #print(cosineScores)
        score_codes.update({student_dir1:cosineScores})
    #checkPairCodes(codes)
    #print(score_codes)
    #print top 10 highest
    for key1 in score_codes.keys():
        print (score_codes.get(key1))
        for key2 in score_codes.get(key1).keys():
            #print(key1 + " - " + key2 + ": " + score_codes.get(key1).get(key2))
            if (key1 != key2) and (score_codes.get(key1).get(key2)>SCORE_THRESHOLD):
                print(key1 +" - "+ key2 +": " + score_codes.get(key1).get(key2))
