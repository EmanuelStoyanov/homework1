ZODIAC = {
    range(321, 421): 'Aries',
    range(421, 521): 'Taurus',
    range(521, 621): 'Gemini',
    range(621, 722): 'Cancer',
    range(722, 823): 'Leo',
    range(823, 923): 'Virgo',
    range(923, 1023): 'Libra',
    range(1023, 1122): 'Scorpio',
    range(1122, 1222): 'Saggittarius',
    range(101, 120): 'Capricorn',
    range(1222, 1232): 'Capricorn',
    range(120, 219): 'Aquarius',
    range(219, 321): 'Pisces',
}

def what_is_my_sign(day, month):
    for date in ZODIAC:
        if 100*month + day in date:
            return ZODIAC[date]