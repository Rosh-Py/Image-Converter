import sys
import os
from PIL import Image
#Take the input[old,new] dir using command line
#If new dir is not there, then create
#loop through each image and convert into png and save it in new folder


#checking path exists or not
def validate_path(path):
    return os.path.exists(path)

#creating new directory or directories
def create_dir(path):
    try:
        os.makedirs(path)
    except:
        return False

#Function to convert images into png format
def convert_to_png(src_dir, tgt_dir):
    try:
        if validate_path(src_dir):
            if not validate_path(tgt_dir):
                create_dir(tgt_dir)
                list_of_jpg_images = os.listdir(src_dir)

                for file in list_of_jpg_images:
                    with Image.open(f'{src_dir}/{file}') as img:
                        name = file.split('.')[0]
                        if name[1] in ('jpg','jpeg'):
                            img.save(f'{tgt_dir}/{name}.png','png')

        else:
            print('Source directory does not exist')
    except:
        print('Some error occured')



def main():
    try:
        source_dir = sys.argv[1]
        target_dir = sys.argv[2]
        # print(source_dir)
        convert_to_png(source_dir,target_dir)
    except:
        print('Source or target directory is not given. Try again!')




if __name__=="__main__":
    main()
