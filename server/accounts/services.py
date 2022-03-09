from django.conf import settings
from pymongo import MongoClient


class CountViewsServices:
    """
    Данный класс реализует логику для расчёта кол-ва просмотров различных продуктов.
    """

    def __init__(self, product_id: int):
        self.client = MongoClient(host=settings.MONGODB_HOST,
                                  port=settings.MONGODB_PORT,
                                  username=settings.MONGODB_USERNAME,
                                  password=settings.MONGODB_PASSWORD)
        self.collection = self.client[settings.MONGODB_DATABASE]['count_views']
        self.product_id = product_id

    def increase_count_views(self, product_name: str) -> None:
        """
        Увеличивает счётчик кол-ва просмотров.
        :param product_name: название продукта компании
        :return: None
        """
        if self.collection.count_documents({'_id': self.product_id}) == 0:
            self.collection.insert_one({
                '_id': self.product_id,
                'name': product_name,
                'url': f'/accounts/product/message/{self.product_id}',
                'number_views': 0
            })
        else:
            number_views = self.collection.find_one({'_id': self.product_id})['number_views']
            self.collection.update_one({'_id': self.product_id}, {'$set': {'number_views': number_views + 1}})

    def get_count_views(self) -> int:
        """
        Возвращает кол-во просмотров.
        :return: кол-во просмотров
        """
        if self.collection.count_documents({'_id': self.product_id}) == 1:
            return self.collection.find_one({'_id': self.product_id})['number_views']
        return 0

    def delete_count_views_info(self) -> None:
        """
        Удаляет запись о продукте.
        :return: None
        """
        self.collection.delete_one({'_id': self.product_id})

    def update_count_views_info(self, product_name: str) -> None:
        """
        Обновляет запись о продукте компании.
        :param product_name: название продукта компании
        :return: None
        """
        self.collection.update_one({'_id': self.product_id}, {'$set': {'name': product_name}})
