# Generated by Django 4.2.1 on 2023-05-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_usluga_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usluga',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
