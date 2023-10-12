# 2023-10-12

def calculate_average_from_dict(score):
    if type(score) is dict:
        values = list(score.values())
        return sum(values)/len(score)

student_scores = {"김인하":92, "이인하":92, "박인하":78}
avg_score = calculate_average_from_dict(student_scores)
print(f"평균 점수: {avg_score:.2f}")



def remove_value(main_arr, target):
    return [ i for i in main_arr if target != i]
    # arr = main_arr[:]
    # while target in arr:
    #     arr.remove(target)
    # return arr

numbers = [1, 2, 3, 2, 4, 2, 5]
value_remove = 2
new_numbers = remove_value(numbers, value_remove)
print(numbers, new_numbers)




