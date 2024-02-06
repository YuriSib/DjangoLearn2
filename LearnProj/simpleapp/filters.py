from django_filters import FilterSet, ModelMultipleChoiceFilter, ModelChoiceFilter
from .models import Product, UsedFor


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
    # фильтр по одному из параметров
    # used_for = ModelChoiceFilter(
    #     field_name='productusedfor__used_for',
    #     queryset=UsedFor.objects.all(),
    #     label='Обрабатываемый материал',
    #     empty_label='Любой'
    # )
    # фильтр по многим параметрам
    used_for = ModelMultipleChoiceFilter(
        field_name='productusedfor__used_for',
        queryset=UsedFor.objects.all(),
        label='Обрабатываемый материал',
        conjoined=False #фильтрация по вхождению нескольких параметром в товар
    )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': ['lt', 'gt'],
        }
