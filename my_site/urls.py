from django.urls import path
from django.views.generic import TemplateView

app_name = 'my_site'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('preobrasovatel1045/', TemplateView.as_view(template_name='preobrasovatel1045.html'),
         name='preobrasovatel1045'),
    path('vipryamitel_vir_150_15/', TemplateView.as_view(template_name='vipryamitel_vir_150_15.html'),
         name='vipryamitel_vir_150_15'),
    path('vipryamitel_vi_300_15/', TemplateView.as_view(template_name='vipryamitel_vi_3000_15.html'),
         name='vipryamitel_vi_3000_15'),
    path('vipryamitel_vi_400_12/', TemplateView.as_view(template_name='vipryamitel_vi_400_12.html'),
         name='vipryamitel_vi_400_12'),
    path('vipryamitel_vi_100_30/', TemplateView.as_view(template_name='vipryamitel_vi_100_30.html'),
         name='vipryamitel_vi_100_30'),
    path('vipryamitel_vi_600_30/', TemplateView.as_view(template_name='vipryamitel_vi_600_30.html'),
         name='vipryamitel_vi_600_30'),
    path('vipryamitel_vi_1200_30/', TemplateView.as_view(template_name='vipryamitel_vi_1200_30.html'),
         name='vipryamitel_vi_1200_30'),
]
