from django.contrib import admin

# Importar modelos desde apps de backend
from panel.models import Page_Model, Backend_Search_Model, Message_Contact_Model, Frontend_Search_Model, Message_Agent_Model
from agent.models import Agent_Model
from blog.models import Article_Model, Category_Model
from customer.models import Customer_Model
from realstate.models import Realstate_Model, Realstate_Type_Model, Message_Realstate_Model

# Registrar modelos en admin
admin.site.register(Page_Model)
admin.site.register(Backend_Search_Model)
admin.site.register(Frontend_Search_Model)
admin.site.register(Message_Contact_Model)
admin.site.register(Message_Agent_Model)

admin.site.register(Agent_Model)
admin.site.register(Article_Model)
admin.site.register(Category_Model)

#admin.site.register(Customer_Model)
admin.site.register(Realstate_Model)
admin.site.register(Realstate_Type_Model)
admin.site.register(Message_Realstate_Model)
