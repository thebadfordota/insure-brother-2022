class ProductFilterServices:
    """
    Данный класс реализует фильтрацию полей таблицы 'Product'.
    """

    def __init__(self, form, product_info):
        self.form = form
        self.product_info = product_info

    def get_filtered_fields(self):
        if self.form.is_valid():
            if self.form.cleaned_data['price']:
                self.product_info = self.product_info.filter("term", price=self.form.cleaned_data['price'])
            if self.form.cleaned_data['duration_of_action']:
                self.product_info = self.product_info.filter("term", duration_of_action=self.form.cleaned_data['duration_of_action'])
            if self.form.cleaned_data['appearance_date']:
                self.product_info = self.product_info.query("match", appearance_date=self.form.cleaned_data['appearance_date'])
            if self.form.cleaned_data['product_name']:
                self.product_info = self.product_info.query("match", name=self.form.cleaned_data['product_name'])
        return self.product_info.to_queryset()
