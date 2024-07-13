def append_file_content(source_file_path, target_file_path):
    # 使用 with 语句打开源文件，以只读方式读取内容
    with open(source_file_path, 'r') as source_file:
        # 读取源文件的内容
        content_to_append = source_file.read()

    # 使用 with 语句打开目标文件，以追加方式打开
    with open(target_file_path, 'a') as target_file:
        # 将源文件的内容追加到目标文件中
        target_file.write(content_to_append)


# 调用函数进行文件内容追加
append_file_content('source.txt', 'target.txt')