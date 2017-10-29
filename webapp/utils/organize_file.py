import os
import random
from shutil import copyfile

def list_subtract(x,y):
    "subtract list y from x"
    return [item for item in x if item not in y]

def sample_file(from_dir,num):
    "sample `num` files from `from-dir`, return absolute filenames"
    if (num == 1):
        return os.path.join(
            from_dir,
            random.sample(os.listdir(from_dir), num)[0]
        )
    else:
        return [os.path.join(from_dir,filename)
                for filename in random.sample(os.listdir(from_dir), num)]

def copy_image_files(prod_img_source_dir,cust_img_source_dir,
                     prod_img_target_dir,cust_img_target_dir,classes):
    for c in classes:
        # copy product image
        prod_source_class_dir =  os.path.join(prod_img_source_dir,c)
        prod_img_file = sample_file(from_dir=prod_source_class_dir,num=1)
        prod_target_class_dir = os.path.join(prod_img_target_dir,c)
        copyfile(src=prod_img_file,dst=os.path.join(prod_target_class_dir,
                                                    os.path.basename(prod_img_file)))
        # copy customer images
        cust_source_class_dir = os.path.join(cust_img_source_dir,c)
        # get 7 correct files
        correct_files = sample_file(from_dir=cust_source_class_dir,num=7)
        # get 3 incorrect files
        incorrect_files = []
        noise_classes = random.sample(list_subtract(x=classes,y=[c]),3)
        for n_c in noise_classes:
            noise_class_dir = os.path.join(cust_img_source_dir,n_c)
            noise_file = sample_file(from_dir=noise_class_dir,num=1)
            incorrect_files.append(noise_file)

        for file in correct_files + incorrect_files:
            copyfile(src=file, dst=os.path.join(cust_img_target_dir,c,
                                                         os.path.basename(file)))


if __name__ == "__main__":
    CLASSES =['back_pack', 'bike', 'bike_helmet', 'bookcase', 'bottle', 'calculator', 'desktop_computer', 'desk_chair', 'desk_lamp', 'file_cabinet', 'headphones', 'keyboard'
, 'laptop_computer', 'letter_tray', 'mobile_phone', 'monitor', 'mouse', 'mug', 'paper_notebook', 'pen', 'phone', 'printer', 'projector', 'punchers', 'ring_binder', 'ruler', 'scissors', 'speaker', 'stapler', 'tape_dispenser', 'trash_can']
    prod_img_source_dir = "F:/data/domain_adaptation_images/amazon"
    cust_img_source_dir = "F:/data/domain_adaptation_images/train-test-split/test"
    prod_img_target_dir = "F:/Project/annotation_webapp/media/product"
    cust_img_target_dir = "F:/Project/annotation_webapp/media/customer"
    # create folders for each class
    for c in CLASSES:
        cat_dir = os.path.join(prod_img_target_dir,c)
        if not os.path.exists(cat_dir):
            os.makedirs(cat_dir)
        cat_dir = os.path.join(cust_img_target_dir, c)
        if not os.path.exists(cat_dir):
            os.makedirs(cat_dir)
    print("folders created")
    # copy files
    copy_image_files(prod_img_source_dir=prod_img_source_dir,prod_img_target_dir=prod_img_target_dir,
                     cust_img_source_dir=cust_img_source_dir,cust_img_target_dir=cust_img_target_dir,classes=CLASSES)