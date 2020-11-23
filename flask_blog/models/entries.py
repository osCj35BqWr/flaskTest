from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from flask_blog.lib.utils import is_production
import os


class Entry(Model):
    class Meta:
        table_name = os.environ.get('table_name')
        region = 'ap-northeast-1'
        aws_access_key_id = os.environ.get('SERVERLESS_AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.environ.get('SERVERLESS_AWS_SECRERT_KEY')

    MeasureDateTime = UnicodeAttribute(hash_key=True, null=False)
    value = NumberAttribute(null=True)
    fileName = UnicodeAttribute(null=True)

