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
    ('HU', 'Hungarian'),
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
    ('HU', 'Hungary'),
    ('IE', 'Ireland'),
    ('IS', 'Iceland'),
    ('IT', 'Italy'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
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
    ('EEA', 'EEA'),
)


AGREEMENT = (
    ('strongly agree', 'strongly agree'),
    ('agree', 'agree'),
    ('neutral', 'neutral'),
    ('disagree', 'disagree'),
    ('strongly disagree', 'strongly disagree'),
    ('don\'t know', 'don\'t know'),
)


LEVEL_DATA = ('very high', 'high', 'medium', 'low', 'very low', 'don\'t know')
LEVEL = [(i, i) for i in LEVEL_DATA]


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


STATE_OF_WORK_DATA = (
    'not planned',
    'planned',
    'under development',
    'currently being implemented'
)
STATE_OF_WORK = [(i, i) for i in STATE_OF_WORK_DATA]


NEEDED_INFO_DATA = (
    'Uncertainty estimates',
    'Local/community level information',
    'Consideration of different time periods',
    'Estimates of costs',
    'Estimates of benefits',
    'Information on interdependencies across sectors',
    'Consideration of social issues',
)
NEEDED_INFO = [(i, i) for i in NEEDED_INFO_DATA]


ADAPTATION_SCALE_DATA = (
    'national level',
    'sub-national level',
    'trans-national level',
    'sectoral level',
    'cross-sectoral level',
)
ADAPTATION_SCALE = [(i, i) for i in ADAPTATION_SCALE_DATA]

ASSESSMENT_SCALE_DATA = (
    'national level',
    'sub-national level',
    'trans-national level'
)
ASSESSMENT_SCALE = [(i, i) for i in ASSESSMENT_SCALE_DATA]



IDENTIFIED_OPTIONS_DATA = (
    'Expert judgement',
    'Participatory processes',
    'Cost and benefit assessment',
    'Multi-criteria analyses',
)
IDENTIFIED_OPTIONS = [(i, i) for i in IDENTIFIED_OPTIONS_DATA]


ADAPTATION_ACTIONS_DATA = (
    u'Grey options (i.e. technological, such as river flood defence, beach nourishment)',
    u'Green options (i.e. ecosystem-based approaches that use nature’s multiple services, such as crop diversification, enhancing the ability of indigenous plant and animal species to move across landscapes)',
    u'Soft options (i.e. managerial, legal and policy approaches, such as awareness-raising initiatives, passing legislation, creating early warning systems, insurance, planning instruments)',
    'Combined options',
)
ADAPTATION_ACTIONS = [(i, i) for i in ADAPTATION_ACTIONS_DATA]


MONITOR_REPORT_EVALUATE_DATA = (
    'Monitoring',
    'Reporting',
    'Evaluation',
)
MONITOR_REPORT_EVALUATE = [(i, i) for i in MONITOR_REPORT_EVALUATE_DATA]


INSTRUMENTS_DATA = (
    'yes',
    'under development',
    'no',
    'don\'t know',
)
INSTRUMENTS = [(i, i) for i in INSTRUMENTS_DATA]


MAIN_INSTRUMENTS_DATA = (
    'Information (e.g. dissemination, education, guidelines)',
    'Main-streaming',
    'Financial support (e.g. subsidies, taxes)',
    'Legislation',
    'Partnering instruments (e.g. PPPs)',
    'Action plans',
)
MAIN_INSTRUMENTS = [(i, i) for i in MAIN_INSTRUMENTS_DATA]


FINANCING_MECHANISMS_DATA = (
    'Explicit budgetary allocations',
    'Project based public support',
    'Public-private partnerships',
    'Insurance mechanisms',
)
FINANCING_MECHANISMS = [(i, i) for i in FINANCING_MECHANISMS_DATA]


PROCESS_STAGE_DATA = (
    'Adaptation process has not started',
    'Agenda setting (i.e. adaptation is politically recognised as important)',
    'Formulation (i.e. responsible actors respond by formulating adaptation policies)',
    'Decision (i.e. policymakers have adopted an adaptation policy)',
    'Implementation (i.e. measures foreseen in the policy are being implemented)',
    'Monitoring and evaluation (i.e. review and updates of policy/actions)',
)
PROCESS_STAGE = [(i, i) for i in PROCESS_STAGE_DATA]


