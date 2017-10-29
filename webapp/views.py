import random
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from webapp.models import Product, LabeledBy, UserProfile
from django.db.transaction import atomic
from django.contrib.auth.decorators import login_required

@csrf_exempt
def user_login(request):
    if request.user.is_authenticated():
        return redirect("/survey")

    message=''
    if (request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if (not user):
            message='Either the username or password is not correct'
        else:
            login(request, user)
            return redirect("/survey")

    return render(request, "login.html",{'message':message})

def user_logout(request):
    logout(request)
    return redirect("/")

# Create your views here.
@login_required
def home(request):
    # randomly pick a product
    unfinished_products = list(Product.objects.filter(is_labeling_finished=False))
    unfinished_products = [p for p in unfinished_products if not LabeledBy.objects.filter(user=request.user,product=p).exists()]
    if (len(unfinished_products)==0):
        return render(request,"finished.html")
    else:
        product = random.sample(unfinished_products,1)[0]
    # retrieve its product image
    product_image = product.productimage_set.all()[0].image_path
    # retrieve its customer images
    cust_imgs = product.customerimage_set.all()
    img_list = [item.image_path for item in cust_imgs]
    # retrieve user performance
    profile = UserProfile.objects.get(user=request.user)
    return render(request,"index.html",{"num_imgs":len(cust_imgs),"img_list":img_list,
                                        "product_img":product_image,"product_name":product.name,
                                        "user_name":request.user.first_name,"num_imgs_labeled":profile.num_images_labeled})


@atomic
def save_annotation(product,annotations):
    cust_imgs = product.customerimage_set.all()
    # save annotations
    assert len(cust_imgs) == len(annotations)
    all_confirmed = True
    for i in range(len(annotations)):
        cust_img = cust_imgs[i]
        cust_img.label_score += int(annotations[i])
        cust_img.times_labeled += 1
        cust_img.save()
        if (not cust_img.is_label_confirmed()):
            all_confirmed = False
    # check if the product labelling has been confirmed
    if (all_confirmed):
        product.is_labeling_finished = True
        product.save()

@atomic
def save_user_record(user,product,num_annotations):
    LabeledBy.objects.create(
        user = user,
        product = product,
        record_time = timezone.now()
    )
    profile = UserProfile.objects.get(user=user)
    profile.num_products_labeled += 1
    profile.num_images_labeled += num_annotations
    profile.last_time_label = timezone.now()
    profile.save()


@login_required
def submit_annotation(request):
    product_name = request.GET.get("product_name")
    annotations = request.GET.get("annotations")
    annotations_ls = annotations.split(",")
    # save the annotations
    product = Product.objects.get(name=product_name)
    save_annotation(product=product,annotations=annotations_ls)
    save_user_record(user=request.user,product=product,num_annotations = len(annotations))
    # return to index page
    return redirect("/survey")