import django as django
from django.db import models
from django.db.models import Sum

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/3.2/ref/models/fields/
    """

    date = models.DateField(
        verbose_name='日付',
        default=django.utils.timezone.now,
    )

    money = models.IntegerField(
        verbose_name='金額',
        blank=True,
        null=True,
    )

    type_choice = (
        (1, '売上'),
        (2, '酒'),
        (3, 'レイ'),
        (4, 'ヒカル'),
        (5, 'シン'),
        (6, '店'),
        (7, '他'),
    )

    type = models.IntegerField(
        verbose_name='分類',
        choices=type_choice,
        blank=True,
        null=True,
    )

    other = models.CharField(
        verbose_name='備考',
        max_length=100,
        blank=True,
        null=True,
    )

    # # サンプル項目1 文字列
    # sample_1 = models.CharField(
    #     verbose_name='サンプル項目1 文字列',
    #     max_length=20,
    #     blank=True,
    #     null=True,
    # )
    #
    # # サンプル項目2 メモ
    # sample_2 = models.TextField(
    #     verbose_name='サンプル項目2 メモ',
    #     blank=True,
    #     null=True,
    # )
    #
    # # サンプル項目3 整数
    # sample_3 = models.IntegerField(
    #     verbose_name='サンプル項目3 整数',
    #     blank=True,
    #     null=True,
    # )
    #
    # # サンプル項目4 浮動小数点
    # sample_4 = models.FloatField(
    #     verbose_name='サンプル項目4 浮動小数点',
    #     blank=True,
    #     null=True,
    # )
    #
    # # サンプル項目5 固定小数点
    # sample_5 = models.DecimalField(
    #     verbose_name='サンプル項目5 固定小数点',
    #     max_digits=5,
    #     decimal_places=2,
    #     blank=True,
    #     null=True,
    # )
    #
    # # サンプル項目6 ブール値
    # sample_6 = models.BooleanField(
    #     verbose_name='サンプル項目6 ブール値',
    # )
    #
    # # サンプル項目7 日付
    # sample_7 = models.DateField(
    #     verbose_name='サンプル項目7 日付',
    #     blank=True,
    #     null=True,
    # )
    #
    # # サンプル項目8 日時
    # sample_8 = models.DateTimeField(
    #     verbose_name='サンプル項目8 日時',
    #     blank=True,
    #     null=True,
    # )
    #
    # # サンプル項目9 選択肢（固定）
    # sample_9_choice = (
    #     (1, '選択１'),
    #     (2, '選択２'),
    #     (3, '選択３'),
    # )
    #
    # sample_9 = models.IntegerField(
    #     verbose_name='サンプル項目9_選択肢（固定）',
    #     choices=sample_9_choice,
    #     blank=True,
    #     null=True,
    # )
    #
    # # サンプル項目9 選択肢（マスタ連動）
    # sample_10 = models.ForeignKey(
    #     User,
    #     verbose_name='サンプル項目10_選択肢（マスタ連動）',
    #     blank=True,
    #     null=True,
    #     related_name='sample_10',
    #     on_delete=models.SET_NULL,
    # )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.date.__str__()

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = '日別情報'
        verbose_name_plural = '日別情報'

    def type_name(self):
        return self.get_type_display()

    def total(self):
        qs = Item.objects.filter(date__month=self.date.month, created_by=self.created_by).aggregate(Sum('money'))
        sum = qs['money__sum']
        if not sum:
            sum = 0
        return sum
