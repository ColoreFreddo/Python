src_file = open("test.txt", "r")
content = src_file.read()
src_file.close()
dest_file = open("output.txt", "w")
dest_file.write(content)
dest_file.close()