def only_diff_elements(set_1, set_2):
    symmetric_diff = set_1.symmetric_difference(set_2)
    return symmetric_diff


set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
