import django_tables2 as tables
from .models import Equipment, UserProfile, Company, LendPeriods
from datetime import timedelta, date


class PeriodsTable(tables.Table):
    """
    Table to render LendingPeriods from database
    """
    def render_name(self, record):
        return '<a href="/periods/show/%s">%s</a>' % (record.id, record.name)

    class Meta:
        model = LendPeriods
        attrs = {'class': 'books_table'}
        sequence = ('name', 'days_amount')
        fields = ('name', 'days_amount')


class CompanyTable(tables.Table):
    """
    Table to render Companies from database
    """
    def render_name(self, record):
        return '<a href="/companies/show/%s">%s</a>' % (record.id, record.name)

    class Meta:
        model = Company
        attrs = {'class': 'books_table'}
        sequence = ('name',)
        fields = ('name',)


class EquipmentTable(tables.Table):
    """
    Table to render Equipments from database
    """
    company = tables.Column()

    lend_period = tables.Column(verbose_name="Borrow for")

    def render_title(self, record):
        return '<a href="/equipments/show/%d">%s</a>' % (record.id, record.title)

    def render_company(self, value):
        return '%s' % (value.__unicode__())[8:]

    def render_lend_period(self, record):
        if record.lend_by != None:
            return 'Already lent'
        else:
            return "<a href='/equipments/borrow/%s' onclick='javascript:return confirm(\"Do you want to borrow %s for %s?\")'>%s</a>" % (record.id, record.title, record.lend_period, record.lend_period.__unicode__())

    class Meta:
        model = Equipment
        attrs = {'class': 'books_table'}
        sequence = ('title', 'company', 'price', 'lend_period')
        fields = ('title', 'company', 'price', 'lend_period')


class EquipmentTableUser(EquipmentTable):
    """
    This table renders equipments, but is used to present
    equipments borrowed by the user and thus slightly differs from EquipmentTable
    """
    lend_period = tables.Column(verbose_name="Need to return in")

    def render_lend_period(self, record):
        tekst = (record.lend_from + timedelta(days=record.lend_period.days_amount) - date.today()).__str__()[0:-9]
        if int(tekst[0:-5]) > 0:
            return '%s' % (record.lend_from + timedelta(days=record.lend_period.days_amount) - date.today()).__str__()[0:-9]
        else:
            return '<span class="deadline">After the deadline!</span>'

    class Meta:
        model = Equipment
        attrs = {'class': 'books_table'}
        sequence = ('title', 'company', 'price', 'lend_period')
        fields = ('title', 'company', 'price', 'lend_period')


class FriendTable(tables.Table):
    """
    Table presents user's friend
    """
    gravator = tables.Column(accessor='gravator_url')
    first_name = tables.Column(accessor='user.first_name')
    last_name = tables.Column(accessor='user.last_name')
    facebook = tables.Column(accessor='fb_name')

    def render_gravator(self, record):
        return '<a href="/users/%s"><img src="%s"></img></a>' % (record.user.username,
                                                                 record.user.profile.gravator_url())

    def render_facebook(self, record):
        if record.user.profile.fb_name:
            return '<a href="http://facebook.com/%s">%s</a>' % (record.user.profile.fb_name, record.user.profile.fb_name)
        else:
            return '<span class="blank">-&lt;Blank&gt;-</span>'

    class Meta:
        model = UserProfile
        attrs = {'class': 'books_table'}
        fields = ('gravator', 'user', 'first_name', 'last_name', 'facebook')
        sequence = ('gravator', 'user', 'first_name', 'last_name', 'facebook')
