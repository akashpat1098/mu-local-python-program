import os
def soldier(srcfile,file,format):
    os.chdir(srcfile)
    i=1
    files=os.listdir(srcfile)
    with open(file) as f:
        fileList=f.read().split("\n")

    for file in files:
        if file not in fileList:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1]==format:
            os.rename(file,f"{i}{format}")
            i+=1
# pass 1 arg as name of the folder in which file has to process and 2 as file having names of file  
# which has to ignore
soldier("F:\\aaaaaaa\\testDirectory",
"F:\\aaaaaaa\\codes\\Python program\\folderprettifyerWords.txt",".jpg")