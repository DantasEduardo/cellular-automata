def copy(list):
    copy_list = []
    for i in list:
        arr = []
        for j in i:
            arr.append(j)
        copy_list.append(arr)

    return copy_list



def check_cells(cells):
    new_state = copy(cells)
    
    width = len(cells)
    height = len(cells[0])

    for x in range(width):
        for y in range(height):
            
            sum = 0
            if x != 0 and y != 0:
                if cells[x-1][y-1] == 1:
                    sum+=1

            if x != 0:
                if cells[x-1][y] == 1:
                    sum+=1
            
            if x != 0 and y != width-1:
                if cells[x-1][y+1] == 1:
                    sum+=1
                
            if y != 0:
                if cells[x][y-1] == 1:
                    sum+=1
                
            if y != width-1:
                if cells[x][y+1] == 1:
                    sum+=1

            if x != height-1 and y != 0:
                if cells[x+1][y-1] == 1:
                    sum+=1
                
            if x != height-1:
                if cells[x+1][y] == 1:
                    sum+=1
                
            if x != height-1 and y != width-1:
                if cells[x+1][y+1] == 1:
                    sum+=1

            if sum < 2:
                new_state[x][y] = 0

            elif sum > 3:
                new_state[x][y] = 0

            elif sum == 3:
                new_state[x][y] = 1

            elif sum == 2:
                new_state[x][y] = new_state[x][y]    

    print("Finished processing")            
    return new_state            
