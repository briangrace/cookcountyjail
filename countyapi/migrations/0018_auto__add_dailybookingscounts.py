# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DailyBookingsCounts'
        db.create_table('countyapi_dailybookingscounts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('booking_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_as', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_b', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_bk', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_in', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_lb', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_lw', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_lt', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_w', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_wh', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_minors', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_as', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_b', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_bk', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_in', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_lb', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_lw', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_lt', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_w', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_wh', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('male_minors', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('countyapi', ['DailyBookingsCounts'])

    def backwards(self, orm):
        # Deleting model 'DailyBookingsCounts'
        db.delete_table('countyapi_dailybookingscounts')

    models = {
        'countyapi.chargeshistory': {
            'Meta': {'object_name': 'ChargesHistory'},
            'charges': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'charges_citation': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_seen': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'charges_history'", 'to': "orm['countyapi.CountyInmate']"})
        },
        'countyapi.countyinmate': {
            'Meta': {'ordering': "['-jail_id']", 'object_name': 'CountyInmate'},
            'age_at_booking': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bail_amount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bail_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'booking_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'discharge_date_earliest': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'discharge_date_latest': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'jail_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'primary_key': 'True'}),
            'last_seen_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'countyapi.courtdate': {
            'Meta': {'ordering': "['date']", 'object_name': 'CourtDate'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'court_dates'", 'to': "orm['countyapi.CountyInmate']"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'court_dates'", 'to': "orm['countyapi.CourtLocation']"})
        },
        'countyapi.courtlocation': {
            'Meta': {'object_name': 'CourtLocation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'branch_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'room_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'countyapi.dailybookingscounts': {
            'Meta': {'ordering': "['booking_date']", 'object_name': 'DailyBookingsCounts'},
            'booking_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'female_as': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_bk': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_in': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_lb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_lt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_lw': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_minors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_w': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_wh': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male_as': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_bk': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_in': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_lb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_lt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_lw': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_minors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_w': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_wh': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'countyapi.dailypopulationcounts': {
            'Meta': {'ordering': "['booking_date']", 'object_name': 'DailyPopulationCounts'},
            'booking_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'female_as': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_bk': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_in': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_lb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_lt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_lw': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_w': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'female_wh': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male_as': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_bk': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_in': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_lb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_lt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_lw': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_w': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_wh': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'countyapi.housinghistory': {
            'Meta': {'object_name': 'HousingHistory'},
            'housing_date_discovered': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'housing_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'housing_history'", 'to': "orm['countyapi.HousingLocation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'housing_history'", 'to': "orm['countyapi.CountyInmate']"})
        },
        'countyapi.housinglocation': {
            'Meta': {'object_name': 'HousingLocation'},
            'division': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'housing_location': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'in_jail': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'in_program': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'sub_division': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sub_division_location': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'countyapi.inmatesummaries': {
            'Meta': {'object_name': 'InmateSummaries'},
            'current_inmate_count': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['countyapi']