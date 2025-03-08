from django.contrib import admin, messages
from . import models
from django.db.models import Sum, Count, Q


def mark_as_unverified(modeladmin, request, queryset):
    updated = queryset.update(status=0)
    modeladmin.message_user(request, f'{updated} записей помечены как непроверенные', messages.SUCCESS)

mark_as_unverified.short_description = 'Пометить как непроверенные'

def mark_as_verified(modeladmin, request, queryset):
    updated = queryset.update(status=1)
    modeladmin.message_user(request, f'{updated} записей помечены как проверенные', messages.SUCCESS)

mark_as_verified.short_description = 'Пометить как проверенные'

def mark_as_cancelled(modeladmin, request, queryset):
    updated = queryset.update(status=2)
    modeladmin.message_user(request, f'{updated} записей помечены как отмененные', messages.SUCCESS)
    
mark_as_cancelled.short_description = 'Пометить как отмененные'

def mark_as_completed(modeladmin, request, queryset):
    updated = queryset.update(status=3)
    modeladmin.message_user(request, f'{updated} записей помечены как выполненные', messages.SUCCESS)

mark_as_completed.short_description = 'Пометить как выполненные'

def mark_as_rejected(modeladmin, request, queryset):
    updated = queryset.update(status = 2)
    modeladmin.message_user(request, f'{updated} записей помечены как отклоненные', messages.SUCCESS)

mark_as_rejected.short_description = 'Пометить как отклоненные'

def mark_is_published(modeladmin, request, queryset):
    updated = queryset.update(status = 3)
    modeladmin.message_user(request, f'{updated} записей помечены как опубликованные', messages.SUCCESS)

mark_is_published.short_description = 'Пометить как опубликованные'


class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Ценовая категория'
    parameter_name = 'price_range'
    
    def lookups(self, request, model_admin):
        return [
            ('low', 'До 1000 руб.'),
            ('medium', '1000-3000 руб.'),
            ('high', 'Более 3000 руб.'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(services__price__lte=1000)
        elif self.value() == 'medium':
            return queryset.filter(services__price__gte=1000, services__price__lte=3000)
        elif self.value() == 'high':
            return queryset.filter(services__price__gt=3000)
        return queryset


class RegularClientFilter(admin.SimpleListFilter):
    title = 'Постоянный клиент'
    parameter_name = 'is_regular'
    
    def lookups(self, request, model_admin):
        return [
            ('yes', 'Да (3+ записи)'),
            ('no', 'Нет (менее 3 записей)'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'yes':
            regular_phones = models.Visit.objects.values('phone')\
                .annotate(visit_count=Count('id'))\
                .filter(visit_count__gte=3)\
                .values_list('phone', flat=True)
            return queryset.filter(phone__in=regular_phones)
        
        if self.value() == 'no':
            non_regular_phones = models.Visit.objects.values('phone')\
                .annotate(visit_count=Count('id'))\
                .filter(visit_count__lt=3)\
                .values_list('phone', flat=True)
            return queryset.filter(phone__in=non_regular_phones)
        
        return queryset


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name', 'price']
    search_fields = ['name', 'description']
    ordering = ['name']


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    actions = [mark_as_unverified, mark_as_verified, mark_as_rejected, mark_is_published]
    list_display = ['author_name', 'master', 'rating', 'status', 'created_at' ]
    list_filter = ['rating', 'created_at', 'status', 'master']
    search_fields = ['author_name', 'text', 'master']
    readonly_fields = ['created_at', 'text', 'rating', 'master']
    list_pero_page = 20
    ordering = ['-created_at']
    list_editable = ['status']


@admin.register(models.Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'description', 'phone', 'address']
    ordering = ['first_name', 'last_name']
    filter_horizontal = ['services']


@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):

    def get_total_price(self, obj):
        total = obj.services.aggregate(total=Sum('price'))['total']
        return f'{total or 0} руб.'

    get_total_price.short_description = 'Общая стоимость услуг'

    actions = [mark_as_unverified, mark_as_verified, mark_as_cancelled, mark_as_completed]
    list_display = ['name', 'phone', 'created_at', 'status', 'master', 'get_total_price']
    list_filter = ['status', 'master', 'created_at', RegularClientFilter, PriceRangeFilter]
    search_fields = ['name', 'phone', 'comments']
    list_per_page = 20
    ordering = ['-created_at']
    filter_horizontal = ['services']
    list_editable = ['status']
