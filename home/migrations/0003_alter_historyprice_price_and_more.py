# Generated by Django 4.1.3 on 2023-01-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_historyprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyprice',
            name='price',
            field=models.FloatField(null=True, blank=True),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='historyprice',
            unique_together={('ticker', 'date')},
        ),
    ]