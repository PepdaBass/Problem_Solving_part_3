import random

def addends_find_target():
    target_sum = int(input('Please enter a number between 10 and 20: '))
    rough_draft_list = random_addends(4)
    print(rough_draft_list)
    final_addends_list = edit_appends_list(rough_draft_list)
    two_element_solution = adding_counter(target_sum, final_addends_list)



def random_addends(amount_of_numbers_needed):
    limit_of_four = 1
    addends_list = []
    four_random_numbers = False
    while four_random_numbers is False:
        if limit_of_four <= amount_of_numbers_needed:
            rando_num = random.randrange(1, 15)
            limit_of_four += 1
            addends_list.append(rando_num)
        elif limit_of_four > amount_of_numbers_needed:
            four_random_numbers = True
            break
    return addends_list

def edit_appends_list(rough_draft_list_edit):
    is_duplicates = True
    second_draft = rough_draft_list_edit
    while is_duplicates is True:
        if second_draft[0] == second_draft[1] or second_draft[0] == second_draft[2] or second_draft[0] == second_draft[3]:
            second_draft.pop(0)
            second_draft.append(random_addends(1))
        elif second_draft[1] == second_draft[2] or second_draft[1] == second_draft[3]:
            second_draft.pop(1)
            second_draft.append(random_addends(1))
        elif second_draft[2] == second_draft[3]:
            second_draft.pop(2)
            second_draft.append(random_addends(1))
        else:
            is_duplicates = False
            return second_draft

def adding_counter(target_sum2, final_addends_list2):
    index1 = 0
    index2 = 1
    only_solution = []
    only_two_addends = False
    while only_two_addends is False:
        index_counter = False
        if index2 <= 3 and (target_sum2 == final_addends_list2[index1] + final_addends_list2[index2]):
            only_solution.append(final_addends_list2[index1])
            only_solution.append(final_appends_list2[index2])
        elif index2 <= 3 and (target_sum2 != final_addends_list2[index1] + final_addends_list2[index2]):
            index2 += 1
        elif index1 == 2 and index2 > 3:
            only_two_addends = True
            break
        elif index2 > 3:
            while index_counter is False:
                if index1 == 0:
                    index1 += 1
                    index2 = 2
                    index_counter = True
                elif index1 == 1:
                    index1 += 1
                    index2 = 3
                    index_counter = True
    return only_solution
        

addends_find_target()
print(adding_counter())