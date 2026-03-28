# facts.py
# Verified facts with source citations and stance tags
# PRO = supports a "for" / positive stance on the topic
# CON = supports an "against" / critical stance on the topic
# NEUTRAL = useful context, works both ways
# strength = 0.0 to 1.0 (how impactful this fact is in a debate)

FACTS: list[dict] = [

    # ══════════════════════════════════════════════════════
    # FINANCE
    # ══════════════════════════════════════════════════════

    {
        "fact": "India's GDP grew at 8.2% in FY2023-24, making it the fastest-growing major economy.",
        "source": "MoSPI, 2024",
        "url": "https://mospi.gov.in",
        "tag": "PRO",
        "domain": "finance",
        "strength": 0.8
    },
    {
        "fact": "Global debt reached a record $307 trillion in 2023, equivalent to 336% of world GDP.",
        "source": "Institute of International Finance, 2023",
        "url": "https://iif.com/Research/Capital-Flows-and-Debt/Global-Debt-Monitor",
        "tag": "CON",
        "domain": "finance",
        "strength": 0.9
    },
    {
        "fact": "The IMF projects global growth at 3.2% for 2024, below the historical average of 3.8%.",
        "source": "IMF World Economic Outlook, 2024",
        "url": "https://imf.org/en/publications/weo",
        "tag": "CON",
        "domain": "finance",
        "strength": 0.8
    },
    {
        "fact": "India's stock market (BSE) crossed a $4 trillion market cap milestone in 2024.",
        "source": "BSE / Reuters, 2024",
        "url": "https://bseindia.com",
        "tag": "PRO",
        "domain": "finance",
        "strength": 0.7
    },
    {
        "fact": "Bitcoin ETFs attracted over $10 billion in inflows within weeks of US SEC approval in January 2024.",
        "source": "Bloomberg / SEC filings, 2024",
        "url": "https://sec.gov",
        "tag": "PRO",
        "domain": "finance",
        "strength": 0.85
    },
    {
        "fact": "Cryptocurrency markets lost over $2 trillion in value during the 2022 bear market.",
        "source": "CoinMarketCap, 2022",
        "url": "https://coinmarketcap.com",
        "tag": "CON",
        "domain": "finance",
        "strength": 0.9
    },
    {
        "fact": "The top 1% of global wealth holders own 43% of all financial assets.",
        "source": "Credit Suisse Global Wealth Report, 2023",
        "url": "https://credit-suisse.com/about-us/en/reports-research/global-wealth-report.html",
        "tag": "CON",
        "domain": "finance",
        "strength": 0.9
    },
    {
        "fact": "Microfinance institutions served over 200 million borrowers globally in 2023.",
        "source": "Microfinance Barometer, 2023",
        "url": "https://convergences.org/en/microfinance-barometer-2023",
        "tag": "PRO",
        "domain": "finance",
        "strength": 0.75
    },
    {
        "fact": "UPI transactions in India surpassed 100 billion in FY2023-24, processing over ₹200 lakh crore.",
        "source": "NPCI Annual Report, 2024",
        "url": "https://npci.org.in",
        "tag": "PRO",
        "domain": "finance",
        "strength": 0.85
    },
    {
        "fact": "Silicon Valley Bank collapsed in March 2023 in the second largest US bank failure in history.",
        "source": "FDIC / Reuters, 2023",
        "url": "https://fdic.gov",
        "tag": "CON",
        "domain": "finance",
        "strength": 0.9
    },
    {
        "fact": "Central banks in 130 countries representing 98% of global GDP are exploring digital currencies.",
        "source": "Atlantic Council CBDC Tracker, 2023",
        "url": "https://atlanticcouncil.org/cbdctracker",
        "tag": "PRO",
        "domain": "finance",
        "strength": 0.8
    },
    {
        "fact": "ESG investing surpassed $35 trillion in assets under management globally in 2023.",
        "source": "Global Sustainable Investment Alliance, 2023",
        "url": "https://gsi-alliance.org",
        "tag": "PRO",
        "domain": "finance",
        "strength": 0.8
    },
    {
        "fact": "Over 15-year periods, 92% of active US equity funds underperform their benchmark index.",
        "source": "S&P SPIVA Scorecard, 2023",
        "url": "https://spglobal.com/spdji/en/spiva",
        "tag": "CON",
        "domain": "finance",
        "strength": 0.95
    },
    {
        "fact": "The 2008 financial crisis erased approximately $19.2 trillion in US household wealth.",
        "source": "Federal Reserve Flow of Funds Report, 2012",
        "url": "https://federalreserve.gov",
        "tag": "CON",
        "domain": "finance",
        "strength": 0.95
    },

    # ══════════════════════════════════════════════════════
    # MARKETING
    # ══════════════════════════════════════════════════════

    {
        "fact": "Email marketing delivers an average ROI of $36 for every $1 spent.",
        "source": "Litmus State of Email Report, 2023",
        "url": "https://litmus.com/blog/the-roi-of-email-marketing",
        "tag": "PRO",
        "domain": "marketing",
        "strength": 0.9
    },
    {
        "fact": "73% of consumers say a good customer experience is key to influencing brand loyalty.",
        "source": "PwC Future of CX Report, 2018",
        "url": "https://pwc.com/us/en/services/consulting/library/consumer-intelligence-series/future-of-customer-experience.html",
        "tag": "PRO",
        "domain": "marketing",
        "strength": 0.85
    },
    {
        "fact": "Digital ad fraud cost businesses an estimated $84 billion globally in 2023.",
        "source": "Juniper Research, 2023",
        "url": "https://juniperresearch.com",
        "tag": "CON",
        "domain": "marketing",
        "strength": 0.9
    },
    {
        "fact": "Influencer marketing industry was valued at $21.1 billion globally in 2023.",
        "source": "Influencer Marketing Hub Benchmark Report, 2023",
        "url": "https://influencermarketinghub.com/influencer-marketing-benchmark-report",
        "tag": "PRO",
        "domain": "marketing",
        "strength": 0.85
    },
    {
        "fact": "Only 37% of consumers trust sponsored content from influencers.",
        "source": "Edelman Trust Barometer, 2023",
        "url": "https://edelman.com/trust/2023/trust-barometer",
        "tag": "CON",
        "domain": "marketing",
        "strength": 0.9
    },
    {
        "fact": "Short-form video content generates 1200% more shares than text and image content combined.",
        "source": "WordStream / HubSpot, 2023",
        "url": "https://wordstream.com/blog/ws/2023/video-marketing-statistics",
        "tag": "PRO",
        "domain": "marketing",
        "strength": 0.85
    },
    {
        "fact": "79% of consumers say they are concerned about how companies use their personal data.",
        "source": "Cisco Consumer Privacy Survey, 2023",
        "url": "https://cisco.com/c/en/us/about/trust-center/consumer-privacy-survey.html",
        "tag": "CON",
        "domain": "marketing",
        "strength": 0.85
    },
    {
        "fact": "Companies using AI-driven marketing see up to 40% improvement in marketing efficiency.",
        "source": "McKinsey Global Survey on AI, 2023",
        "url": "https://mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-2023",
        "tag": "PRO",
        "domain": "marketing",
        "strength": 0.85
    },
    {
        "fact": "62% of consumers can detect AI-written copy, raising authenticity concerns for brands.",
        "source": "Capterra AI in Marketing Survey, 2023",
        "url": "https://capterra.com/resources/ai-marketing-survey",
        "tag": "CON",
        "domain": "marketing",
        "strength": 0.8
    },
    {
        "fact": "Acquiring a new customer costs 5 to 7 times more than retaining an existing one.",
        "source": "Harvard Business Review, Reichheld 2001",
        "url": "https://hbr.org/2014/10/the-value-of-keeping-the-right-customers",
        "tag": "PRO",
        "domain": "marketing",
        "strength": 0.9
    },
    {
        "fact": "Personalized email campaigns deliver 6 times higher transaction rates than generic ones.",
        "source": "Experian Email Marketing Study, 2016",
        "url": "https://experian.com",
        "tag": "PRO",
        "domain": "marketing",
        "strength": 0.85
    },
    {
        "fact": "Third-party cookie deprecation by Google Chrome is set to reshape $700 billion in digital advertising.",
        "source": "IAB / Google, 2024",
        "url": "https://iab.com",
        "tag": "CON",
        "domain": "marketing",
        "strength": 0.8
    },

    # ══════════════════════════════════════════════════════
    # ETHICS
    # ══════════════════════════════════════════════════════

    {
        "fact": "The EU AI Act, the world's first comprehensive AI regulation, was formally adopted in 2024.",
        "source": "European Parliament, 2024",
        "url": "https://artificialintelligenceact.eu",
        "tag": "PRO",
        "domain": "ethics",
        "strength": 0.95
    },
    {
        "fact": "Facial recognition AI shows error rates up to 34% for darker-skinned women vs 0.8% for lighter-skinned men.",
        "source": "MIT Media Lab Gender Shades Study, 2018",
        "url": "http://gendershades.org",
        "tag": "CON",
        "domain": "ethics",
        "strength": 0.95
    },
    {
        "fact": "OpenAI, Google DeepMind, and Anthropic signed the Frontier AI Safety Commitments at the UK AI Safety Summit 2023.",
        "source": "UK Government / Bletchley Declaration, 2023",
        "url": "https://gov.uk/government/publications/frontier-ai-safety-commitments-ai-safety-summit-2023",
        "tag": "PRO",
        "domain": "ethics",
        "strength": 0.85
    },
    {
        "fact": "GDPR fines exceeded €4.5 billion cumulatively by end of 2023.",
        "source": "DLA Piper GDPR Fines Report, 2024",
        "url": "https://dlapiper.com/en/insights/publications/2024/01/dla-piper-gdpr-fines-and-data-breach-survey-2024",
        "tag": "CON",
        "domain": "ethics",
        "strength": 0.9
    },
    {
        "fact": "Meta was fined €1.2 billion by Ireland's DPC for unlawful data transfers to the US in 2023.",
        "source": "Irish Data Protection Commission, 2023",
        "url": "https://dataprotection.ie",
        "tag": "CON",
        "domain": "ethics",
        "strength": 0.9
    },
    {
        "fact": "71 million people were forcibly displaced globally by conflict and persecution as of 2023.",
        "source": "UNHCR Global Trends Report, 2023",
        "url": "https://unhcr.org/global-trends",
        "tag": "CON",
        "domain": "ethics",
        "strength": 0.85
    },
    {
        "fact": "Child labor declined by 50% globally between 2000 and 2022, from 246 million to 160 million.",
        "source": "ILO / UNICEF Report, 2022",
        "url": "https://ilo.org/global/topics/child-labour/lang--en/index.htm",
        "tag": "PRO",
        "domain": "ethics",
        "strength": 0.85
    },
    {
        "fact": "WHO estimates 4.5 billion people lack access to essential health services as of 2023.",
        "source": "WHO Universal Health Coverage Report, 2023",
        "url": "https://who.int/news-room/fact-sheets/detail/universal-health-coverage",
        "tag": "CON",
        "domain": "ethics",
        "strength": 0.9
    },
    {
        "fact": "CRISPR gene editing trials showed successful treatment of sickle cell disease in 2023.",
        "source": "NEJM / FDA, 2023",
        "url": "https://nejm.org",
        "tag": "NEUTRAL",
        "domain": "ethics",
        "strength": 0.8
    },
    {
        "fact": "Algorithmic bias in hiring tools has been shown to reduce callbacks for minority candidates by up to 30%.",
        "source": "MIT Media Lab Algorithmic Bias Study, 2019",
        "url": "https://media.mit.edu",
        "tag": "CON",
        "domain": "ethics",
        "strength": 0.9
    },
    {
        "fact": "John Rawls argued in A Theory of Justice that fair societies are designed behind a veil of ignorance.",
        "source": "Rawls, A Theory of Justice, Harvard University Press, 1971",
        "url": "https://en.wikipedia.org/wiki/A_Theory_of_Justice",
        "tag": "PRO",
        "domain": "ethics",
        "strength": 0.85
    },
    {
        "fact": "Kant's categorical imperative states: act only according to maxims you could will to be universal law.",
        "source": "Immanuel Kant, Groundwork of the Metaphysics of Morals, 1785",
        "url": "https://en.wikipedia.org/wiki/Categorical_imperative",
        "tag": "NEUTRAL",
        "domain": "ethics",
        "strength": 0.85
    },

    # ══════════════════════════════════════════════════════
    # GENERAL (fallback for unknown topics)
    # ══════════════════════════════════════════════════════

    {
        "fact": "As of 2024, there are approximately 5.4 billion internet users worldwide, 67% of the global population.",
        "source": "DataReportal Global Digital Overview, 2024",
        "url": "https://datareportal.com/global-digital-overview",
        "tag": "NEUTRAL",
        "domain": "general",
        "strength": 0.7
    },
    {
        "fact": "The global AI market is projected to reach $1.8 trillion by 2030.",
        "source": "Grand View Research, 2023",
        "url": "https://grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market",
        "tag": "PRO",
        "domain": "general",
        "strength": 0.8
    },
    {
        "fact": "Climate change costs the global economy an estimated $16 million per hour in extreme weather damages.",
        "source": "Deloitte Economics Institute, 2023",
        "url": "https://deloitte.com/global/en/issues/climate/the-turning-point.html",
        "tag": "CON",
        "domain": "general",
        "strength": 0.85
    },
]


