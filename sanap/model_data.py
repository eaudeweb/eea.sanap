# -*- coding: utf-8

LANGUAGES = (
    ('BG', 'Bulgarian'),
    ('CS', 'Czech'),
    ('DA', 'Danish'),
    ('DE', 'German'),
    ('EL', 'Greek'),
    ('EN', 'English'),
    ('ES', 'Spanish'),
    ('ET', 'Estonian'),
    ('FI', 'Finnish'),
    ('FR', 'French'),
    ('GA', 'Irish'),
    ('H', 'Hungarian'),
    ('IS', 'Icelandic'),
    ('IT', 'Italian'),
    ('LB', 'Luxembourgish'),
    ('LT', 'Lithuanian'),
    ('LV', 'Latvian'),
    ('MT', 'Maltese'),
    ('NL', 'Dutch'),
    ('NO', 'Norwegian'),
    ('PL', 'Polish'),
    ('PT', 'Portuguese'),
    ('RM', 'Rhaeto-Romance'),
    ('RO', 'Romanian'),
    ('SK', 'Slovak'),
    ('SL', 'Slovenian'),
    ('SV', 'Swedish'),
    ('TR', 'Turkish'),
)


YES_NO = (
    ('0', 'No'),
    ('1', 'Yes'),
)


COUNTRIES = (
    ('AL', 'Albania'),
    ('AT', 'Austria'),
    ('BA', 'Bosnia-Herzegovina'),
    ('BE', 'Belgium'),
    ('BG', 'Bulgaria'),
    ('CH', 'Switzerland'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DE', 'Germany'),
    ('DK', 'Denmark'),
    ('EE', 'Estonia'),
    ('ES', 'Spain'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GB', 'United Kingdom'),
    ('GR', 'Greece'),
    ('HR', 'Croatia'),
    ('H', 'Hungary'),
    ('IE', 'Ireland'),
    ('IS', 'Iceland'),
    ('IT', 'Italy'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('L', 'Luxembourg'),
    ('LV', 'Latvia'),
    ('ME', 'Montenegro'),
    ('MK', 'Macedonia (FYR)'),
    ('MT', 'Malta'),
    ('NL', 'Netherlands'),
    ('NO', 'Norway'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('RO', 'Romania'),
    ('RS', 'Serbia'),
    ('SE', 'Sweden'),
    ('SI', 'Slovenia'),
    ('SK', 'Slovakia'),
    ('TR', 'Turkey'),
)


AGREEMENT = (
    ('strongly agree', 'strongly agree'),
    ('agree', 'agree'),
    ('neutral', 'neutral'),
    ('disagree', 'disagree'),
    ('strongly disagree', 'strongly disagree'),
    ('don\'t know', 'don\'t know'),
)


TRIGGER_DATA = (
    'Extreme weather events',
    'Damage costs',
    'UNFCCC process',
    'EU policies',
    'Adaptation in neighbouring countries',
    'Scientific research',
    'Public pressure',
    'Lobbying from private sector',
    'Forerunner sectors',
    'Media coverage',

)
TRIGGERS = [(i, i) for i in TRIGGER_DATA]


BARRIER_DATA = (
    'Lack of political commitment/will',
    'Unclear responsibilities',
    'Limited cooperation among stakeholders',
    'Lack of (financial, human) resources',
    'Uncertainties',
    'Lack of knowledge generation',
    'Lack of knowledge exchange',
    'Lack of data such as socio-economic, climate and other physical data',
    'Limited capacity in the policy, practitioner and/or research communities',
    'Conflicting values and interests',
    'No adequate adaptation options available',
    'Legal issues (e.g. conflicting legislations)',
)
BARRIERS = [(i, i) for i in BARRIER_DATA]


EFFECTIVENESS_DATA = (
    'very effective',
    'effective',
    'medium effective',
    'less effective',
    'not effective',
    'no mechanism in place',
    'don\'t know'
)
EFFECTIVENESS = [(i, i) for i in EFFECTIVENESS_DATA]


STATUS_DATA = (
    'yes',
    'currently under development',
    'not yet, but planned',
    'no',
    'don\'t know',
)
STATUS = [(i, i) for i in STATUS_DATA]


PLANNING_DATA = (
    'not planned',
    'planned but work has not started',
    'update of assessment has started',
    'update already available',
    'don\'t know'
)
PLANNING = [(i, i) for i in PLANNING_DATA]


NEEDED_INFO_DATA = (
    'Uncertainty estimates',
    'Local/community level information',
    'Time period',
    'Estimate of costs',
    'Estimate of benefits',
    'Interdependencies across sectors',
    'Social vulnerability'
)
NEEDED_INFO = [(i, i) for i in NEEDED_INFO_DATA]


ADAPTATION_SCALE_DATA = (
    'national level',
    'sub-national level',
    'sectoral level',
    'cross-sectoral',
)
ADAPTATION_SCALE = [(i, i) for i in ADAPTATION_SCALE_DATA]


IDENTIFIED_OPTIONS_DATA = (
    'Expert judgement',
    'Participatory processes',
    'Cost and benefit assessment',
    'Multi-criteria analyses',
)
IDENTIFIED_OPTIONS = [(i, i) for i in IDENTIFIED_OPTIONS_DATA]


ADAPTATION_ACTIONS_DATA = (
    'Grey measures (i.e. technological such as river flood defence, beach nourishment)',
    'Green measures (i.e. ecosystem-based approaches that use nature\'s multiple services such as crop diversification, enhancing the ability of indigenous plant and animal species to move across landscapes) ',
    'Soft measures  (i.e. behavioural, managerial, legal and policy approaches that includes e.g. awareness raising initiatives, passing legislations, early warning systems, insurances, planning instruments)',
)
ADAPTATION_ACTIONS = [(i, i) for i in ADAPTATION_ACTIONS_DATA]












