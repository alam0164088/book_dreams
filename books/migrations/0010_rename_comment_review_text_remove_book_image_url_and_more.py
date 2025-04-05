# Generated by Django 5.1.7 on 2025-04-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_download_link_alter_book_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='added_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booktype',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
