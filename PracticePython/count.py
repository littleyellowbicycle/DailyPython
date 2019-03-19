import os.path

def countLine(dirpath):
    blank, comments, codelines, totalines, count, temp = 0, 0, 0, 0, 0, 0
    if(os.path.exists(dirpath)):
        print('obj path is:%s'%dirpath)
    else:
        return
    filelist=os.listdir(dirpath)
    for f in filelist:
        if os.path.splitext(f)[1]=='.py':
            with open(f,'r',encoding='utf-8')as fp:
                print(f)
                while true:
                    line=fp.readline()
                    if not line:
	                    break
					elif line.strip().startwith('#'):
						comments+=1
					elif line.strip().startwith('"""') or line.strip().startwith("'''"):
						comments+=1
						if(line.count("'''")==1)or (line.count('"""')==1):
							while True：
								line=fp.readline()
								totalines+=1
								comments+=1
								if('"""' in line) or ("'''" in line):
									break
					elif line.strip():
						codelines+=1
					else:
						blank+=1
					totalines+=1
					print('the nuber of totalines is : ' + str(totalines-1))
					print('the nuber of comments is : ' + str(comments))
					print('the nuber of codelines is : ' + str(codelines))
					print('the nuber of blanklines is : ' + str(blank))            



countLine(".\\")    