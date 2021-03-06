# Generated by Django 2.2.19 on 2021-05-17 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование бригады')),
                ('quantity', models.IntegerField(verbose_name='Численность человек')),
                ('foreman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Бригадир')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Номер заказа')),
                ('year', models.DateField(verbose_name='Дата заказа')),
                ('erp', models.CharField(blank=True, max_length=100, null=True, verbose_name='GUID из ERP')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('change', models.IntegerField(blank=True, null=True, verbose_name='Смена')),
                ('drawing', models.FloatField(blank=True, null=True, verbose_name='Отсутствие чертежей')),
                ('deviations', models.FloatField(blank=True, null=True, verbose_name='Отсутствие решения по выявленным отклонениям')),
                ('personal', models.FloatField(blank=True, null=True, verbose_name='Отсутствие персонала')),
                ('otk', models.FloatField(blank=True, null=True, verbose_name='Отсутствие ОТК')),
                ('vp', models.FloatField(blank=True, null=True, verbose_name='Отсутствие ВП и/или представителя заказчика')),
                ('proektant', models.FloatField(blank=True, null=True, verbose_name='Отсутствие представителя проектанта')),
                ('ogt', models.FloatField(blank=True, null=True, verbose_name='Отсутствие представителя ОГТ для решения блокирующих вопросов')),
                ('other_order', models.FloatField(blank=True, null=True, verbose_name='Переход на другой заказ/другие работы')),
                ('ssz', models.FloatField(blank=True, null=True, verbose_name='Отсутствие ССЗ')),
                ('complect_zavod', models.FloatField(blank=True, null=True, verbose_name='Отсутствие комплектующих по межзаводской кооперации')),
                ('complect_workshop', models.FloatField(blank=True, null=True, verbose_name='Отсутствие комплектующих по межцеховой кооперации')),
                ('pki', models.FloatField(blank=True, null=True, verbose_name='Отсутствие ПКИ')),
                ('materials', models.FloatField(blank=True, null=True, verbose_name='Отсутствие расходных/вспомогательных материалов')),
                ('osn', models.FloatField(blank=True, null=True, verbose_name='Отсутствие оснастки')),
                ('instr', models.FloatField(blank=True, null=True, verbose_name='Отсутствие инструмента')),
                ('prisp', models.FloatField(blank=True, null=True, verbose_name='Отсутствие приспособлений')),
                ('card_valid', models.FloatField(blank=True, null=True, verbose_name='Доработка по причине карт разрешений')),
                ('quality', models.FloatField(blank=True, null=True, verbose_name='Добработка по причине исправления качества')),
                ('brigade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assembly.Brigade', verbose_name='Бригада')),
                ('foreman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Бригадир')),
            ],
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование подразделения')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование работ')),
                ('description', models.CharField(max_length=150, verbose_name='Обозначение')),
                ('date', models.DateField(verbose_name='Срок')),
                ('laboriousness', models.FloatField(verbose_name='Трудоемкость')),
                ('de_facto', models.FloatField(blank=True, default=0, null=True, verbose_name='Фактическая трудоемкость')),
                ('status', models.IntegerField(choices=[(1, 'Создано'), (2, 'В работе'), (3, 'Закрыто')], default=1, verbose_name='Статус')),
                ('create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Разработчик')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assembly.Order', verbose_name='Заказ на производство')),
                ('subdivision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assembly.Subdivision', verbose_name='Подразделение')),
            ],
        ),
        migrations.CreateModel(
            name='Task_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_out', models.FloatField(blank=True, null=True, verbose_name='Значение')),
                ('report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assembly.Report', verbose_name='Отчет')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assembly.Task', verbose_name='Задание')),
            ],
        ),
        migrations.CreateModel(
            name='Task_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('on_work', models.DateTimeField(blank=True, null=True, verbose_name='Взято в работу')),
                ('closed', models.DateTimeField(blank=True, null=True, verbose_name='Закрыто')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assembly.Task', verbose_name='Задание')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assembly.Subdivision', verbose_name='Подразделение'),
        ),
        migrations.AddField(
            model_name='report',
            name='task',
            field=models.ManyToManyField(blank=True, null=True, through='assembly.Task_Report', to='assembly.Task', verbose_name='Задание'),
        ),
        migrations.AddField(
            model_name='brigade',
            name='subdivision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assembly.Subdivision', verbose_name='Подразделение'),
        ),
    ]
