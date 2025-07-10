def print_christmas_tree(height:int)->str:
    if height < 2:
        raise Exception("Height can not be less than two")
    christmas_tree_str = ""
    
    christmas_tree_str+= " X\n"
    christmas_tree_str+="XXX\n"
    christmas_tree_str+=" |"
    return christmas_tree_str
    