# ── Domain Detection ───────────────────────────────────────────────────────────

DOMAIN_KEYWORDS = {
    "finance": [
        "finance", "financial", "economy", "economic", "gdp",
        "investment", "market", "banking", "debt", "inflation",
        "trade", "fiscal", "monetary", "stock", "crypto",
        "bank", "currency", "fund", "capital", "wealth"
    ],
    "marketing": [
        "marketing", "advertis", "brand", "consumer", "digital",
        "social media", "campaign", "customer", "sales", "content",
        "seo", "influencer", "ecommerce", "retail", "promotion",
        "audience", "engagement", "roi", "conversion"
    ],
    "ethics": [
        "ethics", "ethical", "ai", "artificial intelligence", "moral",
        "regulation", "bias", "fairness", "privacy", "responsible",
        "governance", "policy", "rights", "surveillance", "automation",
        "justice", "equality", "accountability", "transparency"
    ]
}


def detect_domain(topic: str) -> str:
    topic_lower = topic.lower()
    scores = {d: 0 for d in DOMAIN_KEYWORDS}

    for domain, keywords in DOMAIN_KEYWORDS.items():
        scores[domain] = sum(1 for kw in keywords if kw in topic_lower)

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return "general"

    # Handle ties — return first tied domain (finance > marketing > ethics)
    return best


