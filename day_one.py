def perrywinkle(historian_array1, historian_array2):
    sorted_list1 = sorted(historian_array1)
    sorted_list2 = sorted(historian_array2)
    total_distance = 0
    index = 0

    while index < len(sorted_list1):
       total_distance += abs(sorted_list1[index] - sorted_list2[index])
       index += 1

    print(total_distance)

list1 = [
  99006,
  38540,
  18133,
  70780,
  38316,
  61729,
  57462,
  91153,
  76573,
  76155,
  24171,
  10666,
  73383,
  86077,
  40710,
  58326,
  67654,
  64826,
  70235,
  66149,
  24077,
  46497,
  78959,
  49339,
  54141,
  96148,
  60258,
  23099,
  41307,
  65974,
  40769,
  65277,
  20836,
  12863,
  30718,
  65114,
  46146,
  14591,
  99705,
  64713,
  18767,
  50856,
  19757,
  89557,
  54062,
  69386,
  91224,
  68269,
  47118,
  49799,
  42535,
  69994,
  52436,
  24596,
  86843,
  96155,
  25680,
  10905,
  73049,
  35651,
  13185,
  47380,
  11526,
  22640,
  28081,
  91214,
  70299,
  69491,
  14166,
  44639,
  39531,
  29197,
  97941,
  89154,
  74726,
  42065,
  67812,
  17072,
  73245,
  11680,
  68304,
  98762,
  51469,
  93672,
  19665,
  16645,
  58364,
  92331,
  97903,
  86845,
  50676,
  75338,
  87166,
  89047,
  33371,
  90980,
  92511,
  47738,
  81003,
  87425,
  86444,
  24802,
  26115,
  89747,
  46823,
  70790,
  45381,
  71680,
  56603,
  20721,
  54715,
  70245,
  95000,
  61672,
  69277,
  18422,
  89751,
  82454,
  18812,
  12403,
  51380,
  70840,
  56957,
  80981,
  42793,
  40184,
  75791,
  54948,
  25442,
  88023,
  34476,
  73955,
  40956,
  59337,
  84175,
  61172,
  20032,
  11394,
  89416,
  58763,
  71522,
  41390,
  89374,
  45927,
  13265,
  19150,
  82687,
  44626,
  44561,
  97948,
  14766,
  38684,
  74001,
  75864,
  65366,
  53729,
  90293,
  37726,
  70804,
  10158,
  46905,
  71830,
  26957,
  62648,
  16278,
  72223,
  68493,
  63124,
  39953,
  46199,
  51574,
  56997,
  15042,
  29355,
  32667,
  91910,
  45361,
  57209,
  21891,
  69835,
  94443,
  55059,
  15688,
  32147,
  86293,
  34923,
  44962,
  82598,
  40003,
  13023,
  27866,
  67002,
  91012,
  66044,
  33331,
  83739,
  46420,
  94463,
  89002,
  11437,
  22418,
  21411,
  32217,
  88031,
  35905,
  35647,
  51955,
  74030,
  81468,
  43969,
  46194,
  85098,
  19106,
  39507,
  49298,
  46755,
  65761,
  77565,
  99407,
  71358,
  40988,
  15235,
  85560,
  22336,
  30214,
  33528,
  65883,
  28514,
  54235,
  40814,
  30738,
  23352,
  74158,
  74379,
  13703,
  65060,
  98105,
  63511,
  14335,
  95359,
  88133,
  95532,
  51153,
  14718,
  13804,
  91397,
  43643,
  76512,
  64507,
  56558,
  94652,
  80650,
  56524,
  97034,
  78284,
  63253,
  70398,
  20457,
  38983,
  80593,
  32158,
  15099,
  78903,
  62941,
  11803,
  49738,
  27243,
  93339,
  68583,
  46703,
  66461,
  50187,
  15890,
  52412,
  88293,
  44630,
  85179,
  52028,
  84567,
  19950,
  51147,
  34362,
  83960,
  17612,
  44656,
  33483,
  51670,
  96300,
  95240,
  21850,
  52441,
  32254,
  68525,
  74508,
  80323,
  65300,
  24288,
  66066,
  16209,
  29819,
  74036,
  62630,
  34134,
  46966,
  73363,
  95916,
  21327,
  37034,
  80617,
  24686,
  25133,
  93810,
  68870,
  38845,
  41953,
  76876,
  20112,
  91690,
  12865,
  35744,
  49085,
  86030,
  88533,
  43415,
  34986,
  99785,
  91725,
  30670,
  94247,
  96381,
  59252,
  17282,
  45938,
  79072,
  55769,
  78572,
  87331,
  60162,
  71125,
  40031,
  52638,
  44289,
  63865,
  18898,
  95301,
  22055,
  53205,
  28323,
  90363,
  89953,
  73798,
  45863,
  98470,
  71795,
  33778,
  98946,
  21994,
  30707,
  51523,
  71441,
  33909,
  10691,
  29496,
  42230,
  68830,
  79249,
  44218,
  79729,
  32224,
  30279,
  38608,
  45483,
  32047,
  70586,
  76474,
  32742,
  98317,
  42335,
  65316,
  81775,
  96023,
  12721,
  73700,
  79390,
  90694,
  91565,
  86422,
  92810,
  74624,
  68037,
  28396,
  89780,
  30962,
  23460,
  77012,
  21031,
  66950,
  65128,
  28012,
  57394,
  98281,
  77495,
  74936,
  91250,
  91241,
  91314,
  88290,
  20940,
  94073,
  27646,
  60072,
  24487,
  93468,
  34827,
  42629,
  72808,
  67231,
  47920,
  95716,
  14507,
  38335,
  59119,
  27496,
  49592,
  59259,
  14976,
  32138,
  49659,
  11006,
  27301,
  59332,
  91052,
  63614,
  13512,
  85275,
  19247,
  40663,
  92257,
  68520,
  87435,
  59634,
  48762,
  37318,
  49411,
  34658,
  35706,
  93123,
  17924,
  87196,
  57740,
  22830,
  51620,
  75848,
  14772,
  18592,
  66676,
  44102,
  47056,
  86148,
  40518,
  41596,
  78037,
  35795,
  18723,
  93797,
  97671,
  23699,
  97919,
  16785,
  62616,
  15930,
  82441,
  32656,
  77413,
  72752,
  25097,
  19543,
  75318,
  19415,
  20997,
  35202,
  72538,
  44842,
  28326,
  17462,
  42990,
  20421,
  17182,
  49471,
  31823,
  90999,
  52439,
  47746,
  50990,
  26573,
  38712,
  69067,
  36559,
  81690,
  52850,
  82635,
  76405,
  78056,
  77790,
  97566,
  91451,
  30371,
  31553,
  40103,
  96713,
  72241,
  21177,
  36285,
  60819,
  89533,
  52878,
  98899,
  21739,
  52895,
  24760,
  61257,
  59243,
  83626,
  73327,
  89469,
  38452,
  91111,
  19932,
  23814,
  11228,
  90008,
  71262,
  75116,
  21556,
  67613,
  18819,
  16596,
  60189,
  91775,
  82183,
  82671,
  27814,
  56740,
  23120,
  57467,
  46686,
  75851,
  43651,
  97125,
  49136,
  91337,
  94434,
  32403,
  41731,
  27543,
  74801,
  14902,
  99047,
  66749,
  76240,
  72198,
  95888,
  32500,
  86753,
  15649,
  56086,
  15311,
  37803,
  53060,
  51967,
  17354,
  10055,
  34244,
  21231,
  59489,
  13639,
  34062,
  83983,
  93647,
  53687,
  70194,
  98944,
  13991,
  87843,
  74448,
  52799,
  75944,
  42844,
  96272,
  17838,
  26081,
  45724,
  47237,
  21228,
  35856,
  93591,
  61212,
  61062,
  96064,
  75537,
  44059,
  81622,
  50667,
  97084,
  13169,
  57322,
  12130,
  82114,
  54596,
  47748,
  24302,
  39283,
  44310,
  82822,
  79286,
  78155,
  26900,
  97801,
  62797,
  80367,
  52103,
  43130,
  28888,
  73180,
  82035,
  25627,
  10869,
  37552,
  84907,
  34645,
  61338,
  83990,
  11269,
  79295,
  43221,
  86001,
  34108,
  95413,
  19964,
  82521,
  60781,
  57794,
  12298,
  84216,
  36509,
  82594,
  32516,
  50254,
  35816,
  60865,
  61952,
  53399,
  77087,
  96779,
  13853,
  22933,
  58086,
  21436,
  50170,
  86579,
  26267,
  77545,
  43670,
  21175,
  87781,
  52791,
  48617,
  96403,
  67474,
  98932,
  46899,
  79574,
  30104,
  76149,
  70412,
  33000,
  59971,
  88217,
  15130,
  56015,
  54238,
  35684,
  88659,
  40206,
  81346,
  35433,
  84398,
  64460,
  32488,
  77815,
  61406,
  93879,
  33472,
  86621,
  31585,
  92665,
  51965,
  99377,
  20257,
  79455,
  44861,
  94931,
  34821,
  34053,
  35378,
  99445,
  30344,
  68931,
  57795,
  51592,
  52107,
  44792,
  81960,
  93395,
  53268,
  30699,
  44246,
  71363,
  84318,
  50198,
  58232,
  76277,
  22162,
  77444,
  77344,
  84109,
  64076,
  56650,
  69278,
  78847,
  81571,
  44644,
  90621,
  59174,
  43079,
  46349,
  69355,
  67085,
  66194,
  91560,
  96434,
  57896,
  12385,
  13553,
  39494,
  33031,
  84179,
  76823,
  78648,
  49568,
  13913,
  13779,
  19801,
  53472,
  54951,
  78858,
  33043,
  66269,
  69674,
  56156,
  15052,
  74147,
  16337,
  57835,
  35937,
  79379,
  37535,
  48559,
  72941,
  13143,
  98319,
  21984,
  52205,
  37942,
  30925,
  85946,
  29975,
  16606,
  10354,
  43214,
  75801,
  85088,
  23246,
  14264,
  97821,
  90143,
  43233,
  19501,
  62214,
  70520,
  98507,
  57062,
  19520,
  45602,
  22321,
  58654,
  40844,
  99926,
  27878,
  92982,
  24451,
  24960,
  78368,
  73870,
  64409,
  68720,
  84679,
  85561,
  61418,
  23592,
  79447,
  79307,
  43133,
  67547,
  25054,
  18090,
  42348,
  53062,
  12477,
  32590,
  43150,
  90232,
  54157,
  10397,
  40228,
  10069,
  82220,
  51061,
  24569,
  92802,
  21675,
  55904,
  32060,
  99313,
  64724,
  41313,
  92841,
  48903,
  32705,
  29306,
  12758,
  92611,
  37798,
  72934,
  17322,
  31246,
  42506,
  91039,
  41966,
  37154,
  80080,
  25042,
  63465,
  51158,
  71697,
  68447,
  59005,
  72699,
  77876,
  32324,
  80836,
  79063,
  92346,
  98008,
  52358,
  61687,
  19947,
  57697,
  81721,
  46459,
  25740,
  78645,
  80369,
  33120,
  86551,
  79500,
  87802,
  96810,
  63959,
  36968,
  56795,
  12699,
  80955,
  54674,
  89734,
  56820,
  33215,
  51005,
  54487,
  40303,
  89364,
  99804,
  47249,
  13318,
  71579,
  42237,
  10936,
  94920,
  97531,
  55195,
  37609,
  32421,
  86247,
  75761,
  92502,
  24793,
  79928,
  61966,
  54823,
  12390,
  98087,
  28305,
  11694,
  25773,
  10237,
  53818,
  90140,
  16877,
  70440,
  20425,
  31119,
  64934,
  41053,
  59199,
  96208,
  47865,
  72676,
  36328,
  87171,
  33085,
  29549,
  16365,
  21309,
  78146,
  77480,
  33026,
  78593,
  51671,
  24897,
  66982,
  10601,
  90805,
  98801,
  69006,
  87117,
  51999,
  69463,
  79838,
  87352,
  70793,
  65518,
  63083,
  14321,
  71218,
  68794,
  61356,
  29130,
  50008,
  75342,
  22229,
  43553,
  56266,
  26755,
  43604,
  69206,
  83729,
  97816,
  74873,
  96518,
  26091,
  35139,
  77138,
  63035,
  90356,
  64708,
  68272,
  87370,
  81179,
  91200,
  68973,
  44889,
  56893,
  28208,
  16017,
  33656,
  95864,
  85836,
  94113,
  38652,
  59247,
  64534,
  83964,
  15724,
  55105,
  13237,
  34736,
  95583,
  34797,
  47199,
  20631,
]

