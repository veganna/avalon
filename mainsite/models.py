from django.db import models

# Create your models here.

class nftTeam(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    photo = models.ImageField(blank=True)

class contactSubjects(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name


class contactMessages(models.Model):
    nameField = models.CharField(max_length=255, null=False)
    mailField = models.EmailField(max_length=255, null=False)
    subjectField = models.ForeignKey(contactSubjects, on_delete=models.CASCADE)
    messageField = models.TextField()
    dateField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameField

class roadMapSteps(models.Model):
    stepName = models.CharField(max_length=100)

    
    def __str__(self):
        return self.stepName

class roadMapModel(models.Model):
    quarterTitle = models.CharField(max_length=20)
    quarterList = models.ManyToManyField(roadMapSteps)


    def __str__(self):
        return self.quarterTitle

class faqCategories(models.Model):
    faqName = models.CharField(max_length=50)

    def __str__(self):
        return self.faqName

class faqItem(models.Model):
    faqTitle = models.CharField(max_length=255)
    faqText = models.TextField()
    faqCategorie = models.ForeignKey(faqCategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.faqTitle

class nftUsers(models.Model): ## Should change for accounts
    nftName = models.CharField(max_length=255)
    nftPhoto = models.ImageField(blank=True)

    def __str__(self):
        return self.nftName

class nftCategory(models.Model):
    nftCategoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.nftCategoryName

class nftTag(models.Model):
    nftTagName = models.CharField(max_length=25)
    nftTagColor = models.CharField(max_length=25)

    def __str__(self):
        return self.nftTagName

class nftCoin(models.Model):
    nftCoinName = models.CharField(max_length=25)
    nftConvertValue = models.FloatField( default = 0 )

    def abvName(self):
        return self.nftCoinName[0:3]

    def __str__(self):
        return self.nftCoinName

class nftRarity(models.Model):
    nftRarityName = models.CharField(max_length=50)

    def __str__(self):
        return self.nftRarityName

class nftElement(models.Model):
    nftElementName = models.CharField(max_length=50)

    def __str__(self):
        return self.nftElementName

class nftType(models.Model):
    nftTypeName = models.CharField(max_length=50)

    def __str__(self):
        return self.nftTypeName

class nftItem(models.Model):
    nftTitle = models.CharField(max_length=255)
    nftCreators = models.ForeignKey(nftUsers, on_delete=models.CASCADE, related_name='creator')
    nftCategories = models.ManyToManyField(nftCategory)
    nftCoins = models.ForeignKey(nftCoin, on_delete=models.CASCADE)
    nftPrice = models.FloatField(default = 0)
    nftPhoto = models.ImageField(blank=True)
    nftLikes = models.IntegerField(default = 0)
    nftTags = models.ForeignKey(nftTag, on_delete=models.CASCADE, null=True)
    nftWatched = models.IntegerField(default = 0)
    nftOwner = models.ForeignKey(nftUsers, on_delete=models.CASCADE, related_name='owner', null=True)
    nftDescription = models.TextField(default = '')
    nftCountDown = models.IntegerField(default = 0)
    nftRarities = models.ForeignKey(nftRarity, on_delete=models.CASCADE, null=True)
    nftElements = models.ForeignKey(nftElement, on_delete=models.CASCADE, null=True)
    nftTypes = models.ForeignKey(nftType, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nftTitle

    def convert(self):
        return format(self.nftPrice * self.nftCoins.nftConvertValue, '.3f')

    def countdown(self):
        hours = int(self.nftCountDown / 3600)
        minutes = int(self.nftCountDown / 60 % 60)
        seconds = int(self.nftCountDown % 60)
        return f'{hours} : {minutes} : {seconds}'

