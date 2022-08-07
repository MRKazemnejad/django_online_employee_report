from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime,timedelta
import pytz



class Command(BaseCommand):
    def handle(self, *args, **options):
        now_time=datetime.now(tz=pytz.timezone('Asia/Tehran'))-timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=now_time).delete()
        self.stdout.write('your otp deleted successfully')
