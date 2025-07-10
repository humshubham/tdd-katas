def print_christmas_tree(height:int)->str:
    if height < 2:
        raise Exception("Height can not be less than two")
    christmas_tree_str = ""

    leading_whitespace = height-1
    tree_elements = 1

    while leading_whitespace>=0:
        christmas_tree_str+= " "*leading_whitespace
        christmas_tree_str+="X"*tree_elements
        christmas_tree_str+="\n"
        tree_elements+=2
        leading_whitespace-=1

    #Tree trunk
    christmas_tree_str+=" "*(height-1)
    christmas_tree_str+="|"

    return christmas_tree_str
