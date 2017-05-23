from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
#from .forms import VariationInventoryForm

# Create your models here.
class ProductoQuerySet(models.query.QuerySet):
	def activo(self):
		return self.filter(activo=True)

class ProductoManager(models.Manager):
	def get_queryset(self):
		return ProductoQuerySet(self.model, using=self._db)

	def all(self, *args, **kwargs):
		return self.get_queryset().activo()
		#return self.get_queryset()

	def get_related(self, instance):
		products_one = self.get_queryset().filter(categorias__in = instance.categorias.all())
		products_two = self.get_queryset().filter(default = instance.default)
		qs = (products_one | products_two).exclude(id = instance.id).distinct()
		return qs     
		
class Producto(models.Model):
	nombre = models.CharField(max_length = 120)
	descripcion = models.TextField(blank = True, null= True)
	precio = models.DecimalField(decimal_places = 2, max_digits = 20)
	precio_promocion = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = True)
	activo = models.BooleanField(default = True) 
	categorias = models.ManyToManyField('Categoria', blank=True)
	inventario = models.IntegerField(null=True, blank = True)
	default = models.ForeignKey('Categoria', related_name = 'default_categoria', null=True, blank=True)

	objects = ProductoManager()

	class Meta:
		ordering = ['-nombre']


	def get_absolute_url(self):
		return reverse("producto_detalle", kwargs={"pk":self.pk})

	def get_image_url(self):
		img = self.productoimage_set.first()
		if img:
			return img.image.url
		return img


	def __str__(self):
		return self.nombre

	# producto imagen
	# producto categoria	

# class Variation(models.Model):
# 	product = models.ForeignKey(Product)
# 	title = models.CharField(max_length = 120)
# 	price = models.DecimalField(decimal_places = 2, max_digits = 20)
# 	sale_price = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = True)
# 	active = models.BooleanField(default = True) 
# 	inventory = models.IntegerField(null=True, blank = True)

# 	#objects = VariationManager()
# 	def __str__(self):
# 		return self.title

# 	def get_price(self):
# 		if self.sale_price is not None:
# 			return self.sale_price
# 		else:
# 			return self.price

# 	def get_absolute_url(self):
# 		return self.product.get_absolute_url()

# 	def get_html_price(self):
# 		if self.sale_price is not None:
# 			html_text = "<span class='sale-price'>%s</span><span class='og-price'>%s</span>"%(self.sale_price, self.price)
# 		else:
# 			html_text = "<span class='price'>%s</span>"%(self.price)
# 		return mark_safe(html_text)

# 	def add_to_cart(self):
# 		return "%s?item=%s&qty=1" %(reverse("cart"), self.id)

# 	def remove_from_cart(self):
# 		return "%s?item=%s&qty=1&delete=True" %(reverse("cart"), self.id)

# 	def get_title(self):
# 		return "%s - %s" %(self.product.title, self.title)


# def product_post_save_receiver(sender, instance, created, *args, **kwargs):
	
# 	product = instance
# 	variations = product.variation_set.all()
# 	#varations = Variation.objects.filter(product = product)
# 	if variations.count() == 0:
# 		new_var = Variation()
# 		new_var.product = product
# 		new_var.title = "Default"
# 		new_var.price = product.price
# 		new_var.save()
	

# post_save.connect(product_post_save_receiver, sender = Product)

def image_upload_to(instance, filename):
	nombre = instance.producto.nombre
	slug = slugify(title)
	basename, file_extension = filename.split(".")[1]
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "/productos/%s/%s" %(slug, filename)

def image_upload_to_featured(instance, filename):
	nombre = instance.producto.nombre
	slug = slugify(title)
	basename, file_extension = filename.split(".")[1]
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "/productos/%s/featured/%s" %(slug, filename)

class ProductoImage(models.Model):
	producto = models.ForeignKey(Producto)
	image = models.ImageField(upload_to='image_upload_to')
	#featured = models.BooleanField(default=False)
	#thumbnail = models.BooleanField(default=False)
	#active = models.BooleanField(default=True)
	#updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.producto.nombre


class Categoria(models.Model):
	nombre = models.CharField(max_length = 120, unique=True)
	slug = models.SlugField(unique=True)
	descripcion = models.TextField(blank = True, null= True)
	activo = models.BooleanField(default = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse("categoria_detalle", kwargs={"slug": self.slug})



class ProductoCategoria(models.Model):
	producto = models.OneToOneField(Producto)
	

	def __str__(self):
		return self.Producto.nombre


# class ProductFeatured(models.Model):
# 	product = models.ForeignKey(Product)
# 	image = models.ImageField(upload_to='image_upload_to_featured')
# 	title = models.CharField(max_length=120, null=True, blank=True)
# 	text = models.CharField(max_length=120, null=True, blank=True)
# 	text_right = models.BooleanField(default=False)
# 	text_css_color = models.CharField(max_length=6, null=True, blank=True)
# 	show_price = models.BooleanField(default=False)
# 	make_image_background = models.BooleanField(default=False)
# 	active = models.BooleanField(default=True)

# 	def __str__(self):
# 		return self.product.title