list2 = [ 
  28305,
  91683,
  49738,
  13081,
  55879,
  73383,
  59629,
  56589,
  52850,
  36285,
  76277,
  30707,
  93797,
  24033,
  50187,
  65150,
  30707,
  52850,
  11694,
  71125,
  19630,
  93335,
  47746,
  29442,
  95451,
  29849,
  88293,
  57809,
  66225,
  82114,
  84109,
  79459,
  39953,
  96208,
  30707,
  50745,
  36285,
  81775,
  90954,
  86029,
  78959,
  44136,
  47746,
  74726,
  80955,
  30707,
  49972,
  75801,
  94704,
  57324,
  91397,
  50187,
  94924,
  56660,
  95067,
  75541,
  75049,
  30636,
  91039,
  82698,
  61356,
  49738,
  78959,
  17601,
  24121,
  38947,
  56815,
  64519,
  11598,
  11827,
  65456,
  97770,
  39589,
  67313,
  62661,
  57417,
  40982,
  26967,
  20609,
  79249,
  94322,
  25205,
  55108,
  47746,
  81775,
  69048,
  31379,
  50187,
  65233,
  79249,
  93797,
  48071,
  34605,
  94911,
  43535,
  44540,
  54481,
  98087,
  30707,
  53074,
  36285,
  51147,
  76277,
  63773,
  81775,
  54357,
  40553,
  21755,
  12660,
  25637,
  73383,
  32502,
  47746,
  49279,
  80955,
  20285,
  24379,
  81055,
  71141,
  50187,
  52850,
  30006,
  80955,
  75183,
  45433,
  68802,
  61356,
  15120,
  67654,
  11694,
  29242,
  43439,
  31785,
  60125,
  16414,
  79249,
  96208,
  97531,
  73030,
  39442,
  96208,
  29669,
  91039,
  12473,
  75801,
  40228,
  11428,
  49738,
  79249,
  51147,
  15646,
  16481,
  52850,
  40844,
  71125,
  67654,
  52850,
  97531,
  85744,
  95339,
  21771,
  22746,
  30707,
  69687,
  15961,
  84109,
  27071,
  14353,
  61356,
  93853,
  11750,
  83594,
  93797,
  85961,
  81775,
  96117,
  90326,
  42508,
  82114,
  36285,
  91397,
  40228,
  87731,
  88293,
  69781,
  63879,
  23951,
  96035,
  76078,
  81775,
  11694,
  88124,
  77163,
  48243,
  56996,
  40228,
  37353,
  32287,
  11694,
  89879,
  47746,
  15950,
  84109,
  28305,
  13458,
  65548,
  40377,
  74726,
  75864,
  88293,
  82114,
  86085,
  76277,
  81364,
  88422,
  75801,
  78300,
  69583,
  22393,
  75801,
  49738,
  49799,
  82033,
  50187,
  76277,
  47746,
  73396,
  43873,
  49621,
  84109,
  61805,
  88293,
  76277,
  75470,
  24883,
  51147,
  12843,
  82603,
  55075,
  82342,
  61356,
  43253,
  75098,
  62422,
  98736,
  49738,
  47746,
  75864,
  68412,
  50187,
  62259,
  42322,
  75908,
  70538,
  49799,
  17703,
  91039,
  87050,
  60522,
  79249,
  98087,
  13939,
  12907,
  80063,
  11694,
  37998,
  61846,
  79646,
  81203,
  84109,
  76277,
  98087,
  71125,
  65472,
  89208,
  55747,
  97531,
  81775,
  52513,
  72857,
  65290,
  91039,
  35257,
  86932,
  11694,
  36285,
  49799,
  75864,
  36523,
  67295,
  81775,
  81390,
  52850,
  53968,
  67864,
  47746,
  44630,
  51308,
  83039,
  30707,
  70014,
  84109,
  28305,
  41389,
  76513,
  40844,
  76277,
  55019,
  75864,
  77305,
  61356,
  79249,
  14283,
  52268,
  30707,
  75801,
  68275,
  79249,
  26445,
  94812,
  75801,
  26757,
  76277,
  47935,
  87425,
  61356,
  49799,
  61818,
  22948,
  48072,
  26199,
  80898,
  10743,
  40844,
  75864,
  88293,
  83164,
  75801,
  75801,
  18205,
  38867,
  84251,
  49738,
  49799,
  88087,
  67584,
  56266,
  52850,
  14587,
  75864,
  75131,
  98591,
  18502,
  68172,
  62819,
  74323,
  95233,
  48095,
  42340,
  84109,
  93797,
  73087,
  95149,
  40844,
  80812,
  28305,
  37419,
  96842,
  75801,
  78959,
  56727,
  76277,
  40844,
  44630,
  40844,
  78959,
  11109,
  53918,
  70907,
  96208,
  23222,
  73383,
  12794,
  75864,
  98087,
  82137,
  53606,
  28630,
  59757,
  37599,
  33032,
  68219,
  99744,
  67654,
  93797,
  52028,
  55803,
  75335,
  11694,
  80955,
  46595,
  26699,
  37782,
  12721,
  77978,
  40844,
  91966,
  29130,
  32412,
  61356,
  84970,
  40228,
  98087,
  84109,
  54769,
  15123,
  70469,
  51377,
  77889,
  84109,
  71125,
  85683,
  30904,
  36285,
  92228,
  12721,
  60938,
  75876,
  51147,
  81810,
  11690,
  97587,
  74726,
  96191,
  75780,
  28305,
  71567,
  20940,
  34365,
  87425,
  73879,
  66787,
  77650,
  74726,
  71064,
  84109,
  61356,
  52329,
  66321,
  49146,
  53972,
  18748,
  28607,
  65350,
  91039,
  44630,
  82837,
  61356,
  93628,
  50135,
  40844,
  80873,
  71125,
  62486,
  67654,
  69144,
  43539,
  93556,
  82114,
  10568,
  25428,
  50369,
  84109,
  49738,
  93797,
  68790,
  50187,
  43459,
  84109,
  33697,
  23562,
  32387,
  47280,
  62911,
  40228,
  61356,
  52850,
  78955,
  43107,
  84109,
  49738,
  75864,
  51147,
  20026,
  61356,
  56479,
  80955,
  61356,
  17222,
  47746,
  51207,
  46009,
  97531,
  16534,
  28480,
  40844,
  97678,
  92823,
  96208,
  84654,
  20478,
  52850,
  49799,
  83899,
  96207,
  70318,
  79249,
  95321,
  32973,
  44578,
  84109,
  84109,
  49799,
  76277,
  30707,
  72499,
  70772,
  29213,
  67902,
  98087,
  84109,
  91481,
  76277,
  28310,
  87425,
  32653,
  47746,
  48086,
  74181,
  26300,
  22127,
  70386,
  51147,
  49799,
  97531,
  73630,
  28089,
  40228,
  95585,
  66827,
  50881,
  49799,
  76277,
  98603,
  78528,
  94830,
  39291,
  84044,
  79249,
  44630,
  92069,
  76277,
  11134,
  75864,
  40228,
  37007,
  76277,
  96208,
  91397,
  46791,
  75864,
  91996,
  51147,
  29851,
  85269,
  52850,
  76277,
  88634,
  71603,
  27829,
  63627,
  51147,
  69066,
  28757,
  18555,
  77670,
  81775,
  93797,
  49738,
  28305,
  59101,
  61356,
  93229,
  49378,
  48946,
  79249,
  48408,
  49738,
  67117,
  91039,
  71125,
  40844,
  78959,
  72682,
  50187,
  40844,
  79854,
  50187,
  37752,
  49738,
  70834,
  75801,
  49738,
  28305,
  11554,
  29272,
  79547,
  17772,
  75864,
  71125,
  31822,
  57967,
  68281,
  98087,
  44295,
  28305,
  98087,
  41211,
  80456,
  49738,
  18250,
  52028,
  79249,
  40228,
  28305,
  84109,
  96672,
  40228,
  95091,
  79249,
  52850,
  49515,
  52827,
  75356,
  47746,
  91039,
  34110,
  39055,
  98087,
  16648,
  46277,
  47746,
  63430,
  11694,
  62075,
  98087,
  11745,
  49186,
  49738,
  76496,
  11694,
  75864,
  81580,
  71125,
  88939,
  71941,
  97531,
  49799,
  86504,
  75864,
  15115,
  20872,
  28168,
  47235,
  85595,
  91039,
  27058,
  85302,
  21587,
  12678,
  84154,
  52890,
  73714,
  75864,
  69296,
  44675,
  98087,
  63562,
  47746,
  35044,
  76662,
  88293,
  39552,
  96208,
  68175,
  60399,
  89287,
  98087,
  42276,
  93460,
  63652,
  44752,
  16486,
  28305,
  45573,
  47746,
  62122,
  70443,
  16675,
  57833,
  56613,
  99154,
  56133,
  49357,
  60866,
  47746,
  50560,
  76277,
  85118,
  93797,
  93108,
  21865,
  48676,
  25800,
  77645,
  84109,
  88361,
  19091,
  39510,
  99948,
  76277,
  18403,
  79249,
  91039,
  96572,
  32815,
  75801,
  50187,
  84109,
  87467,
  67654,
  60828,
  56266,
  51324,
  81775,
  72416,
  75864,
  79249,
  30707,
  67654,
  52422,
  30707,
  51147,
  76175,
  79797,
  71125,
  42990,
  76277,
  52004,
  38942,
  93396,
  98425,
  77679,
  19068,
  65962,
  88101,
  42786,
  88293,
  42990,
  61959,
  42529,
  99125,
  59110,
  51147,
  80755,
  17365,
  80268,
  67285,
  87185,
  15806,
  71358,
  87425,
  66100,
  51147,
  80955,
  66978,
  85824,
  40704,
  18149,
  24430,
  11694,
  20525,
  81001,
  98999,
  95761,
  51363,
  25400,
  80955,
  52028,
  71125,
  96208,
  93240,
  88546,
  49349,
  90193,
  35981,
  18658,
  69254,
  25765,
  52028,
  53529,
  47756,
  52850,
  71095,
  99257,
  49799,
  55820,
  75425,
  51328,
  30707,
  85390,
  46509,
  70945,
  23863,
  92788,
  44941,
  79249,
  49799,
  52850,
  52028,
  45636,
  91120,
  61403,
  63921,
  32937,
  25655,
  52028,
  61356,
  49799,
  30225,
  69044,
  94265,
  11694,
  71883,
  91397,
  51147,
  74407,
  47746,
  74541,
  37237,
  21658,
  57210,
  40844,
  61785,
  40228,
  67654,
  11635,
  49799,
  47746,
  47746,
  30707,
  19530,
  15587,
  66426,
  23988,
  71358,
  96208,
  78728,
  72246,
  57550,
  54114,
  76394,
  31516,
  69506,
  79249,
  44630,
  36285,
  95657,
  52028,
  33686,
  50480,
  18338,
  87425,
  68560,
  52028,
  40844,
  40228,
  59999,
  93797,
  60286,
  90784,
  67654,
  98358,
  11694,
  47746,
  82114,
  52850,
  41396,
  27455,
  28885,
  76447,
  95865,
  11694,
  97060,
  36285,
  76277,
  55461,
  30707,
  96245,
  75864,
  51194,
  50041,
  30051,
  14953,
  72188,
  84109,
  57055,
  76277,
  91397,
  65269,
  96439,
  16064,
  43279,
  52850,
  55322,
  28549,
  99138,
  83521,
  87425,
  48785,
  11694,
  71358,
  32908,
  38186,
  87627,
  82946,
  18482,
  32396,
  14774,
  40844,
  56266,
  78349,
  75864,
  79249,
  90262,
  52850,
  56266,
  75864,
  21058,
  51826,
  42990,
  33412,
  51147,
  91039,
  49799,
  72502,
  30308,
  34275,
  36332,
  22962,
  91039,
  15695,
  40878,
  79587,
  14900,
  11694,
  40844,
  56266,
  96208,
  53663,
  75864,
  84834,
  67101,
  11694,
  90467,
  91039,
  11694,
  11694,
  91397,
  85476,
  52028,
  37615,
  66396,
  49735,
  40844,
  81775,
  40844,
  39592,
  40228,
  46979,
  71125,
  40228,
  56266,
  29130,
  28305,
  99523,
  12965,
  36285,
  88293,
  56266,
]


