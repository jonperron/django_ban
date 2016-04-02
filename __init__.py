# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

class Choices:
	DURATIONS = (
			(_'5 minutes',300),
			(_'10 minutes',600),
			(_'20 minutes',1200),
			(_'30 minutes',1800),
			(_'1 hour',3600),
			(_'2 hours',7200),
			(_'5 hours',18000),
			(_'10 hours', 36000),
			(_'1 day',86400),
			(_'2 days',172800),
			(_'1 week',604800),
			(_'2 weeks',1209600),
			(_'1 month',2419200),
			(_'Unlimited',9999999),
		)