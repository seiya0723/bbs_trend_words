from django.core.management.base import BaseCommand

from ...models import Topic,Trend
from ...forms import TrendForm

from pyknp import Juman

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        #トレンドモデルの初期化
        trends  = Trend.objects.all()
        trends.delete()

        # https://pyknp.readthedocs.io/en/latest/pyknp.juman.html
        #デフォルトでJuman++のオブジェクトが作られる。Jumanにしたい場合は、引数にjumanpp=Falseを指定。
        jumanpp = Juman()

        #TODO:ここで投稿されているトピックを調べる
        topics  = Topic.objects.all()

        for topic in topics:

            result  = jumanpp.analysis(topic.comment)

            for m in result.mrph_list():

                if m.hinsi != "名詞":
                    continue

                obj = Trend.objects.filter(word=m.midasi).first()
                if obj:
                    obj.count += 1
                    obj.save()
                else:
                    form    = TrendForm({"word":m.midasi,"count":1})
                    if form.is_valid():
                        form.save()
            