historian_array1 = [
    88450, 58674, 30431, 79176, 51071, 78115, 26281, 99747, 81068, 81760, 91539, 51799, 69353, 64094, 27283, 52983,
    36638, 68035, 26604, 43449, 90472, 20731, 31769, 37135, 64018, 49545, 87888, 89770, 39164, 34963, 69433, 89828,
    51940, 76011, 86044, 42178, 58537, 68039, 91534, 95383, 72575, 63014, 32766, 21621, 65716, 74270, 73720, 22637,
    96044, 93882, 49123, 59778, 62853, 72347, 48833, 64129, 21955, 92027, 38750, 16496, 68900, 13007, 15450, 82750,
    35089, 60190, 92533, 95863, 28192, 36229, 84353, 85760, 68643, 47794, 26171, 14558, 73997, 56966, 26572, 15302,
    25557, 52311, 83219, 47897, 51489, 10737, 14395, 75289, 50622, 33690, 88570, 88810, 76440, 96318, 17056, 90971,
    26526, 64411, 41386, 16374, 69742, 71716, 52237, 63724, 29598, 58958, 70562, 99313, 99705, 38730, 93620, 64261,
    37597, 86139, 81816, 25422, 41188, 91310, 42798, 12672, 51173, 23901, 86756, 72786, 21624, 81152, 76279, 86686,
    96883, 52777, 44760, 48872, 13502, 39968, 49634, 90616, 98097, 94918, 71745, 63978, 96485, 34269, 86448, 40845,
    24852, 49514, 60306, 19242, 42110, 88579, 14788, 22896, 53083, 21419, 16682, 45509, 19280, 35886, 25186, 72836,
    97528, 72387, 83455, 33568, 30442, 83110, 49301, 34315, 41298, 55295, 35412, 52239, 31395, 26416, 62441, 43014,
    73780, 59350, 61061, 41617, 49483, 58955, 36007, 10241, 46681, 89126, 33265, 95319, 73018, 60322, 50982, 12810,
    16293, 74375, 63806, 66212, 65902, 88549, 41289, 68097, 88017, 73445, 38360, 39931, 30391, 46148, 50563, 55685,
    88469, 22810, 32215, 59903, 17397, 10767, 99371, 90831, 65156, 97534, 91168, 26858, 29539, 30333, 99445, 16567,
    32900, 27489, 46422, 91270, 19540, 65489, 76210, 29062, 41201, 45915, 94945, 54375, 21536, 75870, 79743, 20691,
    10352, 83970, 98914, 58938, 51275, 86583, 69981, 27674, 43824, 87336, 56054, 33272, 36755, 73434, 36649, 80713,
    13544, 27841, 84003, 48985, 10176, 58353, 15647, 68910, 46401, 80269, 86290, 95993, 44568, 44398, 41393, 30042,
    31917, 13513, 71906, 75883, 95352, 14275, 69876, 16298, 30864, 19877, 22165, 62660, 72656, 81487, 72705, 22301,
    81495, 88386, 71675, 34867, 41331, 53633, 54664, 29793, 68537, 46224, 36246, 68342, 94273, 97185, 23728, 68264,
    79652, 89531, 98937, 91690, 48648, 32882, 57264, 13447, 35448, 75778, 23234, 49904, 26513, 91793, 27874, 66884,
    45213, 40497, 76273, 39230, 89266, 35518, 16168, 20476, 87694, 45088, 60101, 33643, 84013, 45702, 82641, 20831,
    77611, 82075, 56470, 19621, 59631, 64405, 19772, 86905, 17583, 53767, 37207, 94596, 51890, 52083, 10991, 33366,
    70856, 84010, 95694, 57389, 38239, 92555, 83182, 66779, 89448, 82430, 96968, 93774, 85440, 94915, 81147, 71130,
    74977, 74557, 22159, 31266, 98350, 13272, 95602, 88655, 74822, 11346, 52663, 20323, 94621, 27159, 61249, 22861,
    64142, 29355, 23153, 28248, 70448, 53405, 38065, 37806, 88000, 72790, 33687, 11417, 53871, 45748, 95328, 59125,
    12587, 94131, 42511, 52071, 73868, 38312, 98418, 85457, 16464, 76815, 28900, 49734, 92985, 86926, 93208, 41938,
    67527, 49205, 41165, 40200, 59357, 75079, 60169, 92074, 18585, 43719, 71503, 20439, 50067, 89766, 20035, 29197,
    82716, 15062, 91337, 23698, 86500, 52046, 40868, 96384, 60434, 56290, 57746, 18898, 51209, 67029, 40530, 63443,
    69441, 73700, 41594, 51804, 45731, 36815, 47389, 34424, 31341, 69202, 47466, 13481, 82208, 52875, 38932, 10312,
    99845, 26735, 90820, 64199, 99821, 80212, 54094, 94967, 18831, 69611, 20794, 18926, 17242, 78473, 13515, 84378,
    18489, 12314, 29089, 68433, 87740, 78290, 83596, 16316, 45777, 50505, 73351, 23112, 29172, 11572, 63218, 10094,
    46797, 27552, 31740, 52505, 84303, 18826, 80340, 69924, 37554, 57758, 12994, 28474, 98133, 59181, 19715, 57509,
    48026, 10803, 34768, 73776, 23928, 20765, 44968, 47992, 22902, 42359, 38908, 94050, 25874, 10650, 39759, 17442,
    73455, 43244, 36224, 24323, 40462, 77474, 57622, 47172, 51053, 38866, 14536, 18191, 50783, 32218, 65928, 33554,
    48966, 68980, 92199, 47624, 81484, 36264, 86887, 56559, 69481, 95563, 48042, 89886, 32235, 75609, 93104, 78119,
    73185, 66947, 10279, 74932, 46673, 16885, 50651, 79768, 55122, 75702, 42522, 81922, 67535, 56847, 95298, 79649,
    80679, 39366, 72233, 45780, 27048, 72918, 11115, 18720, 78049, 25027, 39170, 72551, 38283, 71042, 93626, 97077,
    44993, 99937, 92127, 89301, 34485, 70901, 93765, 22641, 96940, 69328, 48593, 62393, 50116, 31287, 46213, 86316,
    52095, 73009, 76994, 52768, 58014, 38328, 86656, 24198, 20644, 80856, 85514, 78541, 89198, 66843, 42847, 10506,
    53734, 56950, 10097, 11735, 47055, 62723, 46747, 85689, 26070, 24973, 98067, 10839, 83064, 11426, 53675, 42916,
    26729, 85296, 70877, 59363, 90177, 65577, 22974, 82930, 48640, 77227, 21808, 12093, 57834, 85449, 31321, 29147,
    54452, 36762, 77729, 38806, 16975, 59754, 92634, 75255, 20579, 10838, 72028, 34045, 10166, 39450, 79156, 99772,
    66119, 84505, 79335, 22607, 70069, 56842, 51924, 53971, 63946, 58512, 83844, 73324, 49874, 96638, 25651, 35046,
    45863, 33827, 74271, 92141, 26165, 29156, 14258, 99336, 56949, 29951, 80133, 69937, 27282, 37999, 35714, 74778,
    65706, 28826, 43880, 65365, 60998, 23464, 63996, 47988, 72134, 43808, 71794, 55139, 68486, 88866, 31014, 25100,
    23168, 86321, 56564, 66443, 34574, 18319, 52080, 34903, 10503, 73547, 71407, 14066, 55291, 49333, 85590, 31583,
    56885, 10853, 54330, 60526, 73313, 64827, 54707, 78727, 81267, 97418, 48561, 27700, 88852, 27571, 30253, 96823,
    15510, 34473, 19128, 66281, 87566, 73327, 90546, 10731, 33757, 53264, 27559, 76671, 14652, 66269, 68360, 47909,
    34184, 56983, 46159, 17929, 19939, 54638, 81041, 82318, 36922, 37124, 97802, 44780, 41587, 79382, 58560, 49390,
    64184, 63363, 31139, 41545, 31298, 27867, 31915, 57731, 16568, 37837, 67097, 66230, 72316, 93233, 53568, 30604,
    52867, 94676, 64541, 75970, 84132, 23468, 41002, 25437, 73367, 61905, 58157, 40049, 88306, 41571, 63613, 81673,
    55528, 27726, 76018, 93265, 67182, 21149, 25611, 84359, 98940, 91702, 49126, 67287, 13917, 38327, 94612, 55182,
    43277, 31570, 75076, 80682, 22072, 12519, 76313, 67075, 65234, 43693, 89876, 17665, 33737, 91753, 59183, 14540,
    74552, 12545, 51062, 96261, 17961, 41550, 44693, 56353, 26427, 10521, 50199, 55779, 13694, 84529, 28117, 28792,
    86182, 72131, 49826, 34390, 74094, 69129, 50073, 37199, 37972, 88066, 84391, 33375, 84125, 68050, 80017, 89775,
    43499, 93020, 28839, 65343, 82862, 35994, 94975, 66142, 65082, 85699, 49094, 89012, 12731, 12574, 23300, 59711,
    48379, 26444, 94298, 64549, 85255, 18260, 89345, 47964, 30500, 40701, 85115, 56810, 49698, 60564, 16225, 89966,
    61233, 31511, 33945, 98473, 41456, 85038, 73588, 25283, 33280, 49275, 87664, 47908, 33245, 42158, 22933, 60641,
    79702, 78739, 22561, 43533, 71914, 14862, 17015, 73903, 43166, 90888, 43451, 99167, 71516, 51747, 37581, 12993,
    32228, 69475, 54981, 81379, 80367, 58566, 26053, 77442, 70340, 83405, 59197, 98773, 32734, 53611, 45926, 53823,
    31731, 97782, 92678, 98973, 63484, 29604, 74422, 80370, 89621, 27363, 11198, 88033, 93444, 35116, 16393, 33628,
    67211, 24757, 73181, 24567, 84081, 34345, 21185, 33414, 30310, 24352, 56004, 14492, 47871, 42912, 91823, 46731,
    24112, 92034, 77157, 29215, 37580, 73593, 11075, 49084
]

