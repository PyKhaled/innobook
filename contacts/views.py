from rest_framework.viewsets import ModelViewSet
from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactsViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

