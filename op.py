# Operator のクラス定義
class Operator:
    def __init__(self, name, headquarters, oran_status, subscribers, *bands):
        self.name = name
        self.headquarters = headquarters
        self.oran_status = oran_status  # non_member, member_inactive, member_active
        self.subscribers = subscribers
        self.bands = bands

    def has_bands(self, number):
        return number in self.bands


# オペレーターのインスタンスを作成
operators = [
    # Jerry より https://zhuanlan.zhihu.com/p/616370411 teamsにあり
    Operator(
        "China Mobile",
        "China",
        "member_inactive",
        1009,
        "B3",  # 2024/06/11 追加
        "B8",  # 2024/06/11 追加
        "B34",
        "B39",
        "B40",
        "B41",
        "n28", # 2025/07/30 https://www.frequencycheck.com/carriers
        "n41",  # 2024/06/11 修正 n78を消去
        "n77", # 2025/12/17 追加
        "n79",
    ),
    Operator(
        "Bharti Airtel",
        "India",
        "member_active",
        472, # updated 2026/4/2 インド国内wireless（TRAI 2026/2末472.65M）。グローバル合計は650M（India 368M + Africa 182M）
        "B3",
        "B5",
        "B8",
        "B1",
        "B40",
        "n1", # udapted 2026/1/28 5Gとしてリファーミング進行中とのこと
        "n40", # udapted 2026/1/28 5Gとしてリファーミング進行中とのこと
        # "n28", 2025/5/8 削除
        "n78",
        "n258",
    ),
    Operator(
        "Reliance Jio",
        "India",
        "member_active",
        493, # updated 2026/4/2 インド国内wireless（TRAI 2026/2末493.11M）
        "B3", # 2025/7/30 追加 https://www.frequencycheck.com/carriers
        "B5", # 2025/7/30 追加 https://www.frequencycheck.com/carriers
        "n3", # 2025/5/8 B3からn3に修正
        "n5", # 2025/5/8 B3からn5に修正
        "B40",
        "n28",
        "n78",
        "n258",
    ),
    Operator(
        "China Telecom",
        "China",
        "member_inactive",
        440.55, # updated 2026/7/6 (2026/3/31時点) https://www.marbridgeconsulting.com/marbridgedaily/2026-04-24/article/115242/chinas_three_main_telcos_report_q1_2026_subscriber_totals
        "B1",  # 2024/6/11 追加修正
        "B3",
        "B5",
        "B40", # 2025/7/30 B41からB40に修正 
        "B41", # 2025/12/17 B41のLTEサポート残りあり
        "n1",  # 2024/6/11 追加修正
        "n5",  # 2025/7/30 追加 https://www.frequencycheck.com/carriers
        "n78",
    ),
    Operator(
        "China Unicom",
        "China",
        "member_inactive",
        340,
        "B1",  # 2024/6/11 追加修正
        "B3",
        "B5", # 2025/5/8 B8からB5に修正
        "B8", # 2025/7/30 追加 https://www.frequencycheck.com/carriers
        "B40",
        "n1",  # 2024/6/11 追加修正
        "n8",  # 2025/7/30 n5からn8に修正 https://www.frequencycheck.com/carriers
        "n78",
    ),
    Operator(
        "China Broadcast",
        "China",
        "member_inactive",
        105,
        "B28",
        "n28",
        "n77",
        "n79",
    ),
    Operator(
        "Telcel", # 2025/7/30 America MovilをTelcelに変更
        "Mexico",
        "non_member",
        84.3, # updated 2026/7/6 メキシコ国内のみに統一（旧312はAmérica Móvilグループ全体の値だった） https://www.tipranks.com/news/company-announcements/america-movil-posts-strong-1q-2026-profit-growth-as-postpaid-and-broadband-drive-expansion
        "B4",
        "B66", # 2025/5/9 削除 → 2025/7/30 復帰 https://www.frequencycheck.com/carriers
        "n5",
        "B7", # 2026/7/6 追加 https://www.frequencycheck.com/carriers
        "n78", # 2026/7/6 追加(主力5G帯) https://www.rcrwireless.com/20220211/business/mexican-telecoms-regulator-paves-way-america-movil-5g-launch
    ),
    Operator(
        "MTN",
        "South Africa",
        "non_member",
        39.8, # updated 2026/7/6 南ア国内のみに統一（旧287はアフリカ/中東19市場のMTN Group全体の値だった） https://mtn-investor.com/reporting/interims-2025/results-overview.php
        "B1", # 2026/7/6 追加 https://www.frequencycheck.com/carriers/mtn-group-south-africa
        "B3",
        "B8", # 2026/7/6 追加 https://www.frequencycheck.com/carriers/mtn-group-south-africa
        "n78",
        "n1", # 2026/7/6 追加 https://www.frequencycheck.com/carriers/mtn-group-south-africa
        "n3", # 2026/7/6 追加 https://www.frequencycheck.com/carriers/mtn-group-south-africa
        "n28", # 2026/7/6 追加 https://www.frequencycheck.com/carriers/mtn-group-south-africa
    ), # 2025/7/30 削除  https://www.frequencycheck.com/carriers
    Operator(
        "Vodafone Group",
        "UK",
        "member_active",
        28.6, # updated 2026/7/6 英国内のみに統一（旧323はグループ全体の値だった）。2025/5のVodafoneThree統合(Vodafone51%/CK Hutchison49%)後の合算値でThree由来の顧客を含む https://www.ispreview.co.uk/index.php/2026/02/vodafonethree-top-1-77-million-uk-broadband-users-as-mobile-shrinks-to-28-6m.html
        "B1",
        "B3",
        "B7",
        "B8",
        "B20",
        "B32",
        "B38",
        "n1", # 2025/7/30 追加  https://www.frequencycheck.com/carriers
        "n8", # 2025/7/30 追加  https://www.frequencycheck.com/carriers
        "n78",
    ),
    Operator(
        "Movistar", # 2025/7/30 Telefonicaから変更  https://www.frequencycheck.com/carriers
        "Spain",
        "member_active",
        16.5, # updated 2026/7/6 スペイン国内のみに統一（旧299はTelefónicaグループ全体の値だった） CNMC 2025/12末 シェア26.24%×63.0M回線 https://www.cnmc.es/prensa/datos-diciembre-telecos-20260219
        "B1",
        "B3",
        "B7",
        "B8",
        "B28",
        "B20",
        "n28",
        "n3",
        "n1",
        "n78",
        "n258",
    ),
    Operator("Orange", "France", "member_active", 22, "B1", "B3", "B7", "B20", "B28", "n1","n3", "n78",), # 20225/12/17 n3 added
    # 2026/7/6 フランス国内のみに統一（旧243はOrangeグループ全体26カ国の値だった）。ARCEPは事業者別の契約者数を公表していないため、bonforfait.frの推定値(2025年末)を暫定使用。要確度改善 https://bonforfait.fr/
    Operator(
        "Vodafone Idea",
        "India",
        "member_active",
        198, # updated 2026/4/2 インド国内wireless（TRAI 2026/2末198.38M）
        "B3",
        "B8",
        "B1",
        "B40",
        "B41",
        "n78",
        # "n258", 2025/12/17 商用非展開で削除
    ),  # https://www.lightreading.com/open-ran/vodafone-idea-launches-open-ran-pilot-in-india-with-mavenir 2024/3/14 added
    Operator(
        "AT&T",
        "United States",
        "member_active",
        235,
        "B2",
        "B4",
        "B5",
        "B12",
        "B14",  # 2024/3/14 追加 https://urgentcomm.com/2021/02/22/att-says-firstnet-band-14-buildout-more-than-90-done-adoption-tops-2-million-connections/
        "B17",
        "B29",
        "B30",
        "B46",
        "B48",
        "B66",
        "n2",
        "n5",
        "n66", 
        "n77",
        "n260",
        "n261",
    ),  
    Operator(
        "Deutsche Telekom",
        "Germany",
        "member_active",
        75.3, # updated 2026/7/6 ドイツ国内のみに統一（旧256はグループ全体の値だった） https://report.telekom.com/interim-report-q1-2026/management-report/development-of-business-in-the-operating-segments/germany.html
        "B1",
        "B3",
        "B7",
        "B8",
        "B20",
        "B28",
        "B32",
        "n1",
        "n3",
        "n28", # 2026/7/6 追加 https://www.telekom.com/en/media/media-information/archive/telekom-5g-transmits-on-700-mhz-1008600
        "n77",
        "n78",
    ),
    Operator(
        "Telecomsel",
        "Indonesia",
        "non_member",
        159,
        "B3",
        "B8",
        "B40",
        "n40",
        "n1",
    ),
    Operator("Telenor", "Norway", "non_member", 2.54, "B3", "B7", "B20", "n78"), # 2025/12/17 n78 added
    # 2026/7/6 ノルウェー国内のみに統一（旧93はグループ全体(北欧+アジア)の値だった） Telenor Q4/FY2025 https://www.telenor.com/binaries/investors/reports-and-information/quarterly/2025/Report-Q4-and-Full-Year-2025.pdf
    Operator("Celcomdigi", "Malaysia", "non_member", 163, "B1", "B3", "B7", "n26", "n28", "n78"),
    Operator(
        "du",
        "UAE",
        "non_member",
        9.7, # 2026/7/6 修正 159は誤記(他事業者と混同と推定) UAE国内のみ https://techafricanews.com/2026/03/04/uae-telecom-operator-du-sustains-growth-with-9-7m-mobile-subscribers/
        "B3",
        "B1",
        "B8",
        "B20",
        "B28",
        "n78",
        "n41", # 2026/7/6 追加 https://www.rcrwireless.com/20250925/5g/du-5g-uae
    ),
    Operator(
        "KPN", "Netherlands", "non_member", 157, "B3", "B7", "B20", "B38", "n1", "n78", "n28"
    ),
    Operator(
        "Verizon",
        "United States",
        "member_active",
        146.8, # updated 2026/7/6 (2026/3/31 retail connections) https://www.verizon.com/about/sites/default/files/Verizon_Fact_Sheet.pdf
        "B13",
        "B2",
        "B4",
        "B5",
        "B46",
        "B48",
        "B66",
        "n2",
        "n5",
        "n66",
        "n77",
        "n260",
        "n261",
    ),  # duplicated n77 was removed 2024/3/25
    Operator("Vodacom", "South Africa", "non_member", 46, "B8", "B3", "B42", "n78"), #2025/12/17 n78 added
    # 2026/7/6 南ア国内のみに統一（旧155はグループ全体8市場の値だった） Vodacom FY2025 https://www.vodacom.com/pdf/investor/annual-results/2025/results-booklet.pdf B42は南ア国内での独立LTE展開が未確認、要確認
    Operator("Ooredoo", "Qatar", "non_member", 121, "B3", "B8", "B1", "n78"), #2025/12/17 n78 added
    # T-Mobile may be part of Deutche Telecom, but left as it is
    Operator(
        "T-Mobile",
        "United States",
        "member_active",
        130.9, # updated 2026/7/6 (2026 Q1 total customer connections)
        "B2",
        "B12",
        "B71",
        "B5",
        "B4",
        "B66",
        "n71",
        "n41",
        # "n258", 2025/12/17 商用未展開とのこと
        "n260",
        "n261",
    ),
    Operator(
        "Viettel", "Vietnam", "non_member", 110, "B3", "n78"), # 2025/12/17 n78 added 
    Operator("BSNL Mobile", "India", "non_member", 93, "B3", "B5", "B28", "B1", "B41", "n28", "n78", "n258"), # updated 2026/4/2 （TRAI 2026/2末92.93M）
    Operator(
        "CMHK", "Hong Kong", "non_member", 120,  "B3", "B7", "B40", "n1", "n78", "n79"
    ),
    Operator("MTN Irancell", "Iran", "non_member", 92, "B3", "B7", "B42", "n78"),
    Operator(
        "Mobile TeleSystems",
        "Russia",
        "non_member",
        84,
        "B3",
        "B7",
        "B8",
        "B20",
        "B34",
        "B38",
        "n7",
        "n79",
        "n258",
    ),
    Operator(
        "NTT Docomo",
        "Japan",
        "member_active",
         92, #updated 2026/1/28
        "B28",
        "B18",
        "B26",
        "B19",
        "B8",
        "B11",
        "B21",
        "B3",
        "B1",
        "B42",
        "n1",
        "n28",
        "n78",
        "n77",
        "n79",
        "n257",
    ),
    Operator(
        "Rakuten Mobile",
        "Japan",
        "member_active",
        10, #updated 2026/4/2 （2025/12/25公式発表 10M突破）
        "B3",
        "B18",
        "B28",
        "n3",
        "n77",
        "n257",
    ),
    Operator("Globe Telecom", "Philippines", "non_member", 54, "B28", "B3", "B7", "B41", "n41", "n78"),
    Operator("Smart", "Philippines", "non_member", 53, "B1", "B3", "B5", "B28", "B40", "B41", "n28", "n41", "n78"),
    Operator("MegaFon", "Russia", "non_member", 71, "B1", "B3", "B7", "B8", "B34", "B41", "n1", "n7", "n78", "n257", "n258"), #2025/12/17 n78 added
    Operator(
        "KDDI",
        "Japan",
        "member_active",
        71, #updated 2026/4/2 （2025年Q2 71.46M）
        "B28",
        "B18",
        "B26",
        "B19",
        "B8",
        "B11",
        "B21",
        "B3",
        "B1",
        "B42",
        "n28",
        "n3",
        "n78",
        "n77",
        "n79",
        "n257",
    ),  # 確度高い KDDI web site
    Operator(
        "Softbank",
        "Japan",
        "member_active",
        56, #updated 2026/4/2 （2025年Q2 56.38M）
        "B12",
        "B28",
        "B17",
        "B18",
        "B26",
        "B19",
        "B8",
        "B11",
        "B21",
        "B3",
        "B4",
        "B2",
        "B1",
        "B39",
        "B40",
        "B38",
        "B42",
        "B41",
        "n77",
        "n79",  # 2025/12/17 一部導入中により追加
        "n257",
    ),  # 4G確度高い Softbank web
    Operator(
        "SK telecom",
        "Korea",
        "member_active",
        30,
        "B1",
        "B3",
        "B5",
        "B7",
        "n78",
        "n257",
    ),  # telecomのtは小文字を使っているので要注意 大文字だと拾わない
    Operator(
        "Chunghwa Telecom",
        "Taiwan",
        "member_active",
        13,
        "B1",
        "B3",
        "B7",
        "B8",
        "n1",
        "n78",
    ),  
]