historian_array2 = [
    63363, 73195, 97265, 36224, 64526, 34829, 65342, 75563, 41201, 39590, 66113, 96883, 19440, 96883, 88579, 37831,
    37255, 36007, 96883, 69865, 75289, 35412, 42457, 22483, 44347, 45637, 11937, 85917, 26074, 57264, 87585, 75289,
    30644, 76423, 69863, 81634, 84529, 39015, 80235, 26816, 20171, 53853, 84529, 89301, 94131, 26729, 99746, 82429,
    16327, 19601, 36007, 64129, 55358, 80203, 47045, 62494, 96883, 12818, 29622, 92138, 26494, 75255, 75255, 57264,
    36007, 26729, 72231, 46766, 34386, 31291, 84529, 94567, 63363, 81334, 63475, 25238, 72059, 79382, 86541, 89301,
    89301, 84529, 10771, 38681, 33757, 70282, 57593, 33474, 53826, 96463, 36007, 37995, 71407, 30287, 63363, 75246,
    85772, 41201, 10166, 92034, 91071, 23782, 32193, 35412, 55182, 55182, 56476, 47299, 70328, 36007, 29617, 33757,
    26576, 77794, 20568, 63744, 26729, 94596, 61799, 96315, 45929, 79382, 95419, 33757, 90149, 20260, 75816, 60299,
    79162, 54244, 69775, 50008, 66090, 94596, 17015, 79382, 94596, 36224, 76703, 94596, 96984, 66751, 64129, 35412,
    28792, 37277, 41587, 81203, 55182, 19310, 36076, 77018, 89301, 62087, 40987, 63363, 80435, 81329, 22123, 88497,
    96823, 18771, 86201, 86544, 94455, 29374, 88579, 69117, 86008, 97010, 88552, 68865, 26729, 51263, 69129, 92675,
    55669, 99109, 22458, 18191, 35412, 33400, 37276, 35159, 33757, 36224, 38854, 13101, 20969, 26729, 88579, 57845,
    33757, 28399, 18191, 85298, 32364, 12193, 15659, 14208, 30570, 22551, 15738, 47827, 46615, 17015, 33757, 74778,
    69721, 57264, 74778, 15150, 57264, 17015, 18191, 51790, 94131, 74778, 84518, 70445, 87613, 71407, 73344, 94131,
    69357, 63148, 63363, 37691, 53813, 45632, 98226, 27996, 74778, 88579, 81121, 41217, 17358, 30864, 89214, 94596,
    83523, 30864, 18386, 55182, 11339, 95003, 47537, 84373, 47258, 25451, 20831, 54103, 63991, 10847, 82725, 71407,
    74784, 88579, 22246, 68185, 71407, 22559, 74778, 41553, 31790, 22871, 47068, 10051, 41201, 66153, 84557, 18191,
    38515, 59458, 89301, 73018, 64129, 63363, 35412, 31473, 79382, 81988, 16975, 18191, 13418, 69274, 79382, 88579,
    94131, 77944, 21687, 50027, 74778, 96823, 42918, 43797, 94131, 88579, 75957, 16975, 33645, 26729, 63363, 29231,
    26729, 20323, 94073, 94596, 67496, 40888, 71920, 95151, 64129, 98592, 27536, 64383, 17296, 13262, 74776, 71407,
    64129, 84529, 23793, 36224, 29166, 85657, 94208, 58668, 93276, 29626, 92034, 46999, 36057, 52055, 36007, 96883,
    96823, 84749, 18508, 11287, 21505, 73018, 36007, 95374, 26729, 33757, 40318, 73018, 38283, 30246, 37453, 61295,
    40290, 75289, 77859, 49009, 36007, 55182, 98585, 73018, 30783, 55798, 63363, 96883, 59291, 76935, 25407, 91090,
    84529, 55182, 75441, 66927, 20323, 26729, 91096, 10128, 68720, 89301, 28749, 61116, 75255, 42996, 44166, 88579,
    83623, 22533, 94131, 36007, 60535, 20323, 92034, 32005, 43943, 84856, 34647, 69129, 63990, 51721, 16975, 16975,
    96823, 34262, 38283, 60452, 33171, 38283, 56577, 88579, 89301, 24744, 88027, 96738, 57264, 74778, 57264, 88579,
    93270, 26792, 20323, 81976, 20831, 97383, 63363, 10369, 96883, 65952, 61691, 41201, 42595, 94596, 79104, 34472,
    92034, 84529, 41587, 74778, 64129, 28042, 67872, 34853, 73018, 14749, 40512, 68267, 38283, 49628, 26729, 70371,
    72474, 35412, 24791, 75289, 16482, 74778, 36007, 48448, 35412, 64129, 45163, 35412, 62440, 24907, 57264, 89301,
    66120, 67913, 80814, 30409, 35412, 79866, 23997, 55182, 76412, 88579, 42343, 33757, 60919, 69441, 33757, 73018,
    67992, 67269, 69129, 57264, 17015, 55182, 83443, 58265, 36224, 26729, 49921, 72074, 74778, 73018, 98846, 81881,
    75255, 29062, 42212, 37612, 79266, 17378, 36224, 35412, 25059, 88579, 75289, 89301, 96823, 89301, 20323, 14174,
    73018, 76950, 17015, 75743, 29064, 52954, 17011, 55182, 87954, 79382, 65592, 89301, 89204, 71407, 24477, 70977,
    63363, 51733, 63523, 24865, 80381, 80809, 13765, 32125, 71446, 75255, 81935, 34338, 94131, 73018, 98893, 43527,
    94596, 96823, 17370, 98708, 96883, 10166, 41536, 20799, 15846, 48609, 94131, 41856, 91508, 74778, 49394, 56999,
    31883, 35412, 82579, 79382, 94131, 64129, 42094, 51705, 69129, 26729, 92034, 17576, 92034, 84529, 36007, 30220,
    88023, 94131, 72394, 71407, 34309, 27570, 79811, 16379, 89301, 30864, 73018, 36224, 63363, 39139, 65171, 69322,
    88579, 36007, 79382, 64129, 96823, 63363, 64129, 47498, 94131, 77254, 33757, 76585, 55182, 88361, 35412, 45354,
    63363, 39645, 36224, 96883, 91861, 79382, 28792, 35412, 96823, 48773, 69129, 79504, 69441, 19369, 80534, 71407,
    50401, 33757, 42731, 35718, 15050, 96459, 45849, 45896, 33757, 79382, 40236, 60254, 71407, 41587, 88894, 17015,
    56376, 18191, 88315, 94131, 91923, 26729, 84529, 88579, 69441, 69768, 71796, 36292, 26729, 79076, 58970, 21478,
    96883, 94179, 30525, 95982, 12420, 38283, 96918, 72045, 94596, 30864, 33757, 31285, 54162, 17015, 64765, 88914,
    58424, 57996, 23710, 18562, 69129, 82046, 26981, 60458, 36630, 69441, 84320, 33757, 14478, 88579, 92034, 63158,
    50172, 11916, 71407, 80677, 94596, 91383, 65553, 57264, 19178, 94131, 26729, 64129, 35509, 64333, 32970, 82464,
    63363, 35412, 57264, 11878, 53456, 96883, 71407, 62639, 68309, 17923, 64129, 44545, 70532, 19086, 73174, 32701,
    77965, 46763, 97150, 94876, 26729, 55182, 63363, 57264, 73018, 18191, 36363, 10066, 38283, 73182, 31911, 92034,
    94596, 84529, 26729, 60376, 37560, 21896, 41377, 89301, 42594, 54093, 90307, 98842, 25642, 26729, 18191, 11966,
    28792, 10074, 92715, 16359, 55338, 15839, 73018, 88579, 35881, 77702, 14286, 43247, 56992, 16975, 35412, 37394,
    27993, 96823, 47334, 19802, 33757, 51325, 71407, 16975, 87710, 35412, 99288, 41201, 29901, 94596, 24533, 75255,
    64129, 13174, 94913, 45809, 79382, 20831, 89301, 54824, 39610, 71407, 36007, 62450, 10166, 90637, 38068, 35412,
    72154, 13310, 64129, 94040, 63836, 69030, 63111, 73018, 89016, 28740, 57264, 75255, 88579, 13741, 86935, 72916,
    60139, 79382, 20831, 23625, 26729, 13330, 84529, 94134, 88075, 53729, 92878, 87543, 96823, 71407, 12864, 45518,
    74778, 15210, 69063, 89301, 69129, 75255, 64129, 96823, 57699, 72346, 29062, 92034, 36661, 36730, 43449, 67538,
    79382, 26729, 30818, 36224, 86727, 88380, 18191, 97146, 68693, 55270, 78554, 71477, 71407, 35412, 94596, 79382,
    23320, 80477, 74426, 74778, 16341, 34543, 92706, 88579, 32503, 55182, 31812, 89622, 64129, 62191, 35566, 80938,
    69441, 48741, 69441, 71722, 46646, 75255, 88579, 36828, 26265, 45338, 65410, 69332, 32597, 50774, 79382, 20831,
    19665, 73931, 55575, 25462, 33757, 15074, 39774, 96883, 75255, 13580, 63598, 57264, 74778, 57264, 71407, 85122,
    14073, 41588, 73524, 31768, 64129, 87448, 96883, 86498, 13657, 20323, 77882, 57264, 58814, 28925, 72601, 63363,
    44349, 17205, 96035, 21008, 12918, 15368, 89301, 93498, 85414, 78097, 33757, 55182, 86059, 78573, 94131, 79382,
    96328, 33757, 23543, 33567, 35412, 94131, 35412, 80466, 17984, 14607, 85280, 49233, 94596, 52671, 94927, 53295,
    20323, 95936, 43308, 47522, 89301, 60237, 93965, 58449, 75255, 31734, 90186, 42157, 24578, 55182, 73018, 38645,
    57264, 20323, 35191, 76180, 15390, 10519, 17015, 96823, 72888, 57264, 14161, 39140, 75255, 92034, 36007, 73158,
    74778, 95808, 89301, 99938, 89301, 36007, 96823, 34885
]

perrywinkle(list1, list2)
