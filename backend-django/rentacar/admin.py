from django.contrib import admin
from .models import Reservation, Customer, Car

#? filter
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter

#? import-export 
from import_export.admin import ImportExportModelAdmin
from .resources import ReservationResource

#! admin panelde customize için ModelAdmin inherit edilmeli
class ReservationAdmin(ImportExportModelAdmin):
    #? hangi field'lar görünsün
    list_display = ("id", "car", "customer", "start_date", "end_date")
    
    #? edit edilmesini istediklerimiz (true/false olursa tik aktif olur, açıklama/yazı vs. değiştirilebilir.)
    list_editable = ( "car", )
    
    #? link olsun, üzerine basınca objeye gitsin,
    #* default name field link'tir.
    #! link olan editable olmaz, birden fazla link olabilir.
    list_display_links = ("customer", )
    
    #? filitreleme için (django'nun default filitrelemesi, çok fazla seçenek yok)
    list_filter = ("car", "customer")
    # list_filter = ("car", ("customer", DateRangeFilter ))
    
    #? sıralama (ilk açılış için) ("-name",) eksi de olabilir,
    ordering = ("start_date",)
    
    #? sayfa üzerinde search box açılıyor,
    #? içinde geçse yeterli, büyük/küçük harf duyarlı değil
    search_fields = ("car",)
    
    #? pagination, default 100
    list_per_page = 5
    
    #? yıl / ay / tarih ayrı ayrı seçilebiliyor.
    #? tarihe göre filitreleme yapıyor, searh box altında çıkıyor,
    date_hierarchy = "start_date"
    
    #?id'ye göre seçim yaptırıyor, yazılmazsa deafult tam liste çıkıyor.
    raw_id_fields = ('customer',)
    
    resource_class = ReservationResource
    
    #! fieldsets kullanınca fields kullanmaya gerek yok, bu daha detaylı bir görünüm veriyor.
    #? her obje, yani her product nasıl görünsün,
    #? burada iki bölüm halinde görmek için ikiye ayırmış,
    #? birinci bölüme isim vermemiş None, ikinciye Optionals Settings yazmış
    #? classes, collapse-kapalı gelir, SHOW yapılır, wide-açık gelir
    #? description, açıklma yazılır.
    fieldsets = (
    #* birinci bölüm;
    ("Reserved Days", {
        #? nasıl görünsün KAPALI/AÇIK  SHOW/HIDE gibi
        # 'classes': ('wide', 'extrapretty'), # wide or collapse
        
        #? hangi fieldlar görünsün, (tuple içindekiler yan yana, diğerleri alt alta)
        #? buraya sadece edit edilebilir field'lar yazılabiliyor.
        "fields": (
            ('start_date', 'end_date', "car"),
        ),
        #? bölüm başına bir açıklama yazmak için kullanalan field, modeldeki description field'tan farklı
        "description" : "Section 1 - Dates"
    }),
    #* ikinci bölüm;
    ('Customer Info', {
        #? nasıl görünsün KAPALI/AÇIK  SHOW/HIDE gibi
        "classes" : ("collapse", ),
        
        #? hangi fieldlar görünsün, (tuple içindekiler yan yana, diğerleri alt alta)
        # "fields" : ("description",),
        # "fields" : ("description", "categories"),
        #? sonradan eklenen image field ilave edildi
        #? buraya sadece edit edilebilir field'lar yazılabiliyor.
        "fields" : ("customer", ),
        
        #? bölüm başına bir açıklama yazmak için kullanalan field, modeldeki description field'tan farklı
        "description" : "Section 2 - Info"
    })
    )

class CustomerAdmin(admin.ModelAdmin):
    #? list_display içine metod'da yazabiliriz, __str__ veya kendi yazdığımız metodlar,
    list_display = ('__str__', 'customer_id')
    list_per_page = 5
class CarAdmin(admin.ModelAdmin):
    pass










# Register your models here.
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)

#! tab/sekmedeki isim 
admin.site.site_title = "Cooper RentACarApp"

#! başlıktaki isim
admin.site.site_header = "Designed by @Cooper"  

#! Home'daki isim
admin.site.index_title = "Rent A Car Django Admin Portal"