from django.db.models import Model, QuerySet
from typing import Dict, List, Type, Union
from django.http import HttpResponseNotFound

# по скольку в тз не придусмотрен вариант удаления и редактирования новостей, эти функции опущены
class IService:
    ''' Service interface '''
    model: Type[Model] = None
    base_query_set: Type[QuerySet] = None


class BaseServiceRead(IService):
    def fetch(self, **filters) -> QuerySet:
        ''' Fetch filtered queryset '''
        return self.base_query_set.filter(**filters).all()
    
    def read(self, pk, **filters) -> Union[Model, None]:
        ''' Read exact object '''
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise HttpResponseNotFound('Not Found')


class BaseServiceWrite(IService):
    def create(self, **data) -> Model:
        ''' Write new object to database '''
        new_object = self.model(**data)
        new_object.save()

        return new_object


class BaseService(BaseServiceRead, BaseServiceWrite):
    ''' 
        Все действия с моделями из бд можно совершать только через наследников этого класса! 
        Запрещается использовать методы .create, .delete, .update и т.д. вне сервисов!
    '''
    pass