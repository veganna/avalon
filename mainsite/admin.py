from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(contactSubjects)

admin.site.register(contactMessages)

admin.site.register(roadMapModel)

admin.site.register(roadMapSteps)

admin.site.register(faqCategories)

admin.site.register(faqItem)

# NFT Items
admin.site.register(nftUsers)
admin.site.register(nftCategory)
admin.site.register(nftTag)
admin.site.register(nftCoin)
admin.site.register(nftItem)

admin.site.register(nftRarity)
admin.site.register(nftElement)
admin.site.register(nftType)

# NFT Team

admin.site.register(nftTeam)