# Generated by Django 4.1.4 on 2022-12-12 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(db_index=True, max_length=20, verbose_name='Название кампании')),
            ],
            options={
                'verbose_name': 'Кампания',
                'verbose_name_plural': 'Кампании',
            },
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('mail', models.EmailField(max_length=50, verbose_name='Адресс электронной почты')),
                ('telephone', models.IntegerField(verbose_name='Номер телефона')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company', verbose_name='Кампания')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('house_number', models.IntegerField(blank=True, null=True, verbose_name='Номер дома')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company', verbose_name='Кампания')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
        ),
    ]
