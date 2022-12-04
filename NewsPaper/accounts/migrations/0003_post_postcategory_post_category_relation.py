# Generated by Django 4.1.3 on 2022-12-01 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('A', 'article'), ('N', 'news')], default='N', max_length=50)),
                ('data_time', models.DateTimeField(auto_now_add=True)),
                ('post_title', models.TextField()),
                ('post_text', models.TextField()),
                ('post_rating', models.IntegerField(default=0)),
                ('author_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.category')),
                ('post_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category_relation',
            field=models.ManyToManyField(through='accounts.PostCategory', to='accounts.category'),
        ),
    ]
