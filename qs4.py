'''
   Employee Salary Analysis A company stores employee salaries in a list.
   Write a function to calculate the average salary, 
   display salaries above the average, and increase every salary by 10%.

'''
def sal_analysis(data:list):
    # displaying the highest salaries
    avg_sal = (sum(data)/len(data))
    abv_avg = [salary for salary in data if salary > avg_sal]
    inc_sal = []
    for sal in data:
        inc_sal[sal]+=(sal*0.1)

        
    print("avg salary, salaries above avg, : \n ",avg_sal,abv_avg,)

