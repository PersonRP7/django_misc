# def seek(instance, gt_or_lt):
#     return Picture.objects.filter(**{f"id__{gt_or_lt}":instance.id}).first()

# def seek_instance(lt_or_gt, instance):
#     try:
#         if lt_or_gt == 'lt':
#             inst = Picture.objects.filter(pk__lt=instance.pk).order_by('-pk').first()
#             return reverse("app:see_picture", kwargs = {"id":inst.id})
#         elif lt_or_gt == 'gt':
#             inst = Picture.objects.filter(pk__gt=instance.pk).order_by('pk').first()
#             return reverse("app:see_picture", kwargs = {'id':inst.id})
#     except Picture.DoesNotExist:
#         return reverse("app:see_picture", kwargs = {'id':inst.id})

# def seek_instance(lt_or_gt, instance):
#     try:
#         if lt_or_gt == 'lt':
#             inst = Picture.objects.filter(pk__lt=instance.pk).order_by('-pk').first()
#             return reverse("app:see_picture", kwargs = {"id":inst.id})
#         elif lt_or_gt == 'gt':
#             inst = Picture.objects.filter(pk__gt=instance.pk).order_by('pk').first()
#             return reverse("app:see_picture", kwargs = {'id':inst.id})
#     except AttributeError:
#         return reverse("app:see_picture", kwargs = {'id':inst.id})

# def seek(instance, gt_or_lt):
#     return Picture.objects.filter(**{f"id__{gt_or_lt}":instance.id}).first()

#Returns id
# def seek_instance(instance, gt_or_lt, pk):
#     return Picture.objects.filter(**{f"id__{gt_or_lt}":instance.id}).order_by(pk).first().id

# def seek_instance(instance, gt_or_lt, pk):
#     inst = Picture.objects.filter(**{f"id__{gt_or_lt}":instance.id}).order_by(pk).first()
#     return reverse("app:see_picture", kwargs={"id":inst.id})