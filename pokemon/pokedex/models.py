from django.db import models

class Pokemon(models.Model):
	id_pokemon = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=20)
	height = models.FloatField()
	weight = models.FloatField()
	hp_base = models.IntegerField()
	attack_base = models.IntegerField()
	attack_sp_base = models.IntegerField()
	defense_base = models.IntegerField()
	defense_sp_base = models.IntegerField()
	speed_base = models.IntegerField()
	chain_evo_rel = models.ForeignKey('ChainEvol', db_column='chain_evol_rel', on_delete=models.PROTECT)

	class Meta:
		managed = True
		db_table = 'pokemon'

	def __str__(self):
		return str(self.name)

class ChainEvol(models.Model):
	id_chain = models.IntegerField(primary_key=True)

	class Meta:
		managed = True
		db_table = 'chain_evol'