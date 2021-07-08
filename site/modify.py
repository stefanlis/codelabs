import io

def alter(file,old_str,new_str):
    file_data = ""
    with io.open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with io.open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
 
alter("./dist/index.html", "\"/", "\"./")
alter("./dist/scripts/main.js", "\"/", "\"./")