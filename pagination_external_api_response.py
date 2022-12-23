from abc import ABC, abstractmethod
import math
import urllib.request
import json


class BasePagination(ABC):
    items_per_page: int
    page: int
    total: int
    total_page: int
    count: int

    def __init__(
            self,
            items_per_page: int = 5,
    ):
        self.items_per_page = items_per_page

    def get_paginated_data(
            self,
            page: int,
    ) -> dict:
        self.page = page
        total_data = self.get_data()
        self.total = len(total_data)
        data = self.__get_data_by_page(total_data)
        self.count = len(data)

        return {
            'data': data,
            'pagination': self.get_pagination()
        }

    def __get_data_by_page(self, total_data: list) -> list:
        self.total_page = math.ceil(len(total_data) / self.items_per_page)
        skip = (self.page - 1) * self.items_per_page
        if not (0 <= self.page <= self.total_page):
            raise Exception('The page is out of range')
        if self.page == self.total_page:
            return total_data[skip:skip + min(len(total_data) % self.items_per_page, self.items_per_page)]
        return total_data[skip:skip + self.items_per_page]

    def get_pagination(self) -> dict:
        return {
            'page': self.page,
            'total': self.total,
            'count': self.count,
            'items_per_page': self.items_per_page,
            'total_page': self.total_page
        }

    @abstractmethod
    def get_data(self) -> list:
        pass


class ExternalAPI(BasePagination):
    def get_data(self) -> list:
        nasa_api_key = 'sjptH8YZDCd4bdiuckx5tBH2z3KfERWqGLUffcGB'
        api_url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={nasa_api_key}'

        request = urllib.request.Request(api_url)
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get('photos')


print(ExternalAPI().get_paginated_data(4))