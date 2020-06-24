# Generated by Django 2.2.4 on 2020-06-17 15:49

import app.utils
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0122_auto_20200615_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('name', models.CharField(max_length=350)),
                ('image', models.ImageField(blank=True, help_text='Poll media asset', null=True, upload_to=app.utils.get_upload_filename)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hackathonregistration',
            name='looking_project',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hackathonregistration',
            name='looking_team_members',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='hook',
            field=models.CharField(choices=[('NO_ACTION', 'No trigger any action'), ('TOWNSQUARE_INTRO', 'Create intro on Townsquare'), ('LOOKING_TEAM_PROJECT', 'Looking for team or project')], default='NO_ACTION', max_length=50),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(blank=True, choices=[('wall_post', 'Wall Post'), ('status_update', 'Update status'), ('new_bounty', 'New Bounty'), ('start_work', 'Work Started'), ('stop_work', 'Work Stopped'), ('work_submitted', 'Work Submitted'), ('work_done', 'Work Done'), ('worker_approved', 'Worker Approved'), ('worker_rejected', 'Worker Rejected'), ('worker_applied', 'Worker Applied'), ('increased_bounty', 'Increased Funding'), ('killed_bounty', 'Canceled Bounty'), ('new_tip', 'New Tip'), ('receive_tip', 'Tip Received'), ('bounty_abandonment_escalation_to_mods', 'Escalated checkin from @gitcoinbot about bounty status'), ('bounty_abandonment_warning', 'Checkin from @gitcoinbot about bounty status'), ('bounty_removed_slashed_by_staff', 'Dinged and Removed from Bounty by Staff'), ('bounty_removed_by_staff', 'Removed from Bounty by Staff'), ('bounty_removed_by_funder', 'Removed from Bounty by Funder'), ('new_crowdfund', 'New Crowdfund Contribution'), ('new_grant', 'New Grant'), ('update_grant', 'Updated Grant'), ('killed_grant', 'Cancelled Grant'), ('negative_contribution', 'Negative Grant Contribution'), ('new_grant_contribution', 'Contributed to Grant'), ('new_grant_subscription', 'Subscribed to Grant'), ('killed_grant_contribution', 'Cancelled Grant Contribution'), ('new_kudos', 'New Kudos'), ('created_kudos', 'Created Kudos'), ('receive_kudos', 'Receive Kudos'), ('joined', 'Joined Gitcoin'), ('played_quest', 'Played Quest'), ('beat_quest', 'Beat Quest'), ('created_quest', 'Created Quest'), ('updated_avatar', 'Updated Avatar'), ('mini_clr_payout', 'Mini CLR Payout'), ('leaderboard_rank', 'Leaderboard Rank'), ('consolidated_leaderboard_rank', 'Consolidated Leaderboard Rank'), ('consolidated_mini_clr_payout', 'Consolidated CLR Payout'), ('hackathon_registration', 'Hackathon Registration'), ('hackathon_new_hacker', 'Hackathon Registration'), ('new_hackathon_project', 'New Hackathon Project'), ('flagged_grant', 'Flagged Grant')], db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('SINGLE_OPTION', 'Single option'), ('SINGLE_CHOICE', 'Single Choice'), ('MULTIPLE_CHOICE', 'Multiple Choices'), ('OPEN', 'Open')], max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='header',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.PollMedia'),
        ),
    ]
