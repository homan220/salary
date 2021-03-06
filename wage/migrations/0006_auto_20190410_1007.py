# Generated by Django 2.1.7 on 2019-04-10 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wage', '0005_auto_20190410_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advanceandloan',
            name='amount',
            field=models.DecimalField(decimal_places=5, max_digits=11, verbose_name='مبلغ'),
        ),
        migrations.AlterField(
            model_name='advanceandloan',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='advanceandloan',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baseinfo.Employee', verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='advanceandloan',
            name='pay_date',
            field=models.DateField(auto_now_add=True, verbose_name='تاریخ پرداخت'),
        ),
        migrations.AlterField(
            model_name='paytype',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='paytype',
            name='title',
            field=models.CharField(max_length=150, verbose_name='عنوان نوع پرداخت'),
        ),
        migrations.AlterField(
            model_name='wage',
            name='is_locked',
            field=models.BooleanField(verbose_name='وضعیت قفل'),
        ),
        migrations.AlterField(
            model_name='wage',
            name='month',
            field=models.IntegerField(verbose_name='ماه'),
        ),
        migrations.AlterField(
            model_name='wage',
            name='pay_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wage.PayType', verbose_name='نوع پرداخت'),
        ),
        migrations.AlterField(
            model_name='wage',
            name='title',
            field=models.CharField(max_length=150, verbose_name='عنوان لیست'),
        ),
        migrations.AlterField(
            model_name='wage',
            name='year',
            field=models.IntegerField(verbose_name='سال'),
        ),
    ]
