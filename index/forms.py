from django import forms
from django.core.exceptions import ValidationError

from .models import Product


def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError("Please input right weight.")


class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label="名字",
        help_text="this is one field.",
        initial="wyu",
        validators=[weight_validate],
    )
    choices_list = [
        (i + 1, v["type"]) for i, v in enumerate(Product.objects.values("type"))
    ]
    type = forms.ChoiceField(choices=choices_list, label="类型")


class ProductModelForm(forms.ModelForm):
    product_id = forms.CharField(max_length=20, label="产品序号")

    class Meta:
        model = Product
        fields = ["name", "type"]
        exclude = []
        labels = {"name": "产品名称", "type": "产品类型"}
        widgets = {"name": forms.widgets.TextInput(attrs={"class": "c1"})}
        field_classed = {"name": forms.CharField}
        help_texts = {"name": ""}
        error_messages = {
            "__all__": {"required": "请输入内容", "invalid": "请检查输入内容"},
            "name": {"required": "请输入数值", "invalid": "请检查数值是否正确"},
        }

    def clean_name(self):
        data = self.cleaned_data["name"]
        return data + "g"
