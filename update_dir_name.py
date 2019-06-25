import os, shutil

bash_dir = os.path.dirname(os.path.abspath(__file__))

for dir_name in os.listdir(bash_dir):
    if not os.path.isdir(os.path.join(bash_dir, dir_name)):
        continue
    count = 0
    for data in dir_name.split('_'):
        try:
            int(data)
            count += 1
        except:
            pass
    if count > 0:
        dir_split_list = dir_name.split('_')
        dir_split_list.sort()
        new_dir_name = '_'.join(dir_split_list)
        print(new_dir_name)
        os.rename(dir_name, new_dir_name)
