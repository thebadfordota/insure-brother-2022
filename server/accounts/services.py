from django.conf import settings
from pymongo import MongoClient


class CountViewsServices:
    """
    Данный класс реализует логику для расчёта кол-ва просмотров различных продуктов.
    """

    def __init__(self):
        self.client = MongoClient(host=settings.MONGODB_HOST,
                                  port=settings.MONGODB_PORT,
                                  username=settings.MONGODB_USERNAME,
                                  password=settings.MONGODB_PASSWORD)
        self.collection = self.client[settings.MONGODB_DATABASE]['count_views']

    def increase_count_views(self, product_id: int, product_name: str) -> None:
        if self.collection.count_documents({'_id': product_id}) == 0:
            self.collection.insert_one({
                '_id': product_id,
                'name': product_name,
                'url': f'/accounts/product/message/{product_id}',
                'number_views': 0
            })
        else:
            number_views = self.collection.find_one({'_id': product_id})['number_views']
            self.collection.update_one({'_id': product_id}, {'$set': {'number_views': number_views + 1}})

    def get_count_views(self, product_id: int) -> int:
        if self.collection.count_documents({'_id': product_id}) == 1:
            return self.collection.find_one({'_id': product_id})['number_views']
        return 0

    def delete_count_views_info(self, product_id: int) -> None:
        self.collection.delete_one({'_id': product_id})

    def update_count_views_info(self, product_id: int, product_name: str) -> None:
        self.collection.update_one({'_id': product_id}, {'$set': {'name': product_name}})

# client = MongoClient(host='mongo', port=27017,
#                                   username='admin', password='admin')
# collection = client['insure_brother']['count_views']
# data = collection.find()
# for el in data:
#     print(el)
# collection.delete_one({'_id': 1})
