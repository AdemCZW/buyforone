# Generated by Django 3.2.5 on 2022-03-07 08:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0024_alter_flight_pd_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='pd_profit',
            field=models.TextField(max_length=100, null=True, verbose_name='數值'),
        ),
        migrations.AddField(
            model_name='flight',
            name='pd_weight',
            field=models.TextField(max_length=100, null=True, verbose_name='重量'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrivalname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='finish',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='fromname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='items',
            field=models.CharField(choices=[('tops', '衣服'), ('pants', '褲子'), ('shoes', '鞋子'), ('accessories', '配件'), ('maintenance', '保養品'), ('makeup', '化妝品'), ('supplemen', '保健食品')], max_length=20),
        ),
        migrations.AlterField(
            model_name='flight',
            name='pd_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]