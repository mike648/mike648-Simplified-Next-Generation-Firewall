from django.db import models

class Packet(models.Model):
    src_ip = models.CharField(max_length=15)
    dst_ip = models.CharField(max_length=15)
    protocol = models.CharField(max_length=10)
    length = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    raw_data = models.TextField(default="null")  # Store raw packet data or a summary
    application = models.CharField(max_length=50, default='Unknown')
    
class PacketFilterRule(models.Model):
    src_ip = models.CharField(max_length=15, blank=True, null=True)
    dst_ip = models.CharField(max_length=15, blank=True, null=True)
    protocol = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(max_length=10, choices=[('allow', 'Allow'), ('deny', 'Deny')])