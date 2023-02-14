from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    tag = models.TextField(verbose_name='Тег')
    # tag.name = str(tag)

    articles = models.ManyToManyField(Article, related_name="scopes", through="ArticleScope")   # связь

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['tag']

    def __str__(self):
        return self.tag

class ArticleScope(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name="article_scopes", verbose_name="Раздел") # ссылка
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_scopes")
    main_tag = models.BooleanField(verbose_name="Основной", default=False)

    class Meta:
        verbose_name = 'Тематика статей'
        verbose_name_plural = 'Тематики статьи'
        ordering = ['-main_tag', 'scope']