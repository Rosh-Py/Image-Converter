import sys
import os
from PIL import Image

#Take the input[old,new] dir using command line
#If new dir is not there, then create
#loop through each image and convert into png and save it in new folder

#checking path exists or not
def validate_path(path):
    '''
    checking path exists or not
    '''
    return os.path.exists(path)

#creating new directory or directories
def create_dir(path):
    '''
    creating new directory or directories
    '''
    try:
        os.makedirs(path)
        return True
    except:
        return False

#Function to convert images into png format
def convert_to_png(src_dir, tgt_dir):
    '''
    Function to convert images into png format
    '''
    if validate_path(src_dir):
        if not validate_path(tgt_dir):
            if create_dir(tgt_dir):

                try:
                    list_dir= os.listdir(src_dir) #listing the directory in a list

                    #Looping through each file and saving it in png format
                    for file in list_dir:
                        with Image.open(f'{src_dir}/{file}') as img:
                            name = file.split('.')[0]
                            img.save(f'{tgt_dir}/{name}.png','png')
                    ######################################################
                except:
                    print('Couldn\'t convert to png')

            else:
                print('Directory couldn\'t be created')
        else:
            pass

    else:
        print('Source directory does not exist')



def main():
    try:
        source_dir = sys.argv[1]
        target_dir = sys.argv[2]
        convert_to_png(source_dir,target_dir)
    except:
        print('Source or target directory is not given. Try again!')




if __name__=="__main__":
    main()
