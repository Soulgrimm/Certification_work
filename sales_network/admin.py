from django.contrib import admin
from django.db.models import QuerySet
from sales_network.models import Link, Product
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date')
    list_display_links = ['title', 'model']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'debt', 'create_time', 'provider_link')
    list_filter = ('city',)
    list_display_links = ['title']
    actions = ['delete_debt']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def delete_debt(self, request, qs: QuerySet):
        qs.update(debt=0.0)

    def provider_link(self, obj):
        url = (
                reverse("admin:sales_network_link_changelist")
                + "?"
                + urlencode({"link__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} </a>', url, obj.provider)

    provider_link.short_description = "Ссылка на 'Поставщика'"
