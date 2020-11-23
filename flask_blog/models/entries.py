from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from flask_blog.lib.utils import is_production
import os


class Entry(Model):
    class Meta:
        # 名称変更する
        table_name = "serverless_blog_entries"
        region = 'ap-northeast-1'
        aws_access_key_id = os.environ.get('SERVERLESS_AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.environ.get('SERVERLESS_AWS_SECRERT_KEY')

    id = NumberAttribute(hash_key=True, null=False)
    title = UnicodeAttribute(null=True)
    text = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default=datetime.now)
