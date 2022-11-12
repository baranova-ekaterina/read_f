text_list = ['1.txt', '2.txt', '3.txt']

task = {}
#for i in text_list:
def read_file(text):
    for i in text_list:
        with open(i, 'rt', encoding='utf-8') as file:
            g = file.read()
            lines = g.count('\n') + 1
            task[i] = lines
    return task
    #return sorted(task.items(), key=lambda item: item[1])
   
read_file(text_list)

sorted_task = sorted(task.items(), key=lambda item: item[1])
print(task)
print(sorted_task)

def wr_file(dic):
    for key, value in dic.items():
        return f'{key}'


#line_count = sum(1 for line in open('file.txt'))        

# Пример 3 - читаем строки (все) - читается все,  но записывается в список
#with open('1.txt', 'r', encoding='utf-8') as f:
    #lines = f.readlines()
    #print(type(lines))
    #print(len(lines))
    #print(lines[1])
    #print(lines)
    
    
