# Generated by Django 3.2.5 on 2022-03-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0025_auto_20220307_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='items',
            field=models.CharField(choices=[('衣服', '衣服'), ('褲子', '褲子'), ('鞋子', '鞋子'), ('配件', '配件'), ('保養品', '保養品'), ('化妝品', '化妝品'), ('保健食品', '保健食品')], max_length=20),
        ),
    ]