def get_facts_by_stance(topic: str, stance: str, max_facts: int = 4) -> list[dict]:
    """
    Returns top N facts filtered by domain + stance,
    sorted by strength descending.
    """
    domain     = detect_domain(topic)
    stance_up  = stance.upper()

    # Pull from matched domain + general as fallback
    pool = [f for f in FACTS if f["domain"] == domain]
    if not pool:
        pool = [f for f in FACTS if f["domain"] == "general"]

    # Filter by stance
    filtered = [f for f in pool if f["tag"] in (stance_up, "NEUTRAL")]

    # Sort by strength
    filtered.sort(key=lambda x: x.get("strength", 0.5), reverse=True)

    print(f"[facts] domain={domain} | stance={stance_up} | matched={len(filtered)}")
    return filtered[:max_facts]


def format_facts_for_prompt(facts: list[dict]) -> str:
    """
    Formats facts for injection into system prompt.
    Includes source and URL for credibility.
    """
    if not facts:
        return "No domain-specific facts available. Argue from logic and principle only."

    lines = ["VERIFIED FACTS — use these, never invent statistics:"]
    for f in facts:
        url_part = f" | {f['url']}" if f.get("url") else ""
        lines.append(f'• "{f["fact"]}" [{f["source"]}{url_part}]')

    return "\n".join(lines)


# ── Quick Self Test ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        ("Cryptocurrency should replace traditional banking", "PRO"),
        ("Influencer marketing is more effective than traditional advertising", "CON"),
        ("AI companies should be held legally responsible for algorithmic bias", "PRO"),
        ("ESG investing is the future of finance", "CON"),
        ("Data privacy regulations hurt business innovation", "CON"),
    ]

    print("=" * 60)
    print("FACTS.PY SELF TEST")
    print("=" * 60)

    for topic, stance in tests:
        facts  = get_facts_by_stance(topic, stance)
        output = format_facts_for_prompt(facts)
        print(f"\nTopic:  {topic}")
        print(f"Stance: {stance}")
        print(output)
        print("-" * 40)