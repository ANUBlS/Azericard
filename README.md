# azericard

Salam Azericard Django ucun kitabxanaya xos geldiniz !

Bu offical library deyil 

Library Azerbaijan Python Users Community ucun yazilib

Asagida examplede nece isdeyeceyi eks olunub Ugurlar

yuklemek ucun 

* `pip install azericard-django`





```python




from azericard.pay import AzeriCard
from django.views import View
from django.http import HttpResponse


class Index(View,AzeriCard):
    terminal = None # That is your personal ID in payment system   
    merch_name = None
    merch_url = None
    key = None
    order = None
    email = None
    desc = None
    amount = None
    rrn = None # Bank reference number 
    int_ref = None # Internal reference number  
    
    
    def get(self, request):
        print(self.terminal)
        return HttpResponse(self.get_data())


````