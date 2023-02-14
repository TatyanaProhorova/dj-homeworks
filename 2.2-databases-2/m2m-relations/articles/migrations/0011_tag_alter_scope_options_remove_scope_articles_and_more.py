# Generated by Django 4.0 on 2023-02-14 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_articlescope_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['is_main', 'tag'], 'verbose_name': 'Тематика статей', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.RemoveField(
            model_name='scope',
            name='articles',
        ),
        migrations.AddField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='article_scopes', to='articles.article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
        migrations.DeleteModel(
            name='ArticleScope',
        ),
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_scopes', to='articles.tag', verbose_name='Раздел'),
        ),
    ]
