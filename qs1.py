'''
Student Marks Analysis A college stores students' marks in a list.
 Write a function that accepts a list of marks and
 displays the highest mark, lowest mark, average mark, 
 and number of students who passed (marks of 40 or above). 

'''

def mark_analysis(data:list):
    # displaying the highest marks
    high_mark =  max(data)
    low_mark = min(data)
    avg_mark = (sum(data)/len(data))
    pass_student = 0
    for _ in data:
        if _ > 40:
            pass_student += 1

    print("highest mark, low mark, avg mark and no of pass students: \n ",high_mark,low_mark,avg_mark,pass_student)


mark_analysis([20,56,84,43,89,74,57,79,64,38,70,96,82,59])