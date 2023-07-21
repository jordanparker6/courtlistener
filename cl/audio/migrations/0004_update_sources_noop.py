# Generated by Django 3.2.18 on 2023-05-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_update_triggers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='source',
            field=models.CharField(blank=True, choices=[('C', 'court website'), ('R', 'public.resource.org'), ('CR', 'court website merged with resource.org'), ('L', 'lawbox'), ('LC', 'lawbox merged with court'), ('LR', 'lawbox merged with resource.org'), ('LCR', 'lawbox merged with court and resource.org'), ('M', 'manual input'), ('A', 'internet archive'), ('H', 'brad heath archive'), ('Z', 'columbia archive'), ('ZC', 'columbia merged with court'), ('ZLC', 'columbia merged with lawbox and court'), ('ZLR', 'columbia merged with lawbox and resource.org'), ('ZLCR', 'columbia merged with lawbox, court, and resource.org'), ('ZR', 'columbia merged with resource.org'), ('ZCR', 'columbia merged with court and resource.org'), ('ZL', 'columbia merged with lawbox'), ('U', 'Harvard, Library Innovation Lab Case Law Access Project'), ('CU', 'court website merged with Harvard'), ('D', 'direct court input'), ('Q', '2020 anonymous database'), ('QU', '2020 anonymous database merged with Harvard'), ('CU', 'court website merged with Harvard'), ('CRU', 'court website merged with public.resource.org and Harvard'), ('DU', 'direct court input merged with Harvard'), ('LU', 'lawbox merged with Harvard'), ('LCU', 'Lawbox merged with court website and Harvard'), ('LRU', 'Lawbox merged with public.resource.org and with Harvard'), ('MU', 'Manual input merged with Harvard'), ('RU', 'public.resource.org merged with Harvard'), ('ZU', 'columbia archive merged with Harvard')], help_text='the source of the audio file, one of: C (court website), R (public.resource.org), CR (court website merged with resource.org), L (lawbox), LC (lawbox merged with court), LR (lawbox merged with resource.org), LCR (lawbox merged with court and resource.org), M (manual input), A (internet archive), H (brad heath archive), Z (columbia archive), ZC (columbia merged with court), ZLC (columbia merged with lawbox and court), ZLR (columbia merged with lawbox and resource.org), ZLCR (columbia merged with lawbox, court, and resource.org), ZR (columbia merged with resource.org), ZCR (columbia merged with court and resource.org), ZL (columbia merged with lawbox), U (Harvard, Library Innovation Lab Case Law Access Project), CU (court website merged with Harvard), D (direct court input), Q (2020 anonymous database), QU (2020 anonymous database merged with Harvard), CU (court website merged with Harvard), CRU (court website merged with public.resource.org and Harvard), DU (direct court input merged with Harvard), LU (lawbox merged with Harvard), LCU (Lawbox merged with court website and Harvard), LRU (Lawbox merged with public.resource.org and with Harvard), MU (Manual input merged with Harvard), RU (public.resource.org merged with Harvard), ZU (columbia archive merged with Harvard)', max_length=10),
        ),
        migrations.AlterField(
            model_name='audioevent',
            name='source',
            field=models.CharField(blank=True, choices=[('C', 'court website'), ('R', 'public.resource.org'), ('CR', 'court website merged with resource.org'), ('L', 'lawbox'), ('LC', 'lawbox merged with court'), ('LR', 'lawbox merged with resource.org'), ('LCR', 'lawbox merged with court and resource.org'), ('M', 'manual input'), ('A', 'internet archive'), ('H', 'brad heath archive'), ('Z', 'columbia archive'), ('ZC', 'columbia merged with court'), ('ZLC', 'columbia merged with lawbox and court'), ('ZLR', 'columbia merged with lawbox and resource.org'), ('ZLCR', 'columbia merged with lawbox, court, and resource.org'), ('ZR', 'columbia merged with resource.org'), ('ZCR', 'columbia merged with court and resource.org'), ('ZL', 'columbia merged with lawbox'), ('U', 'Harvard, Library Innovation Lab Case Law Access Project'), ('CU', 'court website merged with Harvard'), ('D', 'direct court input'), ('Q', '2020 anonymous database'), ('QU', '2020 anonymous database merged with Harvard'), ('CU', 'court website merged with Harvard'), ('CRU', 'court website merged with public.resource.org and Harvard'), ('DU', 'direct court input merged with Harvard'), ('LU', 'lawbox merged with Harvard'), ('LCU', 'Lawbox merged with court website and Harvard'), ('LRU', 'Lawbox merged with public.resource.org and with Harvard'), ('MU', 'Manual input merged with Harvard'), ('RU', 'public.resource.org merged with Harvard'), ('ZU', 'columbia archive merged with Harvard')], help_text='the source of the audio file, one of: C (court website), R (public.resource.org), CR (court website merged with resource.org), L (lawbox), LC (lawbox merged with court), LR (lawbox merged with resource.org), LCR (lawbox merged with court and resource.org), M (manual input), A (internet archive), H (brad heath archive), Z (columbia archive), ZC (columbia merged with court), ZLC (columbia merged with lawbox and court), ZLR (columbia merged with lawbox and resource.org), ZLCR (columbia merged with lawbox, court, and resource.org), ZR (columbia merged with resource.org), ZCR (columbia merged with court and resource.org), ZL (columbia merged with lawbox), U (Harvard, Library Innovation Lab Case Law Access Project), CU (court website merged with Harvard), D (direct court input), Q (2020 anonymous database), QU (2020 anonymous database merged with Harvard), CU (court website merged with Harvard), CRU (court website merged with public.resource.org and Harvard), DU (direct court input merged with Harvard), LU (lawbox merged with Harvard), LCU (Lawbox merged with court website and Harvard), LRU (Lawbox merged with public.resource.org and with Harvard), MU (Manual input merged with Harvard), RU (public.resource.org merged with Harvard), ZU (columbia archive merged with Harvard)', max_length=10),
        ),
    ]