STAKEHOLDERS_CONTRIBUTION_DATA = (
    'very important',
    'important',
    'neutral',
    'less important',
    'not important',
)
STAKEHOLDERS_CONTRIBUTION = [(i, i) for i in STAKEHOLDERS_CONTRIBUTION_DATA]


INVOLVEMENT_DATA = (
    'Governmental stakeholders from national level (e.g. policy makers, public administration, governmental agencies)',
    'Governmental stakeholders from sub-national level (including local level)',
    'Private sector',
    'Interest groups (e.g. farmers\' association, NGOs)',
    'Scientists/researchers',
    'General public'
)
INVOLVEMENT = [(i, i) for i in INVOLVEMENT_DATA]


SECTORS_DATA = (
    'Agriculture',
    'Forestry',
    'Biodiversity',
    'Human health',
    'Water',
    'Marine and fisheries',
    'Coastal areas',
    'Mountain areas',
    'Tourism',
    'Transport',
    'Energy',
    'Built environment',
    'Spatial planning, urban planning',
    'Disaster risk reduction',
    'Civil protection',
    'Industry',
    'Business and services',
    'Financial/Insurance',
    'Cultural heritage',
)
SECTORS = [(i, i) for i in SECTORS_DATA]
SECTORS_EXTENDED = SECTORS + [('Cross-sectoral impacts', 'Cross-sectoral impacts')]

Q = {
    'lead_organisation': 'Name of lead organisation responsible for the reply (including contact details)',
    'organisations': 'List of other stakeholder organisations also involved in filling out this form',
    '1': '1. In my country, in the past five years, the level of public awareness of the need for adaptation as a response to climate change has increased',
    '2': '2. In my country, the need for climate change adaptation has reached the national political agenda',
    '3': '3. In my country, the following influences have triggered adaptation (Please select three most important triggers)',
    '4': '4. In my country, the willingness to develop policies and to take adaptation actions at national level is',
    '5': '5. In my country, in the past five years, there has been an increase in the amount of adaptation-related knowledge (e.g. in relation to vulnerabilities, adaptation options) generated with the aim of informing policy making',
    '6': '6. In my country, uncertainties in future projections (e.g. uncertainties regarding climate change) are explicitly addressed in the adaptation policy process',
    '7': '7. In my country, adaptation objectives are based on an understanding of the impacts, risks and/or vulnerabilities to climate change',
    '8': '8. In my country, integration of adaptation into sectoral policies and programmes is increasing',
    'provide_examples': 'Please provide examples:',
    '9': '9. In my country, aspects that are relevant to climate change mitigation are taken into account in the adaptation policy process',
    '10': '10. In my country, transnational co-operation is considered as an element in our adaptation policy process',
    '11': '11. In my country, the following barriers for adaptation have been identified (Please select the three most important barriers)',
    'p1comments': 'Please use the box below to provide any further comments and thoughts related to the questions above or any information that you wish to share with us (e.g. reports, references)',
    'files': 'Upload documents. If more than one, compress them in one zip file, or upload one at a time. Files are uploaded when you click the Save button at the end of this page.',
    '12': '12. In what stage of the adaptation policy process is your country in?',
    '13': '13. How would you assess the mechanism put in place at national level to coordinate the horizontal integration (i.e. integration into sectors) of the adaptation policy process?',
    '14': '14. How would you assess the mechanism put in place at national level to coordinate the vertical integration (from national to local level) of the adaptation policy process?',
    'h_coordination': 'Horizontal coordination',
    'v_coordination': 'Vertical coordination',
    'c_coordination': 'What was crucial for successful coordination?',
    'm_coordination': 'What was challenging or missing? ',
    '16': '16. Are risk assessments or vulnerability assessments available for your country?',
    'if_yes': 'If yes: available at',
    'text': 'Please insert text and provide references to documents.',
    '17': '17. In relation to the risk and vulnerability assessment available at national level, which of the following sectors have been covered?',
    'coordination': 'Coordination',
    'meth_approach': 'Methodological approach',
    '19': '19. In relation to the national assessment, have you identified the costs of climate change impacts and the costs and benefits of adaptation?',
    '20': '20. In relation to the national assessment, what kind of information is still needed for risk or vulnerability assessments? Please select the three most important issues:',
    '21': '21. In relation to the national assessment, do you plan to update the risk or vulnerability assessments?',
    'req_regular': 'Are there requirements to do so on a regular basis? Please explain.',
    '22': '22. Have you identified and assessed adaptation options on the basis of risk or vulnerability assessments?',
    '23': '23. How have you identified and assessed adaptation options?',
    '24': '24. Please indicate the types of adaptation options identified:',
    '25': '25. Have you prioritised adaptation options?',
    '26': '26. If you have prioritised adaptation options, which methodological approach (e.g. expert judgment, multi-criteria analysis) has been used?',
    '27': '27. Have the adaptation options been included in an action plan?',
    '28': u'28. Please provide a maximum of three examples of what you would consider as ‘good practices’ in adaptation that have already been put in place in your country. Please indicate why they are considered to be ‘good practice’?',
    '29': '29. What are your plans for integrating new information and insights into existing adaptation policies',
    '30a': '<b>Monitoring</b>',
    '30b': '<b>Reporting</b>',
    '30c': '<b>Evaluation</b>',
    'p2comments': 'In case you have selected "Under development" or "Currently being implemented", please provide additional info and upload related documents',
    '32': '32. Are you using policy instruments (see question 33 below for examples) for implementing adaptation actions?',
    '33': '33. If you are already using instruments for implementing adaptation, what are the main instruments in the different sectors in your country?',
    '34': '34. If (additional) instruments for implementation are planned in your country, what are the main instruments you are considering?',
    '35': '35. What are the most important financing mechanisms currently in place (or the mechanisms that will be considered in the future) for implementing adaptation in the sectors you have identified as relevant in your country?',
    'p3comments': 'Please use the box below to provide any further comments and thoughts related to the questions above or any information that you wish to share with us (e.g. reports, references):',
    '36': '36. In your country, how do you address transboundary issues? Which instruments facilitate your work (e.g. EU Regional Policy, EU Interreg projects, biogeographical regions and regional adaptation strategies)?',
    '37': '37. In your country, how do you coordinate adaptation activities across regions or municipalities? Which instruments facilitate your work (e.g. River Basin Management Plans, flood risks mapping, spatial planning taking account of the diversity of territories)?',
    '38': '38. Have you involved stakeholders in the adaptation policy process',
    '39': '39. If yes, how would you assess the general contribution of stakeholders/actors engagement in the adaptation policy process?',
    'development_phase': 'From the national perspective, what has been the involvement of stakeholders in the <strong>development phase</strong> of the adaptation policy process?',
    'implementation_phase': 'From the national perspective, what has been the involvement of stakeholders in the <strong>implementation phase</strong> of the adaptation policy process?',
    'monitor_evaluate_phase': 'From the national perspective, what has been the involvement of stakeholders in the <strong>monitoring and evaluation</strong> of the adaptation policy process?',
    '41': '41. From your experience, what are the three most important elements in running a successful stakeholders process?',
    'p4comments': 'Please use the box below to provide any further comments and thoughts related to the questions above or any information that you wish to share with us (e.g. reports, references):',
    'risk_assessments': 'Risk or vulnerability assessments (e.g. consider other sectors)',
    'legislation': 'Legislation to support adaptation',
    'implementation': 'Implementation',
    'monitoring': 'Monitoring/reporting and evaluation',
    'updating': 'Updating strategy/plan',
    'others': 'Others',
    '43': '43. In your opinion, what are the key issues that will shape the adaptation policy process in your country in the coming years? Please provide a maximum of three issues:',
    '44': '44. What kind of adaptation support (e.g. knowledge, information, decision support tools) would you need from the European level?',
    'feedback': 'You can enter your feedback for this survey - your opinion is kindly appreciated!'
}
