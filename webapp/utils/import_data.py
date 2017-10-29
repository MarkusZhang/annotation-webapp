import sys,os,django

sys.path.extend(['F:/Project/annotation_webapp'])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "annotation_webapp.settings")
django.setup()

from django.contrib.auth.models import User
from webapp.models import Product,ProductImage,CustomerImage, UserProfile, LabeledBy
from django.db.transaction import atomic
from django.core.files import File

@atomic
def import_initial_data(prod_img_dir,cust_img_dir,classes):
    for c in classes:
        # create Product
        product = Product.objects.create(
            name = c,
            brand = "jianda",
            category = "product"
        )
        # create ProductImage
        filename = os.listdir(os.path.join(prod_img_dir,c))[0]
        ProductImage.objects.create(
            product = product,
            image_path = "product/{}/{}".format(c,filename)
        )
        # create CustomerImage
        for f in os.listdir(os.path.join(cust_img_dir,c)):
            CustomerImage.objects.create(
                product = product,
                image_path = "customer/{}/{}".format(c,f)
            )

@atomic
def clean_db():
    ProductImage.objects.all().delete()
    CustomerImage.objects.all().delete()
    LabeledBy.objects.all().delete()
    Product.objects.all().delete()
    for profile in UserProfile.objects.all():
        profile.reset()
        profile.save()

@atomic
def path_fix():
    "remove the prefix / of the image_path"
    for p in ProductImage.objects.all():
        p.image_path = p.image_path[1:]
        p.save()
    for c in CustomerImage.objects.all():
        c.image_path = c.image_path[1:]
        c.save()

@atomic
def clear_label_record():
    "clear all the labeling records"
    for p in CustomerImage.objects.all():
        p.reset()
        p.save()
    for p in Product.objects.all():
        p.is_labeling_finished = False
        p.save()
    LabeledBy.objects.all().delete()
    for profile in UserProfile.objects.all():
        profile.reset()
        profile.save()

def create_initial_profile():
    users = User.objects.all()
    for user in users:
        if not UserProfile.objects.filter(user=user).exists():
            UserProfile.objects.create(
                user = user
            )

if __name__ == "__main__":
    create_initial_profile()
#     CLASSES = ['back_pack', 'bike', 'bike_helmet', 'bookcase', 'bottle', 'calculator', 'desktop_computer', 'desk_chair', 'desk_lamp', 'file_cabinet', 'headphones', 'keyboard'
# , 'laptop_computer', 'letter_tray', 'mobile_phone', 'monitor', 'mouse', 'mug', 'paper_notebook', 'pen', 'phone', 'printer', 'projector', 'punchers', 'ring_binder', 'ruler', 'scissors', 'speaker', 'stapler', 'tape_dispenser', 'trash_can']
#     import_initial_data(prod_img_dir="F:/Project/annotation_webapp/media/product",
#                         cust_img_dir="F:/Project/annotation_webapp/media/customer",
#                         classes=CLASSES